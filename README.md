# Haison dep trai - AI PDF/Image to Word Converter 🚀

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/haison08/chuyenvanban)

Ứng dụng Web AI chuyển đổi tài liệu PDF/Hình ảnh (văn bản hành chính, kế hoạch, quyết định, danh sách Đảng viên/cán bộ) sang file Microsoft Word (.docx) chuẩn thể thức Việt Nam 100%.

## ✨ Tính Năng Nổi Bật

- **AI Vision OCR Đỉnh Cao**: Sử dụng Gemini Vision để nhận diện chuẩn xác tiếng Việt có dấu, kể cả bản scan mờ.
- **Tự Động Nhận Diện Hướng Trang (Portrait / Landscape)**:
  - Trang văn bản thường: Khổ A4 Dọc (Portrait).
  - Trang có bảng biểu danh sách nhiều cột ($\ge 7$ cột): Tự động chuyển sang Khổ A4 Ngang (Landscape) chuẩn thể thức.
- **Tỷ Lệ Bảng Thông Minh**: Tự động phân bổ độ rộng từng cột (TT, Họ tên, Ngày tháng, Địa chỉ, CCCD) và cỡ chữ (9pt - 9.5pt) giúp chữ không bao giờ bị rớt dòng lửng lơ.
- **Chuẩn Thể Thức Hành Chính (Nghị định 30/2020/NĐ-CP)**:
  - 2 cột Quốc hiệu - Tiêu ngữ và Cơ quan ban hành.
  - Phân cấp tiêu đề, thụt đầu dòng đoạn văn.
  - Khối Nơi nhận & Người ký, chừa khoảng trống đóng dấu.
- **Xóa Bỏ Trang Trắng Thừa & Khung Viền**: Tài liệu xuất ra sạch sẽ, đúng chuẩn file văn phòng Word.

---

## 🛠️ Cài Đặt & Chạy Cục Bộ (Local)

### 1. Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

### 2. Khởi chạy ứng dụng Web:
```bash
python3 app.py
```

Mở trình duyệt truy cập: **`http://localhost:5001`**

---

## 🔑 Cấu Hình API Key
Bạn có thể nhập API Key trực tiếp trên giao diện web, hoặc cấu hình biến môi trường:
```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```
