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

    # Điều kiện vay vốn
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

    /* Nền chung */
    .stApp {
        background-color: #f4f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #071b35 0%,
            #0b3761 50%,
            #0e5a8a 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Tiêu đề */
    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b3761 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155a8a !important;
        font-weight: 700 !important;
    }

    /* Nút */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            135deg,
            #0b4f8a,
            #1684c4
        );
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* Metric */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #dbe5ef;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0 5px 18px rgba(13, 59, 102, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3761 !important;
        font-weight: 800;
    }

    /* Card trang chủ */
    .hero-card {
        background: linear-gradient(
            135deg,
            #08264a,
            #0d5287,
            #1684c4
        );
        padding: 32px;
        border-radius: 22px;
        color: white;
        box-shadow: 0 12px 30px rgba(8, 38, 74, 0.20);
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 30px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 16px;
        opacity: 0.92;
    }

    /* Card trạng thái */
    .status-good {
        background-color: #e9f8ef;
        border-left: 5px solid #1e9e58;
        padding: 16px;
        border-radius: 10px;
        color: #176b3c;
        font-weight: 700;
    }

    .status-warning {
        background-color: #fff7df;
        border-left: 5px solid #e4a400;
        padding: 16px;
        border-radius: 10px;
        color: #805f00;
        font-weight: 700;
    }

    .status-bad {
        background-color: #fff0f0;
        border-left: 5px solid #d64545;
        padding: 16px;
        border-radius: 10px;
        color: #8c2525;
        font-weight: 700;
    }

    /* Footer */
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
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">
            <div style="font-size:42px;">🏦</div>

            <div style="
                font-size:19px;
                font-weight:800;
                line-height:1.4;
            ">
                THẨM ĐỊNH
                <br>
                CHO VAY DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                font-weight:600;
                opacity:0.85;
                margin-top:8px;
            ">
                HỖ TRỢ PHÂN TÍCH TÍN DỤNG
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
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Tài chính, Khả năng trả nợ & TSĐB",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-title">
                🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                CHO VAY DOANH NGHIỆP
            </div>

            <div class="hero-subtitle">
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
        Ứng dụng hỗ trợ cán bộ/người dùng thực hiện
        quy trình thẩm định sơ bộ đối với hồ sơ vay vốn
        của doanh nghiệp.
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
            "📈 Khả năng trả nợ",
            "Đã phân tích"
            if st.session_state.da_phan_tich_dscr
            else "Chưa phân tích"
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
            **02 | ĐIỀU KIỆN**

            Kiểm tra điều kiện vay vốn,
            mục đích và phương án sử dụng vốn.
            """
        )

    with c3:
        st.info(
            """
            **03 | PHÂN TÍCH**

            Đánh giá tài chính,
            khả năng trả nợ và TSĐB.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu và
            đưa ra kết luận thẩm định sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Ứng dụng chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ. Kết quả không thay thế quyết định
        cấp tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")

    # -----------------------------------------------------
    # THÔNG TIN DOANH NGHIỆP
    # -----------------------------------------------------

    st.subheader("📋 1. Thông tin doanh nghiệp")

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
            value=st.session_state.thoi_gian_hd
        )

    # -----------------------------------------------------
    # MỤC ĐÍCH VAY
    # -----------------------------------------------------

    st.subheader("💳 2. Mục đích và phương án vay")

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
        danh_sach_muc_dich
    )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập phương án kinh doanh và nhu cầu sử dụng vốn..."
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

    st.divider()

    # -----------------------------------------------------
    # ĐIỀU KIỆN VAY VỐN
    # -----------------------------------------------------

    st.subheader("⚖️ 3. Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Phần này dùng để đánh giá sơ bộ các điều kiện liên quan
        đến hồ sơ vay vốn. Kết quả thực tế còn phụ thuộc vào
        quy định pháp luật và chính sách tín dụng của từng tổ chức tín dụng.
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
            "6. Cam kết sử dụng vốn đúng mục đích?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.dung_muc_dich
            )
        )

        st.session_state.tra_no_dung_han = st.selectbox(
            "7. Cam kết hoàn trả nợ đúng hạn?",
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
                "🔴 Có ít nhất một điều kiện đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Tất cả các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. TÀI CHÍNH + KHẢ NĂNG TRẢ NỢ + TSĐB
# =========================================================

elif menu == "💰 Tài chính, Khả năng trả nợ & TSĐB":

    st.title(
        "💰 TÀI CHÍNH, KHẢ NĂNG TRẢ NỢ & TÀI SẢN BẢO ĐẢM"
    )

    st.info(
        """
        Nhập và phân tích các thông tin tài chính,
        khoản vay, khả năng trả nợ và tài sản bảo đảm.
        """
    )

    # =====================================================
    # PHẦN 1 - TÀI CHÍNH
    # =====================================================

    st.header("1️⃣ PHÂN TÍCH TÀI CHÍNH")

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
            "💧 Dòng tiền từ hoạt động kinh doanh",
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
    # PHẦN 2 - KHOẢN VAY & KHẢ NĂNG TRẢ NỢ
    # =====================================================

    st.header("2️⃣ KHOẢN VAY & KHẢ NĂNG TRẢ NỢ")

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

        st.subheader("📈 Phân tích DSCR")

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

    st.divider()

    # =====================================================
    # PHẦN 3 - TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.header("3️⃣ TÀI SẢN BẢO ĐẢM")

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm
        của khoản vay. Kết quả thực tế còn phụ thuộc vào
        loại tài sản, giá trị định giá, khả năng thanh khoản
        và chính sách của tổ chức tín dụng.
        """
    )

    danh_sach_tsdb = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        danh_sach_tsdb,
        index=danh_sach_tsdb.index(
            st.session_state.co_tsdb
        )
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "🏠 Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có TSĐB hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được đánh giá là không có tài sản bảo đảm."
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
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả được tổng hợp từ hồ sơ, điều kiện vay,
        tình hình tài chính, khả năng trả nợ và tài sản bảo đảm.
        Đây là kết quả hỗ trợ thẩm định sơ bộ, không phải quyết định
        cấp tín dụng chính thức.
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

    if not st.session_state.da_phan_tich_dscr:
        missing.append("Phân tích khả năng trả nợ")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Phân tích tài sản bảo đảm")

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận thẩm định."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:
            st.write(
                f"• {item}"
            )

        st.info(
            "Vui lòng hoàn thiện các mục trên trước khi xem kết quả."
        )

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
        # THÔNG TIN KHOẢN VAY
        # =================================================

        st.subheader("💳 THÔNG TIN KHOẢN VAY")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Số tiền vay",
            f"{st.session_state.so_tien_vay:,.2f} triệu"
        )

        c2.metric(
            "Thời hạn vay",
            f"{st.session_state.thoi_gian_vay} tháng"
        )

        c3.metric(
            "Lãi suất",
            f"{st.session_state.lai_suat:.2f}%/năm"
        )

        st.divider()

        # =================================================
        # CHỈ TIÊU TÀI CHÍNH
        # =================================================

        st.subheader("📈 CHỈ TIÊU TÀI CHÍNH")

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

        # =================================================
        # KHẢ NĂNG TRẢ NỢ
        # =================================================

        st.subheader("📊 KHẢ NĂNG TRẢ NỢ")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Dòng tiền",
            f"{st.session_state.dong_tien:,.2f}"
        )

        c2.metric(
            "Nghĩa vụ trả nợ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )

        c3.metric(
            "DSCR",
            f"{st.session_state.dscr:.2f} lần"
        )

        st.divider()

        # =================================================
        # TÀI SẢN BẢO ĐẢM
        # =================================================

        st.subheader("🏠 TÀI SẢN BẢO ĐẢM")

        c1, c2 = st.columns(2)

        c1.metric(
            "Có TSĐB",
            st.session_state.co_tsdb
        )

        if st.session_state.ltv is not None:

            c2.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

        else:

            c2.metric(
                "LTV",
                "Không áp dụng"
            )

        st.divider()

        # =================================================
        # ĐÁNH GIÁ ĐIỀU KIỆN
        # =================================================

        st.subheader("⚖️ ĐÁNH GIÁ ĐIỀU KIỆN VAY")

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        so_dieu_kien_dat = dieu_kien.count("Có")
        so_dieu_kien_khong = dieu_kien.count("Không")
        so_chua_danh_gia = dieu_kien.count("Chưa đánh giá")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Điều kiện đạt",
            f"{so_dieu_kien_dat}/7"
        )

        c2.metric(
            "Điều kiện không đạt",
            so_dieu_kien_khong
        )

        c3.metric(
            "Chưa đánh giá",
            so_chua_danh_gia
        )

        st.divider()

        # =================================================
        # KẾT LUẬN THẨM ĐỊNH
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

        # Điều kiện pháp lý/vay
        dieu_kien_dat_day_du = (
            so_dieu_kien_dat == 7
        )

        # Tài chính
        tai_chinh_tich_cuc = (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
        )

        # Trả nợ
        kha_nang_tra_no_tot = (
            st.session_state.dscr is not None
            and st.session_state.dscr >= 1
        )

        # TSĐB
        tsdb_phu_hop = True

        if st.session_state.co_tsdb == "Có":

            if (
                st.session_state.ltv is not None
                and st.session_state.ltv <= 70
            ):
                tsdb_phu_hop = True

            else:
                tsdb_phu_hop = False

        elif st.session_state.co_tsdb == "Không":

            tsdb_phu_hop = True

        else:

            tsdb_phu_hop = False

        # =================================================
        # KẾT LUẬN 1 - KHÔNG ĐỦ ĐIỀU KIỆN
        # =================================================

        if so_dieu_kien_khong > 0:

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
                được đánh giá là "Không". Do đó, hồ sơ chưa
                đủ cơ sở để xem xét theo kết quả thẩm định sơ bộ.
                """
            )

        # =================================================
        # KẾT LUẬN 2 - CHƯA ĐỦ DỮ LIỆU
        # =================================================

        elif so_chua_danh_gia > 0:

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
                đánh giá. Cần bổ sung và hoàn thiện thông tin
                trước khi đưa ra kết luận.
                """
            )

        # =================================================
        # KẾT LUẬN 3 - TÍCH CỰC
        # =================================================

        elif (
            dieu_kien_dat_day_du
            and tai_chinh_tich_cuc
            and kha_nang_tra_no_tot
            and tsdb_phu_hop
        ):

            st.markdown(
                """
                <div class="status-good">
                    🟢 HỒ SƠ CÓ CƠ SỞ ĐỂ XEM XÉT CẤP TÍN DỤNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đáp ứng các điều kiện sơ bộ được nhập vào hệ thống.
                Tình hình lợi nhuận, các chỉ tiêu ROA và ROE có tín hiệu tích cực.
                Dòng tiền có khả năng đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR.
                Tài sản bảo đảm, nếu có, có mức LTV phù hợp theo tiêu chí hỗ trợ.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng chi tiết
                theo quy trình và chính sách của tổ chức tín dụng.
                """
            )

        # =================================================
        # KẾT LUẬN 4 - CẦN THẨM ĐỊNH BỔ SUNG
        # =================================================

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
                Hồ sơ chưa đáp ứng đầy đủ các tiêu chí hỗ trợ
                để đưa ra kết luận tích cực. Cần xem xét thêm
                tình hình tài chính, dòng tiền, khả năng trả nợ,
                phương án kinh doanh, lịch sử tín dụng và
                chất lượng tài sản bảo đảm.
                """
            )

        st.divider()

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        # Điều kiện
        ket_qua.append([
            "Năng lực pháp lý",
            st.session_state.nang_luc_phap_ly,
            "Điều kiện hồ sơ"
        ])

        ket_qua.append([
            "Mục đích vay vốn",
            st.session_state.muc_dich_hop_phap,
            "Mục đích sử dụng vốn"
        ])

        ket_qua.append([
            "Phương án sử dụng vốn",
            st.session_state.co_phuong_an,
            "Có phương án"
        ])

        ket_qua.append([
            "Tính khả thi phương án",
            st.session_state.phuong_an_kha_thi,
            "Đánh giá phương án"
        ])

        ket_qua.append([
            "Khả năng trả nợ",
            st.session_state.kha_nang_tra_no,
            "Đánh giá sơ bộ"
        ])

        # Tài chính
        ket_qua.append([
            "LNST",
            "Tích cực"
            if st.session_state.lnst > 0
            else "Cần xem xét",
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ])

        ket_qua.append([
            "ROA",
            "Tích cực"
            if st.session_state.roa > 0
            else "Cần xem xét",
            f"{st.session_state.roa:.2f}%"
        ])

        ket_qua.append([
            "ROE",
            "Tích cực"
            if st.session_state.roe > 0
            else "Cần xem xét",
            f"{st.session_state.roe:.2f}%"
        ])

        ket_qua.append([
            "Tỷ lệ nợ",
            "Tham khảo",
            f"{st.session_state.ty_le_no:.2f}%"
        ])

        # DSCR
        ket_qua.append([
            "DSCR",
            "Tích cực"
            if st.session_state.dscr >= 1
            else "Cần xem xét",
            f"{st.session_state.dscr:.2f} lần"
        ])

        # TSĐB
        if st.session_state.co_tsdb == "Có":

            ket_qua.append([
                "Tài sản bảo đảm",
                "Có",
                f"{st.session_state.gia_tri_tsdb:,.2f} triệu đồng"
            ])

            ket_qua.append([
                "LTV",
                "Phù hợp tham khảo"
                if st.session_state.ltv <= 70
                else "Cần xem xét",
                f"{st.session_state.ltv:.2f}%"
            ])

        else:

            ket_qua.append([
                "Tài sản bảo đảm",
                "Không có",
                "Khoản vay không có TSĐB"
            ])

        df = pd.DataFrame(
            ket_qua,
            columns=[
                "Tiêu chí",
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

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả "Có cơ sở để xem xét cấp tín dụng" không đồng nghĩa
            với việc doanh nghiệp chắc chắn được ngân hàng phê duyệt khoản vay.

            ROA, ROE, LNST, DSCR, LTV và các tiêu chí trong ứng dụng chỉ là
            các chỉ tiêu hỗ trợ thẩm định. Quyết định tín dụng thực tế còn
            phụ thuộc vào hồ sơ pháp lý, mục đích vay, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng, nghĩa vụ nợ,
            tài sản bảo đảm, khả năng thanh khoản và chính sách tín dụng
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
        <br>
        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng
        <br><br>
        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.
    </div>
    """,
    unsafe_allow_html=True
)
