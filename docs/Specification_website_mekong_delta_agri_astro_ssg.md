# TÀI LIỆU ĐẶC TẢ THIẾT KẾ WEBSITE (WEBSITE DESIGN SPECIFICATION)
**Thương hiệu:** Mekong Delta Agri — MDA Agro-Export Knowledge Hub (Minh Tam Trading / MD AGRI TRADING CO., LTD)  
**Mô hình:** Trung tâm Tri thức, Tư vấn Tuân thủ Pháp lý, Đào tạo Xuất Nhập Khẩu Nông sản & Ứng dụng AI  
**Tên miền chính thức:** `https://mekongdeltaagri.com`  
**Hạ tầng lưu trữ (Hosting):** Giữ nguyên Hosting hiện tại (Static Export `dist/` vận hành trên Apache / LiteSpeed / cPanel hoặc Nginx kèm cấu hình `.htaccess`)  
**Nền tảng công nghệ:** Astro 4.x / 5.x (SSG - `output: 'static'`) + TypeScript + Vanilla CSS Tokens  
**Phiên bản:** 3.0 (Chuyển đổi từ WordPress sang Astro SSG, Việt hóa toàn diện, Chuẩn hóa Spacing & Tích hợp SEO/GEO/Agentic Web)

---

## 1. TỔNG QUAN DỰ ÁN, ĐỊNH VỊ & SITEMAP HỆ THỐNG

### 1.1. Mục tiêu Chuyển đổi (WordPress $\rightarrow$ Astro SSG)
1. **Hiệu năng & Bảo mật tuyệt đối trên Hosting cũ:** Loại bỏ hoàn toàn sự nặng nề của database MySQL và các plugin WordPress/Elementor. Website được biên dịch trước thành 100% HTML/CSS tĩnh (`dist/`), tải lên trực tiếp thư mục `public_html` của hosting hiện tại, đạt tốc độ phản hồi tức thì (LCP < 0.8s) và miễn nhiễm với lỗ hổng bảo mật PHP/WordPress.
2. **Bảo toàn Thiết kế & Bản sắc Trang chủ (`mekongdeltaagri.com`):** Giữ nguyên cấu trúc bố cục, luồng câu chuyện, hệ màu nông nghiệp bền vững và hình ảnh đặc trưng của trang Home hiện tại; đồng thời **chuẩn hóa toàn bộ hệ thống lưới (Grid), khoảng cách (Padding/Margin)** và **Việt hóa 100% nội dung** theo văn phong chuyên gia Xuất Nhập Khẩu (XNK) & AI thực chiến.
3. **Chuẩn hóa Typography & GEO/Agentic Web:** Áp dụng bộ font `'Merriweather'` (Heading) và `'Source Serif 4'` (Body), quy chuẩn đường gạch chân tiêu đề `#8DC435`, cấu trúc **BLUF (Bottom Line Up Front)**, dữ liệu có cấu trúc Schema.org, cùng giao thức **`llms.txt`** và **ARD (`ai-catalog.json`, `ard.json`)** giúp các công cụ AI (ChatGPT Search, Perplexity, Google AI Overviews) trích dẫn `mekongdeltaagri.com` làm nguồn tham chiếu uy tín hàng đầu tại Việt Nam.

### 1.2. Định vị Thương hiệu & SEO Metadata Chuẩn Tiếng Việt
* **Tagline định vị:** Hệ sinh thái Tri thức Chứng từ Thương mại, Tư vấn Tuân thủ Quốc tế (FDA, BICON, SPS) & Đào tạo Ứng dụng AI cho Doanh nghiệp Xuất Nhập Khẩu Nông sản Việt Nam.
* **SEO Metadata Trang chủ:**
  - **SEO Title:** `Mekong Delta Agri (MDA Hub) | Đào tạo XNK Thực chiến, Tư vấn Pháp lý & Ứng dụng AI Nông sản`
  - **Meta Description:** `Hệ sinh thái tri thức và đào tạo Xuất Nhập Khẩu nông sản hàng đầu Việt Nam. Tư vấn chứng từ thương mại, mã HS, tuân thủ tiêu chuẩn FDA/BICON/SPS và đào tạo ứng dụng AI & AI Marketing chuyên sâu cho doanh nghiệp XNK.`
* **Thông tin Pháp nhân & Liên hệ Cốt lõi (Chuẩn hóa từ site hiện tại):**
  - **Đơn vị chủ quản:** Công ty TNHH Thương mại MD AGRI (MD AGRI TRADING CO., LTD - Minh Tam Trading)
  - **Địa chỉ:** Tầng 1, 53/104 Trần Khánh Dư, Phường Tân Định, Quận 1, TP. Hồ Chí Minh, Việt Nam
  - **Email liên hệ:** `tue.pham@mekongdeltaagri.com`
  - **Hotline / Zalo:** `0904.622.122` (Mr. Tuệ Phạm)

### 1.3. Kiến trúc Sitemap & Phân bổ Template

```text
https://mekongdeltaagri.com/
├── / (Trang chủ)                                                        [template: homepage]
├── /gioi-thieu (Giới Thiệu)                                             [template: inside_page]
├── /dich-vu (Dịch vụ - Trang tổng quan hệ sinh thái đào tạo & tư vấn)   [template: inside_page]
│   ├── /dich-vu/dao-tao-xnk-1-1 (Đào tạo XNK 1-1)                       [template: inside_page]
│   └── /dich-vu/dao-tao-chuyen-sau-doanh-nghiep (Đào tạo DN)            [template: inside_page]
│       ├── /dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ung-dung-ai-xnk     [template: inside_page]
│       │   (Ứng dụng AI cho doanh nghiệp XNK)
│       └── /dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ai-marketing        [template: inside_page]
│           (AI Marketing cho ngành Nông sản & XNK)
├── /tin-tuc (Tin tức - Cập nhật thông tư, chính sách hải quan & sự kiện)[template: parent_listing]
│   ├── /tin-tuc/[slug] (Tin tức 1, Tin tức 2... - Chi tiết bản tin)     [template: child_detail_news]
│   │   (Cấu trúc: Headline Photo + Content + Shared Elements)
├── /blog (Blog - Cẩm nang XNK, Mã HS, Pháp lý FDA/BICON & AI)           [template: parent_listing_category]
│   ├── /blog/[slug] (Blog Detail - Chi tiết bài viết chuyên sâu)        [template: child_detail_blog]
│   │   (Cấu trúc: Headline Photo + Category Badge + Content + GEO Elements)
├── /dang-ky-thu-khoa-hoc (Đăng ký thử khóa học - Trang chuyển đổi)       [template: cta_page]
│
├── /sitemap.xml (Native Dynamic XML Sitemap tự động sinh khi build)
├── /robots.txt (Chỉ dẫn lập chỉ mục chuẩn Googlebot, Bingbot & AI Bots)
├── /llms.txt (Tệp cấu trúc tri thức chuẩn llmstxt.org cho hệ thống LLMs)
├── /.well-known/ai-catalog.json & /.well-known/ard.json (Đặc tả ARD cho AI Agents)
└── /.htaccess (Cấu hình MIME types, CORS, Caching & Routing cho Hosting truyền thống)
```

---

## 2. HỆ THỐNG THIẾT KẾ (DESIGN SYSTEM TOKENS & SPACING CHUẨN HÓA)

### 2.1. Bảng Màu Đồng Bộ (Color Palette)
Giữ nguyên tone màu nhận diện nông nghiệp xanh - cam năng động của **Mekong Delta Agri**, đồng thời chuẩn hóa mã HEX và độ tương phản (WCAG AA) trên toàn bộ các trang:

| Vai trò | Token CSS | Mã HEX | Ứng dụng cụ thể |
| :--- | :--- | :--- | :--- |
| **Primary Light** | `--primary-light` | `#8DC435` | Đường viền gạch chân Heading (`2px solid`), viền nhấn, badge phụ, hover link. |
| **Primary Mid** | `--primary-mid` | `#34C435` | Icon trạng thái hoàn thành, điểm nhấn danh sách lợi ích (checkmark). |
| **Primary Dark** | `--primary-dark` | `#428442` | Màu chủ đạo thương hiệu: Nút bấm chính, nền khối nhấn, tiêu đề phụ, icon chính. |
| **Primary Deep** | `--primary-deep` | `#2D5E2D` | Dải màu Gradient cho Banner CTA, Header sticky hover và Footer. |
| **Secondary (Accent)**| `--secondary` | `#FF9046` | Nút CTA chuyển đổi cao (Đăng ký học thử), chấm active slider, nhãn nổi bật. |
| **Secondary Hover** | `--secondary-hover` | `#E6782E` | Trạng thái `:hover` của các nút CTA cam. |
| **Background Tints** | `--primary-50` / `100` | `#F4FBE8` / `#E5F6C8` | Nền hộp tóm tắt GEO BLUF, nền Author Box, nền tag danh mục, nền khung thông tư. |
| **Background Main** | `--bg-main` | `#FFFFFF` | Nền chính của trang và vùng đọc nội dung (Prose). |
| **Background Soft** | `--bg-secondary` | `#F7FAF5` | Nền xen kẽ giữa các Section trên trang chủ, nền Card dịch vụ, nền FAQ & Testimonial. |
| **Text Primary** | `--text-primary` | `#374047` | Màu chữ chính cho toàn bộ văn bản và tiêu đề (độ tương phản cao, dịu mắt). |
| **Text Secondary** | `--text-secondary` | `#525E66` | Mô tả dẫn nhập (Lead), ngày đăng, thời lượng đọc, chú thích ảnh. |
| **Border Subtle** | `--border-subtle` | `#E2ECE0` | Đường phân cách nhẹ trong bảng biểu, đường kẻ chia mục, khung form input. |

#### Bảng Màu 4 Danh Mục Chuyên Môn (Áp dụng cho Blog Category)
1. **Chứng Từ & Pháp Lý XNK (`Compliance & Docs`):** Nền `#F4FBE8`, chữ `#428442`, icon `bi-file-earmark-check-fill` (FDA, BICON, SPS, C/O, Mã HS, Thông tư Bộ Tài chính/Bộ Công Thương).
2. **Đào Tạo XNK Thực Chiến (`Practical EXIM`):** Nền `#EEFBE8`, chữ `#217A22`, icon `bi-mortarboard-fill` (Kỹ năng nghiệp vụ XNK 1-1, đàm phán quốc tế, Incoterms, Logistics nông sản).
3. **Ứng Dụng AI Trong XNK (`AI for EXIM`):** Nền `#FFF3EB`, chữ `#C25512`, icon `bi-cpu-fill` (Tự động hóa kiểm tra chứng từ, phân tích thị trường, tra cứu quy định bằng AI).
4. **AI Marketing Quốc Tế (`AI Global Marketing`):** Nền `#428442`, chữ `#FFFFFF`, icon `bi-globe-americas` (Chiến lược tìm kiếm khách hàng B2B toàn cầu, Story Answering, tối ưu GEO xuất khẩu).

---

### 2.2. Hệ Thống Chữ (Typography) & Quy Chuẩn Heading
* **Font chữ Nội dung (Body Font):** `'Source Serif 4'`, system-ui, -apple-system, serif (Google Fonts hỗ trợ đầy đủ tiếng Việt).
  - Cỡ chữ cơ sở (Base size): `17px` (`1.0625rem`), `line-height: 1.75`, màu `#374047`.
* **Font chữ Tiêu đề (Heading Font):** `'Merriweather'`, system-ui, serif.
  - Trọng lượng: `700` (Bold) và `900` (Black), `line-height: 1.3`.
* **Quy chuẩn Gạch chân Tiêu đề (Mandatory Heading Style):**
  Tất cả các tiêu đề cấp độ Section và Article (`.section-title`, `.page-hero__title`, `.article-header__title`, `.prose h2`, `.faq-section__title`, `.shared-block__title`) bắt buộc áp dụng:
  ```css
  border-bottom: 2px solid #8dc435;
  padding-bottom: 20px;
  margin-bottom: 20px;
  ```
* **Thang đo Cỡ chữ (Type Scale Responsive):**
  - `H1`: `clamp(2rem, 3.5vw, 2.75rem)` (`32px` $\rightarrow$ `44px`)
  - `H2`: `clamp(1.5rem, 2.5vw, 2.125rem)` (`24px` $\rightarrow$ `34px`)
  - `H3`: `clamp(1.25rem, 2vw, 1.5rem)` (`20px` $\rightarrow$ `24px`)
  - `H4`: `1.125rem` (`18px`)
  - `Lead / Sapo`: `1.1875rem` (`19px`), `line-height: 1.7`, màu `--text-secondary`.

---

### 2.3. Chuẩn Hóa Khoảng Cách (Padding, Margin & Layout Tokens)
Khắc phục triệt để tình trạng lệch lề, khoảng trắng không đều trên bản WordPress cũ bằng hệ thống Spacing Token cố định (bội số của `8px`):

```css
:root {
  /* Container Widths */
  --container-max: 1200px;
  --prose-max: 820px;
  --container-pad-x: clamp(16px, 4vw, 32px);

  /* Section Vertical Spacing (Padding Top & Bottom đồng bộ) */
  --section-py-desktop: 80px;
  --section-py-tablet: 56px;
  --section-py-mobile: 40px;

  /* Grid & Card Spacing */
  --grid-gap-lg: 32px;
  --grid-gap-md: 24px;
  --grid-gap-sm: 16px;
  --card-padding: 28px;
  --card-radius: 16px;
}

/* Quy tắc Div Phẳng & Chống tràn ngang */
html, body {
  overflow-x: clip;
  margin: 0;
  padding: 0;
}

div {
  border: none;
  margin-left: 0;
  padding-left: 0;
}

.container {
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: var(--container-pad-x);
}
```

---

## 3. ĐẶC TẢ CHI TIẾT TRANG CHỦ (`/` — `template: homepage`)
*(Giữ nguyên thiết kế, bố cục, tone màu và mạch nội dung của `https://mekongdeltaagri.com/`, chuẩn hóa Padding/Margin và chuyển ngữ 100% sang Tiếng Việt)*

### 3.1. Sơ đồ Kiến trúc Trang Chủ (Wireframe)

```text
+---------------------------------------------------------------------------------------------------------+
| [GLOBAL HEADER] Logo MDA (/media/logoMDAgri500x500.webp) | Menu Chính | Social Links | Nút [MENU]       |
+---------------------------------------------------------------------------------------------------------+
| [OFF-CANVAS SLIDE DRAWER MENU] (Cấu trúc điều hướng đa cấp đầy đủ Sitemap + Social Links + CTA)         |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 1: HERO & WELCOME TO MDA AGRO KNOWLEDGE HUB] (Nền #F7FAF5, Padding 80px 0)                     |
|   <--- CỘT TRÁI (50%: CHÀO MỪNG & ĐỊNH VỊ) --->     <--- CỘT PHẢI (50%: SLIDER 4 TRỤ CỘT CỐT LÕI) --->  |
|   Badge: Cộng đồng TP.HCM về Chứng từ & AI XNK      +-------------------------------------------------+ |
|   H1 (gạch chân #8DC435): Chào mừng đến với         | [Carousel 4 Slides - Ảnh thực tế từ MDA]        | |
|   Trung tâm Tri thức Nông sản & XNK MDA             | Slide 1: Sự thật Xuất khẩu Trái cây Việt Nam    | |
|   Lead: Hệ sinh thái tri thức chứng từ thương mại,  | Slide 2: Tuân thủ & Xác thực bằng Trí tuệ AI    | |
|   tư vấn tuân thủ quốc tế (FDA, BICON, SPS) và      | Slide 3: AI Marketing cho ngành Nông sản        | |
|   đào tạo thực chiến giúp doanh nghiệp tự chủ       | Slide 4: Mã HS & Tuân thủ Thương mại XNK        | |
|   chuỗi cung ứng toàn cầu.                          +-------------------------------------------------+ |
|   [CTA Chính: Đăng ký thử khóa học] [CTA Phụ: Khám phá Dịch vụ]                                        |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 2: THƯ VIỆN TRI THỨC & ĐIỂM NÓNG PHÁP LÝ XNK] (Nền #FFFFFF, Padding 80px 0)                    |
|   H2 (gạch chân #8DC435): Tri thức Xuất khẩu Nông sản & Cập nhật Pháp lý Hải quan                       |
|   Lead: Tuyển chọn, biên soạn và giải mã các quy định phức tạp thành hướng dẫn thực thi dễ hiểu nhất.   |
|   +-------------------------------+ +-------------------------------+ +-------------------------------+ |
|   | Thẻ Pháp lý 1 (Nền #F4FBE8)   | | Thẻ Pháp lý 2 (Nền #F4FBE8)   | | Thẻ Pháp lý 3 (Nền #F4FBE8)   | |
|   | [Badge: 85/2026/TT-BTC]       | | [Badge: 42/2026/TT-BCT]       | | [Badge: 110/2026/TT-BTC]      | |
|   | Quy định mới về chứng từ      | | Quy tắc xuất xứ (C/O) & ưu    | | Thủ tục hải quan điện tử &    | |
|   | thuế XNK & phân loại mã HS    | | đãi thuế quan hiệp định FTA   | | kiểm tra chuyên ngành nông sản| |
|   +-------------------------------+ +-------------------------------+ +-------------------------------+ |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 3: CHUYÊN GIA ĐÀO TẠO XNK & AI MARKETING] (Nền #F7FAF5, Padding 80px 0)                        |
|   <--- CỘT TRÁI (50%: HÌNH ẢNH / INFOGRAPHIC) --->  <--- CỘT PHẢI (50%: NỘI DUNG & DỊCH VỤ ĐÀO TẠO) --->|
|   Ảnh đội ngũ chuyên gia & mô hình AI-Driven        H2 (gạch chân #8DC435): Chuyên gia Đào tạo XNK &    |
|   Marketing cho ngành Nông sản xuất khẩu            Chiến lược AI Marketing Nông sản                    |
|   Floating Badge: Đối tác tin cậy đi Úc, Canada,    Đội ngũ MDA đồng hành từ ý tưởng mới đến mở rộng    |
|   Mỹ, EU                                            doanh nghiệp XNK qua 4 chương trình mũi nhọn:       |
|                                                     - Đào tạo XNK Thực chiến 1-1                        |
|                                                     - Đào tạo Chuyên sâu Doanh nghiệp                   |
|                                                     - Ứng dụng AI cho Doanh nghiệp XNK                  |
|                                                     - AI Marketing Nông sản Quốc tế                     |
|                                                     [Nút CTA: Nhận Tư vấn Dịch vụ Đào tạo ->]           |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 4: HỎI ĐÁP CHUYÊN SÂU (AGRO-EXPORT Q&A ACCORDION & LỢI ÍCH HỢP TÁC)] (Nền #FFFFFF, Pad 80px 0) |
|   <--- CỘT TRÁI (45%: CÂU HỎI TRỌNG TÂM) --->       <--- CỘT PHẢI (55%: 3 ACCORDION GEO-FRIENDLY) --->  |
|   H2 (gạch chân #8DC435): Giải đáp Thực chiến       1. [Accordion] Làm thế nào AI biến doanh nghiệp     |
|   Xuất khẩu Nông sản (Q&A)                             địa phương thành đối thủ toàn cầu?               |
|   Câu hỏi mở đầu: "Việc áp sai Mã HS có đang        2. [Accordion] Bạn đang kể câu chuyện chung chung   |
|   khiến sản phẩm cao cấp của bạn trở nên 'vô hình'     hay đang 'Story Answering' đúng nhu cầu người    |
|   trước hải quan và nhà nhập khẩu quốc tế?"            mua quốc tế?                                     |
|   4 Lợi ích cốt lõi (Icon Check #34C435):           3. [Accordion] Hiện diện số của bạn đã đủ chuẩn     |
|   ✔ Hoàn thiện bộ chứng từ & đạt chuẩn quốc tế         'GEO-friendly' để các công cụ AI trích dẫn       |
|   ✔ Xác định đúng thị trường mục tiêu                  như một nguồn cung uy tín từ Việt Nam?           |
|   ✔ Tận dụng tối đa FTA để tối ưu thuế & chi phí                                                        |
|   ✔ Biến thách thức pháp lý thành lợi thế dài hạn                                                       |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 5: SHARED ELEMENTS — GALLERY TÀI LIỆU ĐÀO TẠO MẪU (PDF) & TESTIMONIALS] (Nền #F7FAF5)          |
|   - Khối Gallery: Danh sách các nội dung đào tạo mẫu kèm nút Xem trước / Tải trọn bộ 1 file PDF.        |
|   - Khối Testimonial (Hardcoded): Đánh giá từ học viên 1-1 và Giám đốc Doanh nghiệp XNK Nông sản.       |
+---------------------------------------------------------------------------------------------------------+
| [SECTION 6: KẾT NỐI VỚI CHÚNG TÔI (CONNECT WITH US & CONTACT FORM)] (Full-Width Banner #428442->#2D5E2D)|
|   <--- CỘT TRÁI (THÔNG ĐIỆP & ĐỊA CHỈ) --->         <--- CỘT PHẢI (SHARED ELEMENT: CONTACT FORM) --->   |
|   H2: Kết nối cùng Chuyên gia XNK & AI MDA          Form liên hệ trực tiếp (Họ tên, SĐT/Zalo, Email,    |
|   "Xuất khẩu không chỉ là đưa hàng ra thế giới –    Chương trình quan tâm, Nội dung cần tư vấn)         |
|   đó là hành trình chiến lược từ thủ tục pháp lý    Nút gửi màu Cam (#FF9046)                           |
|   đến thấu hiểu thị trường Úc, Canada, Hoa Kỳ."                                                         |
|   📍 Tầng 1, 53/104 Trần Khánh Dư, P. Tân Định, TPHCM                                                   |
|   📞 0904.622.122 (Mr. Tuệ) | ✉️ tue.pham@...                                                            |
+---------------------------------------------------------------------------------------------------------+
| [GLOBAL FOOTER] Logo MDA + Giới thiệu pháp nhân + Sitemap đa cấp + Social Links + Bản quyền 2024-2026   |
+---------------------------------------------------------------------------------------------------------+
```

### 3.2. Nội dung Việt hóa Chuẩn trên Trang Chủ (Mapping từ trang WordPress gốc)

| Thành phần gốc (Tiếng Anh trên WP) | Nội dung Việt hóa Chuẩn trên Astro SSG |
| :--- | :--- |
| *Welcome to MDA Agro Knowledge Hub* | **Chào mừng đến với Trung tâm Tri thức Nông sản & XNK MDA** |
| *VN Trade Documentation, Compliance Advisory & AI Agro-Export Knowledge* | **Chứng từ Thương mại, Tư vấn Tuân thủ Pháp lý & Tri thức Xuất khẩu Nông sản Ứng dụng AI** |
| *MDA Hub is the definitive trade documentation and knowledge ecosystem for Vietnam's agricultural sector...* | **MDA Hub** là hệ sinh thái tri thức và chứng từ thương mại toàn diện dành cho ngành nông sản Việt Nam. Chúng tôi đơn giản hóa các rào cản pháp lý xuyên biên giới thông qua hoạt động tư vấn tuân thủ chi tiết (**FDA, BICON, SPS**) chuyên biệt cho doanh nghiệp xuất khẩu trái cây nhiệt đới và nông sản chế biến. Lấy đổi mới sáng tạo AI làm động lực, MDA cung cấp hệ thống giải đáp thương mại tự động, phân tích tối ưu hóa công cụ tạo sinh (GEO) và các chương trình đào tạo thực chiến giúp doanh nghiệp tự chủ hoàn toàn chuỗi cung ứng toàn cầu. |
| *Slide 1: The Fruit Export Truth - Sourcing Safely from Vietnam* | **Sự thật về Xuất khẩu Trái cây:** Truy xuất nguồn gốc minh bạch & Thu mua an toàn từ vùng nguyên liệu Việt Nam. |
| *Slide 2: AI Compliance & Verification - Meet Global Standards* | **Tuân thủ & Xác thực bằng AI:** Đáp ứng tiêu chuẩn khắt khe của FDA (Mỹ), BICON (Úc) và SPS quốc tế. |
| *Slide 3: AI-Driven Marketing for the Agriculture sector* | **AI Marketing cho Ngành Nông sản:** Định vị thương hiệu nông sản Việt trên bản đồ chuỗi cung ứng toàn cầu. |
| *Slide 4: HS Code & EXIM Trade Compliance (85/2026/TT-BTC, 42/2026/TT-BCT, 110/2026/TT-BTC)* | **Mã HS & Tuân thủ Thương mại XNK:** Giải mã chuẩn xác các thông tư mới nhất (`85/2026/TT-BTC`, `42/2026/TT-BCT`, `110/2026/TT-BTC`). |
| *AI-Driven Marketing experts for the Agriculture sector* | **Đội ngũ Chuyên gia Đào tạo XNK & Chiến lược AI Marketing Nông sản** |
| *Is a wrong HS Code making your premium products 'invisible' to international customs and buyers?* | **Việc áp sai Mã HS có đang khiến nông sản cao cấp của bạn trở nên "vô hình" trước cơ quan hải quan và nhà mua hàng quốc tế?** |

---

## 4. ĐẶC TẢ CHI TIẾT CÁC TEMPLATE TRANG CON (SITEMAP TEMPLATES)

Hệ thống sử dụng **5 Template chuẩn hóa** trong Astro để phục vụ toàn bộ cây Sitemap mà người dùng yêu cầu:

### 4.1. Template 1: `template inside_page` (`src/layouts/InsidePageLayout.astro`)
Áp dụng cho **6 trang nội dung tĩnh & dịch vụ phân cấp**:
1. **Giới Thiệu** (`/gioi-thieu`)
2. **Dịch vụ (Trang tổng quan)** (`/dich-vu`)
3. **Đào tạo XNK 1-1** (`/dich-vu/dao-tao-xnk-1-1`)
4. **Đào tạo chuyên sâu doanh nghiệp** (`/dich-vu/dao-tao-chuyen-sau-doanh-nghiep`)
5. **Ứng dụng AI cho doanh nghiệp XNK** (`/dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ung-dung-ai-xnk`)
6. **AI Marketing** (`/dich-vu/dao-tao-chuyen-sau-doanh-nghiep/ai-marketing`)

#### Cấu trúc bố cục chuẩn của `template inside_page`:
* **1. Breadcrumb Tự động (Kèm Schema `BreadcrumbList`):**
  - Ví dụ ở trang cấp 3: `Trang chủ > Dịch vụ > Đào tạo chuyên sâu doanh nghiệp > Ứng dụng AI cho doanh nghiệp XNK`.
* **2. Inside Page Hero:**
  - Badge danh mục cha, Tiêu đề `H1` có đường gạch chân `2px solid #8dc435`, đoạn dẫn nhập (Lead) tóm tắt giá trị cốt lõi, và thanh điều hướng nhanh các trang con cùng cấp (Sub-navigation Pills).
* **3. Khối Tóm tắt GEO BLUF (Bottom Line Up Front):**
  - Hộp Callout nền `#F4FBE8` đặt đầu trang trả lời trực diện 3 câu hỏi cho AI Search và người đọc: *Chương trình này dành cho ai? Giải quyết bài toán gì? Kết quả đầu ra sau đào tạo là gì?*
* **4. Thân trang 2 Cột (Desktop Grid 8/4 hoặc Prose + Sidebar):**
  - **Vùng Nội dung Chính:**
    + Đối với trang **Giới Thiệu (`/gioi-thieu`)**: Câu chuyện hình thành Mekong Delta Agri (Minh Tam Trading), Sứ mệnh "True to Fruit" & Minh bạch hóa pháp lý XNK, Tầm nhìn tiên phong AI Nông sản tại thị trường Úc/Canada/Mỹ, Giá trị cốt lõi (Bền vững, Chính xác, Thực chiến).
    + Đối với trang **Dịch vụ (`/dich-vu`)**: Bức tranh tổng thể 2 nhánh đào tạo chính (*Đào tạo XNK 1-1* và *Đào tạo Chuyên sâu Doanh nghiệp* gồm *Ứng dụng AI XNK* & *AI Marketing*), bảng so sánh lộ trình học và cam kết đầu ra.
    + Đối với các trang **Đào tạo chi tiết (`1-1`, `Doanh nghiệp`, `Ứng dụng AI XNK`, `AI Marketing`)**: Đối tượng học viên, Khung chương trình chi tiết theo từng Module (Syllabus), Phương pháp huấn luyện trên bộ chứng từ và dữ liệu thật của doanh nghiệp, Hỏi đáp thường gặp (`FaqAccordion`).
  - **Cột Sidebar Sticky:**
    + Menu điều hướng cây Dịch vụ (Service Tree Navigation) giúp chuyển nhanh giữa các chương trình đào tạo.
    + Thẻ tóm tắt thông tin khóa học (Hình thức học: 1-1 / In-house tại doanh nghiệp, Thời lượng, Giảng viên phụ trách) + Nút chuyển đổi sang trang **Đăng ký thử khóa học (`/dang-ky-thu-khoa-hoc`)**.
* **5. Khu vực Shared Elements cuối trang `inside_page`:**
  - `AuthorGeoBox` (Thông tin Chuyên gia biên soạn/giảng dạy chương trình).
  - `TrainingGalleryPdf` (Danh sách nội dung đào tạo mẫu kèm file PDF tải về).
  - `TestimonialSection` (Cảm nhận học viên/doanh nghiệp thực tế).
  - `ContactForm` (Form đăng ký tư vấn chương trình).

---

### 4.2. Template 2: `template parent listing` — Tin Tức (`/tin-tuc`)
* **Mục đích:** Trang danh sách tổng hợp các bản tin thời sự ngành nông sản, cập nhật thông tư hải quan mới, hoạt động đào tạo của MDA Hub.
* **Cấu trúc hiển thị:**
  - **Breadcrumb:** `Trang chủ > Tin tức`.
  - **Page Header:** `H1` gạch chân `#8dc435` (*"Tin Tức Xuất Nhập Khẩu & Hoạt Động MDA Hub"*), mô tả ngắn.
  - **Featured News (Bản tin tiêu điểm):** Hiển thị nổi bật bản tin mới nhất ở đầu trang (Layout 2 cột: Ảnh Headline 16:9 bên trái + Tiêu đề H2, ngày đăng, tóm tắt, nút đọc tiếp bên phải).
  - **News Listing Grid (Lưới danh sách tin tức):** Lưới 3 cột hiển thị các bản tin (`Tin tức 1`, `Tin tức 2`, ...). Mỗi thẻ hiển thị: Ảnh đại diện (Headline Photo), Ngày xuất bản, Tiêu đề `H3`, Đoạn trích ngắn (Excerpt 3 dòng) và nút *"Xem chi tiết →"*.
  - *Lưu ý khác biệt với Blog:* Trang `/tin-tuc` **không** sử dụng thanh lọc Category để giữ giao diện tinh gọn đúng chuẩn bản tin thời sự.

---

### 4.3. Template 3: `template child detail (News)` — Chi Tiết Tin Tức (`/tin-tuc/[slug]`)
* **Yêu cầu cốt lõi từ Spec người dùng:** `headline photo + content`.
* **Cấu trúc hiển thị:**
  - **Breadcrumb:** `Trang chủ > Tin tức > [Tiêu đề bản tin]`.
  - **News Header:** Tiêu đề `H1` gạch chân `#8dc435`, мета-data gồm Ngày đăng & Thời gian đọc (không gắn nhãn Category).
  - **Headline Photo (`FeaturePhoto.astro`):** Ảnh bìa khổ lớn `1200x630 px` (`aspect-ratio: 16/9`), tối ưu `fetchpriority="high"`, kèm chú thích ảnh (`figcaption`).
  - **News Content (`.prose`):** Nội dung chi tiết bản tin (ví dụ: *Tin tức 1: Giải mã Thông tư 85/2026/TT-BTC và 42/2026/TT-BCT đối với doanh nghiệp xuất khẩu nông sản*; *Tin tức 2: Lễ ký kết đào tạo In-house Ứng dụng AI trong quản trị chứng từ XNK cho doanh nghiệp ĐBSCL*).
  - **Shared Elements đi kèm cuối bài:**
    + `AuthorGeoBox` (Ban biên tập Pháp lý & Tin tức MDA Hub).
    + `SocialLinks` (Chia sẻ & Kết nối kênh truyền thông MDA).
    + `ContactForm` (Đăng ký nhận bản tin pháp lý & tư vấn).
  - **Tin tức liên quan:** 2–3 bản tin khác ở cuối trang.

---

### 4.4. Template 4: `template parent listing + category` — Blog (`/blog`)
* **Yêu cầu cốt lõi từ Spec người dùng:** `parent listing + category`.
* **Cấu trúc hiển thị:**
  - **Breadcrumb:** `Trang chủ > Blog Tri Thức XNK & AI`.
  - **Blog Hub Header:** `H1` gạch chân `#8dc435` (*"Blog Chuyên Sâu: Chứng Từ XNK, Tiêu Chuẩn Quốc Tế & Ứng Dụng AI"*).
  - **Bộ lọc Danh mục (Category Filter Bar) & Tìm kiếm Tức thì:**
    + Các nút lọc Category trực quan: `Tất cả` | `📋 Chứng Từ & Pháp Lý XNK` | `🎓 Đào Tạo XNK Thực Chiến` | `🤖 Ứng Dụng AI Trong XNK` | `🌐 AI Marketing Quốc Tế`.
    + Ô tìm kiếm từ khóa tức thì (ví dụ: *"Mã HS"*, *"FDA"*, *"BICON"*, *"AI Marketing"*).
  - **Blog Listing Grid:** Lưới 3 cột hiển thị các bài viết kèm **Category Badge** nổi bật trên từng thẻ bài viết.

---

### 4.5. Template 5: `template child detail (Blog)` — Chi Tiết Bài Viết Blog (`/blog/[slug]`)
* **Yêu cầu cốt lõi từ Spec người dùng:** `headline photo + category + content`.
* **Cấu trúc hiển thị:**
  - **Breadcrumb:** `Trang chủ > Blog > [Tên Category] > [Tiêu đề bài viết]`.
  - **Blog Detail Header:**
    + **Category Badge (`CategoryBadge.astro`):** Hiển thị rõ danh mục chuyên môn của bài viết (kèm màu sắc nhận diện và icon tương ứng).
    + **Tiêu đề `H1`:** Gạch chân `2px solid #8dc435`.
    + **Meta Info:** Ngày cập nhật, số phút đọc, danh sách Tags.
  - **Author Box (`AuthorGeoBox.astro`):** Đặt ngay dưới Header bài viết để xác thực E-E-A-T với Google & AI Search.
  - **Headline Photo (`FeaturePhoto.astro`):** Ảnh đại diện chuẩn `1200x630 px` kèm chú thích chuyên môn.
  - **Bố cục 2 Cột (Desktop):**
    + **Cột Trái (Sticky Sidebar 270px):** Mục lục bài viết tự động (Sticky TOC) + Hộp CTA mời Đăng ký thử khóa học + Tải tài liệu PDF mẫu.
    + **Cột Phải (Vùng đọc tối đa 820px):**
      1. Hộp tóm tắt trực diện **GEO BLUF Callout** (`> [!SUMMARY] BLUF:`).
      2. Nội dung chuyên sâu (`.prose`) có bảng biểu, ví dụ mã HS, quy trình kiểm dịch thực vật.
      3. Khối Hỏi & Đáp cuối bài (`FaqAccordion.astro` đồng bộ JSON-LD `FAQPage`).
      4. Khối Nguồn tham khảo pháp lý (`SourcesList.astro` dẫn nguồn Tổng cục Hải quan, Bộ Công Thương, FDA, DAFF BICON).
  - **Shared Elements cuối bài:** `TrainingGalleryPdf`, `TestimonialSection`, và `ContactForm`.

---

### 4.6. Template 6: `CTA page` — Đăng Ký Thử Khóa Học (`/dang-ky-thu-khoa-hoc`)
* **Mục đích:** Trang đích chuyển đổi cao (High-Conversion Landing Page) dành riêng cho cá nhân và doanh nghiệp muốn trải nghiệm buổi học thử / tư vấn 1-1 cùng chuyên gia MDA trước khi đăng ký chính thức.
* **Cấu trúc bố cục:**
  - **1. Conversion Hero (2 Cột):**
    + **Cột Trái:** Badge *"Trải nghiệm Thực chiến Miễn phí"*, Tiêu đề `H1` gạch chân `#8dc435`: *"Đăng Ký Học Thử & Đánh Giá Năng Lực XNK - AI Cùng Chuyên Gia MDA"*, danh sách 4 giá trị nhận được ngay trong buổi học thử (Kiểm tra bộ chứng từ/mã HS hiện tại, Demo công cụ AI phân tích thị trường xuất khẩu, Tư vấn lộ trình học 1-1 hoặc In-house, Nhận bộ tài liệu đào tạo mẫu PDF).
    + **Cột Phải:** Khối **`ContactForm.astro`** (Chế độ Đăng ký Học thử mở rộng: Cho phép chọn khóa học muốn thử: *Đào tạo XNK 1-1*, *Đào tạo Doanh nghiệp*, *Ứng dụng AI XNK*, hoặc *AI Marketing*, chọn khung giờ mong muốn).
  - **2. Khối Gallery Nội dung Đào tạo Mẫu (`TrainingGalleryPdf.astro`):**
    + Cho phép người đăng ký xem trước các học phần mẫu và tải ngay 1 file PDF tổng hợp khung chương trình & biểu mẫu chứng từ mẫu.
  - **3. Khối Chuyên gia Đồng hành (`AuthorGeoBox.astro` mở rộng):**
    + Giới thiệu hồ sơ năng lực của giảng viên và chuyên gia tư vấn tại MDA Hub.
  - **4. Khối Đánh giá Học viên & Doanh nghiệp (`TestimonialSection.astro`):**
    + Bảo chứng xã hội (Social Proof) từ các học viên và doanh nghiệp đã tham gia đào tạo.
  - **5. Câu hỏi thường gặp về Buổi Học Thử (`FaqAccordion.astro`).**

---

## 5. ĐẶC TẢ 5 ELEMENT DÙNG CHUNG (SHARED COMPONENTS)

Toàn bộ 5 Element dùng chung được thiết kế dưới dạng các Astro Component độc lập trong `src/components/shared/`, dễ dàng nhúng vào bất kỳ trang nào trong Sitemap:

### 5.1. Author Box (`src/components/shared/AuthorGeoBox.astro`)
* **Mục đích:** Tăng cường tín hiệu **E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)** cho SEO và giúp các công cụ AI (GEO) định danh chính xác tác giả/chuyên gia thẩm định của Mekong Delta Agri.
* **Dữ liệu hiển thị & Microdata Schema (`https://schema.org/Person`):**
  - **Tác giả / Chuyên gia chính:** **Tuệ Phạm (Mr. Tuệ)** — *Chuyên gia Tư vấn Chiến lược XNK Nông sản & Ứng dụng AI (Đồng sáng lập MDA Agro-Export Hub)*.
    + Kinh nghiệm thực chiến: Tư vấn xuất khẩu nông sản, trái cây nhiệt đới & thực phẩm sấy thăng hoa (Freeze-Dried) sang thị trường Úc, Canada, Hoa Kỳ; huấn luyện 1-1 và In-house về chứng từ thương mại, mã HS, tuân thủ FDA/BICON/SPS và AI Marketing.
  - **Hội đồng Thẩm định Pháp lý & AI (Co-Reviewers):**
    + *Ban Pháp lý & Hải quan MDA:* Thẩm định tính chính xác của các thông tư (`85/2026/TT-BTC`, `42/2026/TT-BCT`, `110/2026/TT-BTC`), quy tắc xuất xứ FTA và tiêu chuẩn kiểm dịch.
    + *Ban Công nghệ AI & GEO Marketing MDA:* Thẩm định quy trình tự động hóa AI và chiến lược Story Answering B2B toàn cầu.
  - **Tích hợp Social Links cá nhân/tổ chức:** Zalo (`0904.622.122`), Email (`tue.pham@mekongdeltaagri.com`), LinkedIn / Facebook MDA.
* **Thiết kế giao diện:** Nền `#F4FBE8`, bo góc `16px`, padding `24px`, avatar tròn viền `#8DC435`, tuân thủ quy tắc không viền thừa (`border: none`).

---

### 5.2. Contact Form (`src/components/shared/ContactForm.astro`)
* **Mục đích:** Thu thập thông tin khách hàng tiềm năng (Lead Generation) cho tư vấn dịch vụ và đăng ký học thử, hoạt động ổn định 100% trên **Hosting tĩnh cũ** (không cần chạy PHP backend phức tạp).
* **Trường dữ liệu (Fields):**
  1. Họ và tên (`name` - bắt buộc)
  2. Số điện thoại / Zalo (`phone` - bắt buộc, kiểm tra định dạng SĐT Việt Nam)
  3. Email doanh nghiệp/cá nhân (`email` - bắt buộc)
  4. Tên doanh nghiệp / Ngành hàng nông sản (`company` - tùy chọn)
  5. Chương trình quan tâm (`service` - Dropdown):
     - *Đào tạo XNK Thực chiến 1-1*
     - *Đào tạo Chuyên sâu Doanh nghiệp (In-house)*
     - *Ứng dụng AI cho Doanh nghiệp XNK*
     - *AI Marketing cho Ngành Nông sản*
     - *Tư vấn Chứng từ, Mã HS & Tuân thủ FDA/BICON/SPS*
  6. Nội dung cần tư vấn cụ thể (`message` - Textarea)
* **Cơ chế Gửi dữ liệu trên Hosting Tĩnh (Dual-Mode):**
  - Hỗ trợ gửi qua **AJAX Endpoint (Web3Forms / Formspree / Google Apps Script Webhook)** hoặc gửi trực tiếp về Google Form / Email `tue.pham@mekongdeltaagri.com`, kèm thông báo trạng thái thành công ngay trên trang mà không cần tải lại trang.

---

### 5.3. Testimonial (`src/components/shared/TestimonialSection.astro`)
* **Yêu cầu cốt lõi từ Spec người dùng:** `hardcode content` (Dữ liệu cố định trực tiếp trong mã nguồn component để đạt tốc độ render 0ms, không phụ thuộc CMS/Database).
* **Cấu trúc Dữ liệu Hardcoded (3–4 Đánh giá tiêu biểu):**
  1. **Doanh nghiệp Xuất khẩu Trái cây & Nông sản Chế biến (ĐBSCL):**
     - *Nội dung:* "Trước khi làm việc với MDA Hub, chúng tôi mất rất nhiều thời gian xử lý hồ sơ BICON khi xuất hàng sang Úc và thường xuyên lúng túng khi tra cứu mã HS cho dòng sản phẩm sấy thăng hoa. Khóa đào tạo In-house của Mr. Tuệ đã giúp đội ngũ XNK của công ty làm chủ hoàn toàn quy trình chứng từ và ứng dụng AI để kiểm tra chéo hồ sơ chỉ trong 15 phút."
     - *Người đánh giá:* **Anh Nguyễn Hoàng Nam** — *Giám đốc Điều hành, Doanh nghiệp Chế biến & Xuất khẩu Nông sản Tiền Giang*.
  2. **Học viên Khóa Đào tạo XNK 1-1:**
     - *Nội dung:* "Mình chuyển từ mảng thu mua nội địa sang làm XNK nông sản nên rất sợ sai sót chứng từ C/O và kiểm dịch thực vật. Nhờ lộ trình kèm 1-1 cầm tay chỉ việc trên bộ chứng từ thật tại MDA, chỉ sau 6 tuần mình đã tự tin xử lý trọn vẹn lô hàng đầu tiên đi Canada."
     - *Người đánh giá:* **Chị Trần Minh Thư** — *Chuyên viên Xuất Nhập Khẩu Nông sản, TP.HCM*.
  3. **Doanh nghiệp Ứng dụng AI Marketing Quốc tế:**
     - *Nội dung:* "Chiến lược 'Story Answering' và tối ưu hóa nội dung chuẩn GEO mà đội ngũ AI Marketing của MDA triển khai đã giúp website nông sản của chúng tôi được các công cụ AI quốc tế trích dẫn khi nhà nhập khẩu tìm kiếm nguồn cung đạt chuẩn FDA tại Việt Nam. Lượng thư hỏi hàng (Inquiry) B2B chất lượng tăng rõ rệt."
     - *Người đánh giá:* **Chị Lê Thảo Vy** — *Trưởng phòng Phát triển Thị trường Quốc tế, Công ty Xuất khẩu Thực phẩm Xanh*.
* **Thiết kế giao diện:** Lưới 3 cột (Desktop), nền thẻ `#FFFFFF` trên vùng nền `#F7FAF5`, biểu tượng dấu ngoặc kép `#8DC435`, xếp hạng 5 sao (`#FF9046`), thông tin người đánh giá rõ ràng.

---

### 5.4. Gallery — Danh Sách Nội Dung Đào Tạo Mẫu & 1 File PDF (`src/components/shared/TrainingGalleryPdf.astro`)
* **Yêu cầu cốt lõi từ Spec người dùng:** `Gallery (danh sách các nội dung đào tạo mẫu - 1 pdf file)`.
* **Cấu trúc chức năng & Giao diện:**
  - **Tiêu đề khối (gạch chân `#8dc435`):** *"Thư Viện Nội Dung Đào Tạo Mẫu & Tài Liệu Thực Chiến MDA"*
  - **Lưới Gallery Trực quan (4–6 Thẻ Học phần Mẫu có ảnh Preview bìa tài liệu):**
    1. *Module Mẫu 01 (XNK 1-1):* Bộ Checklist 12 bước kiểm tra Chứng từ Thương mại (Invoice, Packing List, B/L, C/O, Phytosanitary) chống rủi ro kẹt hàng tại cảng đích.
    2. *Module Mẫu 02 (Pháp lý & Mã HS):* Cẩm nang phân loại Mã HS Nông sản & Tối ưu thuế quan FTA theo Thông tư `85/2026/TT-BTC` và `42/2026/TT-BCT`.
    3. *Module Mẫu 03 (Tiêu chuẩn Quốc tế):* Hướng dẫn thực hành đăng ký FDA (Hoa Kỳ), tra cứu điều kiện nhập khẩu BICON (Úc) và tuân thủ SPS.
    4. *Module Mẫu 04 (Ứng dụng AI XNK):* Bộ 25 Câu lệnh (Prompts) AI chuyên dụng giúp tự động rà soát hợp đồng ngoại thương, dịch thuật pháp lý và phân tích rào cản kỹ thuật.
    5. *Module Mẫu 05 (AI Marketing & GEO):* Khung chiến lược "Story Answering" & Xây dựng hồ sơ năng lực số chuẩn GEO thu hút nhà mua hàng B2B toàn cầu.
    6. *Module Mẫu 06 (Case Study Thực tế):* Phân tích hồ sơ xuất khẩu thành công lô hàng Trái cây nhiệt đới & Nông sản sấy sang thị trường Canada & Úc.
  - **Tích hợp Duy nhất 1 File PDF Tổng hợp (`/media/mda-tai-lieu-dao-tao-mau-xnk-ai.pdf`):**
    + Tất cả các thẻ trong Gallery đều liên kết trực tiếp đến **1 tệp PDF tổng hợp chuẩn chỉnh** lưu tại `public/media/mda-tai-lieu-dao-tao-mau-xnk-ai.pdf`.
    + Cung cấp 2 nút hành động rõ ràng:
      1. **[Xem trực tiếp tài liệu PDF (Modal / Tab mới)]** (`bi-eye-fill`)
      2. **[Tải trọn bộ Tài liệu Đào tạo Mẫu (.PDF - 4.2 MB)]** (`bi-file-earmark-pdf-fill`, thuộc tính `download`)

---

### 5.5. Social Link (`src/components/shared/SocialLinks.astro`)
* **Mục đích:** Đồng bộ hóa toàn bộ liên kết mạng xã hội và kênh liên lạc trực tiếp của Mekong Delta Agri tại Header, Off-Canvas Drawer Menu, Author Box, Trang Liên hệ và Footer.
* **Danh sách Kênh Kết nối:**
  - **Facebook Page:** Kênh cộng đồng MDA Agro-Export Knowledge Hub (`bi-facebook`)
  - **LinkedIn:** Hồ sơ chuyên nghiệp MD AGRI TRADING CO., LTD (`bi-linkedin`)
  - **YouTube:** Kênh video chia sẻ kiến thức XNK & AI Nông sản (`bi-youtube`)
  - **Zalo OA / Zalo Chuyên gia:** Kết nối nhanh `https://zalo.me/0904622122` (`bi-chat-dots-fill`)
  - **Email trực tiếp:** `mailto:tue.pham@mekongdeltaagri.com` (`bi-envelope-fill`)
* **Hỗ trợ 3 biến thể hiển thị (Props `variant`):** `'header'` (icon nhỏ gọn), `'drawer'` (nút ngang có nhãn chữ), `'footer'` (nút tròn nền tối).

---

## 6. CHIẾN LƯỢC SEO, GEO & AGENTIC WEB (THEO SPEC HIỆN TẠI)

### 6.1. Tối ưu hóa Công cụ Tạo sinh (GEO - Generative Engine Optimization)
1. **Khối Tóm tắt Trực diện BLUF (Bottom Line Up Front):**
   - Mọi trang Dịch vụ (`inside_page`) và bài viết Blog (`child_detail_blog`) đều mở đầu bằng hộp `> [!SUMMARY] BLUF:` dài 60–90 từ, tóm tắt câu trả lời cốt lõi kèm số liệu/mã thông tư cụ thể để các mô hình AI (ChatGPT, Perplexity, Gemini, Claude) trích xuất nguyên văn.
2. **Hệ thống JSON-LD Schema.org Đa tầng (Tự động tiêm vào `<head>` qua `Layout.astro`):**
   - `Organization` & `LocalBusiness`: Khai báo pháp nhân **MD AGRI TRADING CO., LTD**, địa chỉ `53/104 Trần Khánh Dư, P. Tân Định, TP.HCM`, hotline `0904.622.122`, logo `/media/logoMDAgri500x500.webp`.
   - `Service` & `Course`: Khai báo cho 4 trang dịch vụ đào tạo (*Đào tạo XNK 1-1*, *Đào tạo Doanh nghiệp*, *Ứng dụng AI XNK*, *AI Marketing*).
   - `NewsArticle`: Khai báo cho các bản tin tại `/tin-tuc/[slug]`.
   - `Article` & `TechArticle`: Khai báo cho các bài phân tích chuyên sâu tại `/blog/[slug]`.
   - `FAQPage`: Tự động sinh từ mảng `faqSchema` trên Trang chủ, Trang Dịch vụ và Blog.
   - `BreadcrumbList`: Tự động sinh theo phân cấp URL thực tế.
3. **XML Sitemap Động (`src/pages/sitemap.xml.ts`) & `public/robots.txt`:**
   - Tự động quét toàn bộ các trang tĩnh (Trang chủ, Giới thiệu, 5 trang Dịch vụ, Đăng ký học thử) cùng toàn bộ bài viết trong Collection `news` (`/tin-tuc/[slug]`) và `blog` (`/blog/[slug]`) để xuất ra tệp `/sitemap.xml` chuẩn ISO-8601.
   - `robots.txt` mở quyền truy cập (`Allow: /`) cho cả Googlebot, Bingbot lẫn các AI Crawlers (`GPTBot`, `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`).

### 6.2. Giao thức Agentic Web (`llms.txt` & ARD `ai-catalog.json`, `ard.json`)
* **Tệp `public/llms.txt` (Chuẩn [llmstxt.org](https://llmstxt.org/)):**
  - Cung cấp bản đồ tri thức định dạng Markdown tinh gọn bằng tiếng Việt (kèm mô tả song ngữ cho AI quốc tế) giới thiệu về **Mekong Delta Agri (MDA Hub)**, danh mục dịch vụ đào tạo XNK & AI, danh sách các thông tư hải quan trọng điểm và đường dẫn trực tiếp tới các bài viết chuyên môn.
* **Tệp `public/.well-known/ai-catalog.json` & `public/.well-known/ard.json` (Chuẩn [ARD](https://agenticresourcediscovery.org/spec/)):**
  - Khai báo Manifest JSON (`"specVersion": "1.0"`, `"host": "mekongdeltaagri.com"`) với danh sách các tài nguyên URN (`urn:air:mekongdeltaagri.com:llms-txt`, `urn:air:mekongdeltaagri.com:services-catalog`, `urn:air:mekongdeltaagri.com:training-sample-pdf`, `urn:air:mekongdeltaagri.com:sitemap`) giúp các AI Agent tự hành khám phá dịch vụ và tài liệu đào tạo của MDA chính xác 100%.

---

## 7. KIẾN TRÚC THƯ MỤC ASTRO & CẤU HÌNH HOSTING CŨ

### 7.1. Cấu trúc Thư mục Mã nguồn Dự án (`mekongdeltaagri-astro/`)

```text
mekongdeltaagri-astro/
├── public/
│   ├── .well-known/
│   │   ├── ai-catalog.json                        # Chuẩn ARD cho AI Agents
│   │   └── ard.json                               # Bản sao tương thích chuẩn ARD
│   ├── media/
│   │   ├── logoMDAgri500x500.webp                 # Logo thương hiệu chuẩn của MDA
│   │   ├── mda-tai-lieu-dao-tao-mau-xnk-ai.pdf    # 1 File PDF đào tạo mẫu dùng cho Gallery
│   │   ├── hero-slide-1.jpg ... hero-slide-4.jpg  # Ảnh Slider trang chủ
│   │   ├── news/                                  # Ảnh Headline Photo cho Tin tức
│   │   └── blog/                                  # Ảnh Headline Photo cho Blog
│   ├── .htaccess                                  # Cấu hình Apache/LiteSpeed cho Hosting cũ
│   ├── _headers                                   # Cấu hình dự phòng nếu dùng CDN/Cloudflare
│   ├── ai-catalog.json                            # Fallback ARD ở thư mục gốc
│   ├── llms.txt                                   # Chuẩn llmstxt.org cho hệ thống LLMs
│   └── robots.txt                                 # Chỉ dẫn bọ tìm kiếm & AI bots
├── src/
│   ├── components/
│   │   ├── global/
│   │   │   ├── Header.astro                       # Header + Nút MENU + Social Links
│   │   │   ├── DrawerMenu.astro                   # Menu trượt đa cấp theo đúng Sitemap mới
│   │   │   ├── Footer.astro                       # Footer pháp nhân MD AGRI + Sitemap
│   │   │   └── Preloader.astro                    # Preloader thương hiệu MDA (#8DC435, #428442, #FF9046)
│   │   ├── shared/                                # 5 ELEMENT DÙNG CHUNG BẮT BUỘC
│   │   │   ├── AuthorGeoBox.astro                 # 1. Author Box chuẩn E-E-A-T & Schema Person
│   │   │   ├── ContactForm.astro                  # 2. Contact Form tư vấn & đăng ký học thử
│   │   │   ├── TestimonialSection.astro           # 3. Testimonial (Hardcoded content)
│   │   │   ├── TrainingGalleryPdf.astro           # 4. Gallery nội dung đào tạo mẫu + 1 file PDF
│   │   │   └── SocialLinks.astro                  # 5. Social Links đồng bộ toàn site
│   │   └── ui/
│   │       ├── CategoryBadge.astro                # Huy hiệu danh mục Blog
│   │       ├── FeaturePhoto.astro                 # Ảnh Headline Photo 1200x630
│   │       ├── FaqAccordion.astro                 # Hỏi đáp tương tác HTML5 <details>
│   │       ├── SourcesList.astro                  # Nguồn tham khảo pháp lý
│   │       ├── NewsCard.astro                     # Thẻ hiển thị bản tin (/tin-tuc)
│   │       └── BlogCard.astro                     # Thẻ hiển thị bài viết kèm Category (/blog)
│   ├── content/
│   │   ├── config.ts                              # Khai báo Schema cho 2 Collections: 'news' và 'blog'
│   │   ├── news/                                  # Nội dung Tin tức (.md)
│   │   │   ├── tin-tuc-1-thong-tu-hai-quan-2026.md
│   │   │   └── tin-tuc-2-dao-tao-ai-xnk-dbscl.md
│   │   └── blog/                                  # Nội dung Blog có phân loại Category (.md)
│   │       ├── su-that-xuat-khau-trai-cay-viet-nam.md
│   │       ├── ma-hs-va-tuan-thu-thuong-mai-xnk.md
│   │       └── ung-dung-ai-marketing-nong-san-xuat-khau.md
│   ├── layouts/
│   │   ├── BaseLayout.astro                       # Khung HTML, Head SEO, JSON-LD, Fonts, Preloader
│   │   ├── InsidePageLayout.astro                 # Template: inside_page
│   │   ├── ParentListingLayout.astro              # Template: parent_listing (Tin tức & Blog)
│   │   └── ChildDetailLayout.astro                # Template: child_detail (News Detail & Blog Detail)
│   ├── pages/
│   │   ├── index.astro                            # Trang chủ (template homepage)
│   │   ├── gioi-thieu.astro                       # Giới Thiệu (template inside_page)
│   │   ├── dang-ky-thu-khoa-hoc.astro             # Đăng ký thử khóa học (CTA page)
│   │   ├── dich-vu/
│   │   │   ├── index.astro                        # Dịch vụ tổng quan (template inside_page)
│   │   │   ├── dao-tao-xnk-1-1.astro              # Đào tạo XNK 1-1 (template inside_page)
│   │   │   └── dao-tao-chuyen-sau-doanh-nghiep/
│   │   │       ├── index.astro                    # Đào tạo chuyên sâu DN (template inside_page)
│   │   │       ├── ung-dung-ai-xnk.astro          # Ứng dụng AI cho DN XNK (template inside_page)
│   │   │       └── ai-marketing.astro             # AI Marketing (template inside_page)
│   │   ├── tin-tuc/
│   │   │   ├── index.astro                        # Tin tức Listing (template parent listing)
│   │   │   └── [slug].astro                       # Tin tức Detail (headline photo + content)
│   │   ├── blog/
│   │   │   ├── index.astro                        # Blog Listing + Category (template parent listing + category)
│   │   │   └── [slug].astro                       # Blog Detail (headline photo + category + content)
│   │   └── sitemap.xml.ts                         # Dynamic XML Sitemap Generator
│   └── styles/
│       └── global.css                             # Hệ thống Design Tokens, Typography & Spacing chuẩn
├── astro.config.mjs                               # site: 'https://mekongdeltaagri.com', output: 'static'
└── package.json
```

---

### 7.2. Cấu hình Tương thích Hosting Cũ (`public/.htaccess`)
Vì website vẫn sử dụng **Hosting hiện tại** (thường là Apache / LiteSpeed trên cPanel đang chạy WordPress), khi chuyển sang Astro SSG, toàn bộ thư mục đầu ra `dist/` sẽ thay thế mã nguồn WordPress cũ trong `public_html/`. Tệp `public/.htaccess` được tự động đóng gói vào `dist/.htaccess` để đảm bảo:
1. **Định tuyến URL tĩnh sạch sẽ (Clean URLs):** Tự động khớp `/gioi-thieu` hoặc `/dich-vu/dao-tao-xnk-1-1` tới tệp `index.html` tương ứng mà không cần đuôi `.html`.
2. **Hỗ trợ chuẩn Agentic Web (`/.well-known/*` & `/llms.txt`):** Ép kiểu `Content-Type: application/json; charset=utf-8` và bật `Access-Control-Allow-Origin: *` cho các tệp `ai-catalog.json`, `ard.json` và `llms.txt`.
3. **Chuyển hướng 301 (301 Redirects) bảo toàn SEO từ WordPress cũ:** Tự động chuyển hướng các URL tiếng Anh cũ sang cấu trúc URL tiếng Việt mới để không mất thứ hạng Google:

```apache
# =====================================================================
# MEKONG DELTA AGRI (ASTRO SSG) - .HTACCESS CHO HOSTING TRUYỀN THỐNG
# =====================================================================
RewriteEngine On
RewriteBase /

# 1. Ép buộc HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# 2. Redirect 301 các URL WordPress tiếng Anh cũ sang Sitemap Tiếng Việt mới
Redirect 301 /our-story/ /gioi-thieu/
Redirect 301 /our-story /gioi-thieu/
Redirect 301 /services-products/import-export-consultant/ /dich-vu/
Redirect 301 /services-products/import-export-consultant /dich-vu/
Redirect 301 /argo-export/ /blog/
Redirect 301 /community/grow-with-us/ /gioi-thieu/

# 3. Cấu hình MIME Types & CORS cho Agentic Web (llms.txt & ARD .well-known)
<IfModule mod_mime.c>
  AddType application/json .json
  AddType text/plain .txt
  AddCharset UTF-8 .txt .json .html .xml
</IfModule>

<IfModule mod_headers.c>
  <FilesMatch "^(ai-catalog\.json|ard\.json|llms\.txt|sitemap\.xml)$">
    Header set Access-Control-Allow-Origin "*"
    Header set X-Robots-Tag "index, follow"
  </FilesMatch>
</IfModule>

# 4. Xử lý Clean Directory URLs cho Astro Static Build
RewriteCond %{REQUEST_FILENAME} -d
RewriteCond %{REQUEST_FILENAME}/index.html -f
RewriteRule ^(.*?)/?$ $1/index.html [L]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L,QSA]

# 5. Nén Gzip/Brotli & Cache tĩnh tăng tốc Core Web Vitals trên Hosting cũ
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType application/pdf "access plus 1 month"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

---

### 7.3. Định nghĩa Content Schema (`src/content/config.ts`)
Phân tách rõ ràng 2 luồng nội dung **Tin tức (`news`)** và **Blog (`blog`)** theo đúng yêu cầu Template của Sitemap:

```typescript
import { defineCollection, z } from 'astro:content';

// 1. Collection Tin Tức (/tin-tuc/[slug]) -> Headline Photo + Content (Không yêu cầu Category)
const newsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.string(),
    updatedDate: z.string().optional(),
    headlinePhoto: z.string(),
    headlinePhotoAlt: z.string(),
    headlinePhotoCaption: z.string().optional(),
    author: z.string().default('Ban Biên Tập Pháp Lý & XNK MDA'),
    featured: z.boolean().default(false),
  }),
});

// 2. Collection Blog (/blog/[slug]) -> Headline Photo + Category + Content + GEO Schema
const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishDate: z.string(),
    updatedDate: z.string().optional(),
    category: z.enum([
      'Chứng Từ & Pháp Lý XNK',
      'Đào Tạo XNK Thực Chiến',
      'Ứng Dụng AI Trong XNK',
      'AI Marketing Quốc Tế',
    ]),
    headlinePhoto: z.string(),
    headlinePhotoAlt: z.string(),
    headlinePhotoCaption: z.string().optional(),
    author: z.string().default('Tuệ Phạm (Mr. Tuệ)'),
    readingTime: z.string().default('6 phút đọc'),
    tags: z.array(z.string()).default([]),
    faqSchema: z
      .array(
        z.object({
          question: z.string(),
          answer: z.string(),
        })
      )
      .optional(),
    sources: z
      .array(
        z.object({
          title: z.string(),
          url: z.string().url(),
        })
      )
      .optional(),
  }),
});

export const collections = {
  news: newsCollection,
  blog: blogCollection,
};
```

---

### 7.4. Quy trình Triển khai lên Hosting Hiện Tại (Deployment Workflow)
1. **Sao lưu bản WordPress hiện tại:** Nén toàn bộ thư mục `public_html` và xuất file SQL dự phòng trên cPanel trước khi chuyển đổi.
2. **Build bản tĩnh Astro:**
   ```bash
   npm install
   npm run build
   ```
   Lệnh này tạo ra thư mục `dist/` chứa toàn bộ các trang HTML tĩnh đã biên dịch, ảnh, file PDF đào tạo mẫu, `sitemap.xml`, `llms.txt`, `.well-known/ai-catalog.json` và `.htaccess`.
3. **Đẩy lên Hosting cũ:**
   - Tải toàn bộ nội dung bên trong thư mục `dist/` lên `public_html/` của hosting hiện tại (qua FTP/SFTP, cPanel File Manager, hoặc GitHub Actions FTP Deploy tự động mỗi khi `git push`).