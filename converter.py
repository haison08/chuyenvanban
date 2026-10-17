import os
import json
import time
import base64
import requests
import fitz  # PyMuPDF
from PIL import Image
from docx_builder import build_docx_from_structure
from sample_data import get_sample_document_structure

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#') and '=' in line:
                k, v = line.strip().split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

DEFAULT_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

CANDIDATE_MODELS = [
    "gemini-3.8-flash",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-1.5-flash",
    "gemini-pro-latest"
]

def extract_pdf_pages_to_images(pdf_path, output_dir, dpi=180):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=dpi)
        img_name = f"page_{page_num + 1}.png"
        img_path = os.path.join(output_dir, img_name)
        pix.save(img_path)
        image_paths.append(img_path)
        
    return image_paths, len(doc)

def parse_page_with_gemini(image_path, api_key=None):
    key_to_use = (api_key or DEFAULT_API_KEY or "").strip()
    if not key_to_use:
        raise Exception("Chưa có khóa Google Gemini API Key. Bạn hãy tạo khóa miễn phí tại https://aistudio.google.com/apikey và dán vào ô bên dưới nhé!")
    
    # Detect proper mime type
    ext = os.path.splitext(image_path)[1].lower()
    mime_type = "image/jpeg" if ext in ('.jpg', '.jpeg') else "image/png"
    
    with open(image_path, "rb") as f:
        img_bytes = f.read()
    b64_img = base64.b64encode(img_bytes).decode("utf-8")
    
    prompt = """
Bạn là một chuyên gia phân tích thị giác và bóc tách cấu trúc tài liệu văn bản chuyên nghiệp.
Nhiệm vụ của bạn là đọc hình ảnh trang tài liệu này và chuyển đổi thành cấu trúc JSON chuẩn xác 100% để tạo file Word (.docx).

YÊU CẦU ĐẶC BIỆT:
1. Đọc đúng 100% chữ tiếng Việt có dấu, không bỏ sót chữ nào.
2. Nhận diện thể thức văn bản:
   - Nếu là phần đầu có Quốc hiệu/Tiêu ngữ và Đơn vị ban hành: phân tách thành "type": "header_table" với 2 cột left và right.
   - Nếu là Tiêu đề: "type": "heading", level 1, bold true, align center.
   - Nếu là Đoạn văn: "type": "paragraph", align "justify", first_indent 28, chứa các "runs" với bold, italic tương ứng.
   - Nếu là Bảng biểu: "type": "table", liệt kê các hàng "rows" với từng ô "cells" (kèm row, col, rowspan, colspan, text, align, bold). Đảm bảo giữ nguyên các từ không bị ngắt quãng vô lý (ví dụ: "không", "Lê Văn Hòa", ngày tháng "30/9/1960").
   - Nếu là Khung trang trí (maket sân khấu): "type": "maket_box", items bên trong.
   - Nếu là Nơi nhận và Chữ ký: "type": "signature_block", gồm "recipients" và "signatory". Chừa khoảng trống cho chữ ký bằng {"is_space": true, "space": 35}.
3. Xác định hướng trang:
   - QUAN TRỌNG: Nếu trang có bảng biểu nhiều cột (từ 6 cột trở lên, ví dụ danh sách Đảng viên, bảng thống kê) hoặc tài liệu dàn theo bề ngang: BẮT BUỘC đặt "orientation": "landscape".
   - Chỉ đặt "orientation": "portrait" khi là tài liệu văn bản đọc xuôi ít cột thông thường.
4. QUY TẮC SỐNG CÒN VỀ ĐƯỜNG KẺ VÀ KHUNG VIỀN (BORDERS):
   - TUYỆT ĐỐI KHÔNG TỰ TIỆN THÊM KHUNG VIỀN NẾU BẢN GỐC KHÔNG CÓ!
   - Các phần chia 2 cột như:
     + Chữ ký, người khai (ví dụ: "NGƯỜI KHAI")
     + 2 cột chữ ký xét duyệt (ví dụ: "XÉT, ĐỀ NGHỊ CỦA ĐẢNG UỶ" và "XÉT, ĐỀ NGHỊ CỦA CHI BỘ")
     + Phần số hiệu/mã mẫu ở góc phải (ví dụ: "Mẫu 6-HHD")
     BẮT BUỘC đặt "has_border": false (hoặc dùng "signature_block", "paragraph") để KHÔNG BỊ VẼ KHUNG ĐEN.
   - CHỈ đặt "has_border": true khi đó thực sự là MỘT BẢNG KẺ Ô LƯỚI RÕ RÀNG TRONG ẢNH GỐC (như bảng danh sách đảng viên, bảng biểu thống kê).

Trả về DUY NHẤT một khối mã JSON hợp lệ:
{
  "orientation": "portrait" (hoặc "landscape"),
  "elements": [
    ...
  ]
}
"""

    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": b64_img
                    }
                }
            ]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "application/json"
        }
    }

    last_error = None
    # Try models with automatic fallback
    for model_name in CANDIDATE_MODELS:
        url = GEMINI_API_URL.format(model=model_name, key=key_to_use)
        for attempt in range(2):
            try:
                resp = requests.post(url, json=payload, timeout=60)
                if resp.status_code == 200:
                    data = resp.json()
                    text_content = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    if text_content.startswith("```json"):
                        text_content = text_content[7:]
                    elif text_content.startswith("```"):
                        text_content = text_content[3:]
                    if text_content.endswith("```"):
                        text_content = text_content[:-3]
                    return json.loads(text_content.strip())
                elif resp.status_code == 401 or "API_KEY" in resp.text:
                    raise Exception("Khóa API Gemini của bạn không hợp lệ hoặc đã bị vô hiệu hóa (Lỗi 401). Bạn hãy vào https://aistudio.google.com/apikey tạo một khóa API mới miễn phí (bắt đầu bằng AIzaSy...) và nhập vào ô API Key nhé!")
                elif resp.status_code in (500, 503, 429):
                    last_error = f"Model {model_name} đang bận (mã {resp.status_code})"
                    time.sleep(1.5)
                    continue
                else:
                    last_error = f"Lỗi ({resp.status_code}): {resp.text}"
                    break
            except Exception as e:
                if "401" in str(e) or "API_KEY" in str(e):
                    raise e
                last_error = str(e)
                time.sleep(0.5)

    raise Exception(f"Không thể kết nối tới mô hình AI: {last_error}")

def parse_page_local_fallback(page, page_num):
    rect = page.rect
    is_landscape = rect.width > rect.height
    orientation = "landscape" if is_landscape else "portrait"
    
    text_page = page.get_text("blocks")
    elements = []
    
    # Sort blocks from top to bottom
    text_page.sort(key=lambda b: (b[1], b[0]))
    
    for block in text_page:
        b_text = block[4].strip()
        if not b_text:
            continue
            
        lines = b_text.split("\n")
        first_line = lines[0].strip()
        
        if any(h in first_line.upper() for h in ["KẾ HOẠCH", "QUYẾT ĐỊNH", "BÁO CÁO", "THÔNG BÁO", "BẢNG TỔNG HỢP"]):
            elements.append({
                "type": "heading",
                "text": b_text,
                "bold": True,
                "align": "center",
                "size": 13.5,
                "space_before": 3,
                "space_after": 3
            })
        elif first_line.startswith(("I.", "II.", "III.", "IV.", "1.", "2.", "3.", "4.")):
            elements.append({
                "type": "heading",
                "text": b_text,
                "bold": True,
                "align": "left",
                "size": 13,
                "space_before": 2,
                "space_after": 2,
                "first_indent": 28
            })
        else:
            elements.append({
                "type": "paragraph",
                "text": b_text,
                "align": "justify",
                "size": 13,
                "space_after": 2,
                "first_indent": 28
            })
            
    if not elements:
        elements.append({
            "type": "paragraph",
            "text": f"[Trang {page_num + 1} - Đã quét ảnh]",
            "align": "center",
            "size": 13
        })
        
    return {
        "orientation": orientation,
        "elements": elements
    }

def convert_document(file_path, output_docx_path, api_key=None, options=None, progress_callback=None):
    if options is None:
        options = {}
        
    is_demo = options.get("is_demo", False)
    effective_api_key = api_key or DEFAULT_API_KEY
    
    if progress_callback:
        progress_callback("extracting_pages", "Đang trích xuất và kết xuất các trang hình ảnh độ nét cao...")
        
    file_ext = os.path.splitext(file_path)[1].lower()
    temp_dir = os.path.join(os.path.dirname(output_docx_path), "temp_pages")
    os.makedirs(temp_dir, exist_ok=True)
    
    page_images = []
    num_pages = 1
    
    if file_ext == ".pdf":
        page_images, num_pages = extract_pdf_pages_to_images(file_path, temp_dir)
    elif file_ext in (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"):
        img = Image.open(file_path)
        img_name = f"page_1{file_ext}"
        img_path = os.path.join(temp_dir, img_name)
        img.save(img_path)
        page_images = [img_path]
        num_pages = 1
        
    if is_demo:
        if progress_callback:
            progress_callback("ai_analyzing", "Đang kích hoạt AI Vision trích xuất từng trang tài liệu...")
        doc_structure = get_sample_document_structure()
    elif effective_api_key:
        doc_structure = {"pages": []}
        for idx, img_path in enumerate(page_images):
            if progress_callback:
                progress_callback("ai_analyzing", f"AI Vision đang phân tích & nhận diện cấu trúc trang {idx + 1}/{num_pages}...")
            try:
                page_data = parse_page_with_gemini(img_path, api_key=effective_api_key)
                doc_structure["pages"].append(page_data)
            except Exception as e:
                print(f"Warning: Gemini failed on page {idx+1}: {e}. Using fallback.")
                if file_ext == ".pdf":
                    doc = fitz.open(file_path)
                    page_data = parse_page_local_fallback(doc[idx], idx)
                    doc_structure["pages"].append(page_data)
                else:
                    raise e
    else:
        if progress_callback:
            progress_callback("local_parsing", "Đang phân tích cấu trúc văn bản cục bộ...")
        doc_structure = {"pages": []}
        if file_ext == ".pdf":
            doc = fitz.open(file_path)
            for idx, page in enumerate(doc):
                page_data = parse_page_local_fallback(page, idx)
                doc_structure["pages"].append(page_data)
        else:
            doc_structure["pages"].append({
                "orientation": "portrait",
                "elements": [{"type": "paragraph", "text": "Hình ảnh đã tải lên", "align": "center"}]
            })
            
    if progress_callback:
        progress_callback("building_word", "Đang lắp ráp định dạng bảng biểu, phông chữ và căn lề Word (.docx)...")
        
    build_docx_from_structure(doc_structure, output_docx_path, options=options)
    
    if progress_callback:
        progress_callback("completed", "Chuyển đổi hoàn tất 100%! Sẵn sàng tải về.")
        
    return {
        "output_path": output_docx_path,
        "page_count": num_pages,
        "pages_preview": [os.path.basename(p) for p in page_images]
    }
