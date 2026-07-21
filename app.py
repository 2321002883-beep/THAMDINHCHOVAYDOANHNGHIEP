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
# 2. SESSION STATE
# =========================================================

default_values = {

    # =========================
    # HỒ SƠ DOANH NGHIỆP
    # =========================

    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,

    # =========================
    # ĐIỀU KIỆN VAY
    # =========================

    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # =========================
    # TÀI CHÍNH
    # =========================

    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # =========================
    # KHOẢN VAY
    # =========================

    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,
    "tong_nghia_vu": None,

    # =========================
    # TÀI SẢN BẢO ĐẢM
    # =========================

    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None
}


for key, value in default_values.items():

    if key not in st.session_state:

        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN PREMIUM
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN CHÍNH
    ================================= */

    .stApp {

        background:
        linear-gradient(
            135deg,
            #f7faff 0%,
            #eef4fb 45%,
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
            #0b2d52 50%,
            #07345c 100%
        );

        border-right: 1px solid rgba(255,255,255,0.08);

    }


    section[data-testid="stSidebar"] * {

        color: white !important;

    }


    section[data-testid="stSidebar"] .stRadio label {

        padding: 10px 12px;

        border-radius: 10px;

        transition: all 0.2s ease;

    }


    section[data-testid="stSidebar"] .stRadio label:hover {

        background: rgba(255,255,255,0.12);

        transform: translateX(4px);

    }


    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {

        color: #08264b !important;

        font-weight: 800 !important;

        letter-spacing: -0.5px;

    }


    h2 {

        color: #0b3b6f !important;

        font-weight: 750 !important;

    }


    h3 {

        color: #12518a !important;

        font-weight: 700 !important;

    }


    /* ================================
       CARD
    ================================= */

    .premium-card {

        background: rgba(255,255,255,0.95);

        padding: 24px;

        border-radius: 20px;

        border: 1px solid #e3ebf5;

        box-shadow:
        0 10px 30px rgba(8,38,75,0.08);

        margin-bottom: 20px;

    }


    /* ================================
       HERO
    ================================= */

    .hero {

        background:
        linear-gradient(
            135deg,
            #071a33,
            #0b4275,
            #087ea4
        );

        padding: 40px;

        border-radius: 24px;

        color: white;

        margin-bottom: 25px;

        box-shadow:
        0 15px 35px rgba(7,26,51,0.22);

    }


    .hero h1 {

        color: white !important;

        font-size: 36px;

        margin-bottom: 12px;

    }


    .hero p {

        color: rgba(255,255,255,0.88);

        font-size: 16px;

    }


    /* ================================
       KPI CARD
    ================================= */

    .kpi-card {

        background: white;

        padding: 22px;

        border-radius: 18px;

        border: 1px solid #e4edf7;

        box-shadow:
        0 8px 25px rgba(8,38,75,0.07);

        min-height: 135px;

    }


    .kpi-title {

        color: #64748b;

        font-size: 14px;

        font-weight: 600;

    }


    .kpi-value {

        color: #08264b;

        font-size: 23px;

        font-weight: 800;

        margin-top: 12px;

    }


    /* ================================
       PROCESS CARD
    ================================= */

    .process-card {

        background: white;

        padding: 20px;

        border-radius: 18px;

        border: 1px solid #e3ebf5;

        text-align: center;

        min-height: 200px;

        box-shadow:
        0 7px 20px rgba(8,38,75,0.06);

    }


    .process-number {

        font-size: 28px;

        font-weight: 800;

        color: #087ea4;

    }


    .process-title {

        font-size: 16px;

        font-weight: 700;

        color: #08264b;

        margin-top: 8px;

    }


    /* ================================
       NÚT
    ================================= */

    .stButton > button {

        background:
        linear-gradient(
            135deg,
            #0b4275,
            #087ea4
        );

        color: white;

        border: none;

        border-radius: 12px;

        padding: 10px 22px;

        font-weight: 700;

    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
        0 8px 20px rgba(8,126,164,0.25);

    }


    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {

        background: white;

        padding: 20px;

        border-radius: 18px;

        border: 1px solid #e2eaf4;

        box-shadow:
        0 8px 25px rgba(8,38,75,0.06);

    }


    /* ================================
       FOOTER
    ================================= */

    .footer {

        text-align: center;

        padding: 25px;

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
            padding:20px 5px;
        ">

        <div style="
            font-size:48px;
        ">
        🏦
        </div>

        <h2 style="
            color:white !important;
            font-size:18px;
            line-height:1.4;
        ">
        HỆ THỐNG THẨM ĐỊNH
        </h2>

        <p style="
            color:#b8d7f2 !important;
            font-size:12px;
        ">
        CHO VAY DOANH NGHIỆP
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    menu = st.radio(
        "ĐIỀU HƯỚNG HỆ THỐNG",
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
            border-radius:14px;
            text-align:center;
        ">

        <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH</b>

        <br>

        <small>
        Phân tích và đánh giá hồ sơ vay vốn doanh nghiệp
        </small>

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


    # =====================================================
    # TRẠNG THÁI HỒ SƠ
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)


    # HỒ SƠ

    with c1:

        if st.session_state.ten_dn:

            ho_so_status = "Đã nhập"

        else:

            ho_so_status = "Chưa nhập"


        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-title">
            🏢 HỒ SƠ DOANH NGHIỆP
            </div>

            <div class="kpi-value">
            {ho_so_status}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # TÀI CHÍNH

    with c2:

        if st.session_state.roa is not None:

            tai_chinh_status = "Đã phân tích"

        else:

            tai_chinh_status = "Chưa phân tích"


        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-title">
            💰 PHÂN TÍCH TÀI CHÍNH
            </div>

            <div class="kpi-value">
            {tai_chinh_status}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # KHOẢN VAY

    with c3:

        if st.session_state.tong_nghia_vu is not None:

            khoan_vay_status = "Đã phân tích"

        else:

            khoan_vay_status = "Chưa thiết lập"


        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-title">
            💳 KHOẢN VAY
            </div>

            <div class="kpi-value">
            {khoan_vay_status}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ĐIỂM

    with c4:

        if st.session_state.roa is not None:

            diem_status = "Tối đa 90 điểm"

        else:

            diem_status = "Chưa đánh giá"


        st.markdown(
            f"""
            <div class="kpi-card">

            <div class="kpi-title">
            🎯 MÔ HÌNH THẨM ĐỊNH
            </div>

            <div class="kpi-value">
            {diem_status}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


    # =====================================================
    # QUY TRÌNH
    # =====================================================

    st.subheader(
        "🚀 QUY TRÌNH THẨM ĐỊNH"
    )


    c1, c2, c3, c4 = st.columns(4)


    process_data = [

        (
            c1,
            "01",
            "🏢",
            "HỒ SƠ DOANH NGHIỆP",
            "Nhập thông tin pháp lý, ngành nghề và thời gian hoạt động."
        ),

        (
            c2,
            "02",
            "💰",
            "PHÂN TÍCH TÀI CHÍNH",
            "Đánh giá LNST, ROA, ROE và tỷ lệ nợ."
        ),

        (
            c3,
            "03",
            "💳",
            "KHẢ NĂNG TRẢ NỢ",
            "Phân tích dòng tiền và nghĩa vụ trả nợ."
        ),

        (
            c4,
            "04",
            "📊",
            "KẾT QUẢ THẨM ĐỊNH",
            "Tổng hợp các tiêu chí và đưa ra kết quả hỗ trợ."
        )

    ]


    for col, number, icon, title, desc in process_data:

        with col:

            st.markdown(
                f"""
                <div class="process-card">

                <div class="process-number">
                {number}
                </div>

                <div style="font-size:30px;">
                {icon}
                </div>

                <div class="process-title">
                {title}
                </div>

                <p style="
                    font-size:13px;
                    color:#64748b;
                    line-height:1.5;
                ">
                {desc}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )


    st.divider()


    st.subheader(
        "📌 TRẠNG THÁI HỒ SƠ HIỆN TẠI"
    )


    if st.session_state.ten_dn:

        st.success(
            f"🏢 Doanh nghiệp đang được thẩm định: "
            f"**{st.session_state.ten_dn}**"
        )

    else:

        st.info(
            "📋 Chưa có thông tin doanh nghiệp. "
            "Vui lòng bắt đầu tại mục **Hồ sơ doanh nghiệp**."
        )


    st.warning(
        "⚠️ Kết quả của hệ thống chỉ mang tính chất hỗ trợ "
        "thẩm định, không thay thế quyết định tín dụng thực tế."
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title(
        "🏢 HỒ SƠ DOANH NGHIỆP"
    )


    st.caption(
        "Nhập thông tin nhận diện và hồ sơ cơ bản của doanh nghiệp."
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )


    st.subheader(
        "📋 THÔNG TIN DOANH NGHIỆP"
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


        st.session_state.thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )


    st.subheader(
        "💳 MỤC ĐÍCH VAY"
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
        placeholder="Nhập mô tả chi tiết phương án sử dụng vốn..."
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
    ):

        if st.session_state.ten_dn == "":

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                "✅ Đã lưu thông tin hồ sơ doanh nghiệp."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    )


    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "điều kiện vay vốn. Đây không phải là toàn bộ điều kiện "
        "pháp lý bắt buộc áp dụng chung cho mọi khoản vay."
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )


    st.subheader(
        "1️⃣ ĐIỀU KIỆN CƠ BẢN"
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
        "</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )


    st.subheader(
        "2️⃣ CAM KẾT CỦA KHÁCH HÀNG"
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


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    st.success(
        "✅ Thông tin điều kiện vay vốn đã được cập nhật."
    )


# =========================================================
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title(
        "💰 PHÂN TÍCH TÀI CHÍNH"
    )


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
    )


    st.subheader(
        "📊 NHẬP SỐ LIỆU TÀI CHÍNH"
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


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    if st.button(
        "📊 PHÂN TÍCH TÀI CHÍNH"
    ):

        if st.session_state.tong_tai_san <= 0:

            st.error(
                "Tổng tài sản phải lớn hơn 0."
            )

        elif st.session_state.von_chu_so_huu <= 0:

            st.error(
                "Vốn chủ sở hữu phải lớn hơn 0."
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


        st.subheader(
            "📈 KẾT QUẢ PHÂN TÍCH"
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
            chart.set_index("Chỉ tiêu")
        )


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title(
        "💳 THÔNG TIN KHOẢN VAY"
    )


    st.caption(
        "Đơn vị: triệu đồng | Lãi suất: %/năm"
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
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


    st.markdown(
        "</div>",
        unsafe_allow_html=True
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


        st.divider()


        c1, c2, c3 = st.columns(3)


        c1.metric(
            "GỐC / THÁNG",
            f"{tien_goc:,.2f}"
        )


        c2.metric(
            "LÃI THÁNG ĐẦU",
            f"{tien_lai:,.2f}"
        )


        c3.metric(
            "TỔNG NGHĨA VỤ / THÁNG",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )


        st.success(
            "✅ Đã tính toán nghĩa vụ trả nợ."
        )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title(
        "🏠 TÀI SẢN BẢO ĐẢM"
    )


    st.info(
        "LTV là chỉ tiêu hỗ trợ phân tích tín dụng, "
        "không phải ngưỡng pháp lý chung áp dụng cho mọi khoản vay."
    )


    st.markdown(
        '<div class="premium-card">',
        unsafe_allow_html=True
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


    st.markdown(
        "</div>",
        unsafe_allow_html=True
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
                "Giá trị TSĐB phải lớn hơn 0."
            )


        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "Vui lòng nhập số tiền vay trước."
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
                    "🟡 Cần xem xét thêm chất lượng và tính thanh khoản của TSĐB."
                )


            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."
                )


# =========================================================
# 11. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH TÍN DỤNG"
    )


    st.caption(
        "Tổng hợp kết quả phân tích tài chính, khả năng trả nợ và tài sản bảo đảm."
    )


    if st.session_state.roa is None:

        st.warning(
            "⚠️ Chưa có dữ liệu phân tích tài chính."
        )


        st.info(
            "Vui lòng vào mục 'Phân tích tài chính' "
            "và thực hiện phân tích trước."
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


        # KHẢ NĂNG TRẢ NỢ

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


        # =================================================
        # TỔNG ĐIỂM
        # =================================================

        ty_le_diem = diem / 90 * 100


        st.divider()


        st.subheader(
            "🎯 TỔNG QUAN KẾT QUẢ"
        )


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


        st.progress(
            min(ty_le_diem / 100, 1.0)
        )


        st.write(
            f"Mức độ đạt điểm: **{ty_le_diem:.1f}%**"
        )


        st.divider()


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH"
        )


        if ty_le_diem >= 80:

            st.success(
                f"🟢 ĐỀ XUẤT CHO VAY — "
                f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
            )


            st.info(
                "Hồ sơ có kết quả tương đối tích cực "
                "theo mô hình hỗ trợ. Có thể chuyển sang "
                "bước thẩm định tín dụng chi tiết."
            )


        elif ty_le_diem >= 60:

            st.warning(
                f"🟡 CẦN THẨM ĐỊNH BỔ SUNG — "
                f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
            )


            st.info(
                "Cần xem xét thêm dòng tiền, khả năng trả nợ, "
                "lịch sử tín dụng, phương án sử dụng vốn và TSĐB."
            )


        else:

            st.error(
                f"🔴 CHƯA ĐỀ XUẤT CHO VAY — "
                f"Doanh nghiệp đạt mức đánh giá {ty_le_diem:.1f}%."
            )


            st.info(
                "Hồ sơ còn nhiều tiêu chí chưa đạt "
                "theo mô hình đánh giá. Cần xem xét "
                "bổ sung hoặc điều chỉnh phương án vay."
            )


        st.divider()


        # =================================================
        # BẢNG CHI TIẾT
        # =================================================

        st.subheader(
            "📋 CHI TIẾT KẾT QUẢ THẨM ĐỊNH"
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


        st.divider()


        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả trên chỉ mang tính chất hỗ trợ thẩm định.

            ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu hỗ trợ
            phân tích tín dụng, không phải điều kiện pháp lý
            bắt buộc chung cho mọi doanh nghiệp.

            Quyết định cho vay thực tế phụ thuộc vào hồ sơ,
            lịch sử tín dụng, dòng tiền, phương án kinh doanh,
            tài sản bảo đảm và chính sách của từng tổ chức tín dụng.
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

    Phân tích tài chính • Khả năng trả nợ • Tài sản bảo đảm

    <br>

    <small>
    Kết quả chỉ mang tính chất hỗ trợ thẩm định tín dụng
    </small>

    </div>
    """,
    unsafe_allow_html=True
)
