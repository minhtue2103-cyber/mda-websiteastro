
# TÀI LIỆU CƠ SỞ (BASE KNOWLEDGE) - HỆ THỐNG AI KIỂM TRA CHỨNG TỪ XNK

## 1. Thông tin Doanh nghiệp & Sản phẩm Cốt lõi
*   **Danh mục sản phẩm/Dịch vụ:**
    *   Thương mại & Xuất khẩu: Nông sản chế biến giá trị cao, chủ lực là trái cây sấy thăng hoa.
    *   Dịch vụ Công nghệ & Đào tạo: Cung cấp các gói tư vấn tích hợp AI và đào tạo vận hành quy trình xuất nhập khẩu an toàn cho nhóm doanh nghiệp SME.
*   **Thị trường mục tiêu & Rào cản:** Tập trung vào Mỹ, Canada, EU và Úc. Rào cản lớn nhất là các chứng nhận chất lượng (FDA, HACCP, GlobalGAP), tiêu chuẩn kiểm dịch thực vật khắt khe, và đặc biệt là rào cản về **bảo mật dữ liệu thương mại (Data Privacy)** theo chuẩn quốc tế (như GDPR của EU).
*   **Mã HS Code chủ lực:** Trái cây sấy (0813.40, 2008.99), Gạo (1006).

## 2. Kiến trúc Công nghệ & Tự động hóa
*   **Mô hình triển khai:** Áp dụng luồng **Agentic AI** chạy theo cấu trúc **Middleware độc lập (Local AI)**. Hệ thống là lớp màng lọc ở giữa, không can thiệp sâu hay ghi đè lên dữ liệu của phần mềm quản trị (ERP) hiện tại.
*   **Bảo mật dữ liệu (Data Masking khắt khe):** Đây là tấm khiên bảo vệ sống còn. Mọi thông tin nhạy cảm (Định danh PII, thông tin khách hàng, đơn giá, giá trị lô hàng) đều được hệ thống tự động che giấu/xóa bỏ cục bộ (Local) trước khi AI tiến hành phân tích. Điều này triệt tiêu hoàn toàn rủi ro rò rỉ dữ liệu thương mại, bảo vệ doanh nghiệp khỏi các án phạt vi phạm bảo mật của đối tác nước ngoài.
*   **Luồng xử lý chứng từ:**
    1. Tiếp nhận chứng từ (Commercial Invoice, Packing List, B/L, C/O, Phytosanitary, L/C MT700).
    2. Bóc tách dữ liệu và che giấu thông tin mật.
    3. AI Agent đối chiếu chéo các điểm xung đột dựa trên luật Incoterms 2020 và UCP 600.
    4. Trích xuất **Báo cáo Phân tích Rủi ro** để nhân sự xét duyệt (Human-in-the-Loop).

## 3. Khung Dịch vụ & Điều kiện Triển khai (Go-to-Market)
*   **Các gói dịch vụ cung cấp:**
    1.  **Gói Đào tạo nhân sự In-house:** Xây dựng năng lực "Kiểm soát hệ thống AI" cho nhân viên chứng từ, dạy cách quản lý ngoại lệ và vận hành luồng Agentic an toàn.
    2.  **Gói Tư vấn SOP quy trình:** Tái cấu trúc và chuẩn hóa quy trình xử lý chứng từ truyền thống để sẵn sàng ứng dụng công nghệ.
    3.  **Gói Chuyển giao công nghệ Local AI:** Cài đặt luồng kiểm tra chứng từ an toàn ngay tại hạ tầng của doanh nghiệp.
*   **Chi phí & Lộ trình triển khai:** 
    *   Chưa áp dụng báo giá đóng gói sẵn. 
    *   Lộ trình tiêu chuẩn là **30 ngày đầu tiên (Discovery Phase)** để khảo sát, hiểu rõ hệ thống/văn hóa của doanh nghiệp và xây dựng bản kế hoạch tích hợp (Integration Plan). Chi phí cụ thể sẽ được thiết lập sau giai đoạn này dựa trên mức độ phức tạp.
*   **Điều kiện tiên quyết đối với SME (Data Readiness):** 
    *   **Về Quy trình:** Doanh nghiệp bắt buộc phải chuẩn hóa và làm rõ luồng dữ liệu hiện tại (từ lúc nhập liệu vào ERP -> nhân viên xử lý -> kết xuất báo cáo) *trước* khi đưa AI vào.
    *   **Về Dữ liệu đầu vào:** Chứng từ mẫu phải đạt chuẩn. File scan phải có chất lượng cao, rõ nét, không bị nghiêng/lệch góc. AI không giải quyết các dữ liệu rác hoặc ảnh chụp mờ nhòe, rung lắc.

## 4. Triết lý Phân quyền & Quản lý Ngoại lệ (Exception Management)
*   **Nguyên tắc cốt lõi:** AI tuyệt đối **không phải** là người ra quyết định cuối cùng. AI đóng vai trò như một chuyên gia mẫn cán, có nhiệm vụ phát hiện rủi ro, đưa ra gợi ý và các lựa chọn.
*   **Phân luồng xử lý:**
    *   *Nhiệm vụ phức tạp/rủi ro cao (Đánh giá L/C, Hợp đồng):* AI xuất báo cáo gắn cờ cảnh báo (Red Flag). Con người nắm 100% quyền ra quyết định cuối cùng.
    *   *Nhiệm vụ lặp lại/đơn giản:* Con người có thể ủy quyền cho AI tự động xử lý và trích xuất dữ liệu, nhưng áp dụng cơ chế **kiểm tra chéo ngẫu nhiên định kỳ (Random Audit)** để giám sát chất lượng.
*   **Đào tạo nhân sự:** Sự khác biệt của nhân sự XNK thời AI là năng lực biết lúc nào nên tin AI, lúc nào cần bác bỏ (Quản trị ngoại lệ), thay vì phó mặc toàn bộ cho máy móc.

## 5. Kịch bản Thực chứng (Use-Cases & Success Stories)
*   **Use-Case 1: Vượt qua bài toán rò rỉ dữ liệu với đối tác EU**
    *   *Bối cảnh:* Một doanh nghiệp nông sản cần kiểm tra hợp đồng ngoại thương và L/C từ một siêu thị lớn tại Đức, nhưng đối tác quy định rất khắt khe về việc cấm đưa dữ liệu lên các nền tảng Cloud/AI công cộng.
    *   *Giải pháp:* Luồng Middleware Local AI được kích hoạt. Tính năng Data Masking tự động bôi đen toàn bộ số tài khoản, tên giám đốc siêu thị và đơn giá mua hàng. AI chỉ đọc các điều khoản vận tải và mô tả hàng hóa.
    *   *Kết quả:* Doanh nghiệp phát hiện ra một điều khoản gài bẫy về trách nhiệm bốc dỡ tại cảng đích (DAP), đồng thời vẫn tuân thủ 100% chuẩn mực bảo mật GDPR, giữ vững uy tín với đối tác EU.
*   **Use-Case 2: Cứu bàn thua trễ hạn giao hàng (ETD) do sai lệch chứng từ**
    *   *Bối cảnh:* Nhân viên chứng từ làm song song 15 bộ hồ sơ, vô tình bỏ qua việc ngày dự kiến tàu chạy (ETD) do Forwarder báo (Booking Note) trễ hơn 2 ngày so với Hạn chót giao hàng (Latest Date of Shipment) ghi trong Field 44C của L/C.
    *   *Giải pháp:* AI Agent rà soát chéo giữa Booking Note và L/C. Nhờ phát hiện mâu thuẫn thời gian, hệ thống bật cảnh báo (Red flag) trước khi doanh nghiệp xác nhận chốt bill với hãng tàu.
    *   *Kết quả:* Nhân viên kịp thời yêu cầu Forwarder đổi chuyến tàu sớm hơn, giúp doanh nghiệp tránh bị ngân hàng phạt lỗi bất hợp lệ L/C (tiết kiệm ~100 USD phí tu chỉnh) và loại bỏ rủi ro bị người mua từ chối thanh toán.

## 6. Ma Trận Thông Tin (Canonical Matrix)

| Nhóm dữ liệu (Category) | Tên Biến / Thông điệp (Variable) | Giá trị Chuẩn / Bắt buộc (Canonical Value) | Các từ/giá trị BỊ CẤM (Anti-patterns / Forbidden) | Căn cứ / Ngữ cảnh áp dụng (Context / Source) |
| :--- | :--- | :--- | :--- | :--- |
| **Định vị & Thuật ngữ** | Cấu trúc giải pháp AI | Middleware AI, Local AI, Luồng Agentic AI | AI Public, Plugin ghi đè ERP, Hệ thống All-in-one | Áp dụng cho các câu hỏi How_To / Kiến trúc hệ thống. |
| **Bảo mật & Rủi ro** | Bảo vệ dữ liệu (Data Masking) | Che giấu dữ liệu nhạy cảm cục bộ. Triệt tiêu rủi ro rò rỉ thông tin, tuân thủ tiêu chuẩn EU, Mỹ, Úc. | Phớt lờ rủi ro lộ data, Upload file PDF nguyên bản cho AI phân tích | Trả lời các câu hỏi Risk (Rủi ro vi phạm bảo mật, lộ giá CIF/FOB). |
| **Dịch vụ & Chi phí** | Lộ trình & Báo giá triển khai | Lộ trình 30 ngày khảo sát & lập kế hoạch. Không có giá đóng gói chung, may đo theo doanh nghiệp. | Báo giá cố định rẻ mạt, Cam kết triển khai trong 1-2 ngày | Áp dụng cho câu hỏi về Cost / Vendor (Đánh giá nhà tư vấn). |
| **Vận hành & Yêu cầu** | Điều kiện đầu vào (Data Readiness) | Luồng ERP minh bạch. File chứng từ scan chất lượng cao, chuẩn quy cách. | Đưa ảnh mờ, nhòe, méo lệch cho AI tự sửa, Hệ thống doanh nghiệp lộn xộn vẫn ráp AI được | Trả lời nhóm câu hỏi Requirements (SME cần chuẩn bị gì trước khi làm AI). |
| **Phân quyền AI** | Quyền quyết định (Decision Making) | AI là trợ lý gợi ý (Gắn cờ/Báo cáo). Con người ra quyết định (100% với task khó, Random Audit với task dễ). | AI ra quyết định cuối cùng, Tự động hóa 100% thay thế con người | Thể hiện triết lý Human-in-the-Loop trong các câu hỏi Troubleshooting. |
| **Tuyển dụng & Đào tạo** | Tiêu chuẩn nhân sự thời AI | Kỹ năng "Quản lý ngoại lệ" (Exception Management), khả năng nhận định khi nào AI sai để can thiệp. | Biết gõ Excel nhanh, Thuộc lòng sách vở, Tin tưởng tuyệt đối vào kết quả của AI | Trả lời các câu hỏi về định hướng nghề nghiệp, xu hướng tuyển dụng Logistics. |