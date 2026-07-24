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
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no_dk": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # Tài chính
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # Chỉ tiêu tài chính
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # Khả năng trả nợ
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

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN ỨNG DỤNG
    ================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eef5fb 50%,
            #f9fbfd 100%
        );
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #071b35 0%,
            #0b3158 50%,
            #0e4d78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0d3b66 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155a8a !important;
        font-weight: 700 !important;
    }


    /* ================================
       HERO
    ================================= */

    .hero-card {
        background: linear-gradient(
            135deg,
            #06264a,
            #0c568c,
            #1496c7
        );

        padding: 38px;
        border-radius: 24px;
        color: white;

        box-shadow:
            0 15px 35px rgba(8,38,74,0.22);

        margin-bottom: 25px;
    }

    .hero-card h1 {
        color: white !important;
        font-size: 32px;
        margin-bottom: 10px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
    }


    /* ================================
       CARD
    ================================= */

    .card {
        background: rgba(255,255,255,0.95);
        padding: 22px;
        border-radius: 18px;

        border: 1px solid #dbe7f2;

        box-shadow:
            0 7px 22px rgba(13,59,102,0.07);

        margin-bottom: 18px;
    }


    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #dce7f2;
        padding: 18px;
        border-radius: 18px;

        box-shadow:
            0 6px 18px rgba(13,59,102,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3761 !important;
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

        font-weight: 700;
        color: white;

        background: linear-gradient(
            135deg,
            #0b4f8a,
            #1688c4
        );

        box-shadow:
            0 5px 15px rgba(11,79,138,0.22);

        transition: 0.25s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 8px 20px rgba(11,79,138,0.3);
    }


    /* ================================
       STATUS
    ================================= */

    .status-good {
        background: #e9f8ef;
        border-left: 5px solid #1e9e58;

        padding: 16px;
        border-radius: 12px;

        color: #176b3c;
        font-weight: 700;
    }

    .status-warning {
        background: #fff7df;
        border-left: 5px solid #e4a400;

        padding: 16px;
        border-radius: 12px;

        color: #805f00;
        font-weight: 700;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 5px solid #d64545;

        padding: 16px;
        border-radius: 12px;

        color: #8c2525;
        font-weight: 700;
    }


    /* ================================
       FOOTER
    ================================= */

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
# 4. SIDEBAR - MENU GỌN 4 MỤC
# =========================================================

with st.sidebar:

    # Nếu có logo.jpg trong cùng thư mục app.py
    try:
        st.image("logo.jpg", width=150)
    except:
        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:50px;
                padding:10px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:18px;
            font-weight:800;
            line-height:1.5;
        ">
            THẨM ĐỊNH
            <br>
            CHO VAY DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "### 📋 DANH MỤC THẨM ĐỊNH"
    )

    menu = st.radio(
        "",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Tài chính, Trả nợ & TSĐB",
            "📊 Kết quả thẩm định"
        ]
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

            <h1>
                🏦 HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Phân tích hồ sơ • Kiểm tra điều kiện vay •
                Đánh giá tài chính • Khả năng trả nợ •
                Tài sản bảo đảm • Tổng hợp kết quả
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👋 Chào mừng bạn đến với hệ thống")

    st.write(
        """
        Hệ thống hỗ trợ cán bộ tín dụng hoặc người sử dụng
        thực hiện thẩm định sơ bộ hồ sơ vay vốn của doanh nghiệp.
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
            "💰 Tài chính",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )

    with c3:
        st.metric(
            "📈 Trả nợ",
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
            mục đích và phương án vay.
            """
        )

    with c2:
        st.success(
            """
            **02 | ĐIỀU KIỆN**

            Kiểm tra điều kiện vay vốn
            và mục đích sử dụng vốn.
            """
        )

    with c3:
        st.warning(
            """
            **03 | PHÂN TÍCH**

            Đánh giá tài chính,
            khả năng trả nợ và TSĐB.
            """
        )

    with c4:
        st.error(
            """
            **04 | KẾT QUẢ**

            Tổng hợp thông tin
            và đưa ra kết luận sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Đây là công cụ hỗ trợ thẩm định sơ bộ.
        Kết quả không thay thế quyết định tín dụng chính thức
        của ngân hàng hoặc tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")

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
            value=int(st.session_state.thoi_gian_hd)
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
            ]
        )

    phuong_an = st.text_area(
        "Phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập nội dung phương án kinh doanh và nhu cầu sử dụng vốn..."
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

            st.success(
                "✅ Đã lưu hồ sơ doanh nghiệp."
            )

    st.divider()

    st.subheader("⚖️ 2. Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Các nội dung dưới đây dùng để kiểm tra sơ bộ điều kiện
        vay vốn. Việc đánh giá chính thức cần căn cứ hồ sơ pháp lý,
        mục đích vay, phương án sử dụng vốn và quy định tín dụng
        hiện hành của tổ chức tín dụng.
        """
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Doanh nghiệp có năng lực pháp lý phù hợp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.nang_luc_phap_ly)
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "Mục đích vay vốn có hợp pháp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.muc_dich_hop_phap)
        )

        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.co_phuong_an)
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn có khả thi?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.phuong_an_kha_thi)
        )

    with c2:

        st.session_state.kha_nang_tra_no_dk = st.selectbox(
            "Doanh nghiệp có khả năng tài chính trả nợ?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.kha_nang_tra_no_dk)
        )

        st.session_state.dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.dung_muc_dich)
        )

        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết hoàn trả nợ đúng hạn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.tra_no_dung_han)
        )

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_dk,
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
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. TÀI CHÍNH, TRẢ NỢ & TSĐB
# =========================================================

elif menu == "💰 Tài chính, Trả nợ & TSĐB":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH, KHẢ NĂNG TRẢ NỢ & TSĐB")

    st.caption(
        "Đơn vị nhập liệu tài chính và khoản vay: triệu đồng"
    )

    # =====================================================
    # PHẦN A - TÀI CHÍNH
    # =====================================================

    st.subheader("📊 A. Phân tích tình hình tài chính")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=float(st.session_state.doanh_thu)
        )

        st.session_state.lnst = st.number_input(
            "📈 Lợi nhuận sau thuế (LNST)",
            value=float(st.session_state.lnst)
        )

        st.session_state.tong_tai_san = st.number_input(
            "🏢 Tổng tài sản",
            min_value=0.0,
            value=float(st.session_state.tong_tai_san)
        )

    with c2:

        st.session_state.von_chu_so_huu = st.number_input(
            "💼 Vốn chủ sở hữu",
            min_value=0.0,
            value=float(st.session_state.von_chu_so_huu)
        )

        st.session_state.no_phai_tra = st.number_input(
            "📌 Nợ phải trả",
            min_value=0.0,
            value=float(st.session_state.no_phai_tra)
        )

        st.session_state.dong_tien = st.number_input(
            "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
            value=float(st.session_state.dong_tien)
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
                "✅ Đã phân tích tình hình tài chính."
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
    # PHẦN B - KHOẢN VAY & KHẢ NĂNG TRẢ NỢ
    # =====================================================

    st.subheader("📈 B. Khoản vay & khả năng trả nợ")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "💰 Số tiền vay",
            min_value=0.0,
            value=float(st.session_state.so_tien_vay)
        )

        st.session_state.thoi_gian_vay = st.number_input(
            "📅 Thời hạn vay (tháng)",
            min_value=1,
            value=int(st.session_state.thoi_gian_vay)
        )

    with c2:

        st.session_state.lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=float(st.session_state.lai_suat)
        )

        st.session_state.nghia_vu_no_cu = st.number_input(
            "💳 Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=float(st.session_state.nghia_vu_no_cu)
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

        if st.button("📈 PHÂN TÍCH DSCR"):

            if st.session_state.dong_tien <= 0:

                st.error(
                    "❌ Dòng tiền kinh doanh phải lớn hơn 0 để tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )

                st.session_state.da_phan_tich_dscr = True

                st.success(
                    "✅ Đã phân tích khả năng trả nợ."
                )

                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )

                if st.session_state.dscr >= 1:

                    st.success(
                        "🟢 Dòng tiền hiện tại đủ hoặc cao hơn nghĩa vụ trả nợ theo mô hình hỗ trợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ theo mô hình hỗ trợ."
                    )

    st.divider()

    # =====================================================
    # PHẦN C - TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader("🏠 C. Tài sản bảo đảm")

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
        ].index(st.session_state.co_tsdb)
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=float(st.session_state.gia_tri_tsdb)
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
                    "🟡 Cần xem xét thêm chất lượng, tính pháp lý và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả dưới đây là kết quả hỗ trợ thẩm định sơ bộ.
        Quyết định tín dụng thực tế cần căn cứ hồ sơ pháp lý,
        hồ sơ tài chính, lịch sử tín dụng, phương án kinh doanh,
        khả năng trả nợ, TSĐB và chính sách tín dụng của ngân hàng.
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

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết quả thẩm định sơ bộ."
        )

        st.write("Các nội dung còn thiếu:")

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
            st.session_state.kha_nang_tra_no_dk,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        co_khong = "Không" in dieu_kien

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

        # =================================================
        # THÔNG TIN KHÁCH HÀNG
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
        # KHẢ NĂNG TRẢ NỢ
        # =================================================

        st.subheader("📈 KHẢ NĂNG TRẢ NỢ & TÀI SẢN BẢO ĐẢM")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Khoản vay",
            f"{st.session_state.so_tien_vay:,.2f} triệu"
        )

        if st.session_state.dscr is not None:

            c2.metric(
                "DSCR",
                f"{st.session_state.dscr:.2f} lần"
            )

        else:

            c2.metric(
                "DSCR",
                "Chưa tính"
            )

        if st.session_state.ltv is not None:

            c3.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

        else:

            c3.metric(
                "LTV",
                "Không áp dụng"
            )

        st.divider()

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

        # -------------------------------------------------
        # TRƯỜNG HỢP 1: CÓ ĐIỀU KIỆN KHÔNG ĐẠT
        # -------------------------------------------------

        if co_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 CHƯA ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ có ít nhất một điều kiện vay vốn cơ bản
                đang được đánh giá là Không. Cần xem xét nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước khi
                tiếp tục thẩm định.
                """
            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 2: CHƯA ĐỦ DỮ LIỆU
        # -------------------------------------------------

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
                Cần hoàn thiện thông tin trước khi đưa ra kết luận
                thẩm định sơ bộ.
                """
            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 3: ĐẠT SƠ BỘ
        # -------------------------------------------------

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
                    🟢 HỒ SƠ CÓ CƠ SỞ ĐỂ TIẾP TỤC XEM XÉT TÍN DỤNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ hiện đáp ứng các điều kiện sơ bộ đã được đánh giá.
                Doanh nghiệp có kết quả kinh doanh dương, các chỉ tiêu
                sinh lời tích cực và dòng tiền có khả năng đáp ứng nghĩa vụ
                trả nợ theo dữ liệu nhập.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
                chi tiết theo quy trình của ngân hàng.
                """
            )

        # -------------------------------------------------
        # TRƯỜNG HỢP 4: CẦN THẨM ĐỊNH BỔ SUNG
        # -------------------------------------------------

        else:

            st.markdown(
                """
                <div class="status-warning">
                    🟡 CẦN THẨM ĐỊNH BỔ SUNG TRƯỚC KHI XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ chưa đáp ứng đầy đủ các chỉ tiêu hỗ trợ theo
                mô hình sơ bộ. Cần xem xét thêm tình hình tài chính,
                dòng tiền, khả năng trả nợ, phương án kinh doanh,
                lịch sử tín dụng và tài sản bảo đảm.
                """
            )

        st.divider()

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        # Điều kiện pháp lý
        if st.session_state.nang_luc_phap_ly == "Có":
            ket_qua.append(
                [
                    "Năng lực pháp lý",
                    "Đạt",
                    "Được đánh giá phù hợp"
                ]
            )
        else:
            ket_qua.append(
                [
                    "Năng lực pháp lý",
                    "Cần xem xét",
                    st.session_state.nang_luc_phap_ly
                ]
            )

        # Mục đích
        if st.session_state.muc_dich_hop_phap == "Có":
            ket_qua.append(
                [
                    "Mục đích vay vốn",
                    "Đạt",
                    "Được đánh giá hợp pháp"
                ]
            )
        else:
            ket_qua.append(
                [
                    "Mục đích vay vốn",
                    "Cần xem xét",
                    st.session_state.muc_dich_hop_phap
                ]
            )

        # Phương án
        if st.session_state.co_phuong_an == "Có":
            ket_qua.append(
                [
                    "Phương án sử dụng vốn",
                    "Đạt",
                    "Có phương án"
                ]
            )
        else:
            ket_qua.append(
                [
                    "Phương án sử dụng vốn",
                    "Cần xem xét",
                    st.session_state.co_phuong_an
                ]
            )

        # Tính khả thi
        if st.session_state.phuong_an_kha_thi == "Có":
            ket_qua.append(
                [
                    "Tính khả thi phương án",
                    "Đạt",
                    "Phương án được đánh giá khả thi"
                ]
            )
        else:
            ket_qua.append(
                [
                    "Tính khả thi phương án",
                    "Cần xem xét",
                    st.session_state.phuong_an_kha_thi
                ]
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
                    "Chưa đánh giá",
                    "Chưa tính DSCR"
                ]
            )

        # TSĐB
        if st.session_state.co_tsdb == "Có":

            if st.session_state.ltv is not None:

                if st.session_state.ltv <= 70:

                    ket_qua.append(
                        [
                            "Tài sản bảo đảm",
                            "Tương đối tốt",
                            f"LTV {st.session_state.ltv:.2f}%"
                        ]
                    )

                else:

                    ket_qua.append(
                        [
                            "Tài sản bảo đảm",
                            "Cần xem xét",
                            f"LTV {st.session_state.ltv:.2f}%"
                        ]
                    )

            else:

                ket_qua.append(
                    [
                        "Tài sản bảo đảm",
                        "Chưa đánh giá",
                        "Chưa tính LTV"
                    ]
                )

        elif st.session_state.co_tsdb == "Không":

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Không có TSĐB",
                    "Cần đánh giá theo chính sách tín dụng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Chưa đánh giá",
                    "Chưa xác định"
                ]
            )

        # Tạo DataFrame
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
            ⚠️ LƯU Ý:

            Kết quả thẩm định trên chỉ mang tính chất hỗ trợ sơ bộ.
            ROA, ROE, LNST, DSCR và LTV không phải là các điều kiện
            pháp lý độc lập để kết luận doanh nghiệp chắc chắn được vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể:
            hồ sơ pháp lý, mục đích sử dụng vốn, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách của
            từng ngân hàng hoặc tổ chức tín dụng.
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
