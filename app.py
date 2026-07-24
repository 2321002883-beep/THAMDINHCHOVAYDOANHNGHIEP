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

default_values = {
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
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no_dk": "Chưa đánh giá",
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

    # Tài sản bảo đảm
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       NỀN CHUNG
    ========================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eaf3fb 50%,
            #f8fbff 100%
        );
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #062448 0%,
            #0b3b66 55%,
            #0d5687 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }

    /* =========================
       TIÊU ĐỀ
    ========================= */

    h1 {
        color: #073b67 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b4d7a !important;
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
            #062b52 0%,
            #08669b 50%,
            #1498c7 100%
        );

        padding: 35px;
        border-radius: 25px;

        color: white;

        box-shadow:
            0 15px 35px
            rgba(4, 45, 82, 0.25);

        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 32px;
        font-weight: 800;
        line-height: 1.3;
        color: white;
        margin-bottom: 12px;
    }

    .hero-text {
        font-size: 17px;
        line-height: 1.7;
        color: rgba(255,255,255,0.92);
    }

    /* =========================
       SIDEBAR TITLE
    ========================= */

    .sidebar-logo {
        text-align: center;
        padding: 15px 5px 20px 5px;
    }

    .sidebar-icon {
        font-size: 50px;
        margin-bottom: 10px;
    }

    .sidebar-title {
        font-size: 20px;
        font-weight: 800;
        line-height: 1.5;
    }

    .sidebar-subtitle {
        font-size: 14px;
        opacity: 0.85;
        margin-top: 8px;
    }

    /* =========================
       SECTION CARD
    ========================= */

    .section-card {
        background: rgba(255,255,255,0.95);

        padding: 22px;

        border-radius: 18px;

        border: 1px solid #d7e5f1;

        box-shadow:
            0 7px 22px
            rgba(10, 67, 105, 0.08);

        margin-bottom: 20px;
    }

    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {
        background: white;

        border: 1px solid #d7e5f1;

        padding: 18px;

        border-radius: 17px;

        box-shadow:
            0 7px 20px
            rgba(10, 67, 105, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #54718b !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #073b67 !important;
        font-weight: 800;
    }

    /* =========================
       BUTTON
    ========================= */

    .stButton > button {
        width: 100%;

        border: none;

        border-radius: 12px;

        padding: 0.7rem 1rem;

        font-weight: 700;

        color: white;

        background: linear-gradient(
            135deg,
            #07528c,
            #1095c9
        );

        box-shadow:
            0 6px 15px
            rgba(7,82,140,0.25);

        transition: 0.25s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 9px 22px
            rgba(7,82,140,0.35);
    }

    /* =========================
       STATUS
    ========================= */

    .status-good {
        background: #e8f8ef;

        border-left: 6px solid #1e9e58;

        padding: 18px;

        border-radius: 12px;

        color: #176b3c;

        font-size: 18px;

        font-weight: 800;
    }

    .status-warning {
        background: #fff7df;

        border-left: 6px solid #e4a400;

        padding: 18px;

        border-radius: 12px;

        color: #805f00;

        font-size: 18px;

        font-weight: 800;
    }

    .status-bad {
        background: #fff0f0;

        border-left: 6px solid #d64545;

        padding: 18px;

        border-radius: 12px;

        color: #8c2525;

        font-size: 18px;

        font-weight: 800;
    }

    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;

        color: #70849a;

        padding: 25px;

        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR - MENU CHÍNH
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">

            <div class="sidebar-icon">
                🏦
            </div>

            <div class="sidebar-title">
                THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div class="sidebar-subtitle">
                HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
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
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Tài chính & khả năng trả nợ",
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
        từ bước tiếp nhận thông tin đến tổng hợp kết quả.
        """
    )

    st.divider()

    st.subheader(
        "📊 TIẾN ĐỘ THẨM ĐỊNH"
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
            "⚖️ Điều kiện",
            "Đã kiểm tra"
            if all(
                x != "Chưa đánh giá"
                for x in [
                    st.session_state.nang_luc_phap_ly,
                    st.session_state.muc_dich_hop_phap,
                    st.session_state.phuong_an_kha_thi
                ]
            )
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
            "📊 Kết quả",
            "Có thể xem"
            if (
                st.session_state.da_luu_ho_so
                and st.session_state.da_phan_tich_tc
                and st.session_state.da_phan_tich_vay
            )
            else "Chưa đủ dữ liệu"
        )

    st.divider()

    st.subheader(
        "🚀 QUY TRÌNH THẨM ĐỊNH"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(
            """
            **01 | HỒ SƠ**

            Nhập thông tin doanh nghiệp,
            mục đích và phương án vay.
            """
        )

    with c2:
        st.info(
            """
            **02 | ĐIỀU KIỆN**

            Kiểm tra điều kiện vay vốn
            và tài sản bảo đảm.
            """
        )

    with c3:
        st.info(
            """
            **03 | TÀI CHÍNH**

            Phân tích LNST, ROA, ROE,
            tỷ lệ nợ và khả năng trả nợ.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu và đưa ra
            kết luận thẩm định sơ bộ.
            """
        )

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của ứng dụng chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ, không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN
# =========================================================

elif menu == "🏢 Hồ sơ & điều kiện":

    st.title(
        "🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN"
    )

    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader(
        "1️⃣ Thông tin doanh nghiệp"
    )

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
            ].index(
                st.session_state.nganh_nghe
            )
        )

    with c2:

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
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
        value=st.session_state.phuong_an,
        placeholder="Nhập mô tả phương án kinh doanh và nhu cầu sử dụng vốn..."
    )

    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
    ):

        if ten_dn.strip() == "":
            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        elif ma_so.strip() == "":
            st.error(
                "❌ Vui lòng nhập mã số doanh nghiệp."
            )

        elif phuong_an.strip() == "":
            st.error(
                "❌ Vui lòng nhập phương án sử dụng vốn."
            )

        else:

            st.session_state.ten_dn = ten_dn
            st.session_state.ma_so = ma_so
            st.session_state.nganh_nghe = nganh_nghe
            st.session_state.thoi_gian_hd = thoi_gian_hd
            st.session_state.muc_dich_vay = muc_dich_vay
            st.session_state.phuong_an = phuong_an

            st.session_state.da_luu_ho_so = True

            st.success(
                "✅ Đã lưu hồ sơ doanh nghiệp."
            )

    st.divider()

    # =====================================================
    # ĐIỀU KIỆN VAY
    # =====================================================

    st.subheader(
        "2️⃣ Kiểm tra điều kiện vay vốn"
    )

    st.info(
        """
        Kiểm tra sơ bộ các điều kiện của khách hàng vay.
        Việc đánh giá thực tế cần căn cứ hồ sơ pháp lý,
        mục đích vay, phương án sử dụng vốn và quy định
        nội bộ của tổ chức tín dụng.
        """
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Năng lực pháp lý phù hợp?",
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
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "Mục đích vay vốn hợp pháp?",
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
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn khả thi?",
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
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no_dk = st.selectbox(
            "Có khả năng tài chính để trả nợ?",
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
                st.session_state.kha_nang_tra_no_dk
            )
        )

        st.session_state.cam_ket_dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
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
                st.session_state.cam_ket_dung_muc_dich
            )
        )

        st.session_state.cam_ket_tra_no = st.selectbox(
            "Cam kết trả nợ đúng hạn?",
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
                st.session_state.cam_ket_tra_no
            )
        )

    # =====================================================
    # TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.divider()

    st.subheader(
        "3️⃣ Tài sản bảo đảm"
    )

    c1, c2 = st.columns(2)

    with c1:

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

    with c2:

        st.session_state.gia_tri_tsdb = st.number_input(
            "Giá trị tài sản bảo đảm (triệu đồng)",
            min_value=0.0,
            value=st.session_state.gia_tri_tsdb
        )

    if st.button(
        "🔍 KIỂM TRA ĐIỀU KIỆN & TSĐB"
    ):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_dk,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        if "Không" in dieu_kien:

            st.error(
                "🔴 Có ít nhất một điều kiện vay vốn đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện vay vốn hiện đang được đánh giá là Có."
            )

        # Tính LTV
        if (
            st.session_state.co_tsdb == "Có"
            and st.session_state.gia_tri_tsdb > 0
            and st.session_state.so_tien_vay > 0
        ):

            st.session_state.ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            st.session_state.da_phan_tich_tsdb = True

            st.info(
                f"📊 LTV hiện tại: {st.session_state.ltv:.2f}%"
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được xác định là không có tài sản bảo đảm."
            )

        else:

            st.warning(
                "⚠️ Chưa thể tính LTV. Vui lòng nhập số tiền vay và giá trị TSĐB."
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & khả năng trả nợ":

    st.title(
        "💰 TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )

    # =====================================================
    # PHÂN TÍCH TÀI CHÍNH
    # =====================================================

    st.subheader(
        "1️⃣ Phân tích tài chính"
    )

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )

        st.session_state.lnst = st.number_input(
            "📈 Lợi nhuận sau thuế (LNST)",
            value=st.session_state.lnst
        )

        st.session_state.tong_tai_san = st.number_input(
            "🏢 Tổng tài sản",
            min_value=0.0,
            value=st.session_state.tong_tai_san
        )

    with c2:

        st.session_state.von_chu_so_huu = st.number_input(
            "💼 Vốn chủ sở hữu",
            min_value=0.0,
            value=st.session_state.von_chu_so_huu
        )

        st.session_state.no_phai_tra = st.number_input(
            "📌 Nợ phải trả",
            min_value=0.0,
            value=st.session_state.no_phai_tra
        )

        st.session_state.dong_tien = st.number_input(
            "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
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

    # =====================================================
    # KHOẢN VAY
    # =====================================================

    st.subheader(
        "2️⃣ Thông tin khoản vay"
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
            "💳 Nghĩa vụ trả nợ hiện tại/tháng",
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

            tong_nghia_vu = (
                st.session_state.nghia_vu_no_cu
                + tien_goc
                + tien_lai
            )

            st.session_state.tien_goc_thang = tien_goc

            st.session_state.tien_lai_thang = tien_lai

            st.session_state.tong_nghia_vu = tong_nghia_vu

            st.session_state.da_phan_tich_vay = True

            st.success(
                "✅ Đã tính nghĩa vụ trả nợ."
            )

    if st.session_state.tong_nghia_vu is not None:

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

    # =====================================================
    # DSCR
    # =====================================================

    st.subheader(
        "3️⃣ Khả năng trả nợ"
    )

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

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

                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )

                if st.session_state.dscr >= 1:

                    st.success(
                        "🟢 Dòng tiền hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ"
    )

    st.info(
        """
        Kết quả được tổng hợp từ thông tin doanh nghiệp,
        điều kiện vay vốn, tình hình tài chính, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

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
            "Thông tin khoản vay"
        )

    if not st.session_state.da_phan_tich_tsdb:
        missing.append(
            "Tài sản bảo đảm"
        )

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:

            st.write(
                f"• {item}"
            )

    else:

        # =================================================
        # KIỂM TRA ĐIỀU KIỆN
        # =================================================

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich_hop_phap,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no_dk,

            st.session_state.cam_ket_dung_muc_dich,

            st.session_state.cam_ket_tra_no

        ]

        co_khong = (
            "Không"
            in dieu_kien
        )

        co_chua_danh_gia = (
            "Chưa đánh giá"
            in dieu_kien
        )

        # =================================================
        # THÔNG TIN DOANH NGHIỆP
        # =================================================

        st.subheader(
            "🏢 THÔNG TIN DOANH NGHIỆP"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Doanh nghiệp",
            st.session_state.ten_dn
        )

        c2.metric(
            "Mã số",
            st.session_state.ma_so
        )

        c3.metric(
            "Ngành nghề",
            st.session_state.nganh_nghe
        )

        # =================================================
        # CHỈ TIÊU TÀI CHÍNH
        # =================================================

        st.divider()

        st.subheader(
            "💰 CHỈ TIÊU TÀI CHÍNH"
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

        # =================================================
        # KHẢ NĂNG TRẢ NỢ
        # =================================================

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

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.divider()

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )

        # Điều kiện không đạt
        if co_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 CHƯA ĐỦ ĐIỀU KIỆN SƠ BỘ
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

        # Chưa đánh giá
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
                Một hoặc nhiều điều kiện vay vốn chưa được
                đánh giá. Cần hoàn thiện thông tin trước khi
                đưa ra kết luận thẩm định.
                """
            )

        # Đủ điều kiện sơ bộ
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
                    🟢 HỒ SƠ CÓ CƠ SỞ ĐỂ XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Các điều kiện vay vốn sơ bộ đang được đánh giá
                là đạt. Kết quả phân tích tài chính và khả năng
                trả nợ có tín hiệu tích cực theo dữ liệu đã nhập.

                Hồ sơ có thể được chuyển sang bước thẩm định
                tín dụng chi tiết theo quy trình của tổ chức
                tín dụng.
                """
            )

        # Cần thẩm định thêm
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
                Hồ sơ chưa có đủ cơ sở để kết luận tích cực
                dựa trên các chỉ tiêu hỗ trợ hiện tại.

                Cần xem xét thêm tình hình tài chính, dòng tiền,
                khả năng trả nợ, phương án kinh doanh, lịch sử
                tín dụng, tài sản bảo đảm và các yếu tố liên quan.
                """
            )

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.divider()

        st.subheader(
            "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
        )

        ket_qua = []

        # Điều kiện
        dieu_kien_dict = {

            "Năng lực pháp lý":
                st.session_state.nang_luc_phap_ly,

            "Mục đích vay hợp pháp":
                st.session_state.muc_dich_hop_phap,

            "Phương án khả thi":
                st.session_state.phuong_an_kha_thi,

            "Khả năng tài chính trả nợ":
                st.session_state.kha_nang_tra_no_dk,

            "Cam kết sử dụng vốn":
                st.session_state.cam_ket_dung_muc_dich,

            "Cam kết trả nợ":
                st.session_state.cam_ket_tra_no
        }

        for ten, gia_tri in dieu_kien_dict.items():

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
                        "Cần bổ sung thông tin"
                    ]
                )

        # LNST
        ket_qua.append(
            [
                "Lợi nhuận sau thuế",
                "Tích cực"
                if st.session_state.lnst > 0
                else "Cần xem xét",
                f"{st.session_state.lnst:,.2f} triệu đồng"
            ]
        )

        # ROA
        ket_qua.append(
            [
                "ROA",
                "Tích cực"
                if st.session_state.roa > 0
                else "Cần xem xét",
                f"{st.session_state.roa:.2f}%"
            ]
        )

        # ROE
        ket_qua.append(
            [
                "ROE",
                "Tích cực"
                if st.session_state.roe > 0
                else "Cần xem xét",
                f"{st.session_state.roe:.2f}%"
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

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả trên chỉ là kết quả thẩm định sơ bộ dựa trên
            dữ liệu được nhập vào hệ thống.

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu hỗ trợ
            phân tích tín dụng, không phải là căn cứ duy nhất để
            quyết định cho vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể:
            hồ sơ pháp lý, mục đích sử dụng vốn, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách tín dụng
            của từng tổ chức tín dụng.
            """
        )


# =========================================================
# 9. FOOTER
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
