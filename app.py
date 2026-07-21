
import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="HỆ THỐNG THẨM ĐỊNH CHO VAY DOANH NGHIỆP",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. SESSION STATE
# =========================================================

if "ten_dn" not in st.session_state:
    st.session_state.ten_dn = ""

if "ma_so" not in st.session_state:
    st.session_state.ma_so = ""

if "nganh_nghe" not in st.session_state:
    st.session_state.nganh_nghe = "Sản xuất"

if "thoi_gian_hd" not in st.session_state:
    st.session_state.thoi_gian_hd = 3

if "nang_luc_phap_ly" not in st.session_state:
    st.session_state.nang_luc_phap_ly = "Chưa đánh giá"

if "muc_dich" not in st.session_state:
    st.session_state.muc_dich = "Chưa đánh giá"

if "co_phuong_an" not in st.session_state:
    st.session_state.co_phuong_an = "Chưa đánh giá"

if "phuong_an_kha_thi" not in st.session_state:
    st.session_state.phuong_an_kha_thi = "Chưa đánh giá"

if "kha_nang_tra_no" not in st.session_state:
    st.session_state.kha_nang_tra_no = "Chưa đánh giá"

if "dung_muc_dich" not in st.session_state:
    st.session_state.dung_muc_dich = "Chưa đánh giá"

if "tra_no_dung_han" not in st.session_state:
    st.session_state.tra_no_dung_han = "Chưa đánh giá"


# =========================================================
# TÀI CHÍNH
# =========================================================

if "doanh_thu" not in st.session_state:
    st.session_state.doanh_thu = 0.0

if "lnst" not in st.session_state:
    st.session_state.lnst = 0.0

if "tong_tai_san" not in st.session_state:
    st.session_state.tong_tai_san = 0.0

if "von_chu_so_huu" not in st.session_state:
    st.session_state.von_chu_so_huu = 0.0

if "no_phai_tra" not in st.session_state:
    st.session_state.no_phai_tra = 0.0

if "dong_tien" not in st.session_state:
    st.session_state.dong_tien = 0.0


if "roa" not in st.session_state:
    st.session_state.roa = None

if "roe" not in st.session_state:
    st.session_state.roe = None

if "ty_le_no" not in st.session_state:
    st.session_state.ty_le_no = None


# =========================================================
# KHOẢN VAY
# =========================================================

if "so_tien_vay" not in st.session_state:
    st.session_state.so_tien_vay = 0.0

if "thoi_gian_vay" not in st.session_state:
    st.session_state.thoi_gian_vay = 12

if "lai_suat" not in st.session_state:
    st.session_state.lai_suat = 0.0

if "nghia_vu_no_cu" not in st.session_state:
    st.session_state.nghia_vu_no_cu = 0.0

if "tong_nghia_vu" not in st.session_state:
    st.session_state.tong_nghia_vu = None


# =========================================================
# TÀI SẢN BẢO ĐẢM
# =========================================================

if "co_tsdb" not in st.session_state:
    st.session_state.co_tsdb = "Chưa đánh giá"

if "gia_tri_tsdb" not in st.session_state:
    st.session_state.gia_tri_tsdb = 0.0

if "ltv" not in st.session_state:
    st.session_state.ltv = None


# =========================================================
# 3. CSS GIAO DIỆN HIỆN ĐẠI
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       TOÀN BỘ ỨNG DỤNG
    ===================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f5f8fc 0%,
            #eef3f9 50%,
            #f8fafc 100%
        );
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1500px;
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #071a33 0%,
            #0b2d52 45%,
            #0f426d 100%
        );

        border-right:
        1px solid rgba(255,255,255,0.08);

        box-shadow:
        5px 0px 20px rgba(0,0,0,0.12);
    }


    section[data-testid="stSidebar"] h1 {

        color:
        white !important;

        font-size:
        22px !important;

        font-weight:
        800 !important;

        line-height:
        1.4;

        text-align:
        center;

        padding:
        10px;

        margin-bottom:
        20px;
    }


    section[data-testid="stSidebar"] * {

        color:
        white;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"] {

        gap:
        8px;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"] label {

        background-color:
        rgba(255,255,255,0.06);

        padding:
        12px 15px;

        border-radius:
        10px;

        margin-bottom:
        6px;

        transition:
        all 0.25s ease;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"] label:hover {

        background-color:
        rgba(255,255,255,0.15);

        transform:
        translateX(4px);
    }


    /* =====================================================
       TIÊU ĐỀ
    ===================================================== */

    h1 {

        color:
        #082b52 !important;

        font-size:
        36px !important;

        font-weight:
        800 !important;

        letter-spacing:
        -0.5px;

        margin-bottom:
        8px;
    }


    h2 {

        color:
        #0b3c6f !important;

        font-weight:
        750 !important;
    }


    h3 {

        color:
        #14558c !important;

        font-weight:
        700 !important;
    }


    .stCaption {

        color:
        #64748b !important;

        font-size:
        14px;
    }


    /* =====================================================
       METRIC - THẺ CHỈ SỐ
    ===================================================== */

    div[data-testid="stMetric"] {

        background:
        rgba(255,255,255,0.95);

        border:
        1px solid #e2e8f0;

        padding:
        20px;

        border-radius:
        16px;

        box-shadow:
        0px 5px 18px rgba(15,23,42,0.07);

        transition:
        all 0.25s ease;

        min-height:
        120px;
    }


    div[data-testid="stMetric"]:hover {

        transform:
        translateY(-4px);

        box-shadow:
        0px 10px 25px rgba(15,23,42,0.12);

        border-color:
        #bfdbfe;
    }


    div[data-testid="stMetricLabel"] {

        color:
        #64748b !important;

        font-size:
        14px !important;

        font-weight:
        600 !important;
    }


    div[data-testid="stMetricValue"] {

        color:
        #0b3c6f !important;

        font-size:
        28px !important;

        font-weight:
        800 !important;
    }


    /* =====================================================
       INPUT
    ===================================================== */

    div[data-baseweb="input"] {

        background-color:
        white;

        border-radius:
        10px;

        border:
        1px solid #dbe4ef;

        transition:
        all 0.2s ease;
    }


    div[data-baseweb="input"]:focus-within {

        border-color:
        #1976d2;

        box-shadow:
        0px 0px 0px 3px
        rgba(25,118,210,0.12);
    }


    /* =====================================================
       SELECTBOX
    ===================================================== */

    div[data-baseweb="select"] > div {

        background-color:
        white;

        border-radius:
        10px;

        border:
        1px solid #dbe4ef;

        min-height:
        42px;
    }


    div[data-baseweb="select"] > div:hover {

        border-color:
        #1976d2;
    }


    /* =====================================================
       TEXT AREA
    ===================================================== */

    textarea {

        background-color:
        white !important;

        border:
        1px solid #dbe4ef !important;

        border-radius:
        10px !important;
    }


    textarea:focus {

        border-color:
        #1976d2 !important;

        box-shadow:
        0px 0px 0px 3px
        rgba(25,118,210,0.12) !important;
    }


    /* =====================================================
       LABEL
    ===================================================== */

    label {

        font-weight:
        600 !important;

        color:
        #334155 !important;
    }


    /* =====================================================
       BUTTON
    ===================================================== */

    .stButton > button {

        width:
        100%;

        min-height:
        45px;

        background:
        linear-gradient(
            135deg,
            #1565c0,
            #1976d2
        );

        color:
        white !important;

        border:
        none;

        border-radius:
        10px;

        font-size:
        15px;

        font-weight:
        700;

        letter-spacing:
        0.2px;

        box-shadow:
        0px 4px 12px
        rgba(21,101,192,0.25);

        transition:
        all 0.25s ease;
    }


    .stButton > button:hover {

        background:
        linear-gradient(
            135deg,
            #0d47a1,
            #1565c0
        );

        transform:
        translateY(-2px);

        box-shadow:
        0px 8px 20px
        rgba(21,101,192,0.35);
    }


    .stButton > button:active {

        transform:
        translateY(0px);
    }


    /* =====================================================
       THÔNG BÁO
    ===================================================== */

    div[data-testid="stAlert"] {

        border-radius:
        12px;

        border:
        none;

        box-shadow:
        0px 3px 12px
        rgba(15,23,42,0.05);
    }


    /* =====================================================
       DATAFRAME
    ===================================================== */

    div[data-testid="stDataFrame"] {

        border-radius:
        12px;

        overflow:
        hidden;

        border:
        1px solid #e2e8f0;

        box-shadow:
        0px 4px 15px
        rgba(15,23,42,0.06);
    }


    /* =====================================================
       BIỂU ĐỒ
    ===================================================== */

    div[data-testid="stArrowVegaLiteChart"] {

        background-color:
        white;

        padding:
        15px;

        border-radius:
        15px;

        box-shadow:
        0px 4px 15px
        rgba(15,23,42,0.06);
    }


    /* =====================================================
       ĐƯỜNG KẺ
    ===================================================== */

    hr {

        border:
        none;

        border-top:
        1px solid #dbe4ef;

        margin-top:
        25px;

        margin-bottom:
        25px;
    }


    /* =====================================================
       RESPONSIVE
    ===================================================== */

    @media (max-width: 900px) {

        .block-container {

            padding-left:
            1rem;

            padding-right:
            1rem;
        }

        h1 {

            font-size:
            28px !important;
        }

        div[data-testid="stMetricValue"] {

            font-size:
            22px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    st.title(
        "🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP"
    )

    st.divider()

    menu = st.radio(
        "CHỨC NĂNG",
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


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.title(
        "🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH"
    )

    st.header(
        "CHO VAY DOANH NGHIỆP"
    )

    st.write(
        "Phân tích tài chính • "
        "Đánh giá khả năng trả nợ • "
        "Tài sản bảo đảm • "
        "Hỗ trợ ra quyết định tín dụng"
    )

    st.divider()

    st.subheader(
        "👋 Chào mừng bạn đến với hệ thống"
    )

    st.info(
        "Hệ thống hỗ trợ cán bộ tín dụng và người học "
        "thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp."
    )

    st.divider()

    st.subheader(
        "📊 CÁC NHÓM ĐÁNH GIÁ"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🏢 Hồ sơ doanh nghiệp",
            "01"
        )

    with c2:

        st.metric(
            "💰 Phân tích tài chính",
            "03"
        )

    with c3:

        st.metric(
            "💳 Thông tin khoản vay",
            "01"
        )

    with c4:

        st.metric(
            "📊 Kết quả thẩm định",
            "AI"
        )

    st.divider()

    st.subheader(
        "🚀 QUY TRÌNH THẨM ĐỊNH"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.info(
            """
            **01**

            🏢 HỒ SƠ DOANH NGHIỆP

            Nhập thông tin pháp lý,
            ngành nghề và thời gian hoạt động.
            """
        )

    with c2:

        st.info(
            """
            **02**

            💰 PHÂN TÍCH TÀI CHÍNH

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )

    with c3:

        st.info(
            """
            **03**

            💳 KHẢ NĂNG TRẢ NỢ

            Đánh giá nghĩa vụ trả nợ
            và dòng tiền doanh nghiệp.
            """
        )

    with c4:

        st.info(
            """
            **04**

            📊 KẾT QUẢ

            Tổng hợp điểm,
            phân loại và đề xuất.
            """
        )

    st.divider()

    st.warning(
        "⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ "
        "thẩm định, không thay thế quyết định tín dụng thực tế."
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title(
        "🏢 HỒ SƠ DOANH NGHIỆP"
    )

    st.subheader(
        "📋 Thông tin pháp lý"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp",
            value=st.session_state.ten_dn
        )

        st.session_state.ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so
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

    st.subheader(
        "💳 Mục đích vay"
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
        "Mô tả phương án sử dụng vốn"
    )

    if st.button(
        "💾 LƯU HỒ SƠ"
    ):

        if st.session_state.ten_dn == "":

            st.error(
                "Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                "Đã lưu thông tin doanh nghiệp."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    )

    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "điều kiện vay vốn."
    )

    st.subheader(
        "1️⃣ Điều kiện cơ bản"
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

    st.subheader(
        "2️⃣ Cam kết của khách hàng"
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

    st.success(
        "Thông tin điều kiện vay vốn đã được cập nhật."
    )


# =========================================================
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title(
        "💰 PHÂN TÍCH TÀI CHÍNH"
    )

    st.caption(
        "Đơn vị: triệu đồng"
    )

    st.subheader(
        "📊 Nhập số liệu tài chính"
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
                "Đã phân tích tài chính thành công."
            )

    if st.session_state.roa is not None:

        st.divider()

        st.subheader(
            "📈 Kết quả phân tích"
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
            "Tỷ lệ nợ",
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


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title(
        "💳 THÔNG TIN KHOẢN VAY"
    )

    st.caption(
        "Đơn vị: triệu đồng"
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

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc/tháng",
            f"{tien_goc:,.2f}"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{tien_lai:,.2f}"
        )

        c3.metric(
            "Tổng nghĩa vụ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )

        st.success(
            "Đã tính toán nghĩa vụ trả nợ."
        )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title(
        "🏠 TÀI SẢN BẢO ĐẢM"
    )

    st.info(
        "LTV là chỉ tiêu hỗ trợ phân tích tín dụng."
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
                    "LTV ở mức tương đối thấp."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "Cần xem xét thêm chất lượng tài sản bảo đảm."
                )

            else:

                st.error(
                    "Số tiền vay lớn hơn giá trị tài sản bảo đảm."
                )


# =========================================================
# 11. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH"
    )

    st.write(
        "Hệ thống tổng hợp kết quả từ các nhóm tiêu chí."
    )

    if st.session_state.roa is None:

        st.warning(
            "⚠️ Chưa có dữ liệu phân tích tài chính."
        )

        st.info(
            "Vui lòng vào mục 'Phân tích tài chính' "
            "và bấm 'Phân tích tài chính' trước."
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

        # =================================================
        # TÍNH ĐIỂM
        # =================================================

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


        # =================================================
        # HIỂN THỊ ĐIỂM
        # =================================================

        st.divider()

        st.subheader(
            "🎯 TỔNG QUAN KẾT QUẢ"
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


        st.divider()


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH"
        )

        ty_le_diem = diem / 90 * 100


        if ty_le_diem >= 80:

            st.success(
                "🟢 ĐỀ XUẤT CHO VAY"
            )

            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
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

            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
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

            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
            )

            st.info(
                "Hồ sơ còn nhiều tiêu chí chưa đạt "
                "theo mô hình đánh giá. Cần xem xét "
                "bổ sung hoặc điều chỉnh phương án vay."
            )


        # =================================================
        # BẢNG CHI TIẾT
        # =================================================

        st.divider()

        st.subheader(
            "📋 CHI TIẾT KẾT QUẢ"
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


        st.warning(
            """
            ⚠️ LƯU Ý:

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

st.caption(
    "🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP"
)
```
