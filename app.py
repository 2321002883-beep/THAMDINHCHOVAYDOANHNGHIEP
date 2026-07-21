import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Hệ thống thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. ĐƯỜNG DẪN LOGO
# =========================================================

LOGO_PATH = Path(__file__).parent / "logo.png"


# =========================================================
# 3. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {

    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "Bổ sung vốn lưu động",
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

    # Tài sản bảo đảm
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_phan_tich_tai_chinh": False,
    "da_phan_tich_khoan_vay": False,
    "da_phan_tich_tsdb": False
}


for key, value in default_values.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 4. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       NỀN CHÍNH
    ============================== */

    .stApp {
        background: #f4f7fb;
    }


    /* ==============================
       SIDEBAR
    ============================== */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #071a33 0%,
            #0b2d52 50%,
            #0d3b66 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }


    /* ==============================
       TIÊU ĐỀ
    ============================== */

    .main-title {
        font-size: 34px;
        font-weight: 900;
        color: #08244a;
        line-height: 1.2;
    }

    .main-subtitle {
        font-size: 17px;
        color: #64748b;
        margin-top: 8px;
    }


    /* ==============================
       HERO
    ============================== */

    .hero-box {
        background: linear-gradient(
            135deg,
            #0b2d52,
            #1769aa
        );

        padding: 35px;
        border-radius: 22px;

        color: white;

        box-shadow:
            0 10px 30px
            rgba(11,45,82,0.20);

        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 32px;
        font-weight: 900;
        line-height: 1.3;
    }

    .hero-sub {
        font-size: 16px;
        margin-top: 12px;
        opacity: 0.9;
    }


    /* ==============================
       CARD
    ============================== */

    .custom-card {
        background: white;

        padding: 22px;

        border-radius: 18px;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 5px 20px
            rgba(15,23,42,0.06);

        height: 100%;
    }

    .card-icon {
        font-size: 35px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 800;
        color: #0b2d52;
        margin-top: 8px;
    }

    .card-text {
        color: #64748b;
        font-size: 14px;
        margin-top: 8px;
    }


    /* ==============================
       SECTION TITLE
    ============================== */

    .section-title {
        font-size: 22px;
        font-weight: 800;
        color: #0b2d52;
        margin-top: 20px;
        margin-bottom: 15px;
    }


    /* ==============================
       METRIC
    ============================== */

    div[data-testid="stMetric"] {

        background: white;

        border-radius: 16px;

        border: 1px solid #e2e8f0;

        padding: 18px;

        box-shadow:
            0 5px 15px
            rgba(15,23,42,0.05);
    }


    /* ==============================
       BUTTON
    ============================== */

    .stButton > button {

        width: 100%;

        border-radius: 12px;

        min-height: 48px;

        font-weight: 800;

        border: none;

        background: #1769aa;

        color: white;
    }

    .stButton > button:hover {

        background: #0b4f85;

        color: white;
    }


    /* ==============================
       FOOTER
    ============================== */

    .footer {

        text-align: center;

        color: #64748b;

        padding: 25px;

        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 5. SIDEBAR
# =========================================================

with st.sidebar:

    # LOGO

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    else:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:70px;
                padding:15px;
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
            font-size:19px;
            font-weight:900;
            margin-bottom:5px;
        ">
        HỆ THỐNG THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )


    st.caption(
        "Hỗ trợ thẩm định cho vay doanh nghiệp"
    )


    st.divider()


    menu = st.radio(
        "CHỨC NĂNG",
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


    st.caption(
        "Phiên bản 2.0"
    )

    st.caption(
        "© 2026"
    )


# =========================================================
# 6. TÍNH TIẾN ĐỘ HỒ SƠ
# =========================================================

steps = [

    bool(st.session_state.ten_dn),

    st.session_state.nang_luc_phap_ly != "Chưa đánh giá",

    st.session_state.da_phan_tich_tai_chinh,

    st.session_state.da_phan_tich_khoan_vay,

    st.session_state.da_phan_tich_tsdb

]

progress = sum(steps) / len(steps)


# =========================================================
# 7. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    # HEADER

    st.markdown(
        """
        <div class="hero-box">

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


    st.markdown(
        '<div class="section-title">👋 Chào mừng bạn đến với hệ thống</div>',
        unsafe_allow_html=True
    )


    st.info(
        "Hệ thống hỗ trợ cán bộ tín dụng và người học "
        "thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp. "
        "Kết quả chỉ mang tính chất hỗ trợ và không thay thế "
        "quyết định tín dụng thực tế."
    )


    # TIẾN ĐỘ

    st.markdown(
        '<div class="section-title">📈 TIẾN ĐỘ HOÀN THIỆN HỒ SƠ</div>',
        unsafe_allow_html=True
    )


    st.progress(
        progress
    )


    st.caption(
        f"Đã hoàn thành {int(progress * 100)}% quy trình thẩm định"
    )


    st.divider()


    # KPI

    st.markdown(
        '<div class="section-title">📊 CÁC NHÓM ĐÁNH GIÁ</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "🏢 HỒ SƠ",
            "01",
            "Thông tin doanh nghiệp"
        )


    with c2:

        st.metric(
            "💰 TÀI CHÍNH",
            "03",
            "ROA • ROE • Nợ"
        )


    with c3:

        st.metric(
            "💳 KHOẢN VAY",
            "01",
            "Khả năng trả nợ"
        )


    with c4:

        st.metric(
            "📊 KẾT QUẢ",
            "AI",
            "Tổng hợp đánh giá"
        )


    st.divider()


    # QUY TRÌNH

    st.markdown(
        '<div class="section-title">🚀 QUY TRÌNH THẨM ĐỊNH</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown(
            """
            <div class="custom-card">

                <div class="card-icon">🏢</div>

                <div class="card-title">
                    01. HỒ SƠ DOANH NGHIỆP
                </div>

                <div class="card-text">
                    Nhập thông tin pháp lý,
                    ngành nghề và thời gian hoạt động.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="custom-card">

                <div class="card-icon">💰</div>

                <div class="card-title">
                    02. PHÂN TÍCH TÀI CHÍNH
                </div>

                <div class="card-text">
                    Phân tích LNST, ROA,
                    ROE và tỷ lệ nợ.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="custom-card">

                <div class="card-icon">💳</div>

                <div class="card-title">
                    03. KHẢ NĂNG TRẢ NỢ
                </div>

                <div class="card-text">
                    Đánh giá dòng tiền
                    và nghĩa vụ trả nợ.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="custom-card">

                <div class="card-icon">📊</div>

                <div class="card-title">
                    04. KẾT QUẢ
                </div>

                <div class="card-text">
                    Tổng hợp điểm,
                    phân loại và đề xuất.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


    st.warning(
        "⚠️ Lưu ý: Kết quả ứng dụng chỉ mang tính chất "
        "hỗ trợ thẩm định. Quyết định cho vay thực tế "
        "thuộc thẩm quyền của tổ chức tín dụng."
    )


# =========================================================
# 8. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title(
        "🏢 HỒ SƠ DOANH NGHIỆP"
    )


    st.info(
        "Nhập thông tin cơ bản của doanh nghiệp và mục đích vay vốn."
    )


    st.markdown(
        '<div class="section-title">📋 Thông tin pháp lý</div>',
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp *",
            value=st.session_state.ten_dn
        )


        st.session_state.ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so
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
        '<div class="section-title">💳 Thông tin mục đích vay</div>',
        unsafe_allow_html=True
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
        height=150
    )


    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
    ):

        if not st.session_state.ten_dn.strip():

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                "✅ Đã lưu thông tin doanh nghiệp."
            )


# =========================================================
# 9. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    )


    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "điều kiện vay vốn. ROA, ROE, tỷ lệ nợ và LTV là "
        "chỉ tiêu hỗ trợ phân tích tín dụng, không phải "
        "điều kiện pháp lý bắt buộc chung."
    )


    st.markdown(
        '<div class="section-title">1️⃣ Điều kiện cơ bản</div>',
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
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.nang_luc_phap_ly)
        )


        st.session_state.muc_dich_hop_phap = st.selectbox(
            "Mục đích vay hợp pháp?",
            [
                "Chưa đánh giá",
                "Có",
                "Không"
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.muc_dich_hop_phap)
        )


        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn?",
            [
                "Chưa đánh giá",
                "Có",
                "Không"
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.co_phuong_an)
        )


    with c2:

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
            ].index(st.session_state.phuong_an_kha_thi)
        )


        st.session_state.kha_nang_tra_no = st.selectbox(
            "Có khả năng tài chính trả nợ?",
            [
                "Chưa đánh giá",
                "Có",
                "Không"
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.kha_nang_tra_no)
        )


    st.markdown(
        '<div class="section-title">2️⃣ Cam kết của khách hàng</div>',
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
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.dung_muc_dich)
        )


    with c2:

        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết hoàn trả nợ đúng hạn?",
            [
                "Chưa đánh giá",
                "Có",
                "Không"
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.tra_no_dung_han)
        )


    st.divider()


    conditions = [

        st.session_state.nang_luc_phap_ly,

        st.session_state.muc_dich_hop_phap,

        st.session_state.co_phuong_an,

        st.session_state.phuong_an_kha_thi,

        st.session_state.kha_nang_tra_no,

        st.session_state.dung_muc_dich,

        st.session_state.tra_no_dung_han

    ]


    so_dat = conditions.count("Có")


    st.metric(
        "Số điều kiện đã đáp ứng",
        f"{so_dat}/7"
    )


    if st.button(
        "⚖️ KIỂM TRA ĐIỀU KIỆN"
    ):

        if "Không" in conditions:

            st.error(
                "🔴 CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ"
            )

        elif "Chưa đánh giá" in conditions:

            st.warning(
                "🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN"
            )

        else:

            st.success(
                "🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ"
            )


# =========================================================
# 10. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title(
        "💰 PHÂN TÍCH TÀI CHÍNH"
    )


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
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

            st.session_state.da_phan_tich_tai_chinh = False


        elif st.session_state.von_chu_so_huu <= 0:

            st.error(
                "❌ Vốn chủ sở hữu phải lớn hơn 0."
            )

            st.session_state.da_phan_tich_tai_chinh = False


        elif st.session_state.no_phai_tra < 0:

            st.error(
                "❌ Nợ phải trả không được âm."
            )

            st.session_state.da_phan_tich_tai_chinh = False


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


            st.session_state.da_phan_tich_tai_chinh = True


            st.success(
                "✅ Phân tích tài chính thành công."
            )


    if st.session_state.da_phan_tich_tai_chinh:

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

                "Giá trị (%)": [

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
# 11. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title(
        "💳 THÔNG TIN KHOẢN VAY"
    )


    st.caption(
        "Đơn vị: triệu đồng"
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
            "Lãi suất cho vay (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )


        st.session_state.nghia_vu_no_cu = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu
        )


    if st.button(
        "💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
    ):

        if st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Số tiền vay phải lớn hơn 0."
            )

        else:

            st.session_state.tien_goc_thang = (
                st.session_state.so_tien_vay
                / st.session_state.thoi_gian_vay
            )


            st.session_state.tien_lai_thang = (

                st.session_state.so_tien_vay

                * st.session_state.lai_suat

                / 100

                / 12

            )


            st.session_state.tong_nghia_vu = (

                st.session_state.nghia_vu_no_cu

                + st.session_state.tien_goc_thang

                + st.session_state.tien_lai_thang

            )


            st.session_state.da_phan_tich_khoan_vay = True


            st.success(
                "✅ Đã tính toán nghĩa vụ trả nợ."
            )


    if st.session_state.da_phan_tich_khoan_vay:

        st.divider()


        c1, c2, c3 = st.columns(3)


        c1.metric(
            "GỐC / THÁNG",
            f"{st.session_state.tien_goc_thang:,.2f}"
        )


        c2.metric(
            "LÃI THÁNG ĐẦU",
            f"{st.session_state.tien_lai_thang:,.2f}"
        )


        c3.metric(
            "TỔNG NGHĨA VỤ / THÁNG",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )


        if st.session_state.dong_tien > 0:

            if (
                st.session_state.dong_tien
                >= st.session_state.tong_nghia_vu
            ):

                st.success(
                    "🟢 Dòng tiền hiện tại có khả năng "
                    "đáp ứng nghĩa vụ trả nợ theo mô hình."
                )

            else:

                st.warning(
                    "🟡 Dòng tiền hiện tại chưa đủ "
                    "đáp ứng nghĩa vụ trả nợ theo mô hình."
                )


# =========================================================
# 12. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title(
        "🏠 TÀI SẢN BẢO ĐẢM"
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
        ],
        index=[
            "Chưa đánh giá",
            "Có",
            "Không"
        ].index(st.session_state.co_tsdb)
    )


    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
    ):

        if st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True


            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )


        elif st.session_state.co_tsdb == "Chưa đánh giá":

            st.error(
                "❌ Vui lòng xác định khoản vay có TSĐB hay không."
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
                    "🟢 LTV ở mức tương đối thấp theo mô hình."
                )


            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng "
                    "và khả năng thanh khoản của TSĐB."
                )


            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 13. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH"
    )


    st.write(
        "Hệ thống tổng hợp các nhóm tiêu chí "
        "để đưa ra kết quả đánh giá sơ bộ."
    )


    # KIỂM TRA DỮ LIỆU

    missing = []


    if not st.session_state.da_phan_tich_tai_chinh:

        missing.append(
            "Phân tích tài chính"
        )


    if not st.session_state.da_phan_tich_khoan_vay:

        missing.append(
            "Thông tin khoản vay"
        )


    if not st.session_state.da_phan_tich_tsdb:

        missing.append(
            "Tài sản bảo đảm"
        )


    if missing:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để thực hiện kết quả thẩm định."
        )


        st.write(
            "Vui lòng hoàn thành:"
        )


        for item in missing:

            st.write(
                f"• {item}"
            )


    else:

        # =================================================
        # 1. TÍNH ĐIỂM
        # =================================================

        diem = 0

        diem_toi_da = 100

        ket_qua = []


        # -------------------------
        # ĐIỀU KIỆN VAY
        # -------------------------

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich_hop_phap,

            st.session_state.co_phuong_an,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no,

            st.session_state.dung_muc_dich,

            st.session_state.tra_no_dung_han

        ]


        so_dieu_kien_dat = dieu_kien.count(
            "Có"
        )


        # Điều kiện pháp lý

        if so_dieu_kien_dat == 7:

            diem += 25

            ket_qua.append(
                [
                    "Điều kiện vay vốn",
                    "Đạt",
                    "Đáp ứng 7/7 điều kiện sơ bộ"
                ]
            )

        elif so_dieu_kien_dat >= 5:

            diem += 15

            ket_qua.append(
                [
                    "Điều kiện vay vốn",
                    "Cần bổ sung",
                    f"Đáp ứng {so_dieu_kien_dat}/7 điều kiện"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Điều kiện vay vốn",
                    "Không đạt",
                    f"Chỉ đáp ứng {so_dieu_kien_dat}/7 điều kiện"
                ]
            )


        # -------------------------
        # LNST
        # -------------------------

        if st.session_state.lnst > 0:

            diem += 10

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


        # -------------------------
        # ROA
        # -------------------------

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
                    "Không đạt",
                    f"{st.session_state.roa:.2f}%"
                ]
            )


        # -------------------------
        # ROE
        # -------------------------

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
                    "Không đạt",
                    f"{st.session_state.roe:.2f}%"
                ]
            )


        # -------------------------
        # TỶ LỆ NỢ
        # -------------------------

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
                    "Không đạt",
                    f"{st.session_state.ty_le_no:.2f}%"
                ]
            )


        # -------------------------
        # KHẢ NĂNG TRẢ NỢ
        # -------------------------

        if (
            st.session_state.dong_tien
            >= st.session_state.tong_nghia_vu
        ):

            diem += 20

            ket_qua.append(
                [
                    "Khả năng trả nợ",
                    "Đạt",
                    "Dòng tiền đáp ứng nghĩa vụ trả nợ"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Khả năng trả nợ",
                    "Không đạt",
                    "Dòng tiền chưa đáp ứng nghĩa vụ trả nợ"
                ]
            )


        # -------------------------
        # TSĐB / LTV
        # -------------------------

        if st.session_state.co_tsdb == "Không":

            diem += 5

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Không áp dụng",
                    "Khoản vay không có TSĐB"
                ]
            )


        elif st.session_state.ltv is not None:

            if st.session_state.ltv <= 70:

                diem += 5

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
        # 2. HIỂN THỊ TỔNG QUAN
        # =================================================

        st.divider()


        st.subheader(
            "🎯 TỔNG QUAN KẾT QUẢ"
        )


        ty_le_diem = (

            diem

            / diem_toi_da

            * 100

        )


        c1, c2, c3, c4 = st.columns(4)


        c1.metric(
            "ĐIỂM THẨM ĐỊNH",
            f"{diem}/{diem_toi_da}"
        )


        c2.metric(
            "TỶ LỆ ĐÁNH GIÁ",
            f"{ty_le_diem:.1f}%"
        )


        c3.metric(
            "ROA",
            f"{st.session_state.roa:.2f}%"
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
            ty_le_diem / 100
        )


        # =================================================
        # 3. KẾT LUẬN
        # =================================================

        st.divider()


        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH"
        )


        # Điều kiện pháp lý không đạt
        # => Không đề xuất cho vay

        if so_dieu_kien_dat < 7:

            st.error(
                "🔴 CHƯA ĐẠT ĐIỀU KIỆN VAY VỐN"
            )


            st.write(
                f"Doanh nghiệp mới đáp ứng "
                f"{so_dieu_kien_dat}/7 điều kiện sơ bộ."
            )


            st.info(
                "Cần hoàn thiện các điều kiện vay vốn "
                "trước khi xem xét cấp tín dụng."
            )


        elif ty_le_diem >= 80:

            st.success(
                "🟢 ĐỀ XUẤT CHO VAY"
            )


            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
            )


            st.info(
                "Hồ sơ có kết quả tích cực theo mô hình "
                "hỗ trợ. Có thể chuyển sang bước thẩm định "
                "tín dụng chi tiết."
            )


        elif ty_le_diem >= 60:

            st.warning(
                "🟡 CẦN THẨM ĐỊNH BỔ SUNG"
            )


            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
            )


            st.info(
                "Cần xem xét thêm dòng tiền, khả năng trả nợ, "
                "lịch sử tín dụng, phương án kinh doanh "
                "và chất lượng tài sản bảo đảm."
            )


        else:

            st.error(
                "🔴 CHƯA ĐỀ XUẤT CHO VAY"
            )


            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
            )


            st.info(
                "Hồ sơ còn nhiều tiêu chí chưa đạt "
                "theo mô hình hỗ trợ thẩm định."
            )


        # =================================================
        # 4. BẢNG CHI TIẾT
        # =================================================

        st.divider()


        st.subheader(
            "📋 CHI TIẾT KẾT QUẢ"
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


        # =================================================
        # 5. KHUYẾN NGHỊ
        # =================================================

        st.divider()


        st.subheader(
            "💡 KHUYẾN NGHỊ THẨM ĐỊNH"
        )


        if st.session_state.lnst <= 0:

            st.warning(
                "• Doanh nghiệp đang có LNST không dương, "
                "cần xem xét nguyên nhân và khả năng cải thiện "
                "hiệu quả kinh doanh."
            )


        if st.session_state.roa <= 0:

            st.warning(
                "• ROA không dương, cần đánh giá hiệu quả "
                "sử dụng tài sản."
            )


        if st.session_state.ty_le_no > 70:

            st.warning(
                "• Tỷ lệ nợ cao, cần xem xét thêm cơ cấu "
                "nguồn vốn và khả năng chịu đựng rủi ro."
            )


        if (
            st.session_state.dong_tien
            < st.session_state.tong_nghia_vu
        ):

            st.warning(
                "• Dòng tiền chưa đủ đáp ứng nghĩa vụ trả nợ "
                "theo mô hình. Cần xem xét lại phương án trả nợ."
            )


        if (
            st.session_state.ltv is not None

            and st.session_state.ltv > 70
        ):

            st.warning(
                "• LTV cao, cần xem xét thêm giá trị, "
                "tính pháp lý và khả năng thanh khoản của TSĐB."
            )


        st.info(
            """
            ⚠️ LƯU Ý QUAN TRỌNG:

            ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu
            hỗ trợ phân tích tín dụng, không phải điều kiện
            pháp lý bắt buộc chung đối với mọi doanh nghiệp.

            Kết quả của ứng dụng chỉ mang tính chất hỗ trợ
            thẩm định. Quyết định cho vay thực tế phụ thuộc
            vào hồ sơ khách hàng, lịch sử tín dụng, dòng tiền,
            phương án kinh doanh, tài sản bảo đảm và chính sách
            tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 14. FOOTER
# =========================================================

st.divider()


st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP</b>

        <br><br>

        Điều kiện vay vốn • Phân tích tài chính •
        Khả năng trả nợ • Tài sản bảo đảm

        <br><br>

        © 2026 | Phiên bản 2.0

    </div>
    """,
    unsafe_allow_html=True
)
