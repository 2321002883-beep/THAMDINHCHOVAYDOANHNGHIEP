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

default_values = {

    # HỒ SƠ DOANH NGHIỆP
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # ĐIỀU KIỆN VAY
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_su_dung_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "su_dung_von_dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # TÀI CHÍNH
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # KẾT QUẢ TÀI CHÍNH
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # KHOẢN VAY
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # KHẢ NĂNG TRẢ NỢ
    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # TÀI SẢN BẢO ĐẢM
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # TRẠNG THÁI
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

    /* =========================================
       NỀN CHÍNH
    ========================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #edf5fb 50%,
            #f8fbff 100%
        );
    }


    /* =========================================
       SIDEBAR
    ========================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #031b33 0%,
            #063b63 50%,
            #075b87 100%
        );
    }


    section[data-testid="stSidebar"] > div {
        background: transparent;
    }


    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }


    /* =========================================
       TIÊU ĐỀ
    ========================================= */

    h1 {
        color: #06345a !important;
        font-weight: 800 !important;
    }


    h2 {
        color: #074b78 !important;
        font-weight: 800 !important;
    }


    h3 {
        color: #075b87 !important;
        font-weight: 750 !important;
    }


    /* =========================================
       HERO
    ========================================= */

    .hero-box {
        background: linear-gradient(
            135deg,
            #032b4d 0%,
            #075b8c 50%,
            #0b98ce 100%
        );

        padding: 35px;

        border-radius: 25px;

        margin-bottom: 25px;

        box-shadow:
            0 12px 30px
            rgba(3, 43, 77, 0.25);

        color: white;

        position: relative;

        overflow: hidden;
    }


    .hero-title {
        color: white;

        font-size: 28px;

        font-weight: 800;

        line-height: 1.4;

        margin-bottom: 15px;
    }


    .hero-text {
        color: rgba(255,255,255,0.9);

        font-size: 15px;

        line-height: 1.7;
    }


    .hero-icon {
        position: absolute;

        right: 35px;

        top: 25px;

        font-size: 85px;

        opacity: 0.16;
    }


    /* =========================================
       CARD
    ========================================= */

    .info-card {
        background: white;

        padding: 22px;

        border-radius: 18px;

        border: 1px solid #dce8f3;

        box-shadow:
            0 6px 20px
            rgba(8,43,76,0.07);

        margin-bottom: 18px;

        transition: 0.25s;
    }


    .info-card:hover {
        transform: translateY(-4px);

        box-shadow:
            0 12px 28px
            rgba(8,43,76,0.12);
    }


    .card-icon {
        font-size: 38px;

        margin-bottom: 10px;
    }


    .card-title {
        color: #074b78;

        font-size: 17px;

        font-weight: 800;

        margin-bottom: 8px;
    }


    .card-text {
        color: #63778a;

        font-size: 14px;

        line-height: 1.6;
    }


    /* =========================================
       METRIC
    ========================================= */

    div[data-testid="stMetric"] {
        background: white;

        border: 1px solid #d9e7f2;

        padding: 18px;

        border-radius: 16px;

        box-shadow:
            0 6px 18px
            rgba(8,43,76,0.07);
    }


    div[data-testid="stMetricLabel"] {
        color: #60758a !important;

        font-weight: 700 !important;
    }


    div[data-testid="stMetricValue"] {
        color: #06456f !important;

        font-weight: 800 !important;
    }


    /* =========================================
       BUTTON
    ========================================= */

    .stButton > button {
        width: 100%;

        min-height: 46px;

        border-radius: 12px;

        border: none;

        color: white;

        font-size: 14px;

        font-weight: 800;

        background: linear-gradient(
            135deg,
            #07518a,
            #0a8bc4
        );

        box-shadow:
            0 6px 16px
            rgba(7,81,138,0.2);

        transition: 0.25s;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 10px 24px
            rgba(7,81,138,0.3);
    }


    /* =========================================
       KẾT LUẬN
    ========================================= */

    .status-good {
        background: #e8f8ef;

        border-left: 7px solid #1c9b58;

        padding: 20px;

        border-radius: 14px;

        color: #17663b;

        font-size: 19px;

        font-weight: 800;
    }


    .status-warning {
        background: #fff7df;

        border-left: 7px solid #e0a000;

        padding: 20px;

        border-radius: 14px;

        color: #765800;

        font-size: 19px;

        font-weight: 800;
    }


    .status-bad {
        background: #fff0f0;

        border-left: 7px solid #d43d3d;

        padding: 20px;

        border-radius: 14px;

        color: #852323;

        font-size: 19px;

        font-weight: 800;
    }


    /* =========================================
       FOOTER
    ========================================= */

    .footer {
        text-align: center;

        color: #71869b;

        padding: 25px;

        font-size: 13px;
    }


    /* =========================================
       INPUT
    ========================================= */

    input,
    textarea {
        border-radius: 10px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    # LOGO
    try:

        st.image(
            "logo.jpg",
            use_container_width=True
        )

    except Exception:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:65px;
                padding:15px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )


    # TÊN HỆ THỐNG
    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:20px;
            font-weight:800;
            line-height:1.5;
            padding:12px 5px;
        ">
            🏦 HỆ THỐNG<br>
            THẨM ĐỊNH TÍN DỤNG
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:12px;
            color:#d9edf7 !important;
            line-height:1.6;
            margin-bottom:15px;
        ">
            HỖ TRỢ THẨM ĐỊNH<br>
            CHO VAY DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown(
        """
        <div style="
            font-size:15px;
            font-weight:800;
            margin-bottom:10px;
        ">
            📋 DANH MỤC THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )


    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Tài chính & Khả năng trả nợ",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )


    st.divider()


    st.markdown(
        """
        <div style="
            text-align:center;
            color:#cfe7f5 !important;
            font-size:12px;
            line-height:1.8;
        ">
            🔐 HỆ THỐNG HỖ TRỢ NỘI BỘ
            <br>
            📊 THẨM ĐỊNH TÍN DỤNG SƠ BỘ
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    # HERO
    st.markdown(
        """
        <div class="hero-box">

            <div class="hero-icon">
                🏦
            </div>

            <div class="hero-title">
                🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH<br>
                CHO VAY DOANH NGHIỆP
            </div>

            <div class="hero-text">
                📋 Quản lý hồ sơ doanh nghiệp
                &nbsp; • &nbsp;
                💰 Phân tích tài chính
                &nbsp; • &nbsp;
                📈 Đánh giá khả năng trả nợ
                &nbsp; • &nbsp;
                🏠 Phân tích tài sản bảo đảm
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("👋 Chào mừng bạn đến với hệ thống")


    st.write(
        """
        Hệ thống hỗ trợ cán bộ tín dụng hoặc người sử dụng
        thực hiện **thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp**,
        tổng hợp thông tin tài chính, khoản vay, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )


    st.divider()


    # TRẠNG THÁI
    st.subheader("📊 TRẠNG THÁI HỒ SƠ")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "🏢 Hồ sơ doanh nghiệp",
            "Đã nhập"
            if st.session_state.da_luu_ho_so
            else "Chưa nhập"
        )


    with c2:

        st.metric(
            "⚖️ Điều kiện vay",
            "Đã kiểm tra"
            if st.session_state.nang_luc_phap_ly != "Chưa đánh giá"
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
            "Sẵn sàng"
            if (
                st.session_state.da_luu_ho_so
                and st.session_state.da_phan_tich_tc
                and st.session_state.da_phan_tich_vay
                and st.session_state.da_phan_tich_tsdb
            )
            else "Chưa đủ dữ liệu"
        )


    st.divider()


    # QUY TRÌNH
    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown(
            """
            <div class="info-card">

                <div class="card-icon">
                    🏢
                </div>

                <div class="card-title">
                    01 | HỒ SƠ DOANH NGHIỆP
                </div>

                <div class="card-text">
                    Nhập thông tin doanh nghiệp,
                    ngành nghề, mục đích vay
                    và phương án sử dụng vốn.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="info-card">

                <div class="card-icon">
                    ⚖️
                </div>

                <div class="card-title">
                    02 | ĐIỀU KIỆN VAY
                </div>

                <div class="card-text">
                    Kiểm tra năng lực pháp lý,
                    mục đích vay, phương án
                    và khả năng trả nợ.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="info-card">

                <div class="card-icon">
                    💰
                </div>

                <div class="card-title">
                    03 | PHÂN TÍCH TÀI CHÍNH
                </div>

                <div class="card-text">
                    Phân tích LNST, ROA, ROE,
                    tỷ lệ nợ, DSCR và
                    tài sản bảo đảm.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="info-card">

                <div class="card-icon">
                    📊
                </div>

                <div class="card-title">
                    04 | KẾT QUẢ THẨM ĐỊNH
                </div>

                <div class="card-text">
                    Tổng hợp dữ liệu và đưa ra
                    kết luận thẩm định sơ bộ
                    hỗ trợ quyết định tín dụng.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.warning(
        """
        ⚠️ **LƯU Ý:** Kết quả của hệ thống chỉ mang tính chất
        **hỗ trợ thẩm định sơ bộ** và không thay thế quyết định
        tín dụng chính thức của ngân hàng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY")

    st.caption(
        "📋 Nhập thông tin doanh nghiệp và đánh giá sơ bộ điều kiện vay vốn"
    )


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader("🏢 1️⃣ THÔNG TIN DOANH NGHIỆP")


    c1, c2 = st.columns(2)


    with c1:

        ten_dn = st.text_input(
            "🏷️ Tên doanh nghiệp",
            value=st.session_state.ten_dn
        )


        ma_so = st.text_input(
            "🆔 Mã số doanh nghiệp",
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
            "🏭 Ngành nghề kinh doanh",
            danh_sach_nganh,
            index=danh_sach_nganh.index(
                st.session_state.nganh_nghe
            )
        )


        thoi_gian_hd = st.number_input(
            "📅 Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )


    # =====================================================
    # MỤC ĐÍCH VAY
    # =====================================================

    st.subheader("💳 2️⃣ MỤC ĐÍCH VÀ PHƯƠNG ÁN VAY")


    muc_dich_list = [
        "Bổ sung vốn lưu động",
        "Mua nguyên vật liệu",
        "Đầu tư máy móc thiết bị",
        "Mở rộng sản xuất",
        "Mua tài sản cố định",
        "Khác"
    ]


    muc_dich_vay = st.selectbox(
        "🎯 Mục đích sử dụng vốn",
        muc_dich_list,
        index=muc_dich_list.index(
            st.session_state.muc_dich_vay
        )
    )


    phuong_an = st.text_area(
        "📝 Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập nội dung phương án kinh doanh, nhu cầu vay và cách sử dụng vốn..."
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


    # =====================================================
    # ĐIỀU KIỆN VAY
    # =====================================================

    st.subheader("⚖️ 3️⃣ KIỂM TRA ĐIỀU KIỆN VAY VỐN")


    st.info(
        """
        🔍 Đánh giá sơ bộ các điều kiện liên quan đến hồ sơ vay vốn.
        Kết quả thực tế cần căn cứ hồ sơ pháp lý, phương án kinh doanh,
        khả năng trả nợ và quy định nội bộ của tổ chức tín dụng.
        """
    )


    options = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "⚖️ Năng lực pháp lý phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )


        st.session_state.muc_dich_hop_phap = st.selectbox(
            "🎯 Mục đích vay vốn hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich_hop_phap
            )
        )


        st.session_state.phuong_an_su_dung_von = st.selectbox(
            "💰 Có phương án sử dụng vốn?",
            options,
            index=options.index(
                st.session_state.phuong_an_su_dung_von
            )
        )


        st.session_state.phuong_an_kha_thi = st.selectbox(
            "📈 Phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )


    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "💳 Có khả năng tài chính trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )


        st.session_state.su_dung_von_dung_muc_dich = st.selectbox(
            "🔐 Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.su_dung_von_dung_muc_dich
            )
        )


        st.session_state.tra_no_dung_han = st.selectbox(
            "⏰ Cam kết trả nợ đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )


    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich_hop_phap,

            st.session_state.phuong_an_su_dung_von,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no,

            st.session_state.su_dung_von_dung_muc_dich,

            st.session_state.tra_no_dung_han

        ]


        if "Không" in dieu_kien:

            st.error(
                "🔴 CÓ ÍT NHẤT MỘT ĐIỀU KIỆN ĐƯỢC ĐÁNH GIÁ LÀ KHÔNG."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 CHƯA THỂ KẾT LUẬN VÌ CÒN ĐIỀU KIỆN CHƯA ĐƯỢC ĐÁNH GIÁ."
            )

        else:

            st.success(
                "🟢 CÁC ĐIỀU KIỆN SƠ BỘ HIỆN ĐANG ĐƯỢC ĐÁNH GIÁ LÀ CÓ."
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title(
        "💰 PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )


    st.caption(
        "💵 Đơn vị nhập liệu: triệu đồng"
    )


    # =====================================================
    # TÀI CHÍNH
    # =====================================================

    st.subheader("📈 1️⃣ PHÂN TÍCH TÀI CHÍNH DOANH NGHIỆP")


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
            "💧 Dòng tiền từ hoạt động kinh doanh / tháng",
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

        st.divider()

        st.subheader("📊 KẾT QUẢ PHÂN TÍCH TÀI CHÍNH")


        c1, c2, c3, c4 = st.columns(4)


        c1.metric(
            "📈 ROA",
            f"{st.session_state.roa:.2f}%"
        )


        c2.metric(
            "💼 ROE",
            f"{st.session_state.roe:.2f}%"
        )


        c3.metric(
            "📌 Tỷ lệ nợ",
            f"{st.session_state.ty_le_no:.2f}%"
        )


        c4.metric(
            "💰 LNST",
            f"{st.session_state.lnst:,.2f}"
        )


    st.divider()


    # =====================================================
    # KHOẢN VAY
    # =====================================================

    st.subheader("💳 2️⃣ THÔNG TIN KHOẢN VAY")


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
            "💵 Gốc / tháng",
            f"{st.session_state.tien_goc_thang:,.2f}"
        )


        c2.metric(
            "📈 Lãi tháng đầu",
            f"{st.session_state.tien_lai_thang:,.2f}"
        )


        c3.metric(
            "💳 Tổng nghĩa vụ / tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )


    st.divider()


    # =====================================================
    # DSCR
    # =====================================================

    st.subheader("📈 3️⃣ KHẢ NĂNG TRẢ NỢ - DSCR")


    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng nhập và tính khoản vay trước."
        )

    else:

        c1, c2 = st.columns(2)


        with c1:

            st.metric(
                "💧 Dòng tiền kinh doanh / tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )


        with c2:

            st.metric(
                "💳 Nghĩa vụ trả nợ / tháng",
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


                st.metric(
                    "📊 DSCR",
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
    # TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader("🏠 4️⃣ TÀI SẢN BẢO ĐẢM")


    st.info(
        """
        🏠 Tài sản bảo đảm là một nội dung hỗ trợ trong thẩm định.
        Cần xem xét loại tài sản, quyền sở hữu, giá trị định giá,
        khả năng thanh khoản và chính sách cho vay của ngân hàng.
        """
    )


    options_tsdb = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    st.session_state.co_tsdb = st.selectbox(
        "🏠 Khoản vay có tài sản bảo đảm?",
        options_tsdb,
        index=options_tsdb.index(
            st.session_state.co_tsdb
        )
    )


    st.session_state.gia_tri_tsdb = st.number_input(
        "💎 Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
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


            st.success(
                "✅ Phân tích tài sản bảo đảm thành công."
            )


            st.metric(
                "📊 Tỷ lệ LTV",
                f"{st.session_state.ltv:.2f}%"
            )


            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ở mức tương đối thấp theo tiêu chí hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm theo dữ liệu nhập."
                )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP"
    )


    st.info(
        """
        🔎 Kết quả được tổng hợp từ thông tin hồ sơ,
        điều kiện vay, tình hình tài chính, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )


    # KIỂM TRA DỮ LIỆU

    missing = []


    if not st.session_state.da_luu_ho_so:

        missing.append("🏢 Hồ sơ doanh nghiệp")


    if not st.session_state.da_phan_tich_tc:

        missing.append("💰 Phân tích tài chính")


    if not st.session_state.da_phan_tich_vay:

        missing.append("💳 Thông tin khoản vay")


    if not st.session_state.da_phan_tich_tsdb:

        missing.append("🏠 Tài sản bảo đảm")


    if len(missing) > 0:

        st.warning(
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ ĐƯA RA KẾT LUẬN."
        )


        st.write(
            "📋 Vui lòng hoàn thành:"
        )


        for item in missing:

            st.write(
                f"🔸 {item}"
            )


        st.stop()


    # ĐIỀU KIỆN VAY

    dieu_kien = [

        st.session_state.nang_luc_phap_ly,

        st.session_state.muc_dich_hop_phap,

        st.session_state.phuong_an_su_dung_von,

        st.session_state.phuong_an_kha_thi,

        st.session_state.kha_nang_tra_no,

        st.session_state.su_dung_von_dung_muc_dich,

        st.session_state.tra_no_dung_han

    ]


    co_dieu_kien_khong = "Không" in dieu_kien

    co_chua_danh_gia = "Chưa đánh giá" in dieu_kien


    # THÔNG TIN DOANH NGHIỆP

    st.subheader("🏢 THÔNG TIN DOANH NGHIỆP")


    c1, c2, c3 = st.columns(3)


    c1.metric(
        "🏷️ Doanh nghiệp",
        st.session_state.ten_dn
    )


    c2.metric(
        "🏭 Ngành nghề",
        st.session_state.nganh_nghe
    )


    c3.metric(
        "📅 Thời gian hoạt động",
        f"{st.session_state.thoi_gian_hd} năm"
    )


    st.divider()


    # CHỈ TIÊU

    st.subheader("📊 CÁC CHỈ TIÊU THẨM ĐỊNH")


    c1, c2, c3, c4 = st.columns(4)


    c1.metric(
        "💰 LNST",
        f"{st.session_state.lnst:,.2f}"
    )


    c2.metric(
        "📈 ROA",
        f"{st.session_state.roa:.2f}%"
    )


    c3.metric(
        "💼 ROE",
        f"{st.session_state.roe:.2f}%"
    )


    c4.metric(
        "📌 Tỷ lệ nợ",
        f"{st.session_state.ty_le_no:.2f}%"
    )


    c1, c2, c3 = st.columns(3)


    c1.metric(
        "📊 DSCR",
        (
            f"{st.session_state.dscr:.2f} lần"
            if st.session_state.dscr is not None
            else "Chưa tính"
        )
    )


    c2.metric(
        "🏠 LTV",
        (
            f"{st.session_state.ltv:.2f}%"
            if st.session_state.ltv is not None
            else "Không áp dụng"
        )
    )


    c3.metric(
        "💳 Số tiền vay",
        f"{st.session_state.so_tien_vay:,.2f}"
    )


    st.divider()


    # =====================================================
    # KẾT LUẬN
    # =====================================================

    st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")


    if co_dieu_kien_khong:

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
            Hồ sơ đang có ít nhất một điều kiện vay vốn được đánh giá
            là Không. Cần xác định rõ nguyên nhân, bổ sung hồ sơ hoặc
            điều chỉnh phương án trước khi xem xét tiếp.
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
            Chưa đủ cơ sở để đưa ra kết luận thẩm định sơ bộ.
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
            Hồ sơ đáp ứng các điều kiện sơ bộ đang được đánh giá.
            Doanh nghiệp có kết quả kinh doanh dương, ROA và ROE dương,
            đồng thời dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ theo
            chỉ tiêu DSCR.

            Hồ sơ có thể được chuyển sang bước thẩm định chi tiết,
            bao gồm kiểm tra hồ sơ pháp lý, CIC, lịch sử tín dụng,
            báo cáo tài chính, phương án kinh doanh, dòng tiền,
            tài sản bảo đảm và các quy định nội bộ của ngân hàng.
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
            Hồ sơ chưa có đủ các tín hiệu tích cực theo mô hình
            hỗ trợ hiện tại. Cần thẩm định bổ sung tình hình tài chính,
            dòng tiền, khả năng trả nợ, phương án kinh doanh,
            lịch sử tín dụng và tài sản bảo đảm.
            """
        )


    st.divider()


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")


    ket_qua = []


    ket_qua.append([
        "⚖️ Năng lực pháp lý",
        "Đạt"
        if st.session_state.nang_luc_phap_ly == "Có"
        else "Cần xem xét",
        st.session_state.nang_luc_phap_ly
    ])


    ket_qua.append([
        "🎯 Mục đích vay vốn",
        "Đạt"
        if st.session_state.muc_dich_hop_phap == "Có"
        else "Cần xem xét",
        st.session_state.muc_dich_hop_phap
    ])


    ket_qua.append([
        "💰 Phương án sử dụng vốn",
        "Đạt"
        if st.session_state.phuong_an_su_dung_von == "Có"
        else "Cần xem xét",
        st.session_state.phuong_an_su_dung_von
    ])


    ket_qua.append([
        "📈 Tính khả thi phương án",
        "Đạt"
        if st.session_state.phuong_an_kha_thi == "Có"
        else "Cần xem xét",
        st.session_state.phuong_an_kha_thi
    ])


    ket_qua.append([
        "💳 Khả năng tài chính trả nợ",
        "Đạt"
        if st.session_state.kha_nang_tra_no == "Có"
        else "Cần xem xét",
        st.session_state.kha_nang_tra_no
    ])


    ket_qua.append([
        "💰 Lợi nhuận sau thuế",
        "Tích cực"
        if st.session_state.lnst > 0
        else "Cần xem xét",
        f"{st.session_state.lnst:,.2f} triệu đồng"
    ])


    ket_qua.append([
        "📈 ROA",
        "Tích cực"
        if st.session_state.roa > 0
        else "Cần xem xét",
        f"{st.session_state.roa:.2f}%"
    ])


    ket_qua.append([
        "💼 ROE",
        "Tích cực"
        if st.session_state.roe > 0
        else "Cần xem xét",
        f"{st.session_state.roe:.2f}%"
    ])


    ket_qua.append([
        "📌 Tỷ lệ nợ",
        "Tham khảo",
        f"{st.session_state.ty_le_no:.2f}%"
    ])


    if st.session_state.dscr is not None:

        ket_qua.append([
            "📊 DSCR",
            "Tích cực"
            if st.session_state.dscr >= 1
            else "Cần xem xét",
            f"{st.session_state.dscr:.2f} lần"
        ])


    if st.session_state.ltv is not None:

        ket_qua.append([
            "🏠 LTV",
            "Tham khảo",
            f"{st.session_state.ltv:.2f}%"
        ])

    else:

        ket_qua.append([
            "🏠 Tài sản bảo đảm",
            "Không áp dụng",
            "Khoản vay không có TSĐB"
        ])


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
        ⚠️ **LƯU Ý QUAN TRỌNG**

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ chỉ là các chỉ tiêu
        hỗ trợ phân tích tín dụng, không phải là căn cứ duy nhất
        để quyết định cho vay.

        Quyết định tín dụng thực tế cần xem xét tổng thể:
        hồ sơ pháp lý doanh nghiệp, mục đích vay vốn, phương án
        kinh doanh, báo cáo tài chính, dòng tiền, lịch sử tín dụng,
        nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm và chính sách
        tín dụng của ngân hàng.

        Kết quả của ứng dụng chỉ có giá trị hỗ trợ thẩm định sơ bộ.
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

        📊 Phân tích tài chính
        &nbsp; • &nbsp;
        💳 Khả năng trả nợ
        &nbsp; • &nbsp;
        🏠 Tài sản bảo đảm

        <br><br>

        🔐 Công cụ hỗ trợ thẩm định sơ bộ hồ sơ tín dụng

    </div>
    """,
    unsafe_allow_html=True
)
