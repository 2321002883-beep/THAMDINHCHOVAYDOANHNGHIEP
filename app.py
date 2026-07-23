ChatGPT





Claim offer

38a7fc9b-c99a-4df5-a3c6-8b6586c0d50d.png
sao bị lỗi v, code sai hay j r

Today 7:08 PM
4575699e-0fe9-4b1d-b9f8-91bd5e4acc30.png
tôi muốn chèn ảnh bên danh mục thẩm định chứ k phải ở trang giữ thì nên để code st.image("logo.jpg") ở dòng nào

Đúng rồi. Nhìn giao diện của bạn thì ảnh hiện tại đang nằm ở trang "Tổng quan", còn bạn muốn ảnh nằm bên trái, trong Sidebar, phía trên mục "📌 DANH MỤC THẨM ĐỊNH".

Bạn cần đặt:

st.image("logo.jpg")
bên trong with st.sidebar:, ngay trước dòng:

st.markdown("### 📌 DANH MỤC THẨM ĐỊNH")
Ví dụ:
with st.sidebar:

    # ẢNH LOGO
    st.image("logo.jpg", use_container_width=True)

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">
            <div style="
                font-size:19px;
                font-weight:800;
            ">
                THẨM ĐỊNH CHO VAY
                DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                margin-top:5px;
                opacity:0.85;
            ">
                HỆ THỐNG HỖ TRỢ CHO VAY
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # TÊN DANH MỤC
    st.markdown("### 📌 DANH MỤC THẨM ĐỊNH")

    menu = st.radio(
        "",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )
⚠️ Quan trọng
Nếu trong code hiện tại của bạn đang có đoạn này ở trang Tổng quan:

st.image("logo.jpg")
thì hãy xóa nó khỏi phần if menu == "🏠 Tổng quan":.

Sau đó chỉ giữ st.image("logo.jpg") ở trong:

with st.sidebar:
Kết quả sẽ là:

SIDEBAR bên trái:

🖼️ ẢNH LOGO
🏦 THẨM ĐỊNH CHO VAY DOANH NGHIỆP
━━━━━━━━━━━━
📌 DANH MỤC THẨM ĐỊNH
🔴 🏠 Tổng quan
⚪ 🏢 Hồ sơ & điều kiện
⚪ 💰 Phân tích tài chính
⚪ 💳 Khoản vay & bảo đảm
⚪ 📊 Kết quả thẩm định

Còn trang Tổng quan bên phải sẽ không còn ảnh lớn nữa.



Pasted text(14).txt
Document
tôi có code r thêm dòng đó vào cho tôi đi

Được. Nếu bạn muốn ảnh logo.jpg nằm ở bên trái, ngay trong phần "DANH MỤC THẨM ĐỊNH" của Sidebar, thì bạn thêm st.image("logo.jpg") bên trong with st.sidebar:, ngay trước dòng st.markdown("📌 DANH MỤC THẨM ĐỊNH").

Ví dụ, phần Sidebar của bạn sửa thành:

# =========================================================
# SIDEBAR - DANH MỤC THẨM ĐỊNH
# =========================================================

with st.sidebar:

    # Logo nằm ở đầu Sidebar
    st.image(
        "logo.jpg",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">
            <div style="
                font-size:22px;
                font-weight:800;
                line-height:1.4;
            ">
                🏦 THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                font-weight:600;
                opacity:0.85;
                margin-top:8px;
            ">
                HỆ THỐNG HỖ TRỢ CHO VAY
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # ==============================
    # DANH MỤC THẨM ĐỊNH
    # ==============================

    st.markdown(
        """
        <div style="
            font-size:17px;
            font-weight:800;
            margin-bottom:12px;
        ">
            📌 DANH MỤC THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.radio(
        "",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )
Nếu bạn muốn ảnh nằm ngay dưới chữ "📌 DANH MỤC THẨM ĐỊNH"
Thì đặt dòng này:

st.image("logo.jpg", use_container_width=True)
ngay sau:

st.markdown(
    """
    <div style="
        font-size:17px;
        font-weight:800;
        margin-bottom:12px;
    ">
        📌 DANH MỤC THẨM ĐỊNH
    </div>
    """,
    unsafe_allow_html=True
)
Kết quả sẽ theo thứ tự:

📌 DANH MỤC THẨM ĐỊNH

      [ ẢNH LOGO ]

🔴 🏠 Tổng quan
⚪ 🏢 Hồ sơ & điều kiện
⚪ 💰 Phân tích tài chính
⚪ 💳 Khoản vay & bảo đảm
⚪ 📊 Kết quả thẩm định
Lưu ý: Nếu bạn đang chạy trên Streamlit Cloud, file logo.jpg phải được đặt cùng thư mục với app.py và phải được push lên GitHub. Nếu tên file của bạn khác, ví dụ logo.png, thì đổi thành:

st.image("logo.png", use_container_width=True)
Nếu mục tiêu của bạn là ảnh nằm bên trái danh mục, nhỏ gọn như một biểu tượng/logo, chứ không phải ảnh nằm phía trên danh mục, thì không nên dùng st.image() trực tiếp; mình có thể sửa phần Sidebar thành logo nhỏ + DANH MỤC THẨM ĐỊNH nằm cạnh nhau, nhìn giống giao diện ngân hàng chuyên nghiệp hơn.


nằm ở bên trên chữ thẩm định cho vay dn

À hiểu rồi 😄 Bạn muốn ảnh logo.jpg nằm ngay phía trên dòng "🏦 THẨM ĐỊNH CHO VAY DOANH NGHIỆP" ở Sidebar, giống bố cục ảnh bạn gửi.

Bạn thay toàn bộ phần Sidebar hiện tại bằng đoạn này:

# =========================================================
# SIDEBAR - DANH MỤC THẨM ĐỊNH
# =========================================================

with st.sidebar:

    # ==============================
    # LOGO - NẰM TRÊN TÊN HỆ THỐNG
    # ==============================

    st.image(
        "logo.jpg",
        use_container_width=True
    )

    # ==============================
    # TÊN HỆ THỐNG
    # ==============================

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">

            <div style="
                font-size:21px;
                font-weight:800;
                line-height:1.5;
                color:white;
            ">
                🏦 THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                font-weight:600;
                color:#b9d7ef;
                margin-top:8px;
            ">
                HỆ THỐNG HỖ TRỢ CHO VAY
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # ==============================
    # DANH MỤC THẨM ĐỊNH
    # ==============================

    st.markdown(
        """
        <div style="
            font-size:17px;
            font-weight:800;
            color:white;
            margin-bottom:12px;
        ">
            📌 DANH MỤC THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.radio(
        "",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )
Vị trí hiển thị sẽ là:
┌──────────────────────────┐
│                          │
│       [ LOGO.JPG ]       │  ← ẢNH
│                          │
│ 🏦 THẨM ĐỊNH CHO VAY     │
│    DOANH NGHIỆP          │
│                          │
│ HỆ THỐNG HỖ TRỢ CHO VAY  │
│                          │
├──────────────────────────┤
│ 📌 DANH MỤC THẨM ĐỊNH    │
│                          │
│ 🔴 🏠 Tổng quan          │
│ ⚪ 🏢 Hồ sơ & điều kiện  │
│ ⚪ 💰 Phân tích tài chính│
│ ⚪ 💳 Khoản vay & bảo đảm│
│ ⚪ 📊 Kết quả thẩm định  │
└──────────────────────────┘
Quan trọng: Nếu ảnh logo.jpg của bạn là ảnh lớn như ảnh doanh nhân trong ảnh chụp màn hình, nó sẽ chiếm rất nhiều chiều cao. Nếu bạn muốn logo nhỏ, gọn nằm trên chữ "THẨM ĐỊNH CHO VAY DOANH NGHIỆP", thì nên dùng kích thước nhỏ hơn bằng CSS hoặc đổi ảnh sang logo vuông.


viết lại full code 

Được. Dưới đây là FULL CODE hoàn chỉnh, bạn copy toàn bộ nguyên khối này vào app.py.

Mình đã chỉnh:

Logo logo.jpg nằm trên chữ "THẨM ĐỊNH CHO VAY DOANH NGHIỆP" ở Sidebar.

Menu được rút gọn còn 5 mục.

Gộp Hồ sơ + Điều kiện vay.

Gộp Khoản vay + Khả năng trả nợ + Tài sản bảo đảm.

Không dùng HTML <h1> bị lỗi hiển thị như trước.

Có kiểm tra điều kiện vay vốn.

Có phân tích ROA, ROE, tỷ lệ nợ.

Có tính nghĩa vụ trả nợ.

Có DSCR.

Có LTV.

Có kết quả thẩm định sơ bộ.

Có kiểm tra dữ liệu trước khi kết luận.

Giao diện Sidebar đẹp hơn.

Lưu ý: File logo.jpg phải đặt cùng thư mục với app.py trên GitHub.

import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Thẩm định cho vay doanh nghiệp",
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
    "muc_dich": "Chưa đánh giá",
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

    # Khả năng trả nợ
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
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       NỀN CHÍNH
    ========================= */

    .stApp {
        background:
        linear-gradient(
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

        background:
        linear-gradient(
            180deg,
            #06203d 0%,
            #08345d 50%,
            #0b4b78 100%
        );

    }


    section[data-testid="stSidebar"] * {

        color: white !important;

    }


    section[data-testid="stSidebar"] hr {

        border-color:
        rgba(255,255,255,0.18);

    }


    /* =========================
       TIÊU ĐỀ
    ========================= */

    h1 {

        color: #08345d !important;

        font-weight: 800 !important;

    }


    h2 {

        color: #0b4b78 !important;

        font-weight: 750 !important;

    }


    h3 {

        color: #11608f !important;

        font-weight: 700 !important;

    }


    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {

        background:
        rgba(255,255,255,0.96);

        border:
        1px solid #d7e4ef;

        padding:
        18px;

        border-radius:
        18px;

        box-shadow:
        0 8px 24px
        rgba(13,59,102,0.08);

    }


    div[data-testid="stMetricLabel"] {

        color:
        #55708d !important;

        font-weight:
        600;

    }


    div[data-testid="stMetricValue"] {

        color:
        #0b3761 !important;

        font-weight:
        800;

    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {

        width:
        100%;

        border:
        none;

        border-radius:
        12px;

        padding:
        0.7rem 1rem;

        font-weight:
        700;

        color:
        white;

        background:
        linear-gradient(
            135deg,
            #0866a6,
            #1495d0
        );

        box-shadow:
        0 5px 15px
        rgba(11,79,138,0.22);

        transition:
        0.25s;

    }


    .stButton > button:hover {

        transform:
        translateY(-2px);

        box-shadow:
        0 8px 20px
        rgba(11,79,138,0.3);

    }


    /* =========================
       INPUT
    ========================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"],
    textarea {

        border-radius:
        10px !important;

    }


    /* =========================
       HERO
    ========================= */

    .hero-card {

        background:
        linear-gradient(
            135deg,
            #06284d,
            #09669b,
            #16a1d4
        );

        padding:
        35px;

        border-radius:
        24px;

        color:
        white;

        box-shadow:
        0 15px 35px
        rgba(8,38,74,0.22);

        margin-bottom:
        25px;

    }


    .hero-title {

        font-size:
        30px;

        font-weight:
        800;

        line-height:
        1.35;

        margin-bottom:
        10px;

    }


    .hero-subtitle {

        font-size:
        16px;

        color:
        rgba(255,255,255,0.9);

    }


    /* =========================
       CARD
    ========================= */

    .section-card {

        background:
        rgba(255,255,255,0.92);

        padding:
        22px;

        border-radius:
        18px;

        border:
        1px solid #dce7f2;

        box-shadow:
        0 6px 20px
        rgba(13,59,102,0.06);

        margin-bottom:
        18px;

    }


    /* =========================
       TRẠNG THÁI
    ========================= */

    .status-good {

        background:
        #e9f8ef;

        border-left:
        5px solid #1e9e58;

        padding:
        16px;

        border-radius:
        12px;

        color:
        #176b3c;

        font-weight:
        700;

    }


    .status-warning {

        background:
        #fff7df;

        border-left:
        5px solid #e4a400;

        padding:
        16px;

        border-radius:
        12px;

        color:
        #805f00;

        font-weight:
        700;

    }


    .status-bad {

        background:
        #fff0f0;

        border-left:
        5px solid #d64545;

        padding:
        16px;

        border-radius:
        12px;

        color:
        #8c2525;

        font-weight:
        700;

    }


    /* =========================
       FOOTER
    ========================= */

    .footer {

        text-align:
        center;

        color:
        #70849a;

        padding:
        20px;

        font-size:
        13px;

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    # -----------------------------------------------------
    # LOGO
    # -----------------------------------------------------

    try:

        st.image(
            "logo.jpg",
            use_container_width=True
        )

    except:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:60px;
                padding:15px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # TÊN HỆ THỐNG
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">

            <div style="
                font-size:21px;
                font-weight:800;
                line-height:1.5;
                color:white;
            ">
                🏦 THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                font-weight:600;
                color:#b9d7ef;
                margin-top:8px;
            ">
                HỆ THỐNG HỖ TRỢ CHO VAY
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            font-size:17px;
            font-weight:800;
            margin-bottom:12px;
        ">
            📌 DANH MỤC THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )


    menu = st.radio(
        "Chọn nội dung",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
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
        Ứng dụng hỗ trợ thực hiện quy trình thẩm định sơ bộ
        đối với hồ sơ vay vốn của doanh nghiệp.
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
            "🏠 Bảo đảm",
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

            Nhập thông tin doanh nghiệp
            và kiểm tra điều kiện vay.
            """
        )


    with c2:

        st.info(
            """
            **02 | TÀI CHÍNH**

            Phân tích doanh thu,
            LNST, ROA, ROE và nợ.
            """
        )


    with c3:

        st.info(
            """
            **03 | KHOẢN VAY**

            Phân tích khoản vay,
            khả năng trả nợ và TSĐB.
            """
        )


    with c4:

        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu và
            đưa ra kết luận sơ bộ.
            """
        )


    st.warning(
        """
        ⚠️ Lưu ý: Ứng dụng chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ. Kết quả không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN
# =========================================================

elif menu == "🏢 Hồ sơ & điều kiện":

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
                "❌ Vui lòng mô tả phương án sử dụng vốn."
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


    st.subheader("⚖️ 2. Kiểm tra điều kiện vay vốn")


    st.info(
        """
        Phần này kiểm tra sơ bộ các điều kiện vay vốn.
        Kết quả chỉ mang tính hỗ trợ và không thay thế
        chính sách tín dụng của tổ chức tín dụng.
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
            "Năng lực pháp lý phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )


        st.session_state.muc_dich = st.selectbox(
            "Mục đích vay vốn hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich
            )
        )


        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn?",
            options,
            index=options.index(
                st.session_state.co_phuong_an
            )
        )


        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )


    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "Có khả năng tài chính trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )


        st.session_state.dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.dung_muc_dich
            )
        )


        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết hoàn trả nợ đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )


    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN"):

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich,

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
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH")


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
                /
                st.session_state.tong_tai_san
                *
                100
            )


            st.session_state.roe = (
                st.session_state.lnst
                /
                st.session_state.von_chu_so_huu
                *
                100
            )


            st.session_state.ty_le_no = (
                st.session_state.no_phai_tra
                /
                st.session_state.tong_tai_san
                *
                100
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
            chart.set_index(
                "Chỉ tiêu"
            )
        )


# =========================================================
# 8. KHOẢN VAY & BẢO ĐẢM
# =========================================================

elif menu == "💳 Khoản vay & bảo đảm":

    st.title("💳 KHOẢN VAY & TÀI SẢN BẢO ĐẢM")


    st.subheader("💰 1. Thông tin khoản vay")


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
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


    if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

        if st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Số tiền vay phải lớn hơn 0."
            )

        else:

            tien_goc = (

                st.session_state.so_tien_vay
                /
                st.session_state.thoi_gian_vay

            )


            tien_lai = (

                st.session_state.so_tien_vay
                *
                st.session_state.lai_suat
                /
                100
                /
                12

            )


            tong_nghia_vu = (

                st.session_state.nghia_vu_no_cu
                +
                tien_goc
                +
                tien_lai

            )


            st.session_state.tien_goc_thang = tien_goc

            st.session_state.tien_lai_thang = tien_lai

            st.session_state.tong_nghia_vu = tong_nghia_vu

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


    st.subheader("📈 2. Khả năng trả nợ")


    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

        st.metric(
            "Dòng tiền kinh doanh/tháng",
            f"{st.session_state.dong_tien:,.2f} triệu đồng"
        )


        if st.button("📈 TÍNH DSCR"):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (

                    st.session_state.dong_tien
                    /
                    st.session_state.tong_nghia_vu

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


    st.divider()


    st.subheader("🏠 3. Tài sản bảo đảm")


    options_tsdb = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        options_tsdb,
        index=options_tsdb.index(
            st.session_state.co_tsdb
        )
    )


    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True


            st.info(
                "Khoản vay được đánh giá là không có tài sản bảo đảm."
            )


        elif st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
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
                /
                st.session_state.gia_tri_tsdb
                *
                100

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
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")


    st.info(
        """
        Kết quả dưới đây được tổng hợp từ dữ liệu người dùng nhập.
        Ứng dụng chỉ hỗ trợ thẩm định sơ bộ và không thay thế
        quyết định tín dụng chính thức.
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
            "Thông tin khoản vay"
        )


    if not st.session_state.da_phan_tich_tsdb:

        missing.append(
            "Tài sản bảo đảm"
        )


    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để tổng hợp kết quả."
        )


        st.write(
            "Các phần còn thiếu:"
        )


        for item in missing:

            st.write(
                f"• {item}"
            )


    else:

        # -------------------------------------------------
        # KIỂM TRA ĐIỀU KIỆN
        # -------------------------------------------------

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich,

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


        # -------------------------------------------------
        # THÔNG TIN DOANH NGHIỆP
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
        # CHỈ TIÊU
        # -------------------------------------------------

        st.subheader(
            "📊 CÁC CHỈ TIÊU CHÍNH"
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
            "Khoản vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )


        st.divider()


        # -------------------------------------------------
        # KẾT LUẬN
        # -------------------------------------------------

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )


        if co_dieu_kien_khong:

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
                Có ít nhất một điều kiện vay vốn cơ bản đang
                được đánh giá là Không. Hồ sơ cần được xem xét,
                bổ sung hoặc điều chỉnh trước khi tiếp tục
                thẩm định tín dụng.
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
                Cần hoàn thiện thông tin trước khi đưa ra kết luận.
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

                🟢 ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CHO VAY

                </div>
                """,
                unsafe_allow_html=True
            )


            st.write(
                """
                Các điều kiện vay vốn cơ bản đang được đánh giá là đạt.
                Các chỉ tiêu tài chính và khả năng trả nợ hiện có tín hiệu
                tích cực theo dữ liệu đã nhập. Hồ sơ có thể được chuyển
                sang bước thẩm định tín dụng chi tiết theo quy trình
                của tổ chức tín dụng.
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
                Hồ sơ chưa thể kết luận đủ điều kiện sơ bộ dựa trên
                các chỉ tiêu hỗ trợ hiện tại. Cần xem xét thêm tình hình
                tài chính, dòng tiền, khả năng trả nợ, phương án kinh doanh,
                lịch sử tín dụng và các yếu tố liên quan.
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


        # Điều kiện pháp lý

        ket_qua.append(
            [
                "Năng lực pháp lý",
                "Đạt"
                if st.session_state.nang_luc_phap_ly == "Có"
                else "Cần xem xét",
                st.session_state.nang_luc_phap_ly
            ]
        )


        # Mục đích

        ket_qua.append(
            [
                "Mục đích vay",
                "Đạt"
                if st.session_state.muc_dich == "Có"
                else "Cần xem xét",
                st.session_state.muc_dich
            ]
        )


        # Phương án

        ket_qua.append(
            [
                "Phương án sử dụng vốn",
                "Đạt"
                if st.session_state.co_phuong_an == "Có"
                else "Cần xem xét",
                st.session_state.co_phuong_an
            ]
        )


        # Tính khả thi

        ket_qua.append(
            [
                "Tính khả thi",
                "Đạt"
                if st.session_state.phuong_an_kha_thi == "Có"
                else "Cần xem xét",
                st.session_state.phuong_an_kha_thi
            ]
        )


        # Khả năng trả nợ

        ket_qua.append(
            [
                "Khả năng tài chính trả nợ",
                "Đạt"
                if st.session_state.kha_nang_tra_no == "Có"
                else "Cần xem xét",
                st.session_state.kha_nang_tra_no
            ]
        )


        # LNST

        ket_qua.append(
            [
                "LNST",
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

            ROA, ROE, LNST, DSCR và LTV là các chỉ tiêu hỗ trợ
            phân tích tín dụng. Không nên sử dụng riêng lẻ các
            chỉ tiêu này để kết luận doanh nghiệp chắc chắn được
            vay vốn.

            Quyết định cho vay thực tế còn phụ thuộc vào hồ sơ
            pháp lý, mục đích sử dụng vốn, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách tín dụng
            của từng tổ chức tín dụng.
            """
        )


# =========================================================
# 10. FOOTER
# =========================================================

st.divider()


st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP</b>

        <br>

        Công cụ hỗ trợ phân tích và thẩm định
        sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo
        và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
Cấu trúc GitHub của bạn cần là:
THAMDINHCHOVAYDOANHNGHIEP
│
├── app.py
│
└── logo.jpg
Trong code trên, phần:

with st.sidebar:
    st.image(
        "logo.jpg",
        use_container_width=True
    )
sẽ đặt logo.jpg ở trên dòng "THẨM ĐỊNH CHO VAY DOANH NGHIỆP", đúng vị trí bạn yêu cầu.


import streamlit as st
import pandas as pd

=========================================================
1. CẤU HÌNH ỨNG DỤNG
=========================================================
st.set_page_config(
page_title="HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP",
page_icon="🏦",
layout="wide",
initial_sidebar_state="expanded"
)

=========================================================
2. KHỞI TẠO SESSION STATE
=========================================================
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

=========================================================
3. CSS GIAO DIỆN
=========================================================
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

=========================================================
4. SIDEBAR - 5 DANH MỤC ĐƠN GIẢN
=========================================================
with st.sidebar:

st.markdown(
    """
    <div class="sidebar-title">
        🏦 THẨM ĐỊNH CHO VAY DOANH NGHIỆP
    </div>

    <div class="sidebar-subtitle">
        HỆ THỐNG HỖ TRỢ CHO VAY 
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

menu = st.radio(
    "📌 DANH MỤC THẨM ĐỊNH",
    [
        "🏠 Tổng quan",
        "🏢 Hồ sơ & điều kiện",
        "💰 Phân tích tài chính",
        "💳 Khoản vay & bảo đảm",
        "📊 Kết quả thẩm định"
    ]
)

st.divider()
=========================================================
5. TRANG TỔNG QUAN
=========================================================
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
=========================================================
6. HỒ SƠ & ĐIỀU KIỆN
=========================================================
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
=========================================================
7. PHÂN TÍCH TÀI CHÍNH
=========================================================
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
=========================================================
8. KHOẢN VAY & BẢO ĐẢM
=========================================================
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
=========================================================
9. KẾT QUẢ THẨM ĐỊNH
=========================================================
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
=========================================================
10. FOOTER
=========================================================
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


Close
