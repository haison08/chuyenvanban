

## 📋 PROMPT BẮT ĐẦU TỪ ĐÂY:

```
Bạn là chuyên gia kiểm định chất lượng (QA) chuyên về chuyển đổi văn bản hành chính từ hình ảnh/PDF sang file Word (.docx). 

Tôi có một ứng dụng web dùng Gemini Vision API để đọc hình ảnh tài liệu, trả về JSON mô tả cấu trúc, rồi dùng thư viện docx.js để sinh file Word. Vấn đề là: **file Word xuất ra KHÔNG giống 100% bố cục mẫu gốc**, đặc biệt khi chạy trên các máy/trình duyệt khác nhau.

Hãy kiểm tra TOÀN BỘ code tôi gửi kèm và tìm + sửa tất cả các lỗi thuộc các nhóm sau:

---

## NHÓM 1: LỖI KHUNG VIỀN XUẤT HIỆN KHI KHÔNG CÓ TRONG MẪU GỐC

Đây là lỗi **nghiêm trọng nhất**. File Word bị thêm khung viền (border) ở những chỗ mà bản gốc KHÔNG có.

### Các nguyên nhân cần kiểm tra:

1. **Bảng bố cục (layout table) bị gán `has_border: true` sai:**
   - Phần "XÉT, ĐỀ NGHỊ CỦA ĐẢNG UỶ" / "XÉT, ĐỀ NGHỊ CỦA CHI BỘ" là 2 cột văn bản song song, KHÔNG có viền → phải là `has_border: false`.
   - Phần header (Quốc hiệu + Đơn vị ban hành) dùng bảng 2 cột bố cục → KHÔNG được có viền.
   - Phần chữ ký (signature_block) dùng bảng ẩn → KHÔNG được có viền.

2. **Logic tự suy `has_border` khi AI không trả về giá trị:**
   - Kiểm tra đoạn code xử lý `if (hasBorder === undefined)`. Nếu AI không nói rõ, code hiện tại tự suy bảng >= 3 cột hoặc >= 2 dòng thì có viền → **SAI**. Phải mặc định `has_border: false` trừ khi ảnh gốc rõ ràng có ô lưới kẻ.

3. **Cell border bị override:**
   - Kiểm tra `cellBorder` có bị set `singleBorder` ở những cell không nên có viền không.
   - Đặc biệt ô "Mẫu 6-HHD" cần viền riêng nhưng KHÔNG được lan viền sang các ô khác cùng hàng.

4. **`tableBorders` bị áp dụng cả `insideHorizontal` và `insideVertical`:**
   - Với bảng `has_border: false`, đảm bảo cả `insideHorizontal` và `insideVertical` đều là `noBorder`.

---

## NHÓM 2: LỖI BỐ CỤC SAI VỊ TRÍ / KHOẢNG CÁCH

### Các nguyên nhân cần kiểm tra:

1. **Phần chữ ký bên phải bị nhảy sang trái hoặc bị dính vào phần khác:**
   - Kiểm tra `width` của `TableCell` trong `signature_block`. Cột trái (Nơi nhận) và cột phải (Ký tên) phải có tỷ lệ chuẩn (khoảng 45% - 55%).
   - Nếu `recipients` rỗng (chỉ có người ký bên phải), bảng vẫn phải đặt ô trái rỗng với đúng width.

2. **Phần "XÉT, ĐỀ NGHỊ" 2 cột bị xếp thành 1 cột dọc thay vì 2 cột ngang:**
   - AI có thể trả sai cấu trúc: thay vì 1 row + 2 cells, lại trả 2 rows + 1 cell mỗi row.
   - Code phải validate: nếu phát hiện pattern "XÉT, ĐỀ NGHỊ CỦA..." ở 2 elements liên tiếp → gộp thành 1 bảng 2 cột.

3. **Khoảng trống chữ ký (space) quá lớn hoặc quá nhỏ:**
   - `{is_space: true, space: 35}` → Kiểm tra đơn vị: `space * 20` DXA có đúng không? 35 * 20 = 700 DXA ≈ 1.2cm. Nên điều chỉnh nếu cần.

4. **Lề trang (margin) khác nhau giữa portrait/landscape:**
   - Kiểm tra margin trái/phải/trên/dưới có phù hợp với khổ giấy A4 chuẩn không.
   - Portrait: margin trái 2.5cm (≈1417 DXA), phải 1.5cm (≈850), trên/dưới 2cm (≈1134).
   - Code hiện tại dùng `left: 1240` cho portrait → có thể hơi nhỏ.

---

## NHÓM 3: LỖI NỘI DUNG VĂN BẢN BỊ GHÉP DÒNG / MẤT DÒNG

### Các nguyên nhân cần kiểm tra:

1. **Nhiều dòng bị ghép thành 1 dòng dài:**
   - AI Gemini thường ghép "Kính gửi:............Đề nghị tặng..." thành 1 chuỗi.
   - Kiểm tra hàm `fixConcatenatedText()` có cover đủ các pattern chưa:
     + "............" + chữ viết hoa → nên ngắt dòng.
     + "năm 2026" + "T/M" → nên ngắt dòng.
     + "kèm theo)" + "..., ngày" → nên ngắt dòng.
   - Thêm các pattern mới nếu cần.

2. **Ký tự `\n` trong JSON không được xử lý thành line break trong Word:**
   - Kiểm tra khi docx.js nhận text chứa `\n`, nó có tạo `break: 1` (line break) hay tạo paragraph mới.
   - `createMultiParagraphs()` phải split `\n` thành các paragraph riêng.
   - `createSingleParagraph()` phải split `\n` trong text thành các TextRun với `break: 1`.

3. **Hàng chấm lửng bị mất hoặc bị rút ngắn:**
   - "Kính gửi:............................................" → phải giữ nguyên số lượng dấu chấm.
   - AI có thể trả "Kính gửi:..." (chỉ 3 chấm) → code nên detect và bổ sung.

---

## NHÓM 4: LỖI BẢNG BIỂU SAI CẤU TRÚC

### Các nguyên nhân cần kiểm tra:

1. **Số cột thực tế khác số cột mẫu gốc:**
   - Bảng gốc 16 cột nhưng AI chỉ trả 12 cột → thiếu cột.
   - Kiểm tra `maxCols` detection logic: phải lấy max từ tất cả rows.

2. **Colspan/Rowspan bị bỏ qua hoặc tính sai:**
   - Ô header gộp nhiều cột: phải có `colspan`.
   - Code hiện tại có set `columnSpan` nhưng KHÔNG trừ đi số cột bị gộp khi lặp → **có thể sinh thừa cell**.

3. **Chiều rộng cột không cân đối:**
   - `col_widths` từ AI có thể sai đơn vị (mm vs DXA vs phần trăm).
   - Kiểm tra phép nhân `w * 56.7` (mm → DXA) có đúng với thực tế không.
   - Tổng các `col_widths` phải bằng `availableWidthDxa`.

4. **Font size trong bảng nhiều cột bị quá nhỏ hoặc quá to:**
   - Kiểm tra logic `cellFontSize` dựa trên `numCols`: có khớp với kích cỡ chữ trong mẫu gốc không.

---

## NHÓM 5: LỖI KHÁC BIỆT GIỮA CÁC TRÌNH DUYỆT / MÁY KHÁC NHAU

### Các nguyên nhân cần kiểm tra:

1. **PDF.js render khác nhau trên các trình duyệt:**
   - Canvas DPI khác nhau → ảnh gửi cho AI có chất lượng khác → AI nhận diện khác.
   - Kiểm tra `scale: 2.0` trong `getViewport()` có đủ cho mọi trình duyệt không.
   - Nên set `devicePixelRatio` cố định khi render canvas.

2. **Font Times New Roman không có trên máy khác:**
   - File Word ghi font "Times New Roman" nhưng máy mở không cài → Word dùng font thay thế → vỡ bố cục.
   - Cân nhắc embed font hoặc dùng font fallback phổ biến.

3. **CDN script load lỗi hoặc phiên bản khác:**
   - `pdf.js`, `docx.js`, `FileSaver.js` load từ CDN → máy khác có thể bị chặn hoặc cache phiên bản cũ.
   - Kiểm tra integrity hash hoặc pin version chính xác.

4. **LocalStorage API key không sync giữa các máy:**
   - API key lưu trong localStorage trên máy A → máy B không có → phải nhập lại.
   - Không phải lỗi nhưng cần UX thông báo rõ ràng.

---

## YÊU CẦU CỤ THỂ:

1. **Kiểm tra từng dòng code** trong file `index.html` tôi gửi kèm.
2. **Liệt kê TẤT CẢ các lỗi** bạn tìm thấy thuộc 5 nhóm trên.
3. **Viết code sửa chữa** cho từng lỗi, đưa ra code TRƯỚC và SAU khi sửa.
4. **Ưu tiên sửa Nhóm 1 (khung viền sai) và Nhóm 2 (bố cục sai vị trí) TRƯỚC**.
5. **Sau khi sửa xong, tóm tắt lại** danh sách thay đổi.

Đặc biệt chú ý: phần cuối trang có 2 khối "XÉT, ĐỀ NGHỊ CỦA ĐẢNG UỶ" và "XÉT, ĐỀ NGHỊ CỦA CHI BỘ" phải nằm cạnh nhau (2 cột), KHÔNG CÓ KHUNG VIỀN, và mỗi dòng trong đó phải nằm trên một dòng riêng biệt.


---

## 💡 HƯỚNG DẪN SỬ DỤNG:

1. Copy toàn bộ nội dung trong khối ` ``` ` ở trên
2. Mở Gemini (hoặc bất kỳ AI nào)
3. Dán prompt + dán thêm toàn bộ code `index.html` vào cuối
4. Nếu có ảnh mẫu gốc, hãy đính kèm ảnh mẫu gốc cùng prompt để AI so sánh trực tiếp
5. AI sẽ kiểm tra từng nhóm lỗi và đưa ra code sửa cụ thể

> [!TIP]
> **Để kết quả tốt nhất**: Đính kèm cả ảnh mẫu gốc (hình chụp tài liệu) cùng với prompt. Gemini sẽ so sánh trực quan giữa mẫu gốc và logic code để phát hiện lỗi chính xác hơn.

> [!WARNING]
> Prompt này chỉ tập trung vào **lỗi bố cục không đúng mẫu**. Không bao gồm lỗi UI/UX của trang web, lỗi bảo mật, hay lỗi performance.
