import streamlit as st
import pandas as pd

# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. KHỞI TẠO SESSION STATE
# =========================================================

DEFAULTS = {
    # Hồ sơ doanh nghiệp
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

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False,
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN CHUNG
    ================================= */

    .stApp {
        background-color: #f4f7fb;
    }

    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background-color: #082b4c;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    section[data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600 !important;
    }

    section[data-testid="stSidebar"] p {
        color: white !important;
    }

    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #073b6b !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b4f8a !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #146da8 !important;
        font-weight: 700 !important;
    }

    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        background-color: #0879c9;
        color: white;
        font-weight: 700;
        min-height: 45px;
    }

    .stButton > button:hover {
        background-color: #075fa0;
        color: white;
    }

    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 16px;
        padding: 18px;
        border: 1px solid #dce6f0;
        box-shadow: 0 4px 14px rgba(0, 50, 100, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #607d98 !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #073b6b !important;
        font-weight: 800 !important;
    }

    /* ================================
       CARD TRANG CHỦ
    ================================= */

    .main-card {
        background-color: white;
        border-radius: 20px;
        padding: 28px;
        border: 1px solid #dce6f0;
        box-shadow: 0 5px 18px rgba(0, 50, 100, 0.08);
        margin-bottom: 20px;
    }

    .welcome-title {
        font-size: 30px;
        font-weight: 800;
        color: #073b6b;
        margin-bottom: 8px;
    }

    .welcome-text {
        color: #5c7185;
        font-size: 16px;
    }

    /* ================================
       MENU CARD
    ================================= */

    .menu-card {
        background-color: white;
        border-radius: 18px;
        padding: 22px;
        min-height: 160px;
        border: 1px solid #dce6f0;
        box-shadow: 0 5px 15px rgba(0, 50, 100, 0.07);
    }

    .menu-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }

    .menu-title {
        color: #075b99;
        font-size: 19px;
        font-weight: 800;
    }

    .menu-text {
        color: #63798d;
        font-size: 14px;
        margin-top: 8px;
    }

    /* ================================
       KẾT LUẬN
    ================================= */

    .result-good {
        background-color: #e8f7ee;
        border-left: 7px solid #1b9b5a;
        border-radius: 14px;
        padding: 22px;
        color: #176b42;
        font-size: 18px;
        font-weight: 800;
    }

    .result-warning {
        background-color: #fff7df;
        border-left: 7px solid #e4a400;
        border-radius: 14px;
        padding: 22px;
        color: #805f00;
        font-size: 18px;
        font-weight: 800;
    }

    .result-bad {
        background-color: #fff0f0;
        border-left: 7px solid #d64545;
        border-radius: 14px;
        padding: 22px;
        color: #8c2525;
        font-size: 18px;
        font-weight: 800;
    }

    /* ================================
       SIDEBAR TITLE
    ================================= */

    .sidebar-title {
        color: white;
        font-size: 20px;
        font-weight: 800;
        text-align: center;
        padding: 10px;
    }

    .sidebar-subtitle {
        color: #b9d7ee;
        font-size: 13px;
        text-align: center;
        padding-bottom: 15px;
    }

    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        color: #71869a;
        font-size: 13px;
        padding: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR - 5 DANH MỤC ĐƠN GIẢN
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">
            🏦 THẨM ĐỊNH TÍN DỤNG
        </div>

        <div class="sidebar-subtitle">
            HỆ THỐNG HỖ TRỢ CHO VAY DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "📌 MENU CHÍNH",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero">

        <h1>
        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP
        </h1>

        <p>
        Phân tích hồ sơ • Đánh giá tài chính • Khả năng trả nợ
        • Tài sản bảo đảm • Hỗ trợ quyết định tín dụng
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📊 TRẠNG THÁI HỒ SƠ")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 Hồ sơ",
            "Đã nhập" if st.session_state.da_luu_ho_so else "Chưa nhập"
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
            "🏠 Bảo đảm",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tsdb
            else "Chưa phân tích"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="menu-card">
                <div class="menu-icon">🏢</div>
                <div class="menu-title">01 | HỒ SƠ</div>
                <div class="menu-text">
                    Nhập thông tin doanh nghiệp
                    và kiểm tra điều kiện vay.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="menu-card">
                <div class="menu-icon">💰</div>
                <div class="menu-title">02 | TÀI CHÍNH</div>
                <div class="menu-text">
                    Phân tích LNST, ROA, ROE
                    và tỷ lệ nợ.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="menu-card">
                <div class="menu-icon">💳</div>
                <div class="menu-title">03 | KHOẢN VAY</div>
                <div class="menu-text">
                    Tính nghĩa vụ trả nợ,
                    DSCR và LTV.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="menu-card">
                <div class="menu-icon">📊</div>
                <div class="menu-title">04 | KẾT QUẢ</div>
                <div class="menu-text">
                    Tổng hợp dữ liệu và
                    đưa ra kết luận sơ bộ.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.warning(
        "⚠️ Lưu ý: Ứng dụng chỉ hỗ trợ thẩm định sơ bộ. "
        "Kết quả không thay thế quyết định tín dụng chính thức "
        "của tổ chức tín dụng."
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN
# =========================================================

elif menu == "🏢 Hồ sơ & điều kiện":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")

    tab1, tab2 = st.tabs(
        [
            "📋 Thông tin doanh nghiệp",
            "⚖️ Điều kiện vay vốn"
        ]
    )

    # =====================================================
    # TAB 1 - HỒ SƠ
    # =====================================================

    with tab1:

        st.subheader("📋 Thông tin doanh nghiệp")

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
                "Mục đích sử dụng vốn",
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
            placeholder="Nhập phương án kinh doanh và cách sử dụng vốn vay..."
        )

        if st.button("💾 LƯU HỒ SƠ"):

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

    # =====================================================
    # TAB 2 - ĐIỀU KIỆN VAY
    # =====================================================

    with tab2:

        st.subheader("⚖️ Kiểm tra điều kiện vay vốn")

        st.info(
            "Các nội dung dưới đây dùng để kiểm tra sơ bộ. "
            "Kết luận thực tế phải căn cứ hồ sơ và quy định nội bộ "
            "của tổ chức tín dụng."
        )

        lua_chon = [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.nang_luc_phap_ly = st.selectbox(
                "1. Có năng lực pháp luật dân sự phù hợp?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.nang_luc_phap_ly
                )
            )

            st.session_state.muc_dich_hop_phap = st.selectbox(
                "2. Mục đích vay vốn hợp pháp?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.muc_dich_hop_phap
                )
            )

            st.session_state.co_phuong_an = st.selectbox(
                "3. Có phương án sử dụng vốn?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.co_phuong_an
                )
            )

            st.session_state.phuong_an_kha_thi = st.selectbox(
                "4. Phương án sử dụng vốn khả thi?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.phuong_an_kha_thi
                )
            )

        with c2:

            st.session_state.kha_nang_tra_no_dk = st.selectbox(
                "5. Có khả năng tài chính để trả nợ?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.kha_nang_tra_no_dk
                )
            )

            st.session_state.cam_ket_dung_muc_dich = st.selectbox(
                "6. Cam kết sử dụng vốn đúng mục đích?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.cam_ket_dung_muc_dich
                )
            )

            st.session_state.cam_ket_tra_no = st.selectbox(
                "7. Cam kết trả nợ đúng hạn?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.cam_ket_tra_no
                )
            )

        if st.button("🔍 KIỂM TRA ĐIỀU KIỆN"):

            dieu_kien = [
                st.session_state.nang_luc_phap_ly,
                st.session_state.muc_dich_hop_phap,
                st.session_state.co_phuong_an,
                st.session_state.phuong_an_kha_thi,
                st.session_state.kha_nang_tra_no_dk,
                st.session_state.cam_ket_dung_muc_dich,
                st.session_state.cam_ket_tra_no
            ]

            if "Không" in dieu_kien:

                st.error(
                    "🔴 Có ít nhất một điều kiện đang được đánh giá là Không."
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
# 7. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH")

    st.caption("Đơn vị nhập liệu: triệu đồng")

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

    if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

        if st.session_state.tong_tai_san <= 0:

            st.error(
                "❌ Tổng tài sản phải lớn hơn 0."
            )

        elif st.session_state.von_chu_so_huu <= 0:

            st.error(
                "❌ Vốn chủ sở hữu phải lớn hơn 0."
            )

        elif st.session_state.no_phai_tra > st.session_state.tong_tai_san:

            st.error(
                "❌ Nợ phải trả không nên lớn hơn tổng tài sản."
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
                "Giá trị (%)": [
                    st.session_state.roa,
                    st.session_state.roe,
                    st.session_state.ty_le_no
                ]
            }
        )

        st.bar_chart(
            chart.set_index("Chỉ tiêu")
        )

        st.info(
            "💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu hỗ trợ "
            "phân tích tài chính. Không có một ngưỡng pháp lý "
            "chung áp dụng cho mọi doanh nghiệp."
        )


# =========================================================
# 8. KHOẢN VAY & BẢO ĐẢM
# =========================================================

elif menu == "💳 Khoản vay & bảo đảm":

    st.title("💳 KHOẢN VAY & TÀI SẢN BẢO ĐẢM")

    tab1, tab2, tab3 = st.tabs(
        [
            "💳 Khoản vay",
            "📈 Khả năng trả nợ",
            "🏠 Tài sản bảo đảm"
        ]
    )

    # =====================================================
    # TAB 1 - KHOẢN VAY
    # =====================================================

    with tab1:

        st.subheader("💳 Thông tin khoản vay")

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.so_tien_vay = st.number_input(
                "💰 Số tiền vay (triệu đồng)",
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

        if st.button("🧮 TÍNH NGHĨA VỤ TRẢ NỢ"):

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
                    "✅ Đã tính nghĩa vụ trả nợ dự kiến."
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

    # =====================================================
    # TAB 2 - DSCR
    # =====================================================

    with tab2:

        st.subheader("📈 Khả năng trả nợ")

        if st.session_state.tong_nghia_vu is None:

            st.warning(
                "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
            )

        else:

            c1, c2 = st.columns(2)

            c1.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )

            c2.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

            if st.button("📈 TÍNH DSCR"):

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
                            "🟢 Dòng tiền hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."
                        )

                    else:

                        st.warning(
                            "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                        )

    # =====================================================
    # TAB 3 - TSĐB
    # =====================================================

    with tab3:

        st.subheader("🏠 Tài sản bảo đảm")

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

        if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

            if st.session_state.co_tsdb == "Chưa đánh giá":

                st.warning(
                    "⚠️ Vui lòng xác định có hoặc không có TSĐB."
                )

            elif st.session_state.co_tsdb == "Không":

                st.session_state.ltv = None
                st.session_state.da_phan_tich_tsdb = True

                st.info(
                    "Khoản vay được xác định là không có TSĐB."
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

                st.session_state.da_phan_tich_tsdb = True

                st.metric(
                    "LTV",
                    f"{st.session_state.ltv:.2f}%"
                )

                if st.session_state.ltv <= 70:

                    st.success(
                        "🟢 LTV ở mức tương đối thấp theo mô hình tham khảo."
                    )

                elif st.session_state.ltv <= 100:

                    st.warning(
                        "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản TSĐB."
                    )

                else:

                    st.error(
                        "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                    )


# =========================================================
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        "Kết quả được tổng hợp từ dữ liệu đã nhập. "
        "Đây là kết quả hỗ trợ phân tích, không phải quyết định "
        "cho vay chính thức."
    )

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append("Hồ sơ doanh nghiệp")

    if not st.session_state.da_phan_tich_tc:
        missing.append("Phân tích tài chính")

    if not st.session_state.da_phan_tich_vay:
        missing.append("Thông tin khoản vay")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Tài sản bảo đảm")

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để tổng hợp kết quả."
        )

        st.write("Các nội dung còn thiếu:")

        for item in missing:
            st.write("• " + item)

    else:

        # =================================================
        # THÔNG TIN DOANH NGHIỆP
        # =================================================

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

        # =================================================
        # CHỈ TIÊU
        # =================================================

        st.subheader("📊 CÁC CHỈ TIÊU CHÍNH")

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

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "DSCR",
            (
                f"{st.session_state.dscr:.2f} lần"
                if st.session_state.dscr is not None
                else "Chưa tính"
            )
        )

        c2.metric(
            "LTV",
            (
                f"{st.session_state.ltv:.2f}%"
                if st.session_state.ltv is not None
                else "Không áp dụng"
            )
        )

        c3.metric(
            "Số tiền vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        st.divider()

        # =================================================
        # KIỂM TRA ĐIỀU KIỆN
        # =================================================

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_dk,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        co_khong = "Không" in dieu_kien
        co_chua_danh_gia = "Chưa đánh giá" in dieu_kien

        tai_chinh_tich_cuc = (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
        )

        kha_nang_tra_no_tich_cuc = (
            st.session_state.dscr is not None
            and st.session_state.dscr >= 1
        )

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

        if co_khong:

            st.markdown(
                """
                <div class="result-bad">
                    🔴 KHÔNG ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.error(
                "Có ít nhất một điều kiện vay vốn đang được đánh giá là Không. "
                "Hồ sơ cần được xem xét hoặc bổ sung trước khi tiếp tục."
            )

        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="result-warning">
                    🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "Vẫn còn điều kiện vay vốn chưa được đánh giá. "
                "Chưa nên đưa ra kết luận về việc đủ điều kiện cho vay."
            )

        elif not tai_chinh_tich_cuc:

            st.markdown(
                """
                <div class="result-warning">
                    🟡 CẦN THẨM ĐỊNH TÀI CHÍNH BỔ SUNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "Các chỉ tiêu tài chính hiện tại chưa cho thấy tín hiệu tích cực "
                "đồng thời về LNST, ROA và ROE. Cần phân tích sâu hơn "
                "tình hình tài chính và nguyên nhân biến động."
            )

        elif not kha_nang_tra_no_tich_cuc:

            st.markdown(
                """
                <div class="result-warning">
                    🟡 KHẢ NĂNG TRẢ NỢ CẦN ĐƯỢC XEM XÉT
                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "DSCR hiện thấp hơn 1 hoặc chưa được tính. "
                "Cần đánh giá thêm dòng tiền và khả năng trả nợ."
            )

        else:

            st.markdown(
                """
                <div class="result-good">
                    🟢 ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT TIẾP
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "Các điều kiện sơ bộ được đánh giá là đạt, "
                "chỉ tiêu tài chính có tín hiệu tích cực và DSCR từ 1 trở lên. "
                "Hồ sơ có thể được chuyển sang bước thẩm định chi tiết."
            )

        st.divider()

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        def them_dieu_kien(ten, gia_tri):

            if gia_tri == "Có":

                ket_qua.append(
                    [ten, "Đạt", "Được đánh giá là Có"]
                )

            elif gia_tri == "Không":

                ket_qua.append(
                    [ten, "Không đạt", "Được đánh giá là Không"]
                )

            else:

                ket_qua.append(
                    [ten, "Chưa đánh giá", "Chưa có kết luận"]
                )


        them_dieu_kien(
            "Năng lực pháp lý",
            st.session_state.nang_luc_phap_ly
        )

        them_dieu_kien(
            "Mục đích vay hợp pháp",
            st.session_state.muc_dich_hop_phap
        )

        them_dieu_kien(
            "Có phương án sử dụng vốn",
            st.session_state.co_phuong_an
        )

        them_dieu_kien(
            "Tính khả thi của phương án",
            st.session_state.phuong_an_kha_thi
        )

        them_dieu_kien(
            "Khả năng tài chính trả nợ",
            st.session_state.kha_nang_tra_no_dk
        )

        them_dieu_kien(
            "Cam kết sử dụng vốn đúng mục đích",
            st.session_state.cam_ket_dung_muc_dich
        )

        them_dieu_kien(
            "Cam kết trả nợ đúng hạn",
            st.session_state.cam_ket_tra_no
        )


        # Tài chính

        if st.session_state.lnst > 0:

            ket_qua.append(
                [
                    "LNST",
                    "Tích cực",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "LNST",
                    "Cần xem xét",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )


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


        if st.session_state.ltv is not None:

            if st.session_state.ltv <= 70:

                ket_qua.append(
                    [
                        "LTV",
                        "Tham khảo tốt",
                        f"{st.session_state.ltv:.2f}%"
                    ]
                )

            else:

                ket_qua.append(
                    [
                        "LTV",
                        "Cần xem xét",
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

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu hỗ trợ
            phân tích tín dụng, không phải điều kiện pháp lý duy nhất
            để quyết định doanh nghiệp có được vay hay không.

            Quyết định cho vay thực tế còn phải xem xét hồ sơ pháp lý,
            mục đích sử dụng vốn, phương án kinh doanh, tình hình tài chính,
            dòng tiền, lịch sử tín dụng, nghĩa vụ nợ, tài sản bảo đảm,
            khả năng trả nợ và chính sách tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 10. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP
        <br>
        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng
        <br><br>
        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.
    </div>
    """,
    unsafe_allow_html=True
)
