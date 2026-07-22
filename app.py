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

# Chỉ số tài chính
"roa": None,
"roe": None,
"ty_le_no": None,

# Khoản vay
"so_tien_vay": 0.0,
"thoi_gian_vay": 12,
"lai_suat": 0.0,
"nghia_vu_no_cu": 0.0,
"tong_nghia_vu": None,

# Tài sản bảo đảm
"co_tsdb": "Chưa đánh giá",
"gia_tri_tsdb": 0.0,
"ltv": None

}

for key, value in default_values.items():
if key not in st.session_state:
st.session_state[key] = value

# =========================================================

# 3. CSS - GIAO DIỆN HIỆN ĐẠI

# =========================================================

st.markdown(
""" <style>

/* ==============================
   NỀN CHÍNH
============================== */

.stApp {
    background:
        linear-gradient(
            135deg,
            #f4f7fb 0%,
            #eef4fb 50%,
            #f8fafc 100%
        );
}


/* ==============================
   SIDEBAR
============================== */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #071a33 0%,
            #0b2b4c 50%,
            #123f66 100%
        );
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 10px 12px;
    border-radius: 10px;
    margin-bottom: 5px;
    transition: 0.2s;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background-color: rgba(255,255,255,0.12);
}


/* ==============================
   TIÊU ĐỀ
============================== */

h1 {
    color: #08243f;
    font-weight: 800;
    letter-spacing: -0.5px;
}

h2 {
    color: #0d3b63;
    font-weight: 750;
}

h3 {
    color: #124e78;
    font-weight: 700;
}


/* ==============================
   CARD
============================== */

.main-card {
    background: rgba(255,255,255,0.92);
    padding: 28px;
    border-radius: 22px;
    border: 1px solid #dce6f1;
    box-shadow:
        0 12px 35px rgba(15, 47, 79, 0.08);
    margin-bottom: 25px;
}

.hero-card {
    background:
        linear-gradient(
            135deg,
            #08243f 0%,
            #0d4773 50%,
            #176d9c 100%
        );
    padding: 35px;
    border-radius: 24px;
    color: white;
    box-shadow:
        0 18px 40px rgba(8,36,63,0.22);
    margin-bottom: 28px;
}

.hero-card h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 8px;
}

.hero-card p {
    color: #e7f3ff;
    font-size: 16px;
}


/* ==============================
   METRIC
============================== */

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.95);
    border: 1px solid #dce6f1;
    padding: 18px;
    border-radius: 16px;
    box-shadow:
        0 7px 20px rgba(15,47,79,0.07);
}

div[data-testid="stMetricLabel"] {
    color: #55708a;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #0b2f4f;
    font-weight: 800;
}


/* ==============================
   BUTTON
============================== */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    border: none;
    background:
        linear-gradient(
            135deg,
            #0b4775,
            #1477a8
        );
    color: white;
    box-shadow:
        0 7px 18px rgba(11,71,117,0.22);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 10px 25px rgba(11,71,117,0.30);
}


/* ==============================
   INPUT
============================== */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    border-radius: 10px;
    border: 1px solid #ccd9e6;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}


/* ==============================
   INFO BOX
============================== */

.info-card {
    background: white;
    border-left: 5px solid #1683b8;
    padding: 18px;
    border-radius: 12px;
    box-shadow:
        0 6px 18px rgba(15,47,79,0.06);
    margin-bottom: 15px;
}

.success-card {
    background: #effaf4;
    border-left: 5px solid #16a05d;
    padding: 18px;
    border-radius: 12px;
}

.warning-card {
    background: #fff8e8;
    border-left: 5px solid #e5a100;
    padding: 18px;
    border-radius: 12px;
}

.danger-card {
    background: #fff1f1;
    border-left: 5px solid #d93434;
    padding: 18px;
    border-radius: 12px;
}


/* ==============================
   FOOTER
============================== */

.footer {
    text-align: center;
    color: #718096;
    padding: 25px;
    font-size: 14px;
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
        padding:15px 5px 20px 5px;
    ">
        <div style="font-size:48px;">🏦</div>

        <div style="
            font-size:18px;
            font-weight:800;
            line-height:1.4;
        ">
            HỆ THỐNG HỖ TRỢ
            <br>
            THẨM ĐỊNH CHO VAY
            <br>
            DOANH NGHIỆP
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    "### 📌 MENU CHỨC NĂNG"
)

menu = st.radio(
    "",
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
    "Phiên bản hỗ trợ thẩm định doanh nghiệp"
)

# =========================================================

# 5. TRANG TỔNG QUAN

# =========================================================

if menu == "🏠 Tổng quan":

st.markdown(
    """
    <div class="hero-card">

        <div style="font-size:52px;">
            🏦
        </div>

        <h1>
            HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
            CHO VAY DOANH NGHIỆP
        </h1>

        <p>
            Phân tích hồ sơ • Đánh giá tài chính •
            Khả năng trả nợ • Tài sản bảo đảm •
            Hỗ trợ quyết định tín dụng
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.subheader(
    "👋 Chào mừng bạn đến với hệ thống"
)

st.markdown(
    """
    <div class="info-card">

    Hệ thống hỗ trợ cán bộ tín dụng và người học
    thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp.

    Quy trình được thực hiện theo hướng:

    <b>Hồ sơ doanh nghiệp → Điều kiện vay vốn →
    Phân tích tài chính → Khả năng trả nợ →
    Tài sản bảo đảm → Kết quả thẩm định</b>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader(
    "📊 CÁC NHÓM ĐÁNH GIÁ"
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🏢 Hồ sơ",
        "01"
    )

with c2:
    st.metric(
        "💰 Tài chính",
        "03"
    )

with c3:
    st.metric(
        "💳 Khoản vay",
        "01"
    )

with c4:
    st.metric(
        "📊 Thẩm định",
        "01"
    )

st.divider()

st.subheader(
    "🚀 QUY TRÌNH THẨM ĐỊNH"
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(
        """
        <div class="main-card">

        <h3>01</h3>

        <b>🏢 HỒ SƠ DOANH NGHIỆP</b>

        <p>
        Nhập thông tin doanh nghiệp,
        ngành nghề, thời gian hoạt động,
        mục đích và phương án sử dụng vốn.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        """
        <div class="main-card">

        <h3>02</h3>

        <b>💰 PHÂN TÍCH TÀI CHÍNH</b>

        <p>
        Phân tích doanh thu, LNST,
        ROA, ROE và tỷ lệ nợ.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        """
        <div class="main-card">

        <h3>03</h3>

        <b>💳 KHẢ NĂNG TRẢ NỢ</b>

        <p>
        Đánh giá nghĩa vụ trả nợ
        và dòng tiền của doanh nghiệp.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with c4:

    st.markdown(
        """
        <div class="main-card">

        <h3>04</h3>

        <b>📊 KẾT QUẢ</b>

        <p>
        Tổng hợp điều kiện vay vốn,
        tài chính, trả nợ và TSĐB.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

st.warning(
    "⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ "
    "thẩm định, không thay thế quyết định tín dụng thực tế."
)

# =========================================================

# 6. HỒ SƠ DOANH NGHIỆP

# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

st.title(
    "🏢 HỒ SƠ DOANH NGHIỆP"
)

st.markdown(
    """
    <div class="info-card">
    Nhập đầy đủ thông tin doanh nghiệp trước khi
    thực hiện các bước thẩm định tiếp theo.
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader(
    "📋 Thông tin doanh nghiệp"
)

c1, c2 = st.columns(2)

with c1:

    st.session_state.ten_dn = st.text_input(
        "Tên doanh nghiệp",
        value=st.session_state.ten_dn,
        placeholder="Nhập tên doanh nghiệp"
    )

    st.session_state.ma_so = st.text_input(
        "Mã số doanh nghiệp",
        value=st.session_state.ma_so,
        placeholder="Nhập mã số doanh nghiệp"
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

st.divider()

st.subheader(
    "💳 Mục đích và phương án sử dụng vốn"
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
    placeholder="Nhập nội dung phương án sử dụng vốn..."
)

st.divider()

if st.button(
    "💾 LƯU HỒ SƠ DOANH NGHIỆP"
):

    if st.session_state.ten_dn.strip() == "":

        st.error(
            "❌ Vui lòng nhập tên doanh nghiệp."
        )

    else:

        st.success(
            "✅ Đã lưu thông tin doanh nghiệp."
        )

# =========================================================

# 7. ĐIỀU KIỆN VAY VỐN

# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

```
st.title(
    "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
)

st.info(
    "Đây là bước kiểm tra sơ bộ các điều kiện vay vốn "
    "trước khi đánh giá sâu về tài chính và rủi ro tín dụng."
)

st.subheader(
    "1️⃣ Điều kiện cơ bản"
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

st.divider()

st.subheader(
    "2️⃣ Cam kết của khách hàng"
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

st.subheader(
    "📊 Nhập số liệu tài chính"
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
        "Dòng tiền thuần từ HĐKD bình quân/tháng",
        value=st.session_state.dong_tien
    )

st.divider()

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

        st.success(
            "✅ Đã phân tích tài chính thành công."
        )

if st.session_state.roa is not None:

    st.divider()

    st.subheader(
        "📈 Kết quả phân tích"
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

# =========================================================

# 9. THÔNG TIN KHOẢN VAY

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
        "Lãi suất (%/năm)",
        min_value=0.0,
        value=st.session_state.lai_suat
    )

    st.session_state.nghia_vu_no_cu = st.number_input(
        "Nghĩa vụ trả nợ hiện tại/tháng",
        min_value=0.0,
        value=st.session_state.nghia_vu_no_cu
    )

st.divider()

if st.button(
    "💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
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

        st.session_state.tong_nghia_vu = (
            st.session_state.nghia_vu_no_cu
            + tien_goc
            + tien_lai
        )

        st.success(
            "✅ Đã tính toán nghĩa vụ trả nợ."
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc/tháng",
            f"{tien_goc:,.2f} triệu"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{tien_lai:,.2f} triệu"
        )

        c3.metric(
            "Tổng nghĩa vụ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f} triệu"
        )

# =========================================================

# 10. TÀI SẢN BẢO ĐẢM

# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

```
st.title(
    "🏠 TÀI SẢN BẢO ĐẢM"
)

st.info(
    "LTV là chỉ tiêu hỗ trợ phân tích tín dụng. "
    "Ngưỡng đánh giá trong ứng dụng cần được điều chỉnh "
    "theo chính sách của từng tổ chức tín dụng."
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
    "Giá trị tài sản bảo đảm (triệu đồng)",
    min_value=0.0,
    value=st.session_state.gia_tri_tsdb
)

st.divider()

if st.button(
    "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
):

    if st.session_state.co_tsdb == "Không":

        st.session_state.ltv = None

        st.info(
            "Khoản vay không có tài sản bảo đảm."
        )

    elif st.session_state.co_tsdb == "Chưa đánh giá":

        st.warning(
            "⚠️ Vui lòng xác định khoản vay có TSĐB hay không."
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
                "🟡 Cần xem xét thêm chất lượng và "
                "khả năng thanh khoản của tài sản bảo đảm."
            )

        else:

            st.error(
                "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."
            )

# =========================================================

# 11. KẾT QUẢ THẨM ĐỊNH

# =========================================================

elif menu == "📊 Kết quả thẩm định":

```
st.title(
    "📊 KẾT QUẢ THẨM ĐỊNH"
)

st.markdown(
    """
    <div class="hero-card">

        <div style="font-size:42px;">
            📊
        </div>

        <h1>
            TỔNG HỢP KẾT QUẢ THẨM ĐỊNH
        </h1>

        <p>
            Điều kiện vay vốn →
            Tình hình tài chính →
            Khả năng trả nợ →
            Tài sản bảo đảm
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# KIỂM TRA DỮ LIỆU
# =====================================================

thieu_du_lieu = []

if st.session_state.ten_dn.strip() == "":
    thieu_du_lieu.append(
        "Tên doanh nghiệp"
    )

if st.session_state.roa is None:
    thieu_du_lieu.append(
        "Phân tích tài chính"
    )

if st.session_state.tong_nghia_vu is None:
    thieu_du_lieu.append(
        "Phân tích khả năng trả nợ"
    )

if st.session_state.so_tien_vay <= 0:
    thieu_du_lieu.append(
        "Số tiền vay"
    )

if st.session_state.tong_tai_san <= 0:
    thieu_du_lieu.append(
        "Tổng tài sản"
    )

if thieu_du_lieu:

    st.warning(
        "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ THẨM ĐỊNH"
    )

    st.write(
        "Vui lòng hoàn thành các nội dung:"
    )

    for item in thieu_du_lieu:

        st.write(
            f"🔸 {item}"
        )

    st.info(
        "Hãy hoàn thành các bước ở menu bên trái "
        "trước khi xem kết quả thẩm định."
    )

else:

    # =================================================
    # 1. KIỂM TRA ĐIỀU KIỆN VAY VỐN
    # =================================================

    st.subheader(
        "1️⃣ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    )

    dieu_kien = {

        "Năng lực pháp lý":
            st.session_state.nang_luc_phap_ly,

        "Mục đích vay hợp pháp":
            st.session_state.muc_dich,

        "Có phương án sử dụng vốn":
            st.session_state.co_phuong_an,

        "Phương án sử dụng vốn khả thi":
            st.session_state.phuong_an_kha_thi,

        "Có khả năng tài chính trả nợ":
            st.session_state.kha_nang_tra_no,

        "Cam kết sử dụng vốn đúng mục đích":
            st.session_state.dung_muc_dich,

        "Cam kết hoàn trả nợ đúng hạn":
            st.session_state.tra_no_dung_han
    }

    ket_qua_dieu_kien = []

    for ten_dieu_kien, ket_qua in dieu_kien.items():

        if ket_qua == "Có":

            ket_qua_dieu_kien.append(
                [
                    ten_dieu_kien,
                    "Đạt",
                    "Đáp ứng"
                ]
            )

        elif ket_qua == "Không":

            ket_qua_dieu_kien.append(
                [
                    ten_dieu_kien,
                    "Không đạt",
                    "Không đáp ứng"
                ]
            )

        else:

            ket_qua_dieu_kien.append(
                [
                    ten_dieu_kien,
                    "Chưa đánh giá",
                    "Cần bổ sung thông tin"
                ]
            )

    df_dieu_kien = pd.DataFrame(
        ket_qua_dieu_kien,
        columns=[
            "Điều kiện",
            "Kết quả",
            "Đánh giá"
        ]
    )

    st.dataframe(
        df_dieu_kien,
        use_container_width=True,
        hide_index=True
    )

    tat_ca_dieu_kien_dat = all(
        value == "Có"
        for value in dieu_kien.values()
    )

    co_dieu_kien_khong_dat = any(
        value == "Không"
        for value in dieu_kien.values()
    )

    # =================================================
    # KHÔNG ĐẠT ĐIỀU KIỆN
    # =================================================

    if co_dieu_kien_khong_dat:

        st.divider()

        st.error(
            "🔴 KHÔNG ĐỦ ĐIỀU KIỆN VAY VỐN"
        )

        st.warning(
            """
            Doanh nghiệp chưa đáp ứng đầy đủ các điều kiện
            vay vốn cơ bản được kiểm tra trong hệ thống.

            Không thể chỉ dựa vào ROA, ROE, LNST hoặc LTV
            để kết luận doanh nghiệp đủ điều kiện vay vốn.
            """
        )

    # =================================================
    # CHƯA ĐÁNH GIÁ ĐỦ
    # =================================================

    elif not tat_ca_dieu_kien_dat:

        st.divider()

        st.warning(
            "🟡 CHƯA ĐỦ CƠ SỞ KẾT LUẬN"
        )

        st.info(
            """
            Một hoặc nhiều điều kiện vay vốn chưa được đánh giá.

            Vui lòng quay lại mục:
            ⚖️ Điều kiện vay vốn

            và hoàn thiện toàn bộ thông tin.
            """
        )

    # =================================================
    # ĐỦ ĐIỀU KIỆN CƠ BẢN
    # =================================================

    else:

        st.success(
            "🟢 DOANH NGHIỆP ĐÁP ỨNG CÁC ĐIỀU KIỆN VAY VỐN CƠ BẢN"
        )

        st.divider()

        # =================================================
        # 2. ĐÁNH GIÁ TÀI CHÍNH
        # =================================================

        st.subheader(
            "2️⃣ ĐÁNH GIÁ TÌNH HÌNH TÀI CHÍNH"
        )

        ket_qua_tai_chinh = []

        if st.session_state.lnst > 0:

            ket_qua_tai_chinh.append(
                [
                    "Lợi nhuận sau thuế",
                    "Tích cực",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )

        else:

            ket_qua_tai_chinh.append(
                [
                    "Lợi nhuận sau thuế",
                    "Rủi ro",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )

        if st.session_state.roa > 0:

            ket_qua_tai_chinh.append(
                [
                    "ROA",
                    "Tích cực",
                    f"{st.session_state.roa:.2f}%"
                ]
            )

        else:

            ket_qua_tai_chinh.append(
                [
                    "ROA",
                    "Rủi ro",
                    f"{st.session_state.roa:.2f}%"
                ]
            )

        if st.session_state.roe > 0:

            ket_qua_tai_chinh.append(
                [
                    "ROE",
                    "Tích cực",
                    f"{st.session_state.roe:.2f}%"
                ]
            )

        else:

            ket_qua_tai_chinh.append(
                [
                    "ROE",
                    "Rủi ro",
                    f"{st.session_state.roe:.2f}%"
                ]
            )

        if st.session_state.ty_le_no <= 70:

            ket_qua_tai_chinh.append(
                [
                    "Tỷ lệ nợ",
                    "Tương đối an toàn",
                    f"{st.session_state.ty_le_no:.2f}%"
                ]
            )

        else:

            ket_qua_tai_chinh.append(
                [
                    "Tỷ lệ nợ",
                    "Rủi ro cao",
                    f"{st.session_state.ty_le_no:.2f}%"
                ]
            )

        df_tai_chinh = pd.DataFrame(
            ket_qua_tai_chinh,
            columns=[
                "Chỉ tiêu",
                "Đánh giá",
                "Giá trị"
            ]
        )

        st.dataframe(
            df_tai_chinh,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # 3. KHẢ NĂNG TRẢ NỢ
        # =================================================

        st.subheader(
            "3️⃣ ĐÁNH GIÁ KHẢ NĂNG TRẢ NỢ"
        )

        dong_tien_du = (
            st.session_state.dong_tien
            >= st.session_state.tong_nghia_vu
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Dòng tiền HĐKD/tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )

        with c2:

            st.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

        with c3:

            if dong_tien_du:

                st.success(
                    "ĐỦ KHẢ NĂNG TRẢ NỢ"
                )

            else:

                st.error(
                    "CHƯA ĐỦ KHẢ NĂNG TRẢ NỢ"
                )

        # =================================================
        # 4. TÀI SẢN BẢO ĐẢM
        # =================================================

        st.subheader(
            "4️⃣ ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM"
        )

        if st.session_state.co_tsdb == "Không":

            tsdb_tot = True

            st.info(
                """
                Khoản vay không có tài sản bảo đảm.

                Việc cấp tín dụng cần căn cứ vào khả năng
                tài chính, dòng tiền và chính sách tín dụng
                của ngân hàng.
                """
            )

        elif st.session_state.ltv is None:

            tsdb_tot = False

            st.warning(
                "⚠️ Chưa có dữ liệu LTV để đánh giá."
            )

        elif st.session_state.ltv <= 70:

            tsdb_tot = True

            st.success(
                f"🟢 LTV = {st.session_state.ltv:.2f}%"
            )

        else:

            tsdb_tot = False

            st.warning(
                f"🟡 LTV = {st.session_state.ltv:.2f}% "
                "- Cần xem xét thêm."
            )

        # =================================================
        # 5. ĐÁNH GIÁ TỔNG HỢP
        # =================================================

        st.divider()

        st.subheader(
            "🎯 KẾT LUẬN THẨM ĐỊNH"
        )

        tai_chinh_tot = (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
            and st.session_state.ty_le_no <= 70
        )

        # =================================================
        # KẾT LUẬN 1
        # =================================================

        if (
            tat_ca_dieu_kien_dat
            and tai_chinh_tot
            and dong_tien_du
            and tsdb_tot
        ):

            st.success(
                "🟢 ĐỦ CƠ SỞ XEM XÉT CẤP TÍN DỤNG"
            )

            st.markdown(
                """
                <div class="success-card">

                <h3>📌 Kết luận hỗ trợ</h3>

                Doanh nghiệp đáp ứng các điều kiện vay vốn
                cơ bản được kiểm tra trong hệ thống.

                Kết quả tài chính tương đối tích cực,
                dòng tiền đáp ứng nghĩa vụ trả nợ được tính toán
                và tài sản bảo đảm có mức LTV phù hợp theo
                ngưỡng mô hình đang sử dụng.

                <br><br>

                <b>Đề xuất:</b>

                Có thể chuyển sang bước thẩm định tín dụng
                chi tiết và trình cấp có thẩm quyền xem xét.

                </div>
                """,
                unsafe_allow_html=True
            )

        # =================================================
        # KẾT LUẬN 2
        # =================================================

        elif (
            tat_ca_dieu_kien_dat
            and dong_tien_du
        ):

            st.warning(
                "🟡 ĐỦ ĐIỀU KIỆN VAY VỐN CƠ BẢN "
                "– CẦN THẨM ĐỊNH BỔ SUNG"
            )

            st.info(
                """
                Doanh nghiệp đã đáp ứng các điều kiện vay vốn
                cơ bản và dòng tiền hiện tại có khả năng đáp ứng
                nghĩa vụ trả nợ được tính toán.

                Tuy nhiên, kết quả tài chính hoặc tài sản bảo đảm
                chưa đủ tích cực để đưa ra đề xuất cho vay ngay.

                Cần tiếp tục kiểm tra:

                • Lịch sử tín dụng/CIC.

                • Báo cáo tài chính.

                • Chất lượng lợi nhuận.

                • Phương án kinh doanh.

                • Dòng tiền thực tế.

                • Tính pháp lý của tài sản bảo đảm.

                • Khả năng thanh khoản của TSĐB.

                • Các nghĩa vụ nợ hiện tại.

                • Chính sách tín dụng của ngân hàng.
                """
            )

        # =================================================
        # KẾT LUẬN 3
        # =================================================

        else:

            st.error(
                "🔴 CHƯA ĐỦ CƠ SỞ ĐỂ ĐỀ XUẤT CHO VAY"
            )

            st.info(
                """
                Doanh nghiệp có thể đã đáp ứng một số điều kiện
                vay vốn cơ bản, nhưng kết quả tài chính hoặc
                khả năng trả nợ chưa đáp ứng yêu cầu của mô hình.

                Cần xem xét và bổ sung:

                • Khả năng tạo dòng tiền.

                • Khả năng trả nợ.

                • Hiệu quả hoạt động kinh doanh.

                • Cơ cấu nợ.

                • Phương án sử dụng vốn.

                • Tài sản bảo đảm nếu có.

                • Các nghĩa vụ tài chính hiện tại.
                """
            )

        # =================================================
        # 6. BẢNG TÓM TẮT
        # =================================================

        st.divider()

        st.subheader(
            "📋 BẢNG TÓM TẮT THẨM ĐỊNH"
        )

        tong_hop = pd.DataFrame(
            [
                [
                    "Điều kiện vay vốn cơ bản",
                    "Đạt"
                    if tat_ca_dieu_kien_dat
                    else "Chưa đạt"
                ],
                [
                    "LNST",
                    "Tích cực"
                    if st.session_state.lnst > 0
                    else "Rủi ro"
                ],
                [
                    "ROA",
                    "Tích cực"
                    if st.session_state.roa > 0
                    else "Rủi ro"
                ],
                [
                    "ROE",
                    "Tích cực"
                    if st.session_state.roe > 0
                    else "Rủi ro"
                ],
                [
                    "Tỷ lệ nợ",
                    "Tương đối an toàn"
                    if st.session_state.ty_le_no <= 70
                    else "Rủi ro cao"
                ],
                [
                    "Khả năng trả nợ",
                    "Đạt"
                    if dong_tien_du
                    else "Chưa đạt"
                ],
                [
                    "Tài sản bảo đảm",
                    "Phù hợp"
                    if tsdb_tot
                    else "Cần xem xét"
                ]
            ],
            columns=[
                "Nội dung",
                "Kết quả"
            ]
        )

        st.dataframe(
            tong_hop,
            use_container_width=True,
            hide_index=True
        )

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả của hệ thống chỉ mang tính chất hỗ trợ
            thẩm định và không phải là quyết định cho vay tự động.

            ROA, ROE, LNST, tỷ lệ nợ, dòng tiền và LTV là các
            chỉ tiêu hỗ trợ phân tích rủi ro tín dụng.

            Các ngưỡng đánh giá trong ứng dụng là mô hình minh họa
            và cần được điều chỉnh theo chính sách tín dụng,
            sản phẩm tín dụng và quy định nội bộ của từng ngân hàng.

            Quyết định cấp tín dụng thực tế cần căn cứ vào hồ sơ
            khách hàng, lịch sử tín dụng/CIC, tình hình tài chính,
            phương án sử dụng vốn, khả năng trả nợ, tài sản bảo đảm
            nếu có, quy định pháp luật hiện hành và chính sách
            tín dụng của tổ chức tín dụng.
            """
        )

# =========================================================

# 12. FOOTER

# =========================================================

st.divider()

st.markdown(
""" <div class="footer">
    🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>

    <br>

    Công cụ hỗ trợ phân tích hồ sơ và đánh giá tín dụng

    <br><br>

</div>
""",
unsafe_allow_html=True

)
