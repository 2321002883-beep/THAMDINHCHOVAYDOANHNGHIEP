import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. KHỞI TẠO SESSION STATE
# =========================================================

DEFAULTS = {
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

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN CAO CẤP
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN CHUNG
    ================================= */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f4f8fc 0%,
                #eef4fa 50%,
                #f8fbff 100%
            );
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #071a33 0%,
                #0b2b50 45%,
                #0e416d 100%
            );
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        padding: 12px 14px;
        border-radius: 12px;
        margin-bottom: 5px;
        transition: all 0.25s ease;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255,255,255,0.12);
        transform: translateX(3px);
    }


    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        color: #0b3866 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #12548a !important;
        font-weight: 700 !important;
    }


    /* ================================
       CARD METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #ffffff,
                #f4f8fc
            );

        border: 1px solid #dce8f3;
        padding: 20px;
        border-radius: 18px;

        box-shadow:
            0 8px 25px rgba(17, 55, 90, 0.08);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-4px);

        box-shadow:
            0 14px 30px rgba(17, 55, 90, 0.15);
    }

    div[data-testid="stMetricLabel"] {
        color: #58708a !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #092f57 !important;
        font-weight: 800 !important;
    }


    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;

        border: none;
        border-radius: 12px;

        padding: 12px 20px;

        font-weight: 700;
        font-size: 15px;

        color: white;

        background:
            linear-gradient(
                135deg,
                #0b5ca8,
                #0877c9
            );

        box-shadow:
            0 6px 15px rgba(8, 119, 201, 0.25);

        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 10px 25px rgba(8, 119, 201, 0.35);

        background:
            linear-gradient(
                135deg,
                #084b8c,
                #0568ad
            );
    }


    /* ================================
       INPUT
    ================================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"] {
        border-radius: 10px !important;
    }

    input,
    textarea {
        border-radius: 10px !important;
    }


    /* ================================
       CONTAINER
    ================================= */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        border: 1px solid #dce7f1 !important;

        box-shadow:
            0 8px 25px rgba(17, 55, 90, 0.06);
    }


    /* ================================
       INFO / SUCCESS / WARNING
    ================================= */

    div[data-testid="stAlert"] {
        border-radius: 14px !important;
    }


    /* ================================
       DATAFRAME
    ================================= */

    div[data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;

        box-shadow:
            0 5px 20px rgba(17, 55, 90, 0.08);
    }


    /* ================================
       DIVIDER
    ================================= */

    hr {
        border: none;
        border-top: 1px solid #d9e5ef;
        margin: 25px 0;
    }


    /* ================================
       HERO
    ================================= */

    .hero {
        padding: 35px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                #071f3b 0%,
                #0a4778 50%,
                #087bc1 100%
            );

        color: white;

        box-shadow:
            0 15px 35px rgba(7, 31, 59, 0.22);

        margin-bottom: 30px;
    }

    .hero h1 {
        color: white !important;
        font-size: 34px !important;
        margin-bottom: 10px;
    }

    .hero p {
        color: #e8f4ff;
        font-size: 16px;
        margin-bottom: 0;
    }


    /* ================================
       SECTION CARD
    ================================= */

    .section-card {
        background: white;

        padding: 25px;

        border-radius: 20px;

        border: 1px solid #e1eaf2;

        box-shadow:
            0 8px 25px rgba(17, 55, 90, 0.07);

        margin-bottom: 20px;
    }


    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;

        padding: 25px;

        color: #6b8196;

        font-size: 13px;
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
        <div style="
            text-align:center;
            padding:20px 5px 15px 5px;
        ">
            <div style="
                font-size:48px;
                margin-bottom:10px;
            ">
                🏦
            </div>

            <div style="
                font-size:18px;
                font-weight:800;
                line-height:1.4;
            ">
                HỆ THỐNG HỖ TRỢ
                <br>
                THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div style="
                margin-top:10px;
                font-size:12px;
                color:#b9d9f2 !important;
            ">
                HỖ TRỢ PHÂN TÍCH TÍN DỤNG
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div style="
            font-size:12px;
            font-weight:700;
            color:#9fc9e8 !important;
            margin-bottom:10px;
        ">
            MENU CHỨC NĂNG
        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.radio(
        "",
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
            background:rgba(255,255,255,0.08);
            padding:15px;
            border-radius:12px;
            font-size:12px;
            line-height:1.6;
            color:#d9edff !important;
        ">
        💡 <b>Hướng dẫn:</b><br>
        Vui lòng nhập dữ liệu theo từng bước,
        sau đó kiểm tra kết quả thẩm định.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero">

            <h1>
                🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Phân tích hồ sơ • Đánh giá tài chính •
                Khả năng trả nợ • Tài sản bảo đảm •
                Hỗ trợ quyết định tín dụng
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👋 Chào mừng bạn đến với hệ thống")

    st.info(
        "Hệ thống hỗ trợ cán bộ tín dụng và người học "
        "thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp."
    )

    st.divider()

    st.subheader("📊 TỔNG QUAN HỆ THỐNG")

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
            "💳 Khoản vay",
            "01"
        )

    with c4:
        st.metric(
            "📊 Kết quả",
            "AI"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.info(
            """
            ### 01

            🏢 **HỒ SƠ DOANH NGHIỆP**

            Nhập thông tin pháp lý,
            ngành nghề và thời gian hoạt động.
            """
        )

    with c2:

        st.info(
            """
            ### 02

            💰 **PHÂN TÍCH TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )

    with c3:

        st.info(
            """
            ### 03

            💳 **KHẢ NĂNG TRẢ NỢ**

            Đánh giá nghĩa vụ trả nợ
            và dòng tiền doanh nghiệp.
            """
        )

    with c4:

        st.info(
            """
            ### 04

            📊 **KẾT QUẢ THẨM ĐỊNH**

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

    st.markdown(
        """
        <div class="hero">

            <h1>🏢 HỒ SƠ DOANH NGHIỆP</h1>

            <p>
                Nhập và quản lý thông tin cơ bản
                của doanh nghiệp vay vốn
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📋 Thông tin pháp lý")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp",
            value=st.session_state.ten_dn,
            placeholder="Nhập tên doanh nghiệp"
        )

        st.session_state.ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so,
            placeholder="Nhập mã số doanh nghiệp"
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

    if st.button("💾 LƯU HỒ SƠ"):

        if st.session_state.ten_dn == "":

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                "✅ Đã lưu thông tin doanh nghiệp thành công."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.markdown(
        """
        <div class="hero">

            <h1>⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN</h1>

            <p>
                Đánh giá sơ bộ các điều kiện vay vốn
                của doanh nghiệp
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "điều kiện vay vốn. Kết quả không thay thế thẩm định "
        "tín dụng thực tế của tổ chức tín dụng."
    )

    st.subheader("1️⃣ Điều kiện cơ bản")

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

    st.subheader("2️⃣ Cam kết của khách hàng")

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

    st.markdown(
        """
        <div class="hero">

            <h1>💰 PHÂN TÍCH TÀI CHÍNH</h1>

            <p>
                Phân tích hiệu quả hoạt động,
                cơ cấu tài sản và mức độ sử dụng nợ
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("📌 Đơn vị nhập liệu: triệu đồng")

    st.subheader("📊 Nhập số liệu tài chính")

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

        st.divider()

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

    st.markdown(
        """
        <div class="hero">

            <h1>💳 THÔNG TIN KHOẢN VAY</h1>

            <p>
                Phân tích nghĩa vụ trả nợ
                và khả năng đáp ứng dòng tiền
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption("📌 Đơn vị nhập liệu: triệu đồng")

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

        st.subheader("📊 KẾT QUẢ NGHĨA VỤ TRẢ NỢ")

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
            "✅ Đã tính toán nghĩa vụ trả nợ."
        )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.markdown(
        """
        <div class="hero">

            <h1>🏠 TÀI SẢN BẢO ĐẢM</h1>

            <p>
                Đánh giá giá trị tài sản bảo đảm
                và tỷ lệ LTV của khoản vay
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "LTV là chỉ tiêu hỗ trợ phân tích tín dụng, "
        "không phải điều kiện pháp lý bắt buộc chung."
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
                "Khoản vay không có tài sản bảo đảm."
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
                    "✅ LTV ở mức tương đối thấp."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "⚠️ Cần xem xét thêm chất lượng tài sản bảo đảm."
                )

            else:

                st.error(
                    "❌ Số tiền vay lớn hơn giá trị tài sản bảo đảm."
                )


# =========================================================
# 11. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.markdown(
        """
        <div class="hero">

            <h1>📊 KẾT QUẢ THẨM ĐỊNH</h1>

            <p>
                Tổng hợp các chỉ tiêu tài chính,
                khả năng trả nợ và tài sản bảo đảm
            </p>

        </div>
        """,
        unsafe_allow_html=True
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

        # HIỂN THỊ ĐIỂM

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

        # KẾT LUẬN

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH")

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

st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>

        <br><br>

        Phục vụ mục đích học tập, nghiên cứu
        và hỗ trợ phân tích tín dụng sơ bộ.

    </div>
    """,
    unsafe_allow_html=True
)
