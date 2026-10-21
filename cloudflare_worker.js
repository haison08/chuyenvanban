/**
 * Cloudflare Worker: Gemini API Proxy for haison08/chuyenvanban
 * Tác dụng: Giấu API Key phía máy chủ, người dùng không cần nhập API key trên web.
 * Miễn phí 100,000 requests/ngày trên Cloudflare Workers.
 */

// API Key dự phòng mặc định (tùy chọn).
// KHUYẾN NGHỊ BẢO MẬT: Không dán trực tiếp API key vào mã nguồn công khai trên GitHub.
// Thay vào đó, hãy cấu hình biến môi trường GEMINI_API_KEY trong Cloudflare Dashboard:
// (Vào Worker > Settings > Variables and Secrets > Add GEMINI_API_KEY)
const DEFAULT_GEMINI_KEY = "";

export default {
  async fetch(request, env, ctx) {
    // 1. Xử lý CORS Preflight (OPTIONS)
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization, x-goog-api-key",
          "Access-Control-Max-Age": "86400",
        },
      });
    }

    // 2. Chỉ chấp nhận POST và GET
    if (request.method !== "POST" && request.method !== "GET") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), {
        status: 405,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      });
    }

    try {
      const url = new URL(request.url);

      // Ưu tiên API key từ:
      // 1. Query parameter nếu client tự gửi: ?key=...
      // 2. Cloudflare Worker Environment Variable: env.GEMINI_API_KEY
      // 3. DEFAULT_GEMINI_KEY đã nhúng sẵn ở trên
      const apiKey = url.searchParams.get("key") || (env && env.GEMINI_API_KEY) || DEFAULT_GEMINI_KEY;

      if (!apiKey) {
        return new Response(JSON.stringify({
          error: "Chưa cấu hình GEMINI_API_KEY. Vui lòng thêm biến môi trường GEMINI_API_KEY trên Cloudflare Worker."
        }), {
          status: 500,
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
          },
        });
      }

      // Xây dựng path chuyển tiếp tới Google Gemini API
      // Mặc định nếu gọi / thì vào gemini-3.8-flash:generateContent
      let targetPath = url.pathname;
      if (!targetPath || targetPath === "/") {
        targetPath = "/v1beta/models/gemini-3.8-flash:generateContent";
      }

      // Giữ lại các query parameters và chèn key của server
      const targetParams = new URLSearchParams(url.searchParams);
      targetParams.set("key", apiKey);

      const targetUrl = `https://generativelanguage.googleapis.com${targetPath}?${targetParams.toString()}`;

      // Chuẩn bị headers cho request chuyển tiếp
      const forwardHeaders = new Headers();
      forwardHeaders.set("Content-Type", request.headers.get("Content-Type") || "application/json");
      const clientIp = request.headers.get("cf-connecting-ip") || request.headers.get("x-real-ip");
      if (clientIp) {
        forwardHeaders.set("X-Forwarded-For", clientIp);
      }

      const response = await fetch(targetUrl, {
        method: request.method,
        headers: forwardHeaders,
        body: request.method === "POST" ? await request.text() : undefined,
      });

      // Lấy dữ liệu trả về từ Gemini
      const responseData = await response.text();

      // Đính kèm đầy đủ CORS headers để GitHub Pages (haison08.github.io) gọi được thoải mái
      return new Response(responseData, {
        status: response.status,
        headers: {
          "Content-Type": response.headers.get("Content-Type") || "application/json",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization, x-goog-api-key",
        },
      });

    } catch (error) {
      return new Response(JSON.stringify({ error: error.message || "Lỗi proxy Cloudflare Worker" }), {
        status: 500,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      });
    }
  },
};
