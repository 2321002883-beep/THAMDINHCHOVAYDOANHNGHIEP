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

DEFAULTS = {
    # Hồ sơ
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no_danh_gia": "Chưa đánh giá",
    "cam_ket_dung_muc_dich": "Chưa đánh giá",
    "cam_ket_tra_no": "Chưa đánh giá",

    # Tài chính
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien_thang": 0.0,

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
    "da_kiem_tra_dieu_kien": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN CHUNG
    ================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eaf3fb 50%,
            #f8fbff 100%
        );
    }

    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #06284a 0%,
            #084b78 55%,
            #0877a8 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }

    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #073b68 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #075486 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #0870a8 !important;
        font-weight: 700 !important;
    }

    /* ================================
       HERO
    ================================= */

    .hero-card {
        background: linear-gradient(
            135deg,
            #062d55 0%,
            #075b91 55%,
            #0796c7 100%
        );
        padding: 35px;
        border-radius: 25px;
        color: white;
        box-shadow: 0 15px 35px rgba(5,55,95,0.25);
        margin-bottom: 30px;
    }

    .hero-title {
        color: white;
        font-size: 31px;
        font-weight: 800;
        line-height: 1.3;
        margin-bottom: 12px;
    }

    .hero-text {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        line-height: 1.7;
    }

    /* ================================
       SIDEBAR TITLE
    ================================= */

    .sidebar-logo {
        text-align: center;
        padding: 15px 5px 25px 5px;
    }

    .sidebar-icon {
        font-size: 52px;
        margin-bottom: 10px;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 800;
        line-height: 1.45;
    }

    .sidebar-subtitle {
        font-size: 14px;
        opacity: 0.85;
        margin-top: 8px;
    }

    .menu-title {
        font-size: 15px;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* ================================
       CARD
    ================================= */

    .info-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #d8e6f2;
        box-shadow: 0 8px 25px rgba(15,65,100,0.08);
        margin-bottom: 18px;
    }

    .info-card h3 {
        margin-top: 0;
    }

    /* ================================
       QUY TRÌNH
    ================================= */

    .process-card {
        background: white;
        border-radius: 18px;
        padding: 22px;
        min-height: 180px;
        border: 1px solid #dceaf5;
        box-shadow: 0 7px 20px rgba(15,65,100,0.07);
    }

    .process-number {
        color: #0877a8;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .process-title {
        color: #073b68;
        font-size: 19px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .process-text {
        color: #526b80;
        font-size: 14px;
        line-height: 1.6;
    }

    /* ================================
       STATUS
    ================================= */

    .status-good {
        background: #e9f8ef;
        border-left: 6px solid #1c9b58;
        padding: 18px;
        border-radius: 12px;
        color: #17683b;
        font-weight: 800;
        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 6px solid #e1a500;
        padding: 18px;
        border-radius: 12px;
        color: #795c00;
        font-weight: 800;
        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 6px solid #d64545;
        padding: 18px;
        border-radius: 12px;
        color: #8a2424;
        font-weight: 800;
        font-size: 18px;
    }

    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d8e6f2;
        padding: 18px;
        border-radius: 17px;
        box-shadow: 0 7px 20px rgba(15,65,100,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #58738a !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #073b68 !important;
        font-weight: 800;
    }

    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 750;
        color: white;
        background: linear-gradient(
            135deg,
            #07518b,
            #0796c7
        );
        box-shadow: 0 6px 17px rgba(7,81,139,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 9px 22px rgba(7,81,139,0.3);
    }

    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        color: #70869a;
        padding: 25px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR - MENU 5 MỤC
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">
            <div class="sidebar-icon">🏦</div>

            <div class="sidebar-title">
                THẨM ĐỊNH CHO VAY<br>
                DOANH NGHIỆP
            </div>

            <div class="sidebar-subtitle">
                Hệ thống hỗ trợ thẩm định sơ bộ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="menu-title">📌 DANH MỤC THẨM ĐỊNH</div>',
        unsafe_allow_html=True
    )

    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & khoản vay",
            "💰 Tài chính & khả năng trả nợ",
            "🏠 Tài sản bảo đảm",
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

    st.subheader("👋 Chào mừng bạn đến với hệ thống")

    st.write(
        """
        Hệ thống hỗ trợ cán bộ tín dụng hoặc người sử dụng
        thực hiện thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp.
        """
    )

    st.divider()

    st.subheader("📊 TRẠNG THÁI HỒ SƠ")

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
            "⚖️ Điều kiện vay",
            "Đã kiểm tra"
            if st.session_state.da_kiem_tra_dieu_kien
            else "Chưa kiểm tra"
        )

    with c3:
        st.metric(
            "💰 Tài chính",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )

    with c4:
        st.metric(
            "💳 Khoản vay",
            "Đã tính"
            if st.session_state.da_phan_tich_vay
            else "Chưa tính"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">01 | HỒ SƠ</div>
                <div class="process-title">Thông tin doanh nghiệp</div>
                <div class="process-text">
                    Nhập thông tin doanh nghiệp,
                    mục đích vay và phương án sử dụng vốn.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">02 | TÀI CHÍNH</div>
                <div class="process-title">Đánh giá tài chính</div>
                <div class="process-text">
                    Phân tích doanh thu, LNST,
                    ROA, ROE và tỷ lệ nợ.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">03 | KHOẢN VAY</div>
                <div class="process-title">Khả năng trả nợ</div>
                <div class="process-text">
                    Tính nghĩa vụ trả nợ,
                    dòng tiền và chỉ tiêu DSCR.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">04 | KẾT QUẢ</div>
                <div class="process-title">Tổng hợp thẩm định</div>
                <div class="process-text">
                    Tổng hợp các yếu tố và đưa ra
                    kết luận thẩm định sơ bộ.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ, không thay thế quyết định tín dụng chính thức
        của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & KHOẢN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & khoản vay":

    st.title("🏢 HỒ SƠ & KHOẢN VAY")

    st.subheader("1️⃣ Thông tin doanh nghiệp")

    c1, c2 = st.columns(2)

    with c1:

        ten_dn = st.text_input(
            "Tên doanh nghiệp",
            value=st.session_state.ten_dn
        )

        ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so
        )

        nganh_nghe = st.selectbox(
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
            ],
            index=[
                "Sản xuất",
                "Thương mại",
                "Dịch vụ",
                "Xây dựng",
                "Vận tải",
                "Công nghệ",
                "Nông nghiệp",
                "Khác"
            ].index(st.session_state.nganh_nghe)
        )

    with c2:

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

        muc_dich_vay = st.selectbox(
            "Mục đích vay vốn",
            [
                "Bổ sung vốn lưu động",
                "Mua nguyên vật liệu",
                "Đầu tư máy móc thiết bị",
                "Mở rộng sản xuất",
                "Mua tài sản cố định",
                "Khác"
            ],
            index=[
                "Bổ sung vốn lưu động",
                "Mua nguyên vật liệu",
                "Đầu tư máy móc thiết bị",
                "Mở rộng sản xuất",
                "Mua tài sản cố định",
                "Khác"
            ].index(st.session_state.muc_dich_vay)
        )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập phương án kinh doanh và nhu cầu sử dụng vốn..."
    )

    if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

        if ten_dn.strip() == "":
            st.error("❌ Vui lòng nhập tên doanh nghiệp.")

        elif ma_so.strip() == "":
            st.error("❌ Vui lòng nhập mã số doanh nghiệp.")

        elif phuong_an.strip() == "":
            st.error("❌ Vui lòng nhập phương án sử dụng vốn.")

        else:

            st.session_state.ten_dn = ten_dn
            st.session_state.ma_so = ma_so
            st.session_state.nganh_nghe = nganh_nghe
            st.session_state.thoi_gian_hd = thoi_gian_hd
            st.session_state.muc_dich_vay = muc_dich_vay
            st.session_state.phuong_an = phuong_an
            st.session_state.da_luu_ho_so = True

            st.success("✅ Đã lưu hồ sơ doanh nghiệp.")


    st.divider()

    st.subheader("2️⃣ Thông tin khoản vay")

    c1, c2 = st.columns(2)

    with c1:

        so_tien_vay = st.number_input(
            "💰 Số tiền vay (triệu đồng)",
            min_value=0.0,
            value=st.session_state.so_tien_vay
        )

        thoi_gian_vay = st.number_input(
            "📅 Thời hạn vay (tháng)",
            min_value=1,
            value=st.session_state.thoi_gian_vay
        )

    with c2:

        lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )

        nghia_vu_no_cu = st.number_input(
            "💳 Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu
        )

    if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

        if so_tien_vay <= 0:

            st.error("❌ Số tiền vay phải lớn hơn 0.")

        else:

            st.session_state.so_tien_vay = so_tien_vay
            st.session_state.thoi_gian_vay = thoi_gian_vay
            st.session_state.lai_suat = lai_suat
            st.session_state.nghia_vu_no_cu = nghia_vu_no_cu

            tien_goc = (
                so_tien_vay / thoi_gian_vay
            )

            tien_lai = (
                so_tien_vay
                * lai_suat
                / 100
                / 12
            )

            tong_nghia_vu = (
                nghia_vu_no_cu
                + tien_goc
                + tien_lai
            )

            st.session_state.tien_goc_thang = tien_goc
            st.session_state.tien_lai_thang = tien_lai
            st.session_state.tong_nghia_vu = tong_nghia_vu
            st.session_state.da_phan_tich_vay = True

            st.success("✅ Đã tính nghĩa vụ trả nợ.")


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

    st.subheader("3️⃣ Kiểm tra điều kiện vay vốn sơ bộ")

    st.info(
        """
        Các nội dung dưới đây là các tiêu chí kiểm tra sơ bộ.
        Quyết định cho vay thực tế còn phụ thuộc hồ sơ pháp lý,
        mục đích sử dụng vốn, phương án kinh doanh, khả năng trả nợ
        và quy định nội bộ của tổ chức tín dụng.
        """
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Năng lực pháp lý phù hợp?",
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
            "Mục đích vay vốn hợp pháp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.co_phuong_an
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn khả thi?",
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

        st.session_state.kha_nang_tra_no_danh_gia = st.selectbox(
            "Có khả năng tài chính trả nợ?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.kha_nang_tra_no_danh_gia
            )
        )

        st.session_state.cam_ket_dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
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
            "Cam kết trả nợ đúng hạn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.cam_ket_tra_no
            )
        )

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_danh_gia,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        st.session_state.da_kiem_tra_dieu_kien = True

        if "Không" in dieu_kien:

            st.error(
                "🔴 Có ít nhất một tiêu chí đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn tiêu chí chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các tiêu chí sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & khả năng trả nợ":

    st.title("💰 TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ")

    st.caption(
        "Đơn vị nhập liệu tài chính: triệu đồng"
    )

    st.subheader("1️⃣ Phân tích tài chính")

    c1, c2 = st.columns(2)

    with c1:

        doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )

        lnst = st.number_input(
            "📈 Lợi nhuận sau thuế (LNST)",
            value=st.session_state.lnst
        )

        tong_tai_san = st.number_input(
            "🏢 Tổng tài sản",
            min_value=0.0,
            value=st.session_state.tong_tai_san
        )

    with c2:

        von_chu_so_huu = st.number_input(
            "💼 Vốn chủ sở hữu",
            min_value=0.0,
            value=st.session_state.von_chu_so_huu
        )

        no_phai_tra = st.number_input(
            "📌 Nợ phải trả",
            min_value=0.0,
            value=st.session_state.no_phai_tra
        )

        dong_tien_thang = st.number_input(
            "💧 Dòng tiền kinh doanh bình quân/tháng",
            value=st.session_state.dong_tien_thang
        )

    if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

        if tong_tai_san <= 0:

            st.error(
                "❌ Tổng tài sản phải lớn hơn 0."
            )

        elif von_chu_so_huu <= 0:

            st.error(
                "❌ Vốn chủ sở hữu phải lớn hơn 0."
            )

        else:

            st.session_state.doanh_thu = doanh_thu
            st.session_state.lnst = lnst
            st.session_state.tong_tai_san = tong_tai_san
            st.session_state.von_chu_so_huu = von_chu_so_huu
            st.session_state.no_phai_tra = no_phai_tra
            st.session_state.dong_tien_thang = dong_tien_thang

            st.session_state.roa = (
                lnst / tong_tai_san * 100
            )

            st.session_state.roe = (
                lnst / von_chu_so_huu * 100
            )

            st.session_state.ty_le_no = (
                no_phai_tra / tong_tai_san * 100
            )

            st.session_state.da_phan_tich_tc = True

            st.success(
                "✅ Phân tích tài chính thành công."
            )


    if st.session_state.roa is not None:

        st.divider()

        st.subheader("📈 Kết quả tài chính")

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

    st.subheader("2️⃣ Phân tích khả năng trả nợ")

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng nhập và tính khoản vay tại mục "
            "'🏢 Hồ sơ & khoản vay' trước."
        )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien_thang:,.2f}"
            )

        with c2:

            st.metric(
                "Tổng nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

        if st.button("📈 TÍNH DSCR"):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien_thang
                    / st.session_state.tong_nghia_vu
                )

                st.session_state.da_phan_tich_dscr = True

                st.divider()

                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )

                if st.session_state.dscr >= 1:

                    st.success(
                        "🟢 Dòng tiền kinh doanh hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền kinh doanh hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


# =========================================================
# 8. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title("🏠 TÀI SẢN BẢO ĐẢM")

    st.info(
        """
        Phân tích tài sản bảo đảm nhằm hỗ trợ đánh giá mức độ
        bảo đảm của khoản vay. Việc chấp nhận tài sản thực tế còn
        phụ thuộc hồ sơ pháp lý, định giá, khả năng thanh khoản,
        loại tài sản và chính sách của tổ chức tín dụng.
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

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        st.session_state.gia_tri_tsdb = gia_tri_tsdb

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được xác định là không có tài sản bảo đảm."
            )

        elif gia_tri_tsdb <= 0:

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
                / gia_tri_tsdb
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
                    "🟡 Cần xem xét thêm chất lượng, tính pháp lý "
                    "và khả năng thanh khoản của tài sản."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm "
                    "theo dữ liệu nhập."
                )


# =========================================================
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả được tổng hợp từ thông tin người dùng nhập.
        Đây là công cụ hỗ trợ thẩm định sơ bộ và không thay thế
        quy trình phê duyệt tín dụng chính thức.
        """
    )

    # ---------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # ---------------------------------------------

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append("Hồ sơ doanh nghiệp")

    if not st.session_state.da_kiem_tra_dieu_kien:
        missing.append("Điều kiện vay vốn")

    if not st.session_state.da_phan_tich_tc:
        missing.append("Phân tích tài chính")

    if not st.session_state.da_phan_tich_vay:
        missing.append("Thông tin khoản vay")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Tài sản bảo đảm")

    if missing:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để tổng hợp kết quả."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:
            st.write(
                f"• {item}"
            )

    else:

        # ---------------------------------------------
        # THÔNG TIN DOANH NGHIỆP
        # ---------------------------------------------

        st.subheader("🏢 THÔNG TIN DOANH NGHIỆP")

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

        # ---------------------------------------------
        # CHỈ TIÊU TÀI CHÍNH
        # ---------------------------------------------

        st.subheader("💰 CHỈ TIÊU TÀI CHÍNH")

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

        st.divider()

        # ---------------------------------------------
        # KHOẢN VAY
        # ---------------------------------------------

        st.subheader("💳 THÔNG TIN KHOẢN VAY")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Số tiền vay",
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

        # ---------------------------------------------
        # KIỂM TRA ĐIỀU KIỆN
        # ---------------------------------------------

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_danh_gia,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        co_khong = "Không" in dieu_kien

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

        # ---------------------------------------------
        # KẾT LUẬN
        # ---------------------------------------------

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )

        if co_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang có ít nhất một tiêu chí điều kiện vay
                được đánh giá là "Không". Cần rà soát nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước khi
                xem xét tiếp.
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
                Chưa nên đưa ra kết luận về khả năng cấp tín dụng
                cho đến khi hoàn thiện thông tin.
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
                    🟢 HỒ SƠ CÓ TÍN HIỆU TÍCH CỰC -
                    ĐỀ XUẤT XEM XÉT THẨM ĐỊNH TIẾP
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Các điều kiện sơ bộ đang được đánh giá là đạt.
                Doanh nghiệp có lợi nhuận dương, các chỉ tiêu ROA,
                ROE dương và dòng tiền hiện tại có khả năng đáp ứng
                nghĩa vụ trả nợ theo dữ liệu nhập.

                Hồ sơ có thể được xem xét chuyển sang bước thẩm định
                tín dụng chi tiết. Tuy nhiên, kết quả này không đồng
                nghĩa với việc doanh nghiệp chắc chắn được phê duyệt
                khoản vay.
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
                Hồ sơ chưa có đủ các tín hiệu tích cực để đưa ra
                kết luận sơ bộ thuận lợi. Cần xem xét thêm tình hình
                tài chính, dòng tiền, khả năng trả nợ, phương án kinh
                doanh, lịch sử tín dụng và các yếu tố liên quan.
                """
            )

        st.divider()

        # ---------------------------------------------
        # BẢNG TỔNG HỢP
        # ---------------------------------------------

        st.subheader(
            "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
        )

        ket_qua = []

        def them_danh_gia(ten, gia_tri):

            if gia_tri == "Có":

                ket_qua.append(
                    [
                        ten,
                        "Đạt",
                        "Đang được đánh giá là Có"
                    ]
                )

            elif gia_tri == "Không":

                ket_qua.append(
                    [
                        ten,
                        "Không đạt",
                        "Đang được đánh giá là Không"
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


        them_danh_gia(
            "Năng lực pháp lý",
            st.session_state.nang_luc_phap_ly
        )

        them_danh_gia(
            "Mục đích vay vốn",
            st.session_state.muc_dich_hop_phap
        )

        them_danh_gia(
            "Phương án sử dụng vốn",
            st.session_state.co_phuong_an
        )

        them_danh_gia(
            "Tính khả thi phương án",
            st.session_state.phuong_an_kha_thi
        )

        them_danh_gia(
            "Khả năng tài chính trả nợ",
            st.session_state.kha_nang_tra_no_danh_gia
        )

        them_danh_gia(
            "Cam kết sử dụng vốn đúng mục đích",
            st.session_state.cam_ket_dung_muc_dich
        )

        them_danh_gia(
            "Cam kết trả nợ đúng hạn",
            st.session_state.cam_ket_tra_no
        )


        # LNST

        if st.session_state.lnst > 0:

            ket_qua.append(
                [
                    "Lợi nhuận sau thuế",
                    "Tích cực",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Lợi nhuận sau thuế",
                    "Cần xem xét",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )


        # ROA

        if st.session_state.roa > 0:

            ket_qua.append(
                [
                    "ROA",
                    "Tích cực",
                    f"{st.session_state.roa:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "ROA",
                    "Cần xem xét",
                    f"{st.session_state.roa:.2f}%"
                ]
            )


        # ROE

        if st.session_state.roe > 0:

            ket_qua.append(
                [
                    "ROE",
                    "Tích cực",
                    f"{st.session_state.roe:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "ROE",
                    "Cần xem xét",
                    f"{st.session_state.roe:.2f}%"
                ]
            )


        # DSCR

        if st.session_state.dscr is not None:

            if st.session_state.dscr >= 1:

                ket_qua.append(
                    [
                        "DSCR",
                        "Tích cực",
                        f"{st.session_state.dscr:.2f} lần"
                    ]
                )

            else:

                ket_qua.append(
                    [
                        "DSCR",
                        "Cần xem xét",
                        f"{st.session_state.dscr:.2f} lần"
                    ]
                )

        else:

            ket_qua.append(
                [
                    "DSCR",
                    "Chưa tính",
                    "Chưa có dữ liệu"
                ]
            )


        # LTV

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

        st.divider()

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu
            hỗ trợ phân tích tín dụng, không phải là căn cứ duy nhất
            để quyết định cho vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể hồ sơ
            pháp lý, mục đích vay, phương án sử dụng vốn, năng lực
            tài chính, dòng tiền, lịch sử tín dụng, khả năng trả nợ,
            tài sản bảo đảm và chính sách tín dụng của tổ chức tín dụng.
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
        <br>
        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng
        <br><br>
        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.
    </div>
    """,
    unsafe_allow_html=True
)
