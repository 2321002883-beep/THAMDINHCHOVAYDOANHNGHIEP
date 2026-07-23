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
# 2. KHỞI TẠO SESSION STATE
# =========================================================

defaults = {
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "",
    "phuong_an": "",

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "cam_ket_dung_muc_dich": "Chưa đánh giá",
    "cam_ket_tra_no": "Chưa đánh giá",

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

    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False
}


for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       NỀN CHÍNH
    ========================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eef5fb 50%,
            #f8fbff 100%
        );
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #062445 0%,
            #0a3862 50%,
            #0d4e7c 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }


    /* =========================
       SIDEBAR LOGO
       QUAN TRỌNG: HTML ĐƯỢC RENDER
    ========================= */

    .sidebar-logo {
        text-align: center;
        padding: 10px 10px 25px 10px;
    }

    .sidebar-logo-icon {
        font-size: 55px;
        margin-bottom: 10px;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 800;
        line-height: 1.5;
        color: white;
    }

    .sidebar-subtitle {
        font-size: 14px;
        margin-top: 8px;
        color: #c8dff3;
    }


    /* =========================
       TIÊU ĐỀ
    ========================= */

    h1 {
        color: #08345c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b4f80 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #12618f !important;
        font-weight: 700 !important;
    }


    /* =========================
       HERO
    ========================= */

    .hero-card {
        background: linear-gradient(
            135deg,
            #062c52 0%,
            #0a5688 50%,
            #1595c5 100%
        );

        padding: 38px;
        border-radius: 25px;
        margin-bottom: 30px;

        box-shadow:
            0 15px 35px rgba(5,45,82,0.25);
    }

    .hero-title {
        color: white;
        font-size: 34px;
        font-weight: 800;
        line-height: 1.3;
        margin-bottom: 12px;
    }

    .hero-text {
        color: rgba(255,255,255,0.92);
        font-size: 17px;
        line-height: 1.7;
    }


    /* =========================
       CARD
    ========================= */

    .section-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #dce8f2;
        box-shadow: 0 7px 22px rgba(13,59,102,0.07);
        margin-bottom: 20px;
    }


    /* =========================
       PROCESS CARD
    ========================= */

    .process-card {
        background: linear-gradient(
            135deg,
            #e9f4ff,
            #d8ebfb
        );

        padding: 22px;
        border-radius: 18px;
        min-height: 180px;

        border: 1px solid #c9e0f3;

        box-shadow:
            0 6px 15px rgba(25,85,130,0.08);
    }

    .process-number {
        color: #0874b8;
        font-size: 15px;
        font-weight: 800;
    }

    .process-title {
        color: #073f6b;
        font-size: 19px;
        font-weight: 800;
        margin-top: 8px;
        margin-bottom: 10px;
    }

    .process-text {
        color: #45677f;
        font-size: 15px;
        line-height: 1.6;
    }


    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d8e5ef;
        padding: 18px;
        border-radius: 17px;

        box-shadow:
            0 7px 20px rgba(13,59,102,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #58748b !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0a4775 !important;
        font-weight: 800;
    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 12px;

        padding: 0.75rem 1rem;

        font-weight: 700;
        color: white;

        background: linear-gradient(
            135deg,
            #0863a2,
            #0e91c5
        );

        box-shadow:
            0 5px 15px rgba(8,99,162,0.25);

        transition: 0.25s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 9px 22px rgba(8,99,162,0.35);
    }


    /* =========================
       INPUT
    ========================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"],
    textarea {
        border-radius: 10px !important;
    }


    /* =========================
       TRẠNG THÁI
    ========================= */

    .status-good {
        background: #e9f8ef;
        border-left: 6px solid #1c9c59;
        padding: 18px;
        border-radius: 12px;
        color: #176b3c;
        font-weight: 800;
        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 6px solid #e4a400;
        padding: 18px;
        border-radius: 12px;
        color: #805f00;
        font-weight: 800;
        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 6px solid #d64545;
        padding: 18px;
        border-radius: 12px;
        color: #8c2525;
        font-weight: 800;
        font-size: 18px;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;
        color: #71869a;
        padding: 25px;
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

    # LOGO / BIỂU TƯỢNG
    st.markdown(
        """
        <div class="sidebar-logo">

            <div class="sidebar-logo-icon">
                🏦
            </div>

            <div class="sidebar-title">
                THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div class="sidebar-subtitle">
                Hệ thống hỗ trợ thẩm định tín dụng
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "### 📌 DANH MỤC THẨM ĐỊNH"
    )

    menu = st.radio(
        "Chọn nội dung",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện",
            "💰 Tài chính & Khả năng trả nợ",
            "💳 Khoản vay & Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )


# =========================================================
# 5. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero-card">

            <div class="hero-title">
                🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                CHO VAY DOANH NGHIỆP
            </div>

            <div class="hero-text">
                Phân tích hồ sơ • Kiểm tra điều kiện vay •
                Đánh giá tài chính • Khả năng trả nợ •
                Tài sản bảo đảm • Tổng hợp kết quả
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader(
        "👋 Chào mừng bạn đến với hệ thống"
    )

    st.write(
        """
        Hệ thống hỗ trợ cán bộ tín dụng hoặc người sử dụng
        thực hiện thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp,
        phân tích tình hình tài chính và tổng hợp các yếu tố
        hỗ trợ đánh giá khoản vay.
        """
    )

    st.divider()

    st.subheader(
        "📊 TÌNH TRẠNG HỒ SƠ"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 Hồ sơ",
            "Đã nhập"
            if st.session_state.da_luu_ho_so
            else "Chưa nhập"
        )

    with c2:
        st.metric(
            "💰 Tài chính",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )

    with c3:
        st.metric(
            "💳 Khoản vay",
            "Đã tính"
            if st.session_state.da_phan_tich_vay
            else "Chưa tính"
        )

    with c4:
        st.metric(
            "🏠 TSĐB",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tsdb
            else "Chưa phân tích"
        )

    st.divider()

    st.subheader(
        "🚀 QUY TRÌNH THẨM ĐỊNH"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    01 | HỒ SƠ
                </div>

                <div class="process-title">
                    🏢 Hồ sơ & Điều kiện
                </div>

                <div class="process-text">
                    Nhập thông tin doanh nghiệp,
                    mục đích vay và kiểm tra
                    điều kiện vay vốn.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    02 | TÀI CHÍNH
                </div>

                <div class="process-title">
                    💰 Phân tích tài chính
                </div>

                <div class="process-text">
                    Phân tích doanh thu, LNST,
                    ROA, ROE, tỷ lệ nợ
                    và dòng tiền.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    03 | KHOẢN VAY
                </div>

                <div class="process-title">
                    💳 Khoản vay & TSĐB
                </div>

                <div class="process-text">
                    Tính nghĩa vụ trả nợ,
                    DSCR và đánh giá
                    tài sản bảo đảm.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    04 | KẾT QUẢ
                </div>

                <div class="process-title">
                    📊 Thẩm định
                </div>

                <div class="process-text">
                    Tổng hợp dữ liệu và đưa ra
                    kết luận thẩm định sơ bộ.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ và không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện":

    st.title(
        "🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN"
    )

    st.subheader(
        "📋 Thông tin doanh nghiệp"
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

        st.session_state.thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
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

        st.session_state.muc_dich_vay = st.selectbox(
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

    st.session_state.phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập phương án kinh doanh và nhu cầu sử dụng vốn..."
    )

    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
    ):

        if st.session_state.ten_dn.strip() == "":

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        elif st.session_state.ma_so.strip() == "":

            st.error(
                "❌ Vui lòng nhập mã số doanh nghiệp."
            )

        elif st.session_state.phuong_an.strip() == "":

            st.error(
                "❌ Vui lòng nhập phương án sử dụng vốn."
            )

        else:

            st.session_state.da_luu_ho_so = True

            st.success(
                "✅ Đã lưu hồ sơ doanh nghiệp."
            )

    st.divider()

    st.subheader(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    )

    st.info(
        """
        Kiểm tra sơ bộ các nhóm điều kiện vay vốn.
        Kết quả thực tế còn phụ thuộc hồ sơ pháp lý,
        mục đích sử dụng vốn, phương án khả thi,
        khả năng trả nợ và chính sách của tổ chức tín dụng.
        """
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "1. Năng lực pháp lý phù hợp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "2. Mục đích vay vốn hợp pháp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.phuong_an_von = st.selectbox(
            "3. Có phương án sử dụng vốn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.phuong_an_von
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "4. Phương án sử dụng vốn khả thi?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "5. Có khả năng tài chính trả nợ?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.kha_nang_tra_no
            )
        )

        st.session_state.cam_ket_dung_muc_dich = st.selectbox(
            "6. Cam kết sử dụng vốn đúng mục đích?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.cam_ket_dung_muc_dich
            )
        )

        st.session_state.cam_ket_tra_no = st.selectbox(
            "7. Cam kết trả nợ đúng hạn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.cam_ket_tra_no
            )
        )

    if st.button(
        "🔍 KIỂM TRA ĐIỀU KIỆN VAY"
    ):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_von,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        if "Không" in dieu_kien:

            st.error(
                "🔴 Có điều kiện đang được đánh giá là Không. Hồ sơ cần được xem xét lại."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title(
        "💰 TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    st.subheader(
        "📈 Phân tích tài chính"
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
            "Dòng tiền từ hoạt động kinh doanh/tháng",
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

            st.session_state.da_phan_tich_tc = True

            st.success(
                "✅ Phân tích tài chính thành công."
            )

    if st.session_state.roa is not None:

        st.divider()

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

    st.divider()

    st.subheader(
        "📈 Khả năng trả nợ - DSCR"
    )

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng sang mục 'Khoản vay & Tài sản bảo đảm' để tính nghĩa vụ trả nợ trước."
        )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )

        with c2:

            st.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

        if st.button(
            "📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
        ):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )

                st.session_state.da_phan_tich_dscr = True

                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )

                if st.session_state.dscr >= 1:

                    st.success(
                        "🟢 Dòng tiền hiện tại đủ hoặc lớn hơn nghĩa vụ trả nợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


# =========================================================
# 8. KHOẢN VAY & TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "💳 Khoản vay & Tài sản bảo đảm":

    st.title(
        "💳 KHOẢN VAY & TÀI SẢN BẢO ĐẢM"
    )

    st.subheader(
        "💰 Thông tin khoản vay"
    )

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
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
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ"
    ):

        if st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Số tiền vay phải lớn hơn 0."
            )

        else:

            goc = (
                st.session_state.so_tien_vay
                / st.session_state.thoi_gian_vay
            )

            lai = (
                st.session_state.so_tien_vay
                * st.session_state.lai_suat
                / 100
                / 12
            )

            tong = (
                st.session_state.nghia_vu_no_cu
                + goc
                + lai
            )

            st.session_state.tien_goc_thang = goc
            st.session_state.tien_lai_thang = lai
            st.session_state.tong_nghia_vu = tong
            st.session_state.da_phan_tich_vay = True

            st.success(
                "✅ Đã tính nghĩa vụ trả nợ."
            )

    if st.session_state.tong_nghia_vu is not None:

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc/tháng",
            f"{st.session_state.tien_goc_thang:,.2f}"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{st.session_state.tien_lai_thang:,.2f}"
        )

        c3.metric(
            "Tổng nghĩa vụ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )

    st.divider()

    st.subheader(
        "🏠 Tài sản bảo đảm"
    )

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm.
        Tỷ lệ chấp nhận thực tế phụ thuộc vào loại tài sản,
        giá trị định giá, tính pháp lý, khả năng thanh khoản
        và chính sách tín dụng của ngân hàng.
        """
    )

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ],
        index=[
            "Chưa đánh giá",
            "Có",
            "Không"
        ].index(
            st.session_state.co_tsdb
        )
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
    ):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định tình trạng tài sản bảo đảm."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được xác định là không có tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
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

            st.session_state.da_phan_tich_tsdb = True

            st.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ở mức tương đối thấp theo mô hình hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của tài sản."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm theo dữ liệu nhập."
                )


# =========================================================
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ"
    )

    st.info(
        """
        Kết quả được tổng hợp từ thông tin doanh nghiệp,
        điều kiện vay vốn, tài chính, khả năng trả nợ,
        khoản vay và tài sản bảo đảm.
        """
    )

    # -----------------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # -----------------------------------------------------

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append(
            "Hồ sơ doanh nghiệp"
        )

    if not st.session_state.da_phan_tich_tc:
        missing.append(
            "Phân tích tài chính"
        )

    if not st.session_state.da_phan_tich_vay:
        missing.append(
            "Khoản vay"
        )

    if not st.session_state.da_phan_tich_tsdb:
        missing.append(
            "Tài sản bảo đảm"
        )

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận thẩm định sơ bộ."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:

            st.write(
                f"• {item}"
            )

    else:

        # -------------------------------------------------
        # THÔNG TIN KHÁCH HÀNG
        # -------------------------------------------------

        st.subheader(
            "🏢 THÔNG TIN DOANH NGHIỆP"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Doanh nghiệp",
            st.session_state.ten_dn
        )

        c2.metric(
            "Ngành nghề",
            st.session_state.nganh_nghe
        )

        c3.metric(
            "Thời gian hoạt động",
            f"{st.session_state.thoi_gian_hd} năm"
        )

        st.divider()

        # -------------------------------------------------
        # CHỈ TIÊU TÀI CHÍNH
        # -------------------------------------------------

        st.subheader(
            "📈 CHỈ TIÊU TÀI CHÍNH"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "LNST",
            f"{st.session_state.lnst:,.2f}"
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
            "Tỷ lệ nợ",
            f"{st.session_state.ty_le_no:.2f}%"
        )

        # -------------------------------------------------
        # KHẢ NĂNG TRẢ NỢ
        # -------------------------------------------------

        st.subheader(
            "💳 KHẢ NĂNG TRẢ NỢ & BẢO ĐẢM"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Khoản vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        c2.metric(
            "DSCR",
            (
                f"{st.session_state.dscr:.2f} lần"
                if st.session_state.dscr is not None
                else "Chưa tính"
            )
        )

        c3.metric(
            "LTV",
            (
                f"{st.session_state.ltv:.2f}%"
                if st.session_state.ltv is not None
                else "Không áp dụng"
            )
        )

        st.divider()

        # -------------------------------------------------
        # KIỂM TRA ĐIỀU KIỆN
        # -------------------------------------------------

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_von,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        co_khong = (
            "Không" in dieu_kien
        )

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

        # -------------------------------------------------
        # KẾT LUẬN
        # -------------------------------------------------

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )

        if co_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 KHÔNG ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang có ít nhất một điều kiện vay vốn
                được đánh giá là Không. Cần xem xét nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước
                khi tiếp tục thẩm định.
                """
            )

        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="status-warning">
                    🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Một hoặc nhiều điều kiện vay vốn chưa được đánh giá.
                Chưa nên đưa ra kết luận đạt hoặc không đạt.
                """
            )

        elif (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
            and st.session_state.dscr is not None
            and st.session_state.dscr >= 1
        ):

            st.markdown(
                """
                <div class="status-good">
                    🟢 CÓ CƠ SỞ XEM XÉT CHO VAY SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Các điều kiện vay vốn đang được đánh giá là đạt.
                Doanh nghiệp có kết quả kinh doanh dương,
                ROA và ROE dương, đồng thời dòng tiền hiện tại
                có khả năng đáp ứng nghĩa vụ trả nợ theo dữ liệu nhập.

                Hồ sơ có thể được xem xét chuyển sang bước
                thẩm định tín dụng chi tiết.
                """
            )

        else:

            st.markdown(
                """
                <div class="status-warning">
                    🟡 CẦN THẨM ĐỊNH BỔ SUNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ chưa có đủ cơ sở để kết luận đủ điều kiện
                cho vay sơ bộ theo các chỉ tiêu đang sử dụng.
                Cần xem xét thêm tình hình tài chính, dòng tiền,
                lịch sử tín dụng, phương án kinh doanh,
                khả năng trả nợ và tài sản bảo đảm.
                """
            )

        st.divider()

        # -------------------------------------------------
        # BẢNG TỔNG HỢP
        # -------------------------------------------------

        st.subheader(
            "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
        )

        ket_qua = []

        # Điều kiện
        dieu_kien_data = [
            (
                "Năng lực pháp lý",
                st.session_state.nang_luc_phap_ly
            ),
            (
                "Mục đích vay vốn",
                st.session_state.muc_dich_hop_phap
            ),
            (
                "Phương án sử dụng vốn",
                st.session_state.phuong_an_von
            ),
            (
                "Tính khả thi phương án",
                st.session_state.phuong_an_kha_thi
            ),
            (
                "Khả năng tài chính trả nợ",
                st.session_state.kha_nang_tra_no
            ),
            (
                "Cam kết sử dụng vốn đúng mục đích",
                st.session_state.cam_ket_dung_muc_dich
            ),
            (
                "Cam kết trả nợ đúng hạn",
                st.session_state.cam_ket_tra_no
            )
        ]

        for ten, gia_tri in dieu_kien_data:

            if gia_tri == "Có":

                ket_qua.append(
                    [
                        ten,
                        "Đạt",
                        "Được đánh giá là Có"
                    ]
                )

            elif gia_tri == "Không":

                ket_qua.append(
                    [
                        ten,
                        "Không đạt",
                        "Được đánh giá là Không"
                    ]
                )

            else:

                ket_qua.append(
                    [
                        ten,
                        "Chưa đánh giá",
                        "Chưa đủ thông tin"
                    ]
                )

        # Tài chính
        ket_qua.append(
            [
                "Lợi nhuận sau thuế",
                "Tích cực"
                if st.session_state.lnst > 0
                else "Cần xem xét",
                f"{st.session_state.lnst:,.2f} triệu đồng"
            ]
        )

        ket_qua.append(
            [
                "ROA",
                "Tích cực"
                if st.session_state.roa > 0
                else "Cần xem xét",
                f"{st.session_state.roa:.2f}%"
            ]
        )

        ket_qua.append(
            [
                "ROE",
                "Tích cực"
                if st.session_state.roe > 0
                else "Cần xem xét",
                f"{st.session_state.roe:.2f}%"
            ]
        )

        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Tham khảo",
                f"{st.session_state.ty_le_no:.2f}%"
            ]
        )

        # DSCR
        if st.session_state.dscr is not None:

            ket_qua.append(
                [
                    "DSCR",
                    "Tích cực"
                    if st.session_state.dscr >= 1
                    else "Cần xem xét",
                    f"{st.session_state.dscr:.2f} lần"
                ]
            )

        # TSĐB
        if st.session_state.ltv is not None:

            ket_qua.append(
                [
                    "LTV",
                    "Tham khảo",
                    f"{st.session_state.ltv:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Không áp dụng",
                    "Khoản vay không có TSĐB"
                ]
            )

        df = pd.DataFrame(
            ket_qua,
            columns=[
                "Tiêu chí",
                "Kết quả",
                "Chi tiết"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả trên chỉ là kết quả thẩm định sơ bộ dựa
            trên dữ liệu người dùng nhập.

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu
            hỗ trợ phân tích, không phải điều kiện pháp lý
            duy nhất để quyết định cho vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể
            hồ sơ pháp lý, mục đích vay, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách
            tín dụng của từng tổ chức tín dụng.
            """
        )


# =========================================================
# 10. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>

        <br><br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
