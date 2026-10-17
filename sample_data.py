def get_sample_document_structure():
    """
    Returns the 100% precise structured layout of the 6-page official document
    tested with the user.
    """
    return {
        "pages": [
            # TRANG 1 & 2 (Portrait flow)
            {
                "orientation": "portrait",
                "elements": [
                    {
                        "type": "header_table",
                        "left": [
                            {"text": "ỦY BAN MTTQ VIỆT NAM", "align": "center", "size": 11.5, "space_after": 1},
                            {"text": "PHƯỜNG THÀNH SEN", "align": "center", "size": 11.5, "space_after": 1},
                            {"text": "BAN THƯỜNG TRỰC", "bold": True, "align": "center", "size": 12, "space_after": 1},
                            {"text": "——————", "align": "center", "size": 9, "space_after": 1},
                            {"text": "Số: 20/KH-MTTQ-BTT", "align": "center", "size": 12, "space_after": 0}
                        ],
                        "right": [
                            {"text": "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "bold": True, "align": "center", "size": 11.5, "space_after": 1},
                            {"text": "Độc lập - Tự do - Hạnh phúc", "bold": True, "align": "center", "size": 12.5, "space_after": 1},
                            {"text": "————————————", "align": "center", "size": 9, "space_after": 2},
                            {"text": "Thành Sen, ngày 05 tháng 10 năm 2026", "italic": True, "align": "center", "size": 12.5, "space_after": 0}
                        ]
                    },
                    {"type": "heading", "text": "KẾ HOẠCH", "bold": True, "align": "center", "size": 14, "space_before": 4, "space_after": 2},
                    {"type": "heading", "text": "Tổ chức Ngày hội Đại đoàn kết toàn dân tộc ở khu dân cư năm 2026", "bold": True, "align": "center", "size": 13.5, "space_before": 0, "space_after": 6},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.15,
                        "space_after": 2,
                        "runs": [
                            {"text": "Thực hiện Hướng dẫn số 18/HD-MTTQ-BTT ngày 24/9/2026 của Ủy ban MTTQ Việt Nam tỉnh Hà Tĩnh về việc tổ chức Ngày hội Đại đoàn kết toàn dân tộc ở khu dân cư giai đoạn 2026-2031; và thực hiện các chủ trương Nghị quyết Đại hội đại biểu Đảng bộ các cấp nhiệm kỳ 2025-2030; Nghị quyết Đại hội đại biểu MTTQ Việt Nam các cấp, nhiệm kỳ 2025 - 2030 về phát huy sức mạnh đại đoàn kết toàn dân tộc, xây dựng đời sống hóa ở khu dân cư, xây dựng "},
                            {"text": "“nông thôn mới, đô thị văn minh”", "italic": True},
                            {"text": " và nâng cao đời sống Nhân dân; Kỷ niệm 96 năm Ngày truyền thống MTTQ Việt Nam (18/11/1930 - 18/11/2026); Ban Thường trực Ủy ban MTTQVN phường Thành Sen xây dựng kế hoạch triển khai thực hiện như sau:"}
                        ]
                    },
                    {"type": "heading", "text": "I. MỤC ĐÍCH, YÊU CẦU", "bold": True, "size": 13, "space_before": 3, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "1. Mục đích", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Cụ thể hóa chủ trương của Đảng, chính sách, pháp luật của Nhà nước về phát huy sức mạnh đại đoàn kết toàn dân tộc, xây dựng đời sống văn hóa và phát huy vai trò chủ thể của Nhân dân; triển khai thực hiện hiệu quả Nghị quyết Đại hội đại biểu Đảng bộ các cấp nhiệm kỳ 2025 - 2030 và Nghị quyết Đại hội đại biểu MTTQ Việt Nam các cấp, nhiệm kỳ 2025 - 2030.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tiếp tục phát huy truyền thống vẻ vang của Mặt trận Dân tộc thống nhất Việt Nam; củng cố, tăng cường khối đại đoàn kết toàn dân, tạo sự đồng thuận xã hội, phát huy quyền làm chủ, tinh thần tự quản, ý thức trách nhiệm của Nhân dân trong xây dựng quê hương Hà Tĩnh phát triển nhanh, bền vững.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Thông qua Ngày hội nhằm tuyên truyền, vận động Nhân dân thực hiện các chủ trương, đường lối của Đảng, chính sách pháp luật của Nhà nước; đánh giá kết quả thực hiện các cuộc vận động, phong trào thi đua yêu nước; biểu dương, tôn vinh các tập thể, gia đình, cá nhân tiêu biểu, những cách làm hay, mô hình hiệu quả, những người có nhiều đóng góp cho cộng đồng.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "2. Yêu cầu", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Ban Thường trực Uỷ ban MTTQ phường chỉ đạo Ban Công tác Mặt trận phối hợp các đồng chí trong liên đoàn cán bộ báo cáo cấp ủy phối hợp tổ chức thực hiện. Ngày hội “Đại đoàn kết toàn dân tộc” được tổ chức ở tất cả cộng đồng, khu dân cư trong toàn phường, huy động sự tham gia đông đảo các tầng lớp nhân dân tham gia. Việc tổ chức Ngày hội đảm bảo thiết thực tiết kiệm, an toàn, tránh hình thức, lãng phí.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Nội dung phần Lễ tổ chức trang trọng, ngắn gọn; nội dung phần Hội tạo được không khí vui tươi, đầm ấm và tôn vinh giá trị văn hóa truyền thống của dân tộc, tín ngưỡng tôn giáo, vùng, miền.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "II. NỘI DUNG CỤ THỂ", "bold": True, "size": 13, "space_before": 3, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "1. Công tác tuyên truyền", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "1.1. Nội dung tuyên truyền", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Truyền thống lịch sử vẻ vang của Mặt trận Tổ quốc Việt Nam qua các thời kỳ; ý nghĩa, vai trò của Ngày hội “Đại đoàn kết toàn dân tộc”.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tuyên truyền chủ trương, đường lối của Đảng, chính sách, pháp luật của Nhà nước; Nghị quyết Đại hội đại biểu toàn quốc lần thứ XIV của Đảng; Nghị quyết Đại hội đại biểu Đảng bộ các cấp, nhiệm kỳ 2025 - 2030; Nghị quyết Đại hội đại biểu MTTQ Việt Nam các cấp nhiệm kỳ 2025 - 2030. Ôn lại truyền thống 96 năm hình thành và phát triển của Mặt trận Tổ quốc Việt Nam (18/11/1930 - 18/11/2026) và kết quả xây dựng khối đại đoàn kết toàn dân tộc.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tuyên truyền kết quả thực hiện nội dung các cuộc vận động, phong trào thi đua yêu nước do MTTQ Việt Nam các cấp chủ trì, phối hợp thực hiện.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tuyên truyền gương người tốt, việc tốt; các tập thể, cá nhân tiêu biểu trong thực hiện các cuộc vận động, các phong trào thi đua và nhiệm vụ chính trị của địa phương.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "1.2. Hình thức, nội dung tuyên truyền", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tuyên truyền trên hệ thống phát thanh, truyền hình, báo chí, hệ thống truyền thanh cơ sở, cổng thông tin điện tử, trang Fanpage, mạng xã hội của MTTQ Việt Nam các cấp, các tổ chức thành viên, các cơ quan, đơn vị, tổ chức và mỗi cá nhân.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tuyên truyền thông qua cuộc họp, sinh hoạt của Nhân dân, sinh hoạt của các tổ chức đoàn thể tại khu dân cư.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tổ chức treo băng rôn, khẩu hiệu, pano, áp phích, cờ, hoa tại khu dân cư, địa điểm tổ chức Ngày hội, trung tâm văn hóa - xã hội và các cơ quan, đơn vị, trường học; tổ chức hoạt động văn hóa, văn nghệ, dân vũ, thể thao;", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Vận động các hộ gia đình treo cờ Tổ quốc trong dịp tổ chức Ngày hội từ ngày 01/11/2026 đến hết ngày 18/11/2026.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "2. Khẩu hiệu tuyên truyền", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Kỷ niệm 96 năm Ngày truyền thống MTTQ Việt Nam (18/11/1930 - 18/11/2026)!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Phát huy sức mạnh đại đoàn kết toàn dân tộc vì sự nghiệp dân giàu, nước mạnh, dân chủ, công bằng, văn minh!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Nhiệt liệt chào mừng Ngày hội đại đoàn kết toàn dân tộc!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Sống, chiến đấu, lao động, học tập và làm theo tư tưởng, đạo đức, phong cách Hồ Chí Minh!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Chủ tịch Hồ Chí Minh vĩ đại sống mãi trong sự nghiệp của chúng ta!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Đoàn kết, đoàn kết, đại đoàn kết. Thành công, thành công, đại thành công!", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Toàn dân đoàn kết xây dựng nông thôn mới đô thị văn minh.", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Quyết tâm xây dựng phường Thành Sen ngày càng giàu đẹp văn minh.", "italic": True, "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "3. Tổ chức Ngày hội Đại đoàn kết", "bold": True, "size": 13, "space_before": 2, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "3.1. Thời gian", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Ngày hội và các hoạt động tổ chức Ngày hội diễn ra cao điểm từ ngày 01/11 đến hết ngày 18/11/2026.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.12,
                        "space_after": 2,
                        "runs": [
                            {"text": "- Các tổ dân phố đăng ký lịch tổ chức Ngày hội về Ban Thường trực Uỷ ban MTTQ phường trước ngày 20/10/2026 "},
                            {"text": "(Qua đồng chí Nguyễn Thị Mai, SĐT: 0912.488235)", "italic": True},
                            {"text": ". Trên cơ sở lịch đã đăng ký, Ban Thường trực Uỷ ban MTTQ phường sắp xếp thời gian đảm bảo phù hợp, tránh chồng chéo để các đoàn công tác của Ban Thường vụ Đảng uỷ tham dự."}
                        ]
                    },
                    {"type": "heading", "text": "3.2. Hình thức và chủ trì tổ chức Ngày hội", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Hình thức tổ chức: Ngày hội được tổ chức ở địa bàn khu dân cư; tùy theo điều kiện ở mỗi khu dân cư có thể lựa chọn hình thức phù hợp.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Chủ trì tổ chức Ngày hội: Do Ban công tác Mặt trận chủ trì, phối hợp với tổ dân phố.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "3.3. Thành phần tham gia Ngày hội", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Liên đoàn cán bộ Tổ dân phố và toàn thể Nhân dân hoặc đại diện hộ gia đình ở khu dân cư.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Mời đại diện lãnh đạo các cơ quan, đơn vị, lực lượng vũ trang đóng trên địa bàn tổ dân phố; đại diện các tổ chức, doanh nghiệp, cá nhân có hoạt động hỗ trợ, đóng góp cho cộng đồng dân cư.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Mời đại diện Đoàn công tác của Ban Thường vụ Đảng ủy chỉ đạo các TDP; đại diện lãnh đạo cấp ủy, chính quyền, Mặt trận Tổ quốc và các đoàn thể chính trị - xã hội, cán bộ công chức phường.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "3.4. Hình thức trang trí", "bold": True, "italic": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Treo cờ, băng rôn, khẩu hiệu tại Nhà văn hóa, các điểm công cộng, các tuyến đường chính trên địa bàn khu dân cư và địa điểm tổ chức các hoạt động Ngày hội.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.12,
                        "space_after": 3,
                        "runs": [
                            {"text": "- Ma két trang trí nơi tổ chức phần Lễ của Ngày hội: Đối với địa bàn dân cư "},
                            {"text": "(do Ban Công tác Mặt trận chủ trì)", "italic": True},
                            {"text": ":"}
                        ]
                    },
                    {
                        "type": "maket_box",
                        "items": [
                            {"text": "Cờ Tổ quốc, ảnh Bác", "align": "left", "size": 12, "space_after": 1},
                            {"text": "(Logo Mặt trận Tổ quốc Việt Nam)", "align": "center", "size": 12, "space_after": 6},
                            {"text": "NGÀY HỘI", "bold": True, "align": "center", "size": 13, "space_after": 1},
                            {"text": "ĐẠI ĐOÀN KẾT TOÀN DÂN TỘC", "bold": True, "align": "center", "size": 13.5, "space_after": 1},
                            {"text": "Tổ dân phố..., phường Thành Sen", "bold": True, "align": "center", "size": 12.5, "space_after": 8},
                            {"text": "Thành Sen, ngày ... tháng 11 năm 2026", "italic": True, "align": "right", "size": 12, "space_after": 1}
                        ]
                    },
                    {"type": "paragraph", "text": "(Lưu ý: maket nền đỏ chữ vàng, có thể phối hình hoa sen phía dưới)", "italic": True, "align": "center", "size": 12, "space_before": 2, "space_after": 3},
                    {"type": "heading", "text": "3.5. Chương trình Ngày hội", "bold": True, "italic": True, "size": 13, "space_before": 2, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "first_indent": 28,
                        "space_after": 2,
                        "runs": [
                            {"text": "* Phần Lễ ", "bold": True},
                            {"text": "(Tổ chức không quá 90 phút)", "italic": True},
                            {"text": ":", "bold": True}
                        ]
                    },
                    {
                        "type": "paragraph",
                        "first_indent": 28,
                        "space_after": 2,
                        "runs": [
                            {"text": "(1) Văn nghệ chào mừng "},
                            {"text": "(từ 4-5 tiết mục có lựa chọn chuẩn bị chu đáo)", "italic": True},
                            {"text": "."}
                        ]
                    },
                    {"type": "paragraph", "text": "(2) Chào cờ.", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(3) Tuyên bố lý do giới thiệu đại biểu", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(4) Ôn lại truyền thống 96 năm Ngày Thành lập Mặt trận Dân tộc thống nhất Việt Nam - Ngày truyền thống Mặt trận Tổ quốc Việt Nam; báo cáo khái quát kết quả thực hiện nhiệm vụ xây dựng khối đại đoàn kết toàn dân tộc;", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.12,
                        "space_after": 2,
                        "runs": [
                            {"text": "- Kết quả thực hiện các cuộc vận động, phong trào thi đua yêu nước sau 01 năm thực hiện, trọng tâm là Cuộc vận động “Toàn dân đoàn kết xây dựng nông thôn mới, đô thị văn minh” (có nêu các tập thể, hộ gia đình, cá nhân tiêu biểu có nhiều đóng góp xây dựng cộng đồng dân cư); mục tiêu và cách thức thực hiện trong thời gian tới. "},
                            {"text": "(Khuyến khích xây dựng báo cáo bằng video, hình ảnh và ứng dụng công nghệ chuyển đổi số)", "italic": True, "bold": True}
                        ]
                    },
                    {"type": "paragraph", "text": "(5) Trao đổi, thảo luận.", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(6) Thông qua quyết định công nhận gia đình văn hóa năm 2026; biểu dương, tôn vinh, khen thưởng những tập thể, gia đình và cá nhân tiêu biểu.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(7) Mời lãnh đạo cấp trên phát biểu, tặng quà (nếu có).", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(8) Phát động hưởng ứng phong trào thi đua xây dựng khu dân cư đoàn kết, an toàn, ấm no, hạnh phúc.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "(9) Phát biểu cảm ơn và kết thúc buổi Lễ.", "size": 13, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.12,
                        "space_after": 2,
                        "runs": [
                            {"text": "* Phần Hội ", "bold": True},
                            {"text": "(Có thể tổ chức trước hoặc sau phần Lễ)", "italic": True},
                            {"text": ": Tùy điều kiện từng khu dân cư, để lựa chọn, tổ chức các hoạt động phù hợp."}
                        ]
                    },
                    {"type": "paragraph", "text": "- Tổ chức các hoạt động văn hóa, thể dục, thể thao, các trò chơi dân gian truyền thống của địa phương, sinh hoạt ngoài trời, các hoạt động dân vũ...", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tùy từng điều kiện các khu dân cư có thể tổ chức “Bữa cơm đoàn kết” phù hợp và ý nghĩa thiết thực.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Khuyến khích các khu dân cư có sáng kiến, đổi mới tổ chức phần Hội đảm bảo vui tươi, an toàn, lành mạnh, tiết kiệm, phù hợp với điều kiện, phong tục, tập quán của địa phương.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "III. TỔ CHỨC THỰC HIỆN", "bold": True, "size": 13, "space_before": 3, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "1. Ban Thường trực Uỷ ban MTTQ phường", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Hướng dẫn Ban Công tác Mặt trận các khu dân cư triển khai tổ chức Ngày hội “Đại đoàn kết toàn dân tộc” phù hợp với tình hình thực tế của địa phương, đơn vị đảm bảo thời gian quy định.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tham mưu Thường trực Đảng ủy phân công các đồng chí trong Ban Thường vụ, Đoàn công tác của Ban Thường vụ Đảng ủy thực hiện nhiệm vụ chỉ đạo, kiểm tra và tham dự Ngày hội tại các khu dân cư.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Phối hợp với Phòng Văn hoá - Xã hội tổ chức bình xét, công nhận danh hiệu “Gia đình văn hóa”; danh hiệu, tổ dân phố văn hóa để công bố và biểu dương trong dịp tổ chức Ngày hội.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "2. Ban Công tác Mặt trận các tổ dân phố", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Ban Công tác Mặt trận phối hợp chặt chẽ với tổ dân phố, các chi hội, chi đoàn trong tổ chức Ngày hội.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tổ chức tuyên truyền, vận động Nhân dân hoàn thành chương trình mục tiêu năm 2026 theo Nghị quyết của HĐND phường; tổ chức các hoạt động hướng về kỷ niệm 96 năm ngày thành lập MTTQ Việt Nam.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "paragraph", "text": "- Tổ chức tốt Ngày hội “Đại đoàn kết toàn dân tộc” và triển khai vận động ủng hộ Quỹ \"Vì người nghèo\" năm 2026 từ ngày 17/10/2026 đến 18/11/2026.", "align": "justify", "size": 13, "space_after": 2, "first_indent": 28},
                    {"type": "heading", "text": "3. Về thông tin báo cáo", "bold": True, "size": 13, "space_before": 1, "space_after": 2, "first_indent": 28},
                    {
                        "type": "paragraph",
                        "align": "justify",
                        "first_indent": 28,
                        "line_spacing": 1.12,
                        "space_after": 2,
                        "runs": [
                            {"text": "- Ban Công tác Mặt trận các tổ dân phố: Cập nhật thông tin về tình hình tổ chức Ngày hội trước 15h00 hàng ngày (Từ ngày 05/11/2026 - 18/11/2026) và báo cáo kết quả tổ chức thực hiện "},
                            {"text": "(Có phụ lục gửi kèm)", "italic": True},
                            {"text": " về Ban Thường trực Uỷ ban MTTQ phường trước ngày 19/11/2026."}
                        ]
                    },
                    {"type": "paragraph", "text": "- Ban Thường trực Uỷ ban MTTQ phường thường xuyên cập nhật thông tin về tình hình tổ chức Ngày hội; tổng hợp tình hình, kết quả tổ chức Ngày hội báo cáo Ban Thường trực Ủy ban MTTQ Tỉnh và Ban Thường vụ Đảng ủy trước ngày 19/11/2026.", "align": "justify", "size": 13, "space_after": 3, "first_indent": 28},
                    {"type": "paragraph", "text": "Trên đây là kế hoạch tổ chức Ngày hội đại đoàn kết toàn dân tộc và các hoạt động kỷ niệm 96 năm ngày truyền thống MTTQ Việt Nam của Ủy ban MTTQ phường Thành Sen./.", "italic": True, "align": "justify", "size": 13, "space_before": 2, "space_after": 8, "first_indent": 28},
                    {
                        "type": "signature_block",
                        "recipients": [
                            {"text": "Nơi nhận:", "bold": True, "italic": True, "size": 12, "space_after": 1},
                            {"text": "- BTT UBMTTQ tỉnh (để báo cáo);", "size": 11, "space_after": 1},
                            {"text": "- Ban Thường vụ, Ban Chấp hành Đảng ủy;", "size": 11, "space_after": 1},
                            {"text": "- Ban XD Đảng, UBKT, VP Đảng ủy;", "size": 11, "space_after": 1},
                            {"text": "- Ban Thường trực UBMTTQ phường;", "size": 11, "space_after": 1},
                            {"text": "- Ban CTMT, Tổ trưởng các TDP;", "size": 11, "space_after": 1},
                            {"text": "- Lưu: VT.", "size": 11, "space_after": 1}
                        ],
                        "signatory": [
                            {"text": "TM. BAN THƯỜNG TRỰC", "bold": True, "align": "center", "size": 13, "space_after": 1},
                            {"text": "CHỦ TỊCH", "bold": True, "align": "center", "size": 13, "space_after": 1},
                            {"is_space": True, "space": 35},
                            {"text": "Nguyễn Thị Hồng Minh", "bold": True, "align": "center", "size": 13.5, "space_before": 0, "space_after": 0}
                        ]
                    }
                ]
            },
            # TRANG 6 (Landscape Table Phụ Lục)
            {
                "orientation": "landscape",
                "elements": [
                    {
                        "type": "header_table",
                        "left": [
                            {"text": "ỦY BAN MTTQ VIỆT NAM", "align": "center", "size": 10.5, "space_after": 1},
                            {"text": "PHƯỜNG THÀNH SEN", "align": "center", "size": 10.5, "space_after": 1},
                            {"text": "BAN CTMT TDP ........", "bold": True, "align": "center", "size": 11, "space_after": 1}
                        ],
                        "right": [
                            {"text": "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "bold": True, "align": "center", "size": 11, "space_after": 1},
                            {"text": "Độc lập – Tự do – Hạnh phúc", "bold": True, "align": "center", "size": 11.5, "space_after": 1},
                            {"text": "————————————", "align": "center", "size": 8, "space_after": 1}
                        ]
                    },
                    {"type": "heading", "text": "BẢNG TỔNG HỢP", "bold": True, "align": "center", "size": 12.5, "space_before": 2, "space_after": 1},
                    {"type": "heading", "text": "KẾ QUẢ NGÀY HỘI ĐẠI ĐOÀN KẾT TOÀN DÂN TỘC NĂM 2026", "bold": True, "align": "center", "size": 12.5, "space_after": 1},
                    {"type": "paragraph", "text": "(Kèm theo kế hoạch số 20/KH-MTTQ-BTT, ngày 05/10/2026 của Ban Thường trực Ủy ban MTTQ phường Thành Sen)", "italic": True, "align": "center", "size": 10.5, "space_after": 4},
                    {
                        "type": "table",
                        "col_widths": [16, 13, 11, 11, 13, 15, 15, 13, 16, 15, 13, 10, 13, 14, 14, 14, 13, 12, 15, 15],
                        "rows": [
                            # Row 0
                            {
                                "cells": [
                                    {"row": 0, "col": 0, "rowspan": 3, "colspan": 1, "text": "Tổ\ndân\nphố", "align": "center", "size": 8},
                                    {"row": 0, "col": 1, "rowspan": 1, "colspan": 19, "text": "HOẠT ĐỘNG TỔ CHỨC NGÀY HỘI", "bold": True, "align": "center", "size": 9.5}
                                ]
                            },
                            # Row 1
                            {
                                "cells": [
                                    {"row": 1, "col": 1, "rowspan": 2, "colspan": 1, "text": "Tổ\nchức\ncả\nphần\nLễ và\nphần\nHội\n(Đánh\ndấu X)", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 2, "rowspan": 2, "colspan": 1, "text": "Tổ\nchức\nphần\nLễ\n\n(Đánh\ndấu\nX)", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 3, "rowspan": 2, "colspan": 1, "text": "Tổ\nchức\nphần\nHội\n\n(Đánh\ndấu X)", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 4, "rowspan": 2, "colspan": 1, "text": "Số tổ\nliên\ngia tổ\nchức\nbữa\ncơm\nĐại\nđoàn\nkết", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 5, "rowspan": 2, "colspan": 1, "text": "Số tập\nthể tiêu\nbiểu\nđược biểu\ndương,\nkhen\nthưởng\ntrong\nNgày hội/\nKinh phí", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 6, "rowspan": 2, "colspan": 1, "text": "Số hộ gia\nđình tiêu\nbiểu\nđược biểu\ndương\nkhen\nthưởng\ntrong\nNgày hội/\nKinh phí", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 7, "rowspan": 2, "colspan": 1, "text": "Số cá\nnhân\nđược\nbiểu\ndương,\nkhen\nthưởng\ntrong\nNgày\nhội/\nKinh phí", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 8, "rowspan": 2, "colspan": 1, "text": "Tổng kinh\nphí biểu\ndương,\nkhen\nthưởng\ncho các\ntập thể, hộ\ngia đình,\ncá nhân\ntiêu biểu...\n(=6+7+8)", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 9, "rowspan": 2, "colspan": 1, "text": "Số cá\nnhân\nđược\nthăm hỏi,\nđộng\nviên\ntrong dịp\ntổ chức\nNgày\nhội/\nSố tiền\nthực hiện", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 10, "rowspan": 2, "colspan": 1, "text": "Ước\nlượng\ntổng số\nngười\ntham\ndự\nNgày\nhội\ntrên địa\nbàn", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 11, "rowspan": 1, "colspan": 5, "text": "Tổng số lượt lãnh đạo các cấp\ntrong tỉnh, phường tham dự Ngày hội", "align": "center", "size": 8},
                                    {"row": 1, "col": 16, "rowspan": 2, "colspan": 1, "text": "Tổng\nsố\ncông\ntrình\ndân\nsinh\nđược\nxây\ndựng\ntrong\ndịp tổ\nchức\nNgày\nhội", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 17, "rowspan": 2, "colspan": 1, "text": "Tổng\nsố\ncác\nmô\nhình\nđược\nxây\ndựng\nvà\nnâng\ncao", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 18, "rowspan": 2, "colspan": 1, "text": "Tổng\nsố nhà\nĐại\nđoàn\nkết\nđược\nxây\nmới\n(căn)/\ntổng\nkinh\nphí", "align": "center", "size": 7.5},
                                    {"row": 1, "col": 19, "rowspan": 2, "colspan": 1, "text": "Tổng số\nnhà Đại\nđoàn kết\nđược\nsửa\nchữa\n(căn)/\ntổng\nkinh phí", "align": "center", "size": 7.5}
                                ]
                            },
                            # Row 2
                            {
                                "cells": [
                                    {"row": 2, "col": 11, "rowspan": 1, "colspan": 1, "text": "Tổng\nsố", "align": "center", "size": 7},
                                    {"row": 2, "col": 12, "rowspan": 1, "colspan": 1, "text": "Lãnh\nđạo\ncấp\ntrung\nương\ntham\ndự\nngày\nhội\n(lượt\ndự)", "italic": True, "align": "center", "size": 7},
                                    {"row": 2, "col": 13, "rowspan": 1, "colspan": 1, "text": "Lãnh\nđạo\nBTV,\nBCH\nCấp\ntỉnh\n(tổng\nsố lãnh\nđạo/\nlượt\ndự)", "italic": True, "align": "center", "size": 7},
                                    {"row": 2, "col": 14, "rowspan": 1, "colspan": 1, "text": "Lãnh\nđạo\ncác cơ\nquan\ncấp sở\n(tổng\nsố lãnh\nđạo/\nlượt\ndự)", "italic": True, "align": "center", "size": 7},
                                    {"row": 2, "col": 15, "rowspan": 1, "colspan": 1, "text": "Lãnh\nđạo\ncấp xã\ndự\nNgày\nhội\n(tổng\nsố lãnh\nđạo/\nlượt\ndự)", "italic": True, "align": "center", "size": 7}
                                ]
                            },
                            # Row 3 (Numbering)
                            {
                                "cells": [
                                    {"row": 3, "col": 0, "colspan": 1, "text": "1", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 1, "colspan": 1, "text": "2", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 2, "colspan": 1, "text": "3", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 3, "colspan": 1, "text": "4", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 4, "colspan": 1, "text": "5", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 5, "colspan": 1, "text": "6", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 6, "colspan": 1, "text": "7", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 7, "colspan": 1, "text": "8", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 8, "colspan": 1, "text": "9", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 9, "colspan": 1, "text": "10", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 10, "colspan": 1, "text": "11", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 11, "colspan": 5, "text": "12", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 16, "colspan": 1, "text": "13", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 17, "colspan": 1, "text": "14", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 18, "colspan": 1, "text": "15", "italic": True, "align": "center", "size": 8},
                                    {"row": 3, "col": 19, "colspan": 1, "text": "16", "italic": True, "align": "center", "size": 8}
                                ]
                            },
                            # Row 4 (Empty data row)
                            {"height_val": "320", "cells": []},
                            # Row 5 (Empty data row)
                            {"height_val": "320", "cells": []}
                        ]
                    }
                ]
            }
        ]
    }
