import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="CreditCheck - Thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {

    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # Tài chính
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,
    "tong_nghia_vu": None,

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Kết quả
    "diem_tham_dinh": None
}


for key, value in default_values.items():

    if key not in st.session_state:

        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =========================================
       NỀN CHÍNH
    ========================================= */

    .stApp {

        background:
        linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef4ff 100%
        );

    }


    /* =========================================
       SIDEBAR
    ========================================= */

    section[data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #071a3d 0%,
            #0b2d63 50%,
            #0f4c81 100%
        );

    }


    section[data-testid="stSidebar"] * {

        color: white !important;

    }


    /* =========================================
       HERO HEADER
    ========================================= */

    .hero {

        background:
        linear-gradient(
            135deg,
            #071a3d 0%,
            #0b3d91 50%,
            #1677ff 100%
        );

        padding: 38px 45px;

        border-radius: 25px;

        color: white;

        margin-bottom: 30px;

        box-shadow:
        0 15px 40px
        rgba(15, 76, 129, 0.25);

    }


    .hero-title {

        font-size: 34px;

        font-weight: 800;

        line-height: 1.35;

        color: white;

    }


    .hero-sub {

        font-size: 16px;

        margin-top: 12px;

        color: #dbeafe;

        line-height: 1.6;

    }


    /* =========================================
       CARD
    ========================================= */

    .custom-card {

        background: white;

        padding: 25px;

        border-radius: 20px;

        border: 1px solid #e2e8f0;

        box-shadow:
        0 8px 25px
        rgba(15, 23, 42, 0.07);

        margin-bottom: 20px;

    }


    /* =========================================
       KPI
    ========================================= */

    .kpi-card {

        background: white;

        padding: 22px;

        border-radius: 20px;

        border: 1px solid #e2e8f0;

        box-shadow:
        0 8px 25px
        rgba(15, 23, 42, 0.07);

        text-align: center;

        min-height: 125px;

    }


    .kpi-icon {

        font-size: 28px;

    }


    .kpi-title {

        color: #64748b;

        font-size: 13px;

        font-weight: 700;

        margin-top: 5px;

    }


    .kpi-value {

        color: #0f172a;

        font-size: 27px;

        font-weight: 800;

        margin-top: 5px;

    }


    /* =========================================
       SECTION TITLE
    ========================================= */

    .section-title {

        font-size: 21px;

        font-weight: 800;

        color: #0f172a;

        margin-top: 20px;

        margin-bottom: 15px;

    }


    /* =========================================
       BUTTON
    ========================================= */

    .stButton > button {

        width: 100%;

        height: 50px;

        border-radius: 13px;

        border: none;

        font-size: 15px;

        font-weight: 800;

        color: white;

        background:
        linear-gradient(
            135deg,
            #1677ff,
            #0047ab
        );

        box-shadow:
        0 7px 20px
        rgba(22, 119, 255, 0.25);

        transition: 0.2s;

    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
        0 10px 25px
        rgba(22, 119, 255, 0.35);

    }


    /* =========================================
       RESULT BOX
    ========================================= */

    .result-green {

        background: #ecfdf5;

        border-left: 7px solid #10b981;

        padding: 25px;

        border-radius: 17px;

        box-shadow:
        0 5px 20px
        rgba(16, 185, 129, 0.08);

    }


    .result-yellow {

        background: #fffbeb;

        border-left: 7px solid #f59e0b;

        padding: 25px;

        border-radius: 17px;

        box-shadow:
        0 5px 20px
        rgba(245, 158, 11, 0.08);

    }


    .result-red {

        background: #fef2f2;

        border-left: 7px solid #ef4444;

        padding: 25px;

        border-radius: 17px;

        box-shadow:
        0 5px 20px
        rgba(239, 68, 68, 0.08);

    }


    /* =========================================
       FOOTER
    ========================================= */

    .footer {

        text-align: center;

        padding: 30px;

        color: #64748b;

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
            padding:25px 5px 15px 5px;
        ">

            <div style="
                font-size:42px;
            ">
                🏦
            </div>

            <div style="
                font-size:23px;
                font-weight:800;
                margin-top:5px;
            ">
                CREDITCHECK
            </div>

            <div style="
                font-size:11px;
                opacity:0.8;
                margin-top:5px;
            ">
                BUSINESS CREDIT APPRAISAL
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    menu = st.radio(
        "MENU CHỨC NĂNG",
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
        "### 📈 TIẾN ĐỘ HỒ SƠ"
    )


    completed = 0


    if st.session_state.ten_dn:

        completed += 1


    if st.session_state.roa is not None:

        completed += 1


    if st.session_state.tong_nghia_vu is not None:

        completed += 1


    if (
        st.session_state.ltv is not None
        or st.session_state.co_tsdb == "Không"
    ):

        completed += 1


    progress = completed / 4


    st.progress(progress)


    st.caption(
        f"Hoàn thành {completed}/4 nhóm thông tin"
    )


    st.divider()


    st.caption(
        "🏦 CREDITCHECK VERSION 2.0"
    )


    st.caption(
        "© 2026"
    )


# =========================================================
# 5. HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
            <br>
            CHO VAY DOANH NGHIỆP
        </div>

        <div class="hero-sub">
            Phân tích tài chính • Đánh giá khả năng trả nợ
            • Tài sản bảo đảm • Hỗ trợ ra quyết định tín dụng
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 6. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        "## 👋 Chào mừng bạn đến với hệ thống"
    )


    st.write(
        "Hệ thống hỗ trợ cán bộ tín dụng và người học "
        "thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp."
    )


    st.divider()


    # KPI

    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown(
            """
            <div class="kpi-card">

                <div class="kpi-icon">🏢</div>

                <div class="kpi-title">
                    HỒ SƠ DOANH NGHIỆP
                </div>

                <div class="kpi-value">
                    01
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="kpi-card">

                <div class="kpi-icon">💰</div>

                <div class="kpi-title">
                    PHÂN TÍCH TÀI CHÍNH
                </div>

                <div class="kpi-value">
                    03
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="kpi-card">

                <div class="kpi-icon">💳</div>

                <div class="kpi-title">
                    THÔNG TIN KHOẢN VAY
                </div>

                <div class="kpi-value">
                    01
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="kpi-card">

                <div class="kpi-icon">📊</div>

                <div class="kpi-title">
                    KẾT QUẢ THẨM ĐỊNH
                </div>

                <div class="kpi-value">
                    AI
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    st.markdown(
        '<div class="section-title">🚀 QUY TRÌNH THẨM ĐỊNH</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.info(
            """
            **01**

            🏢 **HỒ SƠ DOANH NGHIỆP**

            Nhập thông tin pháp lý,
            ngành nghề và thời gian hoạt động.
            """
        )


    with c2:

        st.info(
            """
            **02**

            💰 **PHÂN TÍCH TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )


    with c3:

        st.info(
            """
            **03**

            💳 **KHẢ NĂNG TRẢ NỢ**

            Đánh giá nghĩa vụ trả nợ
            và dòng tiền doanh nghiệp.
            """
        )


    with c4:

        st.info(
            """
            **04**

            📊 **KẾT QUẢ**

            Tổng hợp điểm,
            phân loại và đề xuất.
            """
        )


    st.warning(
        "⚠️ Kết quả chỉ mang tính chất hỗ trợ thẩm định, "
        "không thay thế quyết định tín dụng thực tế."
    )


# =========================================================
# 7. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title(
        "🏢 Hồ sơ doanh nghiệp"
    )


    st.caption(
        "Nhập thông tin cơ bản của doanh nghiệp cần thẩm định."
    )


    st.markdown(
        '<div class="section-title">📋 THÔNG TIN PHÁP LÝ</div>',
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp *",
            value=st.session_state.ten_dn,
            placeholder="Ví dụ: Công ty TNHH ABC"
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


    st.markdown(
        '<div class="section-title">💳 MỤC ĐÍCH VAY</div>',
        unsafe_allow_html=True
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
        placeholder="Nhập mô tả phương án sử dụng vốn..."
    )


    if st.button(
        "💾 LƯU HỒ SƠ"
    ):

        if st.session_state.ten_dn == "":

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                f"✅ Đã lưu hồ sơ: "
                f"{st.session_state.ten_dn}"
            )


# =========================================================
# 8. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title(
        "⚖️ Kiểm tra điều kiện vay vốn"
    )


    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "theo mô hình hỗ trợ thẩm định."
    )


    st.markdown(
        '<div class="section-title">1️⃣ ĐIỀU KIỆN CƠ BẢN</div>',
        unsafe_allow_html=True
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
        '<div class="section-title">2️⃣ CAM KẾT KHÁCH HÀNG</div>',
        unsafe_allow_html=True
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
        "✅ Thông tin điều kiện vay đã được cập nhật."
    )


# =========================================================
# 9. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title(
        "💰 Phân tích tài chính"
    )


    st.caption(
        "Đơn vị tính: triệu đồng"
    )


    st.markdown(
        '<div class="section-title">📊 NHẬP SỐ LIỆU</div>',
        unsafe_allow_html=True
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
                "✅ Đã phân tích thành công."
            )


    if st.session_state.roa is not None:

        st.divider()


        st.markdown(
            '<div class="section-title">📈 KẾT QUẢ</div>',
            unsafe_allow_html=True
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
            chart.set_index(
                "Chỉ tiêu"
            )
        )


# =========================================================
# 10. KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title(
        "💳 Thông tin khoản vay"
    )


    st.caption(
        "Đơn vị tính: triệu đồng"
    )


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "💰 Số tiền vay",
            min_value=0.0,
            value=st.session_state.so_tien_vay
        )


        st.session_state.thoi_gian_vay = st.number_input(
            "📅 Thời hạn vay (tháng)",
            min_value=1,
            value=st.session_state.thoi_gian_vay
        )


    with c2:

        st.session_state.lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )


        st.session_state.nghia_vu_no_cu = st.number_input(
            "💳 Nghĩa vụ nợ hiện tại/tháng",
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
            "✅ Đã tính toán nghĩa vụ trả nợ."
        )


# =========================================================
# 11. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title(
        "🏠 Tài sản bảo đảm"
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
        "🏠 Giá trị tài sản bảo đảm",
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
                "❌ Giá trị TSĐB phải lớn hơn 0."
            )


        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Vui lòng nhập số tiền vay."
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
                    "🟡 Cần xem xét thêm chất lượng TSĐB."
                )


            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH"
    )


    st.caption(
        "Hệ thống tự động tổng hợp dữ liệu từ các bước thẩm định."
    )


    if (
        st.session_state.roa is None
        or st.session_state.tong_nghia_vu is None
    ):

        st.warning(
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ ĐÁNH GIÁ."
        )


        st.info(
            """
            Vui lòng hoàn thành:

            **1.** Nhập và phân tích số liệu tài chính.

            **2.** Nhập thông tin khoản vay.

            **3.** Phân tích khả năng trả nợ.

            **4.** Phân tích tài sản bảo đảm nếu có.

            Sau đó quay lại mục **Kết quả thẩm định**.
            """
        )


    else:

        # =============================================
        # TÍNH ĐIỂM
        # =============================================

        diem = 0


        ket_qua = []


        # Năng lực pháp lý

        if st.session_state.nang_luc_phap_ly == "Có":

            diem += 15

            ket_qua.append(
                [
                    "Năng lực pháp lý",
                    "Đạt",
                    "15 điểm"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Năng lực pháp lý",
                    "Chưa đạt",
                    "0 điểm"
                ]
            )


        # Mục đích vay

        if st.session_state.muc_dich == "Có":

            diem += 10

            ket_qua.append(
                [
                    "Mục đích vay",
                    "Đạt",
                    "10 điểm"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Mục đích vay",
                    "Chưa đạt",
                    "0 điểm"
                ]
            )


        # Phương án

        if st.session_state.phuong_an_kha_thi == "Có":

            diem += 10

            ket_qua.append(
                [
                    "Phương án sử dụng vốn",
                    "Đạt",
                    "10 điểm"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Phương án sử dụng vốn",
                    "Chưa đạt",
                    "0 điểm"
                ]
            )


        # LNST

        if st.session_state.lnst > 0:

            diem += 15

            ket_qua.append(
                [
                    "LNST",
                    "Đạt",
                    f"{st.session_state.lnst:,.0f} triệu đồng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "LNST",
                    "Chưa đạt",
                    "LNST không dương"
                ]
            )


        # ROA

        if st.session_state.roa > 0:

            diem += 10

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
                    "Chưa đạt",
                    f"{st.session_state.roa:.2f}%"
                ]
            )


        # ROE

        if st.session_state.roe > 0:

            diem += 10

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
                    "Chưa đạt",
                    f"{st.session_state.roe:.2f}%"
                ]
            )


        # Tỷ lệ nợ

        if st.session_state.ty_le_no <= 70:

            diem += 10

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
                    "Chưa đạt",
                    f"{st.session_state.ty_le_no:.2f}%"
                ]
            )


        # Khả năng trả nợ

        if (
            st.session_state.dong_tien
            >= st.session_state.tong_nghia_vu
        ):

            diem += 10

            ket_qua.append(
                [
                    "Khả năng trả nợ",
                    "Đạt",
                    "Dòng tiền đáp ứng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Khả năng trả nợ",
                    "Chưa đạt",
                    "Dòng tiền chưa đáp ứng"
                ]
            )


        # LTV

        if st.session_state.ltv is None:

            diem += 10

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Không áp dụng",
                    "Không có TSĐB"
                ]
            )

        elif st.session_state.ltv <= 70:

            diem += 10

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
                    "Chưa đạt",
                    f"{st.session_state.ltv:.2f}%"
                ]
            )


        # =============================================
        # HIỂN THỊ ĐIỂM
        # =============================================

        st.markdown(
            '<div class="section-title">🎯 TỔNG QUAN ĐÁNH GIÁ</div>',
            unsafe_allow_html=True
        )


        c1, c2, c3, c4 = st.columns(4)


        c1.metric(
            "ĐIỂM THẨM ĐỊNH",
            f"{diem}/100"
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
                else "N/A"
            )
        )


        st.progress(
            min(diem / 100, 1.0)
        )


        # =============================================
        # KẾT LUẬN
        # =============================================

        st.markdown(
            '<div class="section-title">📌 KẾT LUẬN THẨM ĐỊNH</div>',
            unsafe_allow_html=True
        )


        if diem >= 80:

            st.markdown(
                """
                <div class="result-green">

                <h2>🟢 ĐỀ XUẤT CHO VAY</h2>

                <p>
                Hồ sơ có mức điểm thẩm định cao.
                Doanh nghiệp đáp ứng tương đối tốt
                các tiêu chí trong mô hình đánh giá.
                </p>

                <b>Khuyến nghị:</b>

                Có thể chuyển sang bước thẩm định
                tín dụng chi tiết.

                </div>
                """,
                unsafe_allow_html=True
            )


        elif diem >= 60:

            st.markdown(
                """
                <div class="result-yellow">

                <h2>🟡 CẦN THẨM ĐỊNH BỔ SUNG</h2>

                <p>
                Hồ sơ còn tồn tại một số tiêu chí
                chưa đạt yêu cầu trong mô hình.
                </p>

                <b>Khuyến nghị:</b>

                Cần kiểm tra thêm dòng tiền,
                lịch sử tín dụng, khả năng trả nợ
                và tài sản bảo đảm.

                </div>
                """,
                unsafe_allow_html=True
            )


        else:

            st.markdown(
                """
                <div class="result-red">

                <h2>🔴 CHƯA ĐỀ XUẤT CHO VAY</h2>

                <p>
                Hồ sơ có mức điểm thấp và còn tồn tại
                nhiều yếu tố rủi ro theo mô hình.
                </p>

                <b>Khuyến nghị:</b>

                Cần xem xét lại phương án vay,
                khả năng tài chính và các điều kiện tín dụng.

                </div>
                """,
                unsafe_allow_html=True
            )


        # =============================================
        # BẢNG CHI TIẾT
        # =============================================

        st.markdown(
            '<div class="section-title">📋 CHI TIẾT CÁC TIÊU CHÍ</div>',
            unsafe_allow_html=True
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
            ⚠️ **Lưu ý quan trọng:**

            Điểm số và ngưỡng phân loại trong ứng dụng
            là mô hình minh họa phục vụ mục đích học tập
            và hỗ trợ thẩm định.

            ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu
            hỗ trợ phân tích tín dụng, không phải điều kiện
            pháp lý bắt buộc chung cho mọi doanh nghiệp.
            """
        )


# =========================================================
# 13. FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        🏦 <b>CREDITCHECK</b>

        <br><br>

        HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

        <br><br>

        Điều kiện vay vốn • Phân tích tài chính •
        Khả năng trả nợ • Tài sản bảo đảm

        <br><br>

        © 2026

    </div>
    """,
    unsafe_allow_html=True
)
