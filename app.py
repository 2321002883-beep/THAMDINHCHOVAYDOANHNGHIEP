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
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
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
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False
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
            #eaf2f9 50%,
            #f8fbff 100%
        );
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #061a33 0%,
            #0b3157 50%,
            #0e4775 100%
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
        color: #08264a !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b3d67 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #145a87 !important;
        font-weight: 700 !important;
    }

    /* =========================
       HERO
    ========================= */

    .hero-card {
        background: linear-gradient(
            135deg,
            #06284d,
            #0b5688,
            #168bc0
        );
        padding: 35px;
        border-radius: 25px;
        color: white;
        box-shadow: 0 15px 35px rgba(5, 40, 77, 0.25);
        margin-bottom: 25px;
    }

    .hero-title {
        color: white;
        font-size: 31px;
        font-weight: 800;
        line-height: 1.35;
        margin-bottom: 12px;
    }

    .hero-text {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        line-height: 1.7;
    }

    /* =========================
       SIDEBAR LOGO
       ========================= */

    .sidebar-title {
        text-align: center;
        font-size: 18px;
        font-weight: 800;
        line-height: 1.5;
        margin-top: 8px;
    }

    .sidebar-subtitle {
        text-align: center;
        font-size: 13px;
        opacity: 0.85;
        margin-top: 5px;
    }

    /* =========================
       METRIC
       ========================= */

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.96);
        border: 1px solid #d8e5f1;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 22px rgba(13,59,102,0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #58718a !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3761 !important;
        font-weight: 800;
    }

    /* =========================
       BUTTON
       ========================= */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            135deg,
            #07528d,
            #1386c2
        );
        box-shadow: 0 5px 15px rgba(11,79,138,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(11,79,138,0.30);
    }

    /* =========================
       CARD
       ========================= */

    .section-card {
        background: rgba(255,255,255,0.92);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #dce7f2;
        box-shadow: 0 6px 20px rgba(13,59,102,0.06);
        margin-bottom: 18px;
    }

    /* =========================
       STATUS
       ========================= */

    .status-good {
        background: #e9f8ef;
        border-left: 6px solid #1e9e58;
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
        color: #71869b;
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

    # Nếu có logo.jpg thì bỏ dấu # ở dòng st.image
    # st.image("logo.jpg", use_container_width=True)

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:8px 5px 15px 5px;
        ">
            <div style="
                font-size:42px;
                margin-bottom:5px;
            ">
                🏦
            </div>

            <div class="sidebar-title">
                THẨM ĐỊNH<br>
                CHO VAY DOANH NGHIỆP
            </div>

            <div class="sidebar-subtitle">
                Hệ thống hỗ trợ thẩm định sơ bộ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "📌 DANH MỤC THẨM ĐỊNH",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện & khoản vay",
            "💰 Tài chính & khả năng trả nợ",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption(
        "🏦 Hệ thống hỗ trợ thẩm định tín dụng"
    )

    st.caption(
        "⚠️ Kết quả chỉ mang tính chất tham khảo."
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

    st.subheader("📊 TÌNH TRẠNG HỒ SƠ")

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

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(
            """
            **01 | HỒ SƠ**

            Nhập thông tin doanh nghiệp,
            ngành nghề và mục đích vay.
            """
        )

    with c2:
        st.info(
            """
            **02 | ĐIỀU KIỆN & KHOẢN VAY**

            Kiểm tra điều kiện vay,
            khoản vay và TSĐB.
            """
        )

    with c3:
        st.info(
            """
            **03 | TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE, tỷ lệ nợ và DSCR.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp các tiêu chí
            và đưa ra kết luận sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ LƯU Ý:

        Hệ thống chỉ hỗ trợ thẩm định sơ bộ.
        Kết quả không thay thế quyết định tín dụng chính thức
        của ngân hàng hoặc tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title("🏢 HỒ SƠ DOANH NGHIỆP")

    st.subheader("📋 Thông tin cơ bản")

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

        nganh_nghe = st.selectbox(
            "Ngành nghề kinh doanh",
            danh_sach_nganh,
            index=danh_sach_nganh.index(
                st.session_state.nganh_nghe
            )
        )

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=int(st.session_state.thoi_gian_hd)
        )

    st.subheader("💳 Nhu cầu vay vốn")

    danh_sach_muc_dich = [
        "Bổ sung vốn lưu động",
        "Mua nguyên vật liệu",
        "Đầu tư máy móc thiết bị",
        "Mở rộng sản xuất",
        "Mua tài sản cố định",
        "Khác"
    ]

    muc_dich_vay = st.selectbox(
        "Mục đích sử dụng vốn",
        danh_sach_muc_dich,
        index=danh_sach_muc_dich.index(
            st.session_state.muc_dich_vay
        )
    )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder=(
            "Nhập phương án kinh doanh, "
            "nguồn trả nợ và nhu cầu sử dụng vốn..."
        )
    )

    if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

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
                "✅ Đã lưu hồ sơ doanh nghiệp thành công."
            )


# =========================================================
# 7. ĐIỀU KIỆN & KHOẢN VAY
# =========================================================

elif menu == "⚖️ Điều kiện & khoản vay":

    st.title("⚖️ ĐIỀU KIỆN & THÔNG TIN KHOẢN VAY")

    tab1, tab2, tab3 = st.tabs(
        [
            "⚖️ Điều kiện vay vốn",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm"
        ]
    )

    # =====================================================
    # TAB 1 - ĐIỀU KIỆN VAY
    # =====================================================

    with tab1:

        st.subheader("⚖️ Kiểm tra điều kiện vay vốn")

        st.info(
            """
            Các nội dung dưới đây là nhóm tiêu chí kiểm tra sơ bộ
            phục vụ thẩm định. Khi thẩm định thực tế cần đối chiếu
            quy định pháp luật hiện hành, hồ sơ pháp lý và chính sách
            tín dụng của từng ngân hàng.
            """
        )

        lua_chon = [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.nang_luc_phap_ly = st.selectbox(
                "1. Doanh nghiệp có năng lực pháp lý phù hợp?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.nang_luc_phap_ly
                )
            )

            st.session_state.muc_dich_hop_phap = st.selectbox(
                "2. Mục đích vay vốn có hợp pháp?",
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
                "4. Phương án sử dụng vốn có khả thi?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.phuong_an_kha_thi
                )
            )

        with c2:

            st.session_state.kha_nang_tra_no = st.selectbox(
                "5. Doanh nghiệp có khả năng trả nợ?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.kha_nang_tra_no
                )
            )

            st.session_state.dung_muc_dich = st.selectbox(
                "6. Có cam kết sử dụng vốn đúng mục đích?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.dung_muc_dich
                )
            )

            st.session_state.tra_no_dung_han = st.selectbox(
                "7. Có cam kết trả nợ đúng hạn?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.tra_no_dung_han
                )
            )

        if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

            dieu_kien = [
                st.session_state.nang_luc_phap_ly,
                st.session_state.muc_dich_hop_phap,
                st.session_state.co_phuong_an,
                st.session_state.phuong_an_kha_thi,
                st.session_state.kha_nang_tra_no,
                st.session_state.dung_muc_dich,
                st.session_state.tra_no_dung_han
            ]

            if "Không" in dieu_kien:

                st.error(
                    "🔴 Có ít nhất một tiêu chí đang được đánh giá là Không."
                )

            elif "Chưa đánh giá" in dieu_kien:

                st.warning(
                    "🟡 Chưa thể hoàn tất kiểm tra vì còn tiêu chí chưa đánh giá."
                )

            else:

                st.success(
                    "🟢 Tất cả các tiêu chí sơ bộ hiện đang được đánh giá là Có."
                )

    # =====================================================
    # TAB 2 - KHOẢN VAY
    # =====================================================

    with tab2:

        st.subheader("💳 Thông tin khoản vay")

        st.caption(
            "Đơn vị nhập liệu: triệu đồng"
        )

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.so_tien_vay = st.number_input(
                "💰 Số tiền vay",
                min_value=0.0,
                value=float(
                    st.session_state.so_tien_vay
                )
            )

            st.session_state.thoi_gian_vay = st.number_input(
                "📅 Thời hạn vay (tháng)",
                min_value=1,
                value=int(
                    st.session_state.thoi_gian_vay
                )
            )

        with c2:

            st.session_state.lai_suat = st.number_input(
                "📈 Lãi suất (%/năm)",
                min_value=0.0,
                value=float(
                    st.session_state.lai_suat
                )
            )

            st.session_state.nghia_vu_no_cu = st.number_input(
                "💳 Nghĩa vụ trả nợ hiện tại/tháng",
                min_value=0.0,
                value=float(
                    st.session_state.nghia_vu_no_cu
                )
            )

        if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

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
                    "✅ Đã tính nghĩa vụ trả nợ tháng đầu."
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
    # TAB 3 - TÀI SẢN BẢO ĐẢM
    # =====================================================

    with tab3:

        st.subheader("🏠 Tài sản bảo đảm")

        st.info(
            """
            LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm của khoản vay.
            Việc chấp nhận tài sản bảo đảm thực tế phụ thuộc vào loại tài sản,
            hồ sơ pháp lý, kết quả định giá, khả năng thanh khoản và chính sách
            của ngân hàng.
            """
        )

        lua_chon_tsdb = [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]

        st.session_state.co_tsdb = st.selectbox(
            "Khoản vay có tài sản bảo đảm?",
            lua_chon_tsdb,
            index=lua_chon_tsdb.index(
                st.session_state.co_tsdb
            )
        )

        st.session_state.gia_tri_tsdb = st.number_input(
            "Giá trị tài sản bảo đảm (triệu đồng)",
            min_value=0.0,
            value=float(
                st.session_state.gia_tri_tsdb
            )
        )

        if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

            if st.session_state.co_tsdb == "Chưa đánh giá":

                st.warning(
                    "⚠️ Vui lòng xác định có hoặc không có tài sản bảo đảm."
                )

            elif st.session_state.co_tsdb == "Không":

                st.session_state.ltv = None
                st.session_state.da_phan_tich_tsdb = True

                st.info(
                    "ℹ️ Khoản vay được khai báo không có tài sản bảo đảm."
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
                        "🟡 Cần xem xét thêm chất lượng, pháp lý và khả năng thanh khoản của TSĐB."
                    )

                else:

                    st.error(
                        "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                    )


# =========================================================
# 8. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & khả năng trả nợ":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ")

    tab1, tab2 = st.tabs(
        [
            "💰 Phân tích tài chính",
            "📈 Khả năng trả nợ"
        ]
    )

    # =====================================================
    # TAB 1 - TÀI CHÍNH
    # =====================================================

    with tab1:

        st.subheader("💰 Phân tích tình hình tài chính")

        st.caption(
            "Đơn vị nhập liệu: triệu đồng"
        )

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.doanh_thu = st.number_input(
                "💵 Doanh thu",
                min_value=0.0,
                value=float(
                    st.session_state.doanh_thu
                )
            )

            st.session_state.lnst = st.number_input(
                "📈 Lợi nhuận sau thuế (LNST)",
                value=float(
                    st.session_state.lnst
                )
            )

            st.session_state.tong_tai_san = st.number_input(
                "🏢 Tổng tài sản",
                min_value=0.0,
                value=float(
                    st.session_state.tong_tai_san
                )
            )

        with c2:

            st.session_state.von_chu_so_huu = st.number_input(
                "💼 Vốn chủ sở hữu",
                min_value=0.0,
                value=float(
                    st.session_state.von_chu_so_huu
                )
            )

            st.session_state.no_phai_tra = st.number_input(
                "📌 Nợ phải trả",
                min_value=0.0,
                value=float(
                    st.session_state.no_phai_tra
                )
            )

            st.session_state.dong_tien = st.number_input(
                "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
                value=float(
                    st.session_state.dong_tien
                )
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

            st.info(
                """
                💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu hỗ trợ phân tích
                tài chính. Không nên sử dụng riêng lẻ để quyết định cho vay.
                Cần xem xét thêm xu hướng tài chính, dòng tiền, cơ cấu nợ,
                ngành nghề và chính sách tín dụng.
                """
            )

    # =====================================================
    # TAB 2 - DSCR
    # =====================================================

    with tab2:

        st.subheader("📈 Phân tích khả năng trả nợ")

        if st.session_state.tong_nghia_vu is None:

            st.warning(
                "⚠️ Vui lòng nhập và tính thông tin khoản vay trước."
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

            if st.button("📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"):

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

                    st.divider()

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

                    st.info(
                        """
                        DSCR là chỉ tiêu hỗ trợ đánh giá khả năng trả nợ.
                        Ngưỡng chấp nhận cụ thể cần căn cứ vào phương pháp
                        tính, chất lượng dòng tiền và chính sách của từng
                        tổ chức tín dụng.
                        """
                    )


# =========================================================
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả dưới đây là kết quả hỗ trợ thẩm định sơ bộ dựa trên
        dữ liệu người dùng nhập. Không phải là quyết định phê duyệt
        hoặc từ chối khoản vay chính thức.
        """
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

    if not st.session_state.da_phan_tich_dscr:
        missing.append("Phân tích khả năng trả nợ")

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận thẩm định sơ bộ."
        )

        st.write(
            "Vui lòng hoàn thành các nội dung sau:"
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
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        co_dieu_kien_khong = (
            "Không" in dieu_kien
        )

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

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
        # CHỈ TIÊU TÀI CHÍNH
        # =================================================

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

        # =================================================
        # KHOẢN VAY
        # =================================================

        st.subheader("💳 THÔNG TIN KHOẢN VAY")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Số tiền vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        c2.metric(
            "Thời hạn",
            f"{st.session_state.thoi_gian_vay} tháng"
        )

        c3.metric(
            "Lãi suất",
            f"{st.session_state.lai_suat:.2f}%/năm"
        )

        c4.metric(
            "DSCR",
            f"{st.session_state.dscr:.2f} lần"
        )

        st.divider()

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

        # -------------------------------------------------
        # TRƯỜNG HỢP 1: CÓ ĐIỀU KIỆN KHÔNG ĐẠT
        # -------------------------------------------------

        if co_dieu_kien_khong:

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
                Hồ sơ đang có ít nhất một tiêu chí điều kiện vay vốn
                được đánh giá là "Không". Cần xác minh nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước khi
                tiếp tục xem xét tín dụng.
                """
            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 2: CHƯA ĐÁNH GIÁ ĐỦ
        # -------------------------------------------------

        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="status-warning">
                    🟡 CHƯA ĐỦ CƠ SỞ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Một hoặc nhiều điều kiện vay vốn chưa được đánh giá.
                Chưa đủ cơ sở để kết luận hồ sơ đạt điều kiện sơ bộ.
                """

            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 3: ĐẠT CÁC ĐIỀU KIỆN HỖ TRỢ
        # -------------------------------------------------

        elif (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
            and st.session_state.dscr >= 1
        ):

            st.markdown(
                """
                <div class="status-good">
                    🟢 HỒ SƠ CÓ TÍN HIỆU TÍCH CỰC - ĐỀ XUẤT XEM XÉT TIẾP
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đáp ứng các điều kiện sơ bộ đã được đánh giá,
                doanh nghiệp có lợi nhuận dương, ROA và ROE dương,
                đồng thời DSCR đạt từ 1 lần trở lên theo dữ liệu nhập.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
                chi tiết để xem xét thêm lịch sử tín dụng, dòng tiền,
                phương án kinh doanh, hồ sơ pháp lý, tài sản bảo đảm,
                nguồn trả nợ và các yếu tố rủi ro khác.
                """
            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 4: CẦN THẨM ĐỊNH BỔ SUNG
        # -------------------------------------------------

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
                Hồ sơ chưa có đủ tín hiệu tích cực theo các chỉ tiêu
                hỗ trợ đang sử dụng. Cần phân tích sâu hơn về tình hình
                tài chính, dòng tiền, khả năng trả nợ, lịch sử tín dụng,
                phương án kinh doanh và mức độ rủi ro trước khi xem xét
                quyết định tín dụng.
                """
            )

        st.divider()

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        # Điều kiện
        danh_sach_dieu_kien = [
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
                st.session_state.co_phuong_an
            ),
            (
                "Tính khả thi phương án",
                st.session_state.phuong_an_kha_thi
            ),
            (
                "Khả năng trả nợ",
                st.session_state.kha_nang_tra_no
            ),
            (
                "Cam kết sử dụng vốn đúng mục đích",
                st.session_state.dung_muc_dich
            ),
            (
                "Cam kết trả nợ đúng hạn",
                st.session_state.tra_no_dung_han
            )
        ]

        for ten, gia_tri in danh_sach_dieu_kien:

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
                        "Chưa có đủ thông tin"
                    ]
                )

        # Tài chính

        ket_qua.append(
            [
                "LNST",
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
                "Tiêu chí thẩm định",
                "Đánh giá",
                "Chi tiết"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # =================================================
        # CẢNH BÁO
        # =================================================

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG:

            Kết quả "Hồ sơ có tín hiệu tích cực - Đề xuất xem xét tiếp"
            KHÔNG đồng nghĩa với việc doanh nghiệp chắc chắn được ngân hàng
            phê duyệt khoản vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể:
            • Hồ sơ pháp lý doanh nghiệp
            • Mục đích và phương án sử dụng vốn
            • Tình hình tài chính và báo cáo tài chính
            • Dòng tiền và nguồn trả nợ
            • Lịch sử tín dụng
            • Nghĩa vụ nợ hiện tại
            • Tài sản bảo đảm và hồ sơ pháp lý của tài sản
            • Kết quả định giá tài sản
            • Rủi ro ngành nghề và thị trường
            • Chính sách tín dụng và thẩm quyền phê duyệt của ngân hàng
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
