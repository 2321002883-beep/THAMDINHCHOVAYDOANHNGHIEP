import streamlit as st
import pandas as pd

# =========================================================

# 1. CẤU HÌNH

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

# HỒ SƠ DOANH NGHIỆP
"ten_dn": "",
"ma_so": "",
"nganh_nghe": "Sản xuất",
"thoi_gian_hd": 3,

# ĐIỀU KIỆN VAY
"nang_luc_phap_ly": "Chưa đánh giá",
"muc_dich": "Chưa đánh giá",
"co_phuong_an": "Chưa đánh giá",
"phuong_an_kha_thi": "Chưa đánh giá",
"kha_nang_tra_no": "Chưa đánh giá",
"dung_muc_dich": "Chưa đánh giá",
"tra_no_dung_han": "Chưa đánh giá",

# TÀI CHÍNH
"doanh_thu": 0.0,
"lnst": 0.0,
"tong_tai_san": 0.0,
"von_chu_so_huu": 0.0,
"no_phai_tra": 0.0,
"dong_tien": 0.0,

"roa": None,
"roe": None,
"ty_le_no": None,

# KHOẢN VAY
"so_tien_vay": 0.0,
"thoi_gian_vay": 12,
"lai_suat": 0.0,
"nghia_vu_no_cu": 0.0,
"tong_nghia_vu": None,

# TÀI SẢN BẢO ĐẢM
"co_tsdb": "Chưa đánh giá",
"gia_tri_tsdb": 0.0,
"ltv": None
```

}

for key, value in default_values.items():

```
if key not in st.session_state:
    st.session_state[key] = value
```

# =========================================================

# 3. CSS PREMIUM BANKING

# =========================================================

st.markdown(
""" <style>

```
/* =====================================================
   GLOBAL
===================================================== */

.stApp {

    background:
    radial-gradient(
        circle at 10% 10%,
        rgba(24,119,242,0.08),
        transparent 28%
    ),

    radial-gradient(
        circle at 90% 20%,
        rgba(0,188,212,0.07),
        transparent 25%
    ),

    linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef5fc 50%,
        #f9fcff 100%
    );

}


/* =====================================================
   MAIN CONTENT
===================================================== */

.main .block-container {

    padding-top: 2rem;

    padding-bottom: 3rem;

    max-width: 1500px;

}


/* =====================================================
   SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #041426 0%,
        #07284b 48%,
        #063b63 100%
    );

    border-right:
    1px solid
    rgba(255,255,255,0.08);

}


section[data-testid="stSidebar"] * {

    color: #ffffff !important;

}


section[data-testid="stSidebar"] .stRadio > label {

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 0.8px;

    color: #a9c9e8 !important;

}


section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {

    gap: 7px;

}


section[data-testid="stSidebar"] .stRadio label {

    padding: 11px 14px;

    border-radius: 12px;

    transition:
    all 0.2s ease;

}


section[data-testid="stSidebar"] .stRadio label:hover {

    background:
    rgba(255,255,255,0.10);

    transform:
    translateX(4px);

}


/* =====================================================
   HEADINGS
===================================================== */

h1 {

    color: #06274b !important;

    font-weight: 850 !important;

    letter-spacing: -1px;

}


h2 {

    color: #073b6d !important;

    font-weight: 800 !important;

}


h3 {

    color: #07538b !important;

    font-weight: 750 !important;

}


/* =====================================================
   PREMIUM HERO
===================================================== */

.hero-premium {

    position: relative;

    overflow: hidden;

    padding: 42px 45px;

    border-radius: 28px;

    background:

    radial-gradient(
        circle at 90% 10%,
        rgba(0,229,255,0.22),
        transparent 25%
    ),

    linear-gradient(
        135deg,
        #031b35 0%,
        #073d6d 55%,
        #087fa3 100%
    );

    box-shadow:
    0 25px 60px
    rgba(4,45,82,0.22);

    margin-bottom: 30px;

    border:
    1px solid
    rgba(255,255,255,0.12);

}


.hero-premium::after {

    content: "";

    position: absolute;

    width: 250px;

    height: 250px;

    right: -80px;

    bottom: -100px;

    border-radius: 50%;

    background:
    rgba(255,255,255,0.06);

}


.hero-icon {

    font-size: 54px;

    margin-bottom: 12px;

}


.hero-title {

    color: #ffffff;

    font-size: 34px;

    font-weight: 850;

    line-height: 1.25;

    letter-spacing: -0.7px;

}


.hero-subtitle {

    color:
    rgba(255,255,255,0.82);

    font-size: 15px;

    margin-top: 12px;

    line-height: 1.7;

}


/* =====================================================
   KPI CARDS
===================================================== */

.kpi {

    position: relative;

    background:
    rgba(255,255,255,0.90);

    backdrop-filter:
    blur(12px);

    border:
    1px solid
    rgba(214,226,240,0.85);

    border-radius: 20px;

    padding: 22px;

    min-height: 145px;

    box-shadow:
    0 12px 35px
    rgba(7,42,77,0.07);

    transition:
    all 0.25s ease;

}


.kpi:hover {

    transform:
    translateY(-5px);

    box-shadow:
    0 18px 40px
    rgba(7,42,77,0.13);

}


.kpi-icon {

    font-size: 25px;

    margin-bottom: 10px;

}


.kpi-label {

    color: #718096;

    font-size: 12px;

    font-weight: 750;

    letter-spacing: 0.7px;

}


.kpi-value {

    color: #06274b;

    font-size: 21px;

    font-weight: 850;

    margin-top: 10px;

}


.kpi-status {

    color: #0b7891;

    font-size: 12px;

    font-weight: 650;

    margin-top: 7px;

}


/* =====================================================
   PROCESS CARDS
===================================================== */

.process {

    background:
    rgba(255,255,255,0.92);

    border:
    1px solid
    #e1eaf3;

    border-radius: 22px;

    padding: 25px;

    min-height: 220px;

    box-shadow:
    0 10px 30px
    rgba(7,42,77,0.06);

    transition:
    all 0.25s ease;

}


.process:hover {

    transform:
    translateY(-6px);

    box-shadow:
    0 18px 40px
    rgba(7,42,77,0.12);

    border-color:
    #8ccde0;

}


.process-number {

    width: 42px;

    height: 42px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 13px;

    background:
    linear-gradient(
        135deg,
        #073b6d,
        #08a0bd
    );

    color: white;

    font-weight: 850;

    font-size: 15px;

    margin-bottom: 18px;

}


.process-icon {

    font-size: 32px;

    margin-bottom: 8px;

}


.process-title {

    color: #082c50;

    font-size: 15px;

    font-weight: 800;

    margin-bottom: 9px;

}


.process-desc {

    color: #718096;

    font-size: 13px;

    line-height: 1.6;

}


/* =====================================================
   SECTION HEADER
===================================================== */

.section-header {

    display: flex;

    align-items: center;

    gap: 10px;

    color: #073b6d;

    font-size: 21px;

    font-weight: 800;

    margin-top: 25px;

    margin-bottom: 20px;

}


/* =====================================================
   PREMIUM BOX
===================================================== */

.premium-box {

    background:
    rgba(255,255,255,0.94);

    border:
    1px solid
    #e1eaf3;

    border-radius: 22px;

    padding: 28px;

    box-shadow:
    0 10px 30px
    rgba(7,42,77,0.06);

    margin-bottom: 24px;

}


/* =====================================================
   METRICS
===================================================== */

div[data-testid="stMetric"] {

    background:
    rgba(255,255,255,0.95);

    border:
    1px solid
    #e2eaf3;

    border-radius: 18px;

    padding: 20px;

    box-shadow:
    0 10px 28px
    rgba(7,42,77,0.06);

}


div[data-testid="stMetricLabel"] {

    color:
    #64748b !important;

    font-weight:
    700 !important;

}


div[data-testid="stMetricValue"] {

    color:
    #073b6d !important;

    font-weight:
    850 !important;

}


/* =====================================================
   BUTTON
===================================================== */

.stButton > button {

    width: 100%;

    border: none;

    border-radius: 13px;

    padding: 12px 22px;

    background:

    linear-gradient(
        135deg,
        #06366a,
        #078da9
    );

    color: white;

    font-weight: 800;

    letter-spacing: 0.2px;

    box-shadow:
    0 8px 22px
    rgba(7,112,155,0.20);

    transition:
    all 0.25s ease;

}


.stButton > button:hover {

    transform:
    translateY(-3px);

    box-shadow:
    0 13px 30px
    rgba(7,112,155,0.30);

}


/* =====================================================
   INPUTS
===================================================== */

div[data-baseweb="input"],
div[data-baseweb="select"] {

    border-radius: 11px;

}


input,
textarea {

    border-radius: 11px !important;

}


/* =====================================================
   ALERTS
===================================================== */

div[data-testid="stAlert"] {

    border-radius: 14px;

    border:
    1px solid
    rgba(0,0,0,0.06);

}


/* =====================================================
   PROGRESS
===================================================== */

div[data-testid="stProgressBar"] {

    height: 12px;

}


/* =====================================================
   FOOTER
===================================================== */

.footer {

    text-align: center;

    padding: 30px;

    color: #64748b;

    font-size: 13px;

    line-height: 1.8;

}


</style>
""",
unsafe_allow_html=True
```

)

# =========================================================

# 4. SIDEBAR

# =========================================================

with st.sidebar:

```
st.markdown(
    """
    <div style="
        text-align:center;
        padding:22px 5px 15px 5px;
    ">

        <div style="
            font-size:52px;
            filter: drop-shadow(0 5px 12px rgba(0,0,0,0.25));
        ">
            🏦
        </div>

        <div style="
            font-size:17px;
            font-weight:850;
            letter-spacing:1px;
            margin-top:10px;
        ">
            HỆ THỐNG THẨM ĐỊNH
        </div>

        <div style="
            color:#9bc7e8 !important;
            font-size:11px;
            font-weight:700;
            letter-spacing:1.5px;
            margin-top:7px;
        ">
            CHO VAY DOANH NGHIỆP
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


st.markdown(
    """
    <div style="
        padding:16px;
        border-radius:16px;
        background:rgba(255,255,255,0.07);
        border:1px solid rgba(255,255,255,0.08);
        text-align:center;
        line-height:1.6;
    ">

        <div style="
            font-size:20px;
            margin-bottom:7px;
        ">
            🔐
        </div>

        <b style="font-size:12px;">
            HỖ TRỢ THẨM ĐỊNH TÍN DỤNG
        </b>

        <br>

        <span style="
            font-size:11px;
            color:#a8c9e4 !important;
        ">
            Phân tích • Đánh giá • Tổng hợp
        </span>

    </div>
    """,
    unsafe_allow_html=True
)
```

# =========================================================

# 5. TỔNG QUAN

# =========================================================

if menu == "🏠 Tổng quan":

```
st.markdown(
    """
    <div class="hero-premium">

        <div class="hero-icon">
            🏦
        </div>

        <div class="hero-title">
            HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
            <br>
            CHO VAY DOANH NGHIỆP
        </div>

        <div class="hero-subtitle">
            Phân tích hồ sơ • Đánh giá tài chính • Khả năng trả nợ
            • Tài sản bảo đảm • Hỗ trợ quyết định tín dụng
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =====================================================
# KPI
# =====================================================

c1, c2, c3, c4 = st.columns(4)


with c1:

    status = (
        "Đã nhập"
        if st.session_state.ten_dn
        else "Chưa nhập"
    )

    st.markdown(
        f"""
        <div class="kpi">

            <div class="kpi-icon">
                🏢
            </div>

            <div class="kpi-label">
                HỒ SƠ DOANH NGHIỆP
            </div>

            <div class="kpi-value">
                {status}
            </div>

            <div class="kpi-status">
                ● Trạng thái hồ sơ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    status = (
        "Đã phân tích"
        if st.session_state.roa is not None
        else "Chưa phân tích"
    )

    st.markdown(
        f"""
        <div class="kpi">

            <div class="kpi-icon">
                💰
            </div>

            <div class="kpi-label">
                PHÂN TÍCH TÀI CHÍNH
            </div>

            <div class="kpi-value">
                {status}
            </div>

            <div class="kpi-status">
                ● ROA • ROE • Tỷ lệ nợ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    status = (
        "Đã phân tích"
        if st.session_state.tong_nghia_vu is not None
        else "Chưa thiết lập"
    )

    st.markdown(
        f"""
        <div class="kpi">

            <div class="kpi-icon">
                💳
            </div>

            <div class="kpi-label">
                KHOẢN VAY
            </div>

            <div class="kpi-value">
                {status}
            </div>

            <div class="kpi-status">
                ● Khả năng trả nợ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c4:

    if st.session_state.roa is not None:

        status = "Sẵn sàng đánh giá"

    else:

        status = "Chưa đánh giá"


    st.markdown(
        f"""
        <div class="kpi">

            <div class="kpi-icon">
                🎯
            </div>

            <div class="kpi-label">
                MÔ HÌNH THẨM ĐỊNH
            </div>

            <div class="kpi-value">
                {status}
            </div>

            <div class="kpi-status">
                ● Tổng điểm tối đa: 90
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# =====================================================
# QUY TRÌNH
# =====================================================

st.markdown(
    """
    <div class="section-header">
        🚀 QUY TRÌNH THẨM ĐỊNH
    </div>
    """,
    unsafe_allow_html=True
)


c1, c2, c3, c4 = st.columns(4)


process_data = [

    (
        c1,
        "01",
        "🏢",
        "HỒ SƠ DOANH NGHIỆP",
        "Nhập thông tin pháp lý, ngành nghề và thời gian hoạt động."
    ),

    (
        c2,
        "02",
        "💰",
        "PHÂN TÍCH TÀI CHÍNH",
        "Đánh giá doanh thu, LNST, ROA, ROE và cơ cấu nợ."
    ),

    (
        c3,
        "03",
        "💳",
        "KHẢ NĂNG TRẢ NỢ",
        "Phân tích nghĩa vụ trả nợ và dòng tiền hoạt động."
    ),

    (
        c4,
        "04",
        "📊",
        "KẾT QUẢ THẨM ĐỊNH",
        "Tổng hợp các tiêu chí và đưa ra kết quả hỗ trợ."
    )

]


for col, number, icon, title, desc in process_data:

    with col:

        st.markdown(
            f"""
            <div class="process">

                <div class="process-number">
                    {number}
                </div>

                <div class="process-icon">
                    {icon}
                </div>

                <div class="process-title">
                    {title}
                </div>

                <div class="process-desc">
                    {desc}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


st.divider()


# =====================================================
# TRẠNG THÁI
# =====================================================

st.markdown(
    """
    <div class="section-header">
        📌 TRẠNG THÁI HỒ SƠ
    </div>
    """,
    unsafe_allow_html=True
)


if st.session_state.ten_dn:

    st.success(
        f"🏢 Hồ sơ đang được xử lý: **{st.session_state.ten_dn}**"
    )

else:

    st.info(
        "📋 Chưa có hồ sơ doanh nghiệp. "
        "Hãy bắt đầu bằng cách chọn **Hồ sơ doanh nghiệp** ở menu bên trái."
    )


st.warning(
    "⚠️ Kết quả của hệ thống chỉ mang tính chất hỗ trợ thẩm định, "
    "không thay thế quyết định tín dụng thực tế."
)
```

# =========================================================

# 6. HỒ SƠ DOANH NGHIỆP

# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

```
st.title(
    "🏢 HỒ SƠ DOANH NGHIỆP"
)

st.caption(
    "Nhập thông tin nhận diện và thông tin cơ bản của doanh nghiệp."
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
)


st.markdown(
    "### 📋 THÔNG TIN DOANH NGHIỆP"
)


c1, c2 = st.columns(2)


with c1:

    st.session_state.ten_dn = st.text_input(
        "Tên doanh nghiệp",
        value=st.session_state.ten_dn,
        placeholder="Ví dụ: Công ty TNHH ABC"
    )


    st.session_state.ma_so = st.text_input(
        "Mã số doanh nghiệp",
        value=st.session_state.ma_so,
        placeholder="Nhập mã số doanh nghiệp"
    )


with c2:

    danh_sach_nganh = [

        "Sản xuất",
        "Thương mại",
        "Dịch vụ",
        "Xây dựng",
        "Vận tải",
        "Công nghệ",
        "Nông nghiệp",
        "Khác"

    ]


    st.session_state.nganh_nghe = st.selectbox(
        "Ngành nghề kinh doanh",
        danh_sach_nganh,
        index=danh_sach_nganh.index(
            st.session_state.nganh_nghe
        )
    )


    st.session_state.thoi_gian_hd = st.number_input(
        "Thời gian hoạt động (năm)",
        min_value=0,
        value=st.session_state.thoi_gian_hd
    )


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
)


st.markdown(
    "### 💳 MỤC ĐÍCH VAY"
)


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
    placeholder="Mô tả chi tiết phương án sử dụng vốn..."
)


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


if st.button(
    "💾 LƯU HỒ SƠ DOANH NGHIỆP"
):

    if st.session_state.ten_dn == "":

        st.error(
            "❌ Vui lòng nhập tên doanh nghiệp."
        )

    else:

        st.success(
            "✅ Đã lưu thông tin hồ sơ doanh nghiệp."
        )
```

# =========================================================

# 7. ĐIỀU KIỆN VAY VỐN

# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

```
st.title(
    "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
)


st.info(
    "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
    "điều kiện vay vốn và hỗ trợ quá trình thẩm định."
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
)


st.markdown(
    "### 1️⃣ ĐIỀU KIỆN CƠ BẢN"
)


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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
)


st.markdown(
    "### 2️⃣ CAM KẾT CỦA KHÁCH HÀNG"
)


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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


st.success(
    "✅ Thông tin điều kiện vay vốn đã được cập nhật."
)
```

# =========================================================

# 8. PHÂN TÍCH TÀI CHÍNH

# =========================================================

elif menu == "💰 Phân tích tài chính":

```
st.title(
    "💰 PHÂN TÍCH TÀI CHÍNH"
)


st.caption(
    "Đơn vị nhập liệu: triệu đồng"
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
)


st.markdown(
    "### 📊 NHẬP SỐ LIỆU TÀI CHÍNH"
)


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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


if st.button(
    "📊 PHÂN TÍCH TÀI CHÍNH"
):

    if st.session_state.tong_tai_san <= 0:

        st.error(
            "Tổng tài sản phải lớn hơn 0."
        )

    elif st.session_state.von_chu_so_huu <= 0:

        st.error(
            "Vốn chủ sở hữu phải lớn hơn 0."
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


    st.markdown(
        "### 📈 KẾT QUẢ PHÂN TÍCH"
    )


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
```

# =========================================================

# 9. THÔNG TIN KHOẢN VAY

# =========================================================

elif menu == "💳 Thông tin khoản vay":

```
st.title(
    "💳 THÔNG TIN KHOẢN VAY"
)


st.caption(
    "Đơn vị: triệu đồng | Lãi suất: %/năm"
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


if st.button(
    "💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
):

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


    st.success(
        "✅ Đã tính toán nghĩa vụ trả nợ."
    )
```

# =========================================================

# 10. TÀI SẢN BẢO ĐẢM

# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

```
st.title(
    "🏠 TÀI SẢN BẢO ĐẢM"
)


st.info(
    "LTV là chỉ tiêu hỗ trợ phân tích tín dụng, "
    "không phải ngưỡng pháp lý chung áp dụng cho mọi khoản vay."
)


st.markdown(
    '<div class="premium-box">',
    unsafe_allow_html=True
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


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


if st.button(
    "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
):

    if st.session_state.co_tsdb == "Không":

        st.session_state.ltv = None


        st.info(
            "Khoản vay không có tài sản bảo đảm."
        )


    elif st.session_state.gia_tri_tsdb <= 0:

        st.error(
            "Giá trị TSĐB phải lớn hơn 0."
        )


    elif st.session_state.so_tien_vay <= 0:

        st.error(
            "Vui lòng nhập số tiền vay trước."
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
                "🟡 Cần xem xét thêm chất lượng và tính thanh khoản của TSĐB."
            )


        else:

            st.error(
                "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."
            )
```

# =========================================================

# 11. KẾT QUẢ THẨM ĐỊNH

# =========================================================

elif menu == "📊 Kết quả thẩm định":

```
st.title(
    "📊 KẾT QUẢ THẨM ĐỊNH TÍN DỤNG"
)


st.caption(
    "Tổng hợp kết quả phân tích tài chính, khả năng trả nợ và tài sản bảo đảm."
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


    # KHẢ NĂNG TRẢ NỢ

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


    # =================================================
    # TÍNH TỶ LỆ ĐIỂM
    # =================================================

    ty_le_diem = diem / 90 * 100


    st.divider()


    st.markdown(
        "### 🎯 TỔNG QUAN KẾT QUẢ"
    )


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


    st.progress(
        min(ty_le_diem / 100, 1.0)
    )


    st.write(
        f"Mức độ đạt điểm: **{ty_le_diem:.1f}%**"
    )


    st.divider()


    # =================================================
    # KẾT LUẬN
    # =================================================

    st.markdown(
        "### 📌 KẾT LUẬN THẨM ĐỊNH"
    )


    if ty_le_diem >= 80:

        st.success(
            f"🟢 ĐỀ XUẤT CHO VAY — "
            f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
        )


        st.info(
            "Hồ sơ có kết quả tương đối tích cực "
            "theo mô hình hỗ trợ. Có thể chuyển sang "
            "bước thẩm định tín dụng chi tiết."
        )


    elif ty_le_diem >= 60:

        st.warning(
            f"🟡 CẦN THẨM ĐỊNH BỔ SUNG — "
            f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
        )


        st.info(
            "Cần xem xét thêm dòng tiền, khả năng trả nợ, "
            "lịch sử tín dụng, phương án sử dụng vốn và TSĐB."
        )


    else:

        st.error(
            f"🔴 CHƯA ĐỀ XUẤT CHO VAY — "
            f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
        )


        st.info(
            "Hồ sơ còn nhiều tiêu chí chưa đạt "
            "theo mô hình đánh giá. Cần xem xét "
            "bổ sung hoặc điều chỉnh phương án vay."
        )


    st.divider()


    # =================================================
    # BẢNG CHI TIẾT
    # =================================================

    st.markdown(
        "### 📋 CHI TIẾT KẾT QUẢ THẨM ĐỊNH"
    )


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


    st.divider()


    st.warning(
        """
        ⚠️ LƯU Ý QUAN TRỌNG

        Kết quả trên chỉ mang tính chất hỗ trợ thẩm định.

        ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu hỗ trợ
        phân tích tín dụng, không phải điều kiện pháp lý
        bắt buộc chung cho mọi doanh nghiệp.

        Quyết định cho vay thực tế phụ thuộc vào hồ sơ,
        lịch sử tín dụng, dòng tiền, phương án kinh doanh,
        tài sản bảo đảm và chính sách của từng tổ chức tín dụng.
        """
    )
```

# =========================================================

# 12. FOOTER

# =========================================================

st.divider()

st.markdown(
""" <div class="footer">

```
    🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>

    <br>

    Phân tích tài chính • Khả năng trả nợ • Tài sản bảo đảm

    <br>

    <span style="font-size:12px;">
    Hệ thống hỗ trợ phân tích và đánh giá hồ sơ tín dụng doanh nghiệp
    </span>

    <br><br>

    <span style="font-size:11px;">
    ⚠️ Kết quả chỉ mang tính chất hỗ trợ thẩm định
    </span>

</div>
""",
unsafe_allow_html=True
```

)
