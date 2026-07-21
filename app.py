import streamlit as st
import pandas as pd

# =========================================================

# 1. CẤU HÌNH TRANG

# =========================================================

st.set_page_config(
page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
page_icon="🏦",
layout="wide",
initial_sidebar_state="expanded"
)

# =========================================================

# 2. SESSION STATE

# =========================================================

default_values = {
"ten_dn": "",
"ma_so": "",
"nganh_nghe": "Sản xuất",
"thoi_gian_hd": 3,

"nang_luc_phap_ly": "Chưa đánh giá",
"muc_dich": "Chưa đánh giá",
"co_phuong_an": "Chưa đánh giá",
"phuong_an_kha_thi": "Chưa đánh giá",
"kha_nang_tra_no": "Chưa đánh giá",
"dung_muc_dich": "Chưa đánh giá",
"tra_no_dung_han": "Chưa đánh giá",

"doanh_thu": 0.0,
"lnst": 0.0,
"tong_tai_san": 0.0,
"von_chu_so_huu": 0.0,
"no_phai_tra": 0.0,
"dong_tien": 0.0,

"roa": None,
"roe": None,
"ty_le_no": None,

"so_tien_vay": 0.0,
"thoi_gian_vay": 12,
"lai_suat": 0.0,
"nghia_vu_no_cu": 0.0,
"tong_nghia_vu": None,

"co_tsdb": "Chưa đánh giá",
"gia_tri_tsdb": 0.0,
"ltv": None

}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================

# 3. CSS - GIAO DIỆN CAO CẤP

# =========================================================

st.markdown(
""" <style>

/* ==============================
   NỀN TOÀN BỘ ỨNG DỤNG
============================== */

.stApp {
    background:
        linear-gradient(
            135deg,
            #f4f7fb 0%,
            #eef4fb 50%,
            #f8fafc 100%
        );
}

/* ==============================
   SIDEBAR
============================== */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #071a33 0%,
            #0b2b52 50%,
            #123f6d 100%
        );
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Logo sidebar */

.sidebar-logo {
    text-align: center;
    padding: 15px 10px 20px 10px;
}

.sidebar-logo-icon {
    font-size: 42px;
    margin-bottom: 5px;
}

.sidebar-title {
    font-size: 18px;
    font-weight: 800;
    line-height: 1.4;
    letter-spacing: 0.5px;
}

.sidebar-subtitle {
    font-size: 12px;
    opacity: 0.75;
    margin-top: 8px;
}

/* ==============================
   TIÊU ĐỀ
============================== */

h1 {
    color: #092b52 !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}

h2 {
    color: #0c3b6e !important;
    font-weight: 750 !important;
}

h3 {
    color: #14558b !important;
    font-weight: 700 !important;
}

/* ==============================
   HEADER CHÍNH
============================== */

.main-header {
    background:
        linear-gradient(
            135deg,
            #071a33 0%,
            #0b3868 55%,
            #1167a8 100%
        );

    padding: 30px 35px;
    border-radius: 22px;
    margin-bottom: 25px;

    box-shadow:
        0 15px 40px rgba(7, 35, 70, 0.18);

    position: relative;
    overflow: hidden;
}

.main-header:before {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
    right: -70px;
    top: -100px;
}

.main-header:after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
    right: 120px;
    bottom: -120px;
}

.main-header-icon {
    font-size: 48px;
    margin-bottom: 5px;
}

.main-header-title {
    color: white;
    font-size: 29px;
    font-weight: 850;
    line-height: 1.25;
    position: relative;
    z-index: 2;
}

.main-header-subtitle {
    color: rgba(255,255,255,0.85);
    font-size: 15px;
    margin-top: 10px;
    position: relative;
    z-index: 2;
}

/* ==============================
   CARD
============================== */

.custom-card {
    background: rgba(255,255,255,0.95);
    padding: 24px;
    border-radius: 18px;
    border: 1px solid #e3eaf2;
    box-shadow:
        0 8px 25px rgba(15, 45, 75, 0.07);
    margin-bottom: 20px;
}

.card-title {
    color: #0b3765;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
}

.card-description {
    color: #66788a;
    font-size: 14px;
    line-height: 1.6;
}

/* ==============================
   KPI
============================== */

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            #ffffff,
            #f7faff
        );

    border: 1px solid #e0e8f1;

    padding: 20px;

    border-radius: 18px;

    box-shadow:
        0 8px 22px rgba(12, 45, 80, 0.07);

    transition: all 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow:
        0 14px 30px rgba(12, 45, 80, 0.12);
}

div[data-testid="stMetricLabel"] {
    color: #63758a !important;
    font-weight: 650 !important;
}

div[data-testid="stMetricValue"] {
    color: #0b3765 !important;
    font-weight: 850 !important;
}

/* ==============================
   INPUT
============================== */

div[data-baseweb="input"] {
    border-radius: 10px;
}

div[data-baseweb="select"] {
    border-radius: 10px;
}

textarea {
    border-radius: 10px !important;
}

/* ==============================
   BUTTON
============================== */

.stButton > button {
    width: 100%;
    min-height: 48px;

    border-radius: 12px;

    border: none;

    background:
        linear-gradient(
            135deg,
            #0b3765,
            #1171b8
        );

    color: white;

    font-size: 15px;
    font-weight: 750;

    box-shadow:
        0 6px 16px rgba(11, 55, 101, 0.2);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 10px 25px rgba(11, 55, 101, 0.3);

    background:
        linear-gradient(
            135deg,
            #0d447b,
            #1484d0
        );

    color: white;
}

/* ==============================
   ALERT
============================== */

div[data-testid="stAlert"] {
    border-radius: 14px;
    border: none;
}

/* ==============================
   DATAFRAME
============================== */

div[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
    box-shadow:
        0 6px 20px rgba(15, 45, 75, 0.06);
}

/* ==============================
   DIVIDER
============================== */

hr {
    border: none;
    border-top: 1px solid #dce5ef;
    margin: 25px 0;
}

/* ==============================
   FOOTER
============================== */

.footer {
    text-align: center;
    color: #718096;
    font-size: 13px;
    padding: 20px;
    margin-top: 30px;
}

/* ==============================
   BADGE
============================== */

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #e9f3ff;
    color: #0b5794;
    font-size: 12px;
    font-weight: 700;
}

</style>
""",
unsafe_allow_html=True

)

# =========================================================

# 4. SIDEBAR

# =========================================================

with st.sidebar:

st.markdown(
    """
    <div class="sidebar-logo">

        <div class="sidebar-logo-icon">
            🏦
        </div>

        <div class="sidebar-title">
            HỆ THỐNG HỖ TRỢ<br>
            THẨM ĐỊNH CHO VAY<br>
            DOANH NGHIỆP
        </div>

        <div class="sidebar-subtitle">
            HỖ TRỢ PHÂN TÍCH TÍN DỤNG
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

menu = st.radio(
    "ĐIỀU HƯỚNG HỆ THỐNG",
    [
        "🏠 Tổng quan",
        "🏢 Hồ sơ doanh nghiệp",
        "⚖️ Điều kiện vay vốn",
        "💰 Phân tích tài chính",
        "💳 Thông tin khoản vay",
        "🏠 Tài sản bảo đảm",
        "📊 Kết quả thẩm định"
    ]
)

st.divider()

st.caption(
    "🏦 Hệ thống hỗ trợ thẩm định"
)

st.caption(
    "Phiên bản 1.0"
)

# =========================================================

# 5. TRANG TỔNG QUAN

# =========================================================

if menu == "🏠 Tổng quan":

st.markdown(
    """
    <div class="main-header">

        <div class="main-header-icon">
            🏦
        </div>

        <div class="main-header-title">
            HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
            CHO VAY DOANH NGHIỆP
        </div>

        <div class="main-header-subtitle">
            Phân tích hồ sơ • Đánh giá tài chính •
            Khả năng trả nợ • Tài sản bảo đảm •
            Hỗ trợ quyết định tín dụng
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="custom-card">

        <div class="card-title">
            👋 CHÀO MỪNG BẠN ĐẾN VỚI HỆ THỐNG
        </div>

        <div class="card-description">
            Hệ thống hỗ trợ cán bộ tín dụng và người học
            thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp.
            Các chỉ tiêu tài chính và thông tin khoản vay được
            tổng hợp nhằm hỗ trợ quá trình phân tích và ra quyết định.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("📊 TỔNG QUAN HỆ THỐNG")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🏢 HỒ SƠ DOANH NGHIỆP",
        "01",
        "Thông tin pháp lý"
    )

with c2:
    st.metric(
        "💰 PHÂN TÍCH TÀI CHÍNH",
        "03",
        "Chỉ tiêu chính"
    )

with c3:
    st.metric(
        "💳 KHOẢN VAY",
        "01",
        "Thông tin khoản vay"
    )

with c4:
    st.metric(
        "📊 THẨM ĐỊNH",
        "AI",
        "Hỗ trợ đánh giá"
    )

st.divider()

st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="custom-card">

        <div style="font-size:32px;">🏢</div>

        <div class="card-title">
        01. HỒ SƠ DOANH NGHIỆP
        </div>

        <div class="card-description">
        Nhập thông tin doanh nghiệp,
        mã số doanh nghiệp, ngành nghề
        và thời gian hoạt động.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="custom-card">

        <div style="font-size:32px;">💰</div>

        <div class="card-title">
        02. PHÂN TÍCH TÀI CHÍNH
        </div>

        <div class="card-description">
        Đánh giá LNST, ROA, ROE,
        tỷ lệ nợ và dòng tiền
        từ hoạt động kinh doanh.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="custom-card">

        <div style="font-size:32px;">💳</div>

        <div class="card-title">
        03. KHẢ NĂNG TRẢ NỢ
        </div>

        <div class="card-description">
        Tính toán gốc, lãi,
        nghĩa vụ trả nợ và đánh giá
        khả năng đáp ứng dòng tiền.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="custom-card">

        <div style="font-size:32px;">📊</div>

        <div class="card-title">
        04. KẾT QUẢ THẨM ĐỊNH
        </div>

        <div class="card-description">
        Tổng hợp các tiêu chí,
        tính điểm và đưa ra
        đề xuất hỗ trợ thẩm định.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

st.warning(
    "⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ "
    "thẩm định, không thay thế quyết định tín dụng thực tế."
)


# =========================================================

# 6. HỒ SƠ DOANH NGHIỆP

# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

```
st.title("🏢 HỒ SƠ DOANH NGHIỆP")

st.markdown(
    '<span class="badge">THÔNG TIN KHÁCH HÀNG DOANH NGHIỆP</span>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("📋 Thông tin pháp lý")

c1, c2 = st.columns(2)

with c1:

    st.session_state.ten_dn = st.text_input(
        "Tên doanh nghiệp",
        value=st.session_state.ten_dn,
        placeholder="Nhập tên doanh nghiệp..."
    )

    st.session_state.ma_so = st.text_input(
        "Mã số doanh nghiệp",
        value=st.session_state.ma_so,
        placeholder="Nhập mã số doanh nghiệp..."
    )

with c2:

    st.session_state.nganh_nghe = st.selectbox(
        "Ngành nghề kinh doanh",
        [
            "Sản xuất",
            "Thương mại",
            "Dịch vụ",
            "Xây dựng",
            "Vận tải",
            "Công nghệ",
            "Nông nghiệp",
            "Khác"
        ]
    )

    st.session_state.thoi_gian_hd = st.number_input(
        "Thời gian hoạt động (năm)",
        min_value=0,
        value=st.session_state.thoi_gian_hd
    )

st.divider()

st.subheader("💳 Mục đích vay vốn")

muc_dich_vay = st.selectbox(
    "Mục đích sử dụng vốn",
    [
        "Bổ sung vốn lưu động",
        "Mua nguyên vật liệu",
        "Đầu tư máy móc thiết bị",
        "Mở rộng sản xuất",
        "Mua tài sản cố định",
        "Khác"
    ]
)

phuong_an = st.text_area(
    "Mô tả phương án sử dụng vốn",
    placeholder="Nhập chi tiết phương án sử dụng vốn..."
)

st.divider()

if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

    if st.session_state.ten_dn == "":

        st.error(
            "❌ Vui lòng nhập tên doanh nghiệp."
        )

    else:

        st.success(
            f"✅ Đã lưu hồ sơ doanh nghiệp: "
            f"{st.session_state.ten_dn}"
        )
```

# =========================================================

# 7. ĐIỀU KIỆN VAY VỐN

# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

st.title("⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN")

st.info(
    "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
    "điều kiện vay vốn của doanh nghiệp."
)

st.subheader("1️⃣ ĐIỀU KIỆN CƠ BẢN")

c1, c2 = st.columns(2)

with c1:

    st.session_state.nang_luc_phap_ly = st.selectbox(
        "Doanh nghiệp có năng lực pháp lý?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

    st.session_state.muc_dich = st.selectbox(
        "Mục đích vay hợp pháp?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

    st.session_state.co_phuong_an = st.selectbox(
        "Có phương án sử dụng vốn?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

with c2:

    st.session_state.phuong_an_kha_thi = st.selectbox(
        "Phương án sử dụng vốn khả thi?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

    st.session_state.kha_nang_tra_no = st.selectbox(
        "Có khả năng tài chính trả nợ?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

st.divider()

st.subheader("2️⃣ CAM KẾT CỦA KHÁCH HÀNG")

c1, c2 = st.columns(2)

with c1:

    st.session_state.dung_muc_dich = st.selectbox(
        "Cam kết sử dụng vốn đúng mục đích?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

with c2:

    st.session_state.tra_no_dung_han = st.selectbox(
        "Cam kết hoàn trả nợ đúng hạn?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]
    )

st.success(
    "✅ Thông tin điều kiện vay vốn đã được cập nhật."
)

# =========================================================

# 8. PHÂN TÍCH TÀI CHÍNH

# =========================================================

elif menu == "💰 Phân tích tài chính":

st.title("💰 PHÂN TÍCH TÀI CHÍNH")

st.caption(
    "Đơn vị nhập liệu: triệu đồng"
)

st.subheader("📊 NHẬP SỐ LIỆU TÀI CHÍNH")

c1, c2 = st.columns(2)

with c1:

    st.session_state.doanh_thu = st.number_input(
        "Doanh thu",
        min_value=0.0,
        value=st.session_state.doanh_thu
    )

    st.session_state.lnst = st.number_input(
        "Lợi nhuận sau thuế (LNST)",
        value=st.session_state.lnst
    )

    st.session_state.tong_tai_san = st.number_input(
        "Tổng tài sản",
        min_value=0.0,
        value=st.session_state.tong_tai_san
    )

with c2:

    st.session_state.von_chu_so_huu = st.number_input(
        "Vốn chủ sở hữu",
        min_value=0.0,
        value=st.session_state.von_chu_so_huu
    )

    st.session_state.no_phai_tra = st.number_input(
        "Nợ phải trả",
        min_value=0.0,
        value=st.session_state.no_phai_tra
    )

    st.session_state.dong_tien = st.number_input(
        "Dòng tiền từ hoạt động kinh doanh",
        value=st.session_state.dong_tien
    )

st.divider()

if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

    if st.session_state.tong_tai_san <= 0:

        st.error(
            "❌ Tổng tài sản phải lớn hơn 0."
        )

    elif st.session_state.von_chu_so_huu <= 0:

        st.error(
            "❌ Vốn chủ sở hữu phải lớn hơn 0."
        )

    else:

        st.session_state.roa = (
            st.session_state.lnst
            / st.session_state.tong_tai_san
            * 100
        )

        st.session_state.roe = (
            st.session_state.lnst
            / st.session_state.von_chu_so_huu
            * 100
        )

        st.session_state.ty_le_no = (
            st.session_state.no_phai_tra
            / st.session_state.tong_tai_san
            * 100
        )

        st.success(
            "✅ Đã phân tích tài chính thành công."
        )

if st.session_state.roa is not None:

    st.divider()

    st.subheader("📈 KẾT QUẢ PHÂN TÍCH")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "ROA",
        f"{st.session_state.roa:.2f}%"
    )

    c2.metric(
        "ROE",
        f"{st.session_state.roe:.2f}%"
    )

    c3.metric(
        "TỶ LỆ NỢ",
        f"{st.session_state.ty_le_no:.2f}%"
    )

    st.subheader("📊 BIỂU ĐỒ CHỈ TIÊU")

    chart = pd.DataFrame(
        {
            "Chỉ tiêu": [
                "ROA",
                "ROE",
                "Tỷ lệ nợ"
            ],
            "Giá trị": [
                st.session_state.roa,
                st.session_state.roe,
                st.session_state.ty_le_no
            ]
        }
    )

    st.bar_chart(
        chart.set_index("Chỉ tiêu")
    )

# =========================================================

# 9. THÔNG TIN KHOẢN VAY

# =========================================================

elif menu == "💳 Thông tin khoản vay":

```
st.title("💳 THÔNG TIN KHOẢN VAY")

st.caption(
    "Đơn vị: triệu đồng | Lãi suất: %/năm"
)

c1, c2 = st.columns(2)

with c1:

    st.session_state.so_tien_vay = st.number_input(
        "Số tiền vay",
        min_value=0.0,
        value=st.session_state.so_tien_vay
    )

    st.session_state.thoi_gian_vay = st.number_input(
        "Thời hạn vay (tháng)",
        min_value=1,
        value=st.session_state.thoi_gian_vay
    )

with c2:

    st.session_state.lai_suat = st.number_input(
        "Lãi suất (%/năm)",
        min_value=0.0,
        value=st.session_state.lai_suat
    )

    st.session_state.nghia_vu_no_cu = st.number_input(
        "Nghĩa vụ trả nợ hiện tại/tháng",
        min_value=0.0,
        value=st.session_state.nghia_vu_no_cu
    )

st.divider()

if st.button("💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"):

    tien_goc = (
        st.session_state.so_tien_vay
        / st.session_state.thoi_gian_vay
    )

    tien_lai = (
        st.session_state.so_tien_vay
        * st.session_state.lai_suat
        / 100
        / 12
    )

    st.session_state.tong_nghia_vu = (
        st.session_state.nghia_vu_no_cu
        + tien_goc
        + tien_lai
    )

    st.success(
        "✅ Đã tính toán nghĩa vụ trả nợ."
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "GỐC / THÁNG",
        f"{tien_goc:,.2f}"
    )

    c2.metric(
        "LÃI THÁNG ĐẦU",
        f"{tien_lai:,.2f}"
    )

    c3.metric(
        "TỔNG NGHĨA VỤ / THÁNG",
        f"{st.session_state.tong_nghia_vu:,.2f}"
    )

# =========================================================

# 10. TÀI SẢN BẢO ĐẢM

# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

st.title("🏠 TÀI SẢN BẢO ĐẢM")

st.info(
    "LTV là chỉ tiêu hỗ trợ phân tích tín dụng, "
    "được tính bằng Số tiền vay / Giá trị tài sản bảo đảm."
)

st.session_state.co_tsdb = st.selectbox(
    "Khoản vay có tài sản bảo đảm?",
    [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]
)

st.session_state.gia_tri_tsdb = st.number_input(
    "Giá trị tài sản bảo đảm",
    min_value=0.0,
    value=st.session_state.gia_tri_tsdb
)

st.divider()

if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

    if st.session_state.co_tsdb == "Không":

        st.session_state.ltv = None

        st.info(
            "ℹ️ Khoản vay không có tài sản bảo đảm."
        )

    elif st.session_state.gia_tri_tsdb <= 0:

        st.error(
            "❌ Giá trị TSĐB phải lớn hơn 0."
        )

    elif st.session_state.so_tien_vay <= 0:

        st.error(
            "❌ Vui lòng nhập số tiền vay trước."
        )

    else:

        st.session_state.ltv = (
            st.session_state.so_tien_vay
            / st.session_state.gia_tri_tsdb
            * 100
        )

        st.metric(
            "LTV",
            f"{st.session_state.ltv:.2f}%"
        )

        if st.session_state.ltv <= 70:

            st.success(
                "🟢 LTV ở mức tương đối thấp."
            )

        elif st.session_state.ltv <= 100:

            st.warning(
                "🟡 Cần xem xét thêm chất lượng tài sản bảo đảm."
            )

        else:

            st.error(
                "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."
            )

# =========================================================

# 11. KẾT QUẢ THẨM ĐỊNH

# =========================================================

elif menu == "📊 Kết quả thẩm định":

```
st.title("📊 KẾT QUẢ THẨM ĐỊNH")

st.write(
    "Hệ thống tổng hợp kết quả từ các nhóm tiêu chí "
    "để hỗ trợ đánh giá sơ bộ hồ sơ tín dụng."
)

if st.session_state.roa is None:

    st.warning(
        "⚠️ Chưa có dữ liệu phân tích tài chính."
    )

    st.info(
        "Vui lòng vào mục 'Phân tích tài chính' "
        "và thực hiện phân tích trước."
    )

elif st.session_state.tong_nghia_vu is None:

    st.warning(
        "⚠️ Chưa có dữ liệu khoản vay."
    )

    st.info(
        "Vui lòng vào mục 'Thông tin khoản vay' "
        "và thực hiện phân tích khả năng trả nợ."
    )

else:

    diem = 0

    ket_qua = []

    # LNST

    if st.session_state.lnst > 0:

        diem += 15

        ket_qua.append(
            [
                "LNST",
                "Đạt",
                f"{st.session_state.lnst:,.2f} triệu đồng"
            ]
        )

    else:

        ket_qua.append(
            [
                "LNST",
                "Không đạt",
                "LNST không dương"
            ]
        )

    # ROA

    if st.session_state.roa > 0:

        diem += 15

        ket_qua.append(
            [
                "ROA",
                "Đạt",
                f"{st.session_state.roa:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "ROA",
                "Không đạt",
                f"{st.session_state.roa:.2f}%"
            ]
        )

    # ROE

    if st.session_state.roe > 0:

        diem += 15

        ket_qua.append(
            [
                "ROE",
                "Đạt",
                f"{st.session_state.roe:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "ROE",
                "Không đạt",
                f"{st.session_state.roe:.2f}%"
            ]
        )

    # TỶ LỆ NỢ

    if st.session_state.ty_le_no <= 70:

        diem += 15

        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Đạt",
                f"{st.session_state.ty_le_no:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Không đạt",
                f"{st.session_state.ty_le_no:.2f}%"
            ]
        )

    # DÒNG TIỀN

    if (
        st.session_state.dong_tien
        >= st.session_state.tong_nghia_vu
    ):

        diem += 15

        ket_qua.append(
            [
                "Khả năng trả nợ",
                "Đạt",
                "Dòng tiền đáp ứng nghĩa vụ"
            ]
        )

    else:

        ket_qua.append(
            [
                "Khả năng trả nợ",
                "Không đạt",
                "Dòng tiền chưa đáp ứng"
            ]
        )

    # LTV

    if st.session_state.ltv is None:

        diem += 15

        ket_qua.append(
            [
                "Tài sản bảo đảm",
                "Không áp dụng",
                "Không có TSĐB"
            ]
        )

    elif st.session_state.ltv <= 70:

        diem += 15

        ket_qua.append(
            [
                "LTV",
                "Đạt",
                f"{st.session_state.ltv:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "LTV",
                "Không đạt",
                f"{st.session_state.ltv:.2f}%"
            ]
        )

    # ==============================================
    # TỔNG QUAN
    # ==============================================

    st.divider()

    st.subheader("🎯 TỔNG QUAN KẾT QUẢ")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "ĐIỂM THẨM ĐỊNH",
        f"{diem}/90"
    )

    c2.metric(
        "ROA",
        f"{st.session_state.roa:.2f}%"
    )

    c3.metric(
        "ROE",
        f"{st.session_state.roe:.2f}%"
    )

    c4.metric(
        "LTV",
        (
            f"{st.session_state.ltv:.2f}%"
            if st.session_state.ltv is not None
            else "Không áp dụng"
        )
    )

    st.divider()

    # ==============================================
    # KẾT LUẬN
    # ==============================================

    st.subheader("📌 KẾT LUẬN THẨM ĐỊNH")

    ty_le_diem = diem / 90 * 100

    if ty_le_diem >= 80:

        st.success(
            "🟢 ĐỀ XUẤT CHO VAY"
        )

        st.metric(
            "MỨC ĐÁNH GIÁ",
            f"{ty_le_diem:.1f}%"
        )

        st.info(
            "Hồ sơ có kết quả tương đối tích cực "
            "theo mô hình hỗ trợ. Có thể chuyển sang "
            "bước thẩm định tín dụng chi tiết."
        )

    elif ty_le_diem >= 60:

        st.warning(
            "🟡 CẦN THẨM ĐỊNH BỔ SUNG"
        )

        st.metric(
            "MỨC ĐÁNH GIÁ",
            f"{ty_le_diem:.1f}%"
        )

        st.info(
            "Cần xem xét thêm dòng tiền, "
            "khả năng trả nợ, lịch sử tín dụng, "
            "phương án sử dụng vốn và tài sản bảo đảm."
        )

    else:

        st.error(
            "🔴 CHƯA ĐỀ XUẤT CHO VAY"
        )

        st.metric(
            "MỨC ĐÁNH GIÁ",
            f"{ty_le_diem:.1f}%"
        )

        st.info(
            "Hồ sơ còn nhiều tiêu chí chưa đạt "
            "theo mô hình đánh giá. Cần xem xét "
            "bổ sung hoặc điều chỉnh phương án vay."
        )

    # ==============================================
    # BẢNG CHI TIẾT
    # ==============================================

    st.divider()

    st.subheader("📋 CHI TIẾT KẾT QUẢ")

    df_ket_qua = pd.DataFrame(
        ket_qua,
        columns=[
            "Tiêu chí",
            "Kết quả",
            "Đánh giá"
        ]
    )

    st.dataframe(
        df_ket_qua,
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        """
        ⚠️ LƯU Ý QUAN TRỌNG:

        Kết quả trên chỉ mang tính chất hỗ trợ thẩm định.

        ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu hỗ trợ
        phân tích tín dụng, không phải điều kiện pháp lý
        bắt buộc chung cho mọi doanh nghiệp.

        Quyết định cho vay thực tế phụ thuộc vào hồ sơ,
        lịch sử tín dụng, dòng tiền, phương án kinh doanh,
        tài sản bảo đảm và chính sách của tổ chức tín dụng.
        """
    )

# =========================================================

# 12. FOOTER

# =========================================================

st.divider()

st.markdown(
""" <div class="footer">

    🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>
    <br>
    Hỗ trợ phân tích hồ sơ và đánh giá tín dụng doanh nghiệp
    <br><br>
    <span style="font-size:12px;">
    ⚠️ Kết quả chỉ mang tính chất hỗ trợ tham khảo
    </span>

</div>
""",
unsafe_allow_html=True

)
