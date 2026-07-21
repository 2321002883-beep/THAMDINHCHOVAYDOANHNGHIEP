```python
import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="CreditVision - Thẩm định cho vay doanh nghiệp",
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
    "ltv": None,

    # Trạng thái
    "ho_so_da_luu": False,
    "tai_chinh_da_phan_tich": False,
    "khoan_vay_da_phan_tich": False,
    "tsdb_da_phan_tich": False,
}


for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       TOÀN BỘ ỨNG DỤNG
    ================================= */

    .stApp {
        background-color: #f4f7fb;
    }

    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #071d35 0%,
            #0b3157 50%,
            #0d4778 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #0b3157 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0d4778 !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #155a8a !important;
        font-weight: 700 !important;
    }

    /* ================================
       KPI CARD
    ================================= */

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #d9e5f0;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0px 5px 18px rgba(11, 49, 87, 0.08);
    }

    div[data-testid="stMetric"] label {
        color: #58738d !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3157 !important;
        font-weight: 800 !important;
    }

    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        min-height: 45px;
        font-weight: 700;
        border: none;
        background: linear-gradient(
            90deg,
            #0b5ea8,
            #1683d8
        );
        color: white;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #084b87,
            #0b6fba
        );
        transform: translateY(-2px);
        box-shadow: 0px 5px 15px rgba(11, 94, 168, 0.25);
    }

    /* ================================
       INPUT
    ================================= */

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea {
        border-radius: 9px;
    }

    /* ================================
       INFO BOX
    ================================= */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* ================================
       CUSTOM HERO
    ================================= */

    .hero-box {
        background: linear-gradient(
            135deg,
            #082b4c 0%,
            #0b5ea8 55%,
            #1683d8 100%
        );
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0px 10px 30px rgba(11, 94, 168, 0.25);
    }

    .hero-logo {
        font-size: 52px;
        margin-bottom: 5px;
    }

    .hero-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    .hero-subtitle {
        font-size: 16px;
        margin-top: 12px;
        opacity: 0.9;
    }

    /* ================================
       SIDEBAR LOGO
    ================================= */

    .sidebar-logo {
        text-align: center;
        padding: 10px;
    }

    .sidebar-logo-icon {
        font-size: 55px;
    }

    .sidebar-logo-title {
        font-size: 18px;
        font-weight: 800;
    }

    .sidebar-logo-subtitle {
        font-size: 12px;
        opacity: 0.8;
    }

    /* ================================
       PROCESS CARD
    ================================= */

    .process-card {
        background-color: white;
        border-radius: 16px;
        padding: 22px;
        min-height: 190px;
        border: 1px solid #dce7f1;
        box-shadow: 0px 5px 18px rgba(11, 49, 87, 0.06);
    }

    .process-number {
        font-size: 28px;
        font-weight: 800;
        color: #0b6fba;
    }

    .process-icon {
        font-size: 30px;
    }

    .process-title {
        font-weight: 800;
        color: #0b3157;
        margin-top: 10px;
    }

    .process-text {
        color: #63788c;
        font-size: 14px;
        margin-top: 8px;
    }

    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        color: #71859a;
        padding: 20px;
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
        <div class="sidebar-logo">
            <div class="sidebar-logo-icon">🏦</div>
            <div class="sidebar-logo-title">
                CREDITVISION
            </div>
            <div class="sidebar-logo-subtitle">
                HỆ THỐNG THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 📌 MENU CHỨC NĂNG")

    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        """
        <div style="
            background: rgba(255,255,255,0.10);
            padding: 15px;
            border-radius: 12px;
            font-size: 13px;
        ">
        💡 <b>Hướng dẫn:</b><br><br>
        1️⃣ Nhập hồ sơ doanh nghiệp<br>
        2️⃣ Kiểm tra điều kiện vay<br>
        3️⃣ Phân tích tài chính<br>
        4️⃣ Nhập thông tin khoản vay<br>
        5️⃣ Đánh giá tài sản bảo đảm<br>
        6️⃣ Xem kết quả thẩm định
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
        <div class="hero-box">

            <div class="hero-logo">
                🏦
            </div>

            <div class="hero-title">
                CREDITVISION
            </div>

            <div class="hero-subtitle">
                HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP
                <br><br>
                Phân tích tài chính • Khả năng trả nợ •
                Tài sản bảo đảm • Hỗ trợ ra quyết định tín dụng
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👋 Chào mừng bạn đến với CreditVision")

    st.info(
        "Hệ thống hỗ trợ cán bộ tín dụng và người học "
        "thực hiện đánh giá sơ bộ hồ sơ vay vốn doanh nghiệp "
        "thông qua các chỉ tiêu tài chính, khả năng trả nợ "
        "và tài sản bảo đảm."
    )

    st.divider()

    st.subheader("📊 TỔNG QUAN HỆ THỐNG")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 HỒ SƠ DOANH NGHIỆP",
            "01"
        )

    with c2:
        st.metric(
            "💰 CHỈ TIÊU TÀI CHÍNH",
            "03"
        )

    with c3:
        st.metric(
            "💳 KHOẢN VAY",
            "01"
        )

    with c4:
        st.metric(
            "📊 KẾT QUẢ",
            "AI"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">01</div>
                <div class="process-icon">🏢</div>
                <div class="process-title">
                    HỒ SƠ DOANH NGHIỆP
                </div>
                <div class="process-text">
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
            <div class="process-card">
                <div class="process-number">02</div>
                <div class="process-icon">💰</div>
                <div class="process-title">
                    PHÂN TÍCH TÀI CHÍNH
                </div>
                <div class="process-text">
                    Đánh giá LNST, ROA, ROE
                    và tỷ lệ nợ.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">03</div>
                <div class="process-icon">💳</div>
                <div class="process-title">
                    KHẢ NĂNG TRẢ NỢ
                </div>
                <div class="process-text">
                    Phân tích nghĩa vụ trả nợ
                    và dòng tiền doanh nghiệp.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-number">04</div>
                <div class="process-icon">📊</div>
                <div class="process-title">
                    KẾT QUẢ THẨM ĐỊNH
                </div>
                <div class="process-text">
                    Tổng hợp điểm đánh giá
                    và đề xuất tín dụng.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.warning(
        "⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ "
        "thẩm định, không thay thế quyết định tín dụng thực tế "
        "của tổ chức tín dụng."
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title("🏢 HỒ SƠ DOANH NGHIỆP")

    st.info(
        "Vui lòng nhập đầy đủ thông tin cơ bản của doanh nghiệp."
    )

    st.subheader("📋 Thông tin doanh nghiệp")

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
            max_value=200,
            value=st.session_state.thoi_gian_hd,
            step=1
        )

    st.divider()

    st.subheader("💳 Mục đích vay vốn")

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
        placeholder="Mô tả chi tiết phương án kinh doanh hoặc sử dụng vốn..."
    )

    st.divider()

    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP",
        type="primary"
    ):

        if not st.session_state.ten_dn.strip():

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        elif not st.session_state.ma_so.strip():

            st.error(
                "❌ Vui lòng nhập mã số doanh nghiệp."
            )

        elif not st.session_state.phuong_an.strip():

            st.error(
                "❌ Vui lòng mô tả phương án sử dụng vốn."
            )

        else:

            st.session_state.ho_so_da_luu = True

            st.success(
                "✅ Đã lưu hồ sơ doanh nghiệp thành công."
            )

    if st.session_state.ho_so_da_luu:

        st.divider()

        st.subheader("📌 TÓM TẮT HỒ SƠ")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Tên doanh nghiệp",
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


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title("⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN")

    st.info(
        "Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ "
        "khả năng đáp ứng điều kiện vay vốn của doanh nghiệp."
    )

    st.subheader("1️⃣ Điều kiện cơ bản")

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

    st.subheader("2️⃣ Cam kết của doanh nghiệp")

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

    st.divider()

    danh_sach_dieu_kien = [
        st.session_state.nang_luc_phap_ly,
        st.session_state.muc_dich,
        st.session_state.co_phuong_an,
        st.session_state.phuong_an_kha_thi,
        st.session_state.kha_nang_tra_no,
        st.session_state.dung_muc_dich,
        st.session_state.tra_no_dung_han
    ]

    so_dat = danh_sach_dieu_kien.count("Có")

    so_khong_dat = danh_sach_dieu_kien.count("Không")

    so_chua_danh_gia = danh_sach_dieu_kien.count(
        "Chưa đánh giá"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "✅ Tiêu chí đạt",
        so_dat
    )

    c2.metric(
        "❌ Tiêu chí không đạt",
        so_khong_dat
    )

    c3.metric(
        "⏳ Chưa đánh giá",
        so_chua_danh_gia
    )

    if so_khong_dat > 0:

        st.error(
            "🔴 Doanh nghiệp đang có tiêu chí chưa đáp ứng. "
            "Cần xem xét và bổ sung hồ sơ."
        )

    elif so_chua_danh_gia > 0:

        st.warning(
            "🟡 Vui lòng hoàn thành toàn bộ tiêu chí "
            "trước khi kết luận."
        )

    else:

        st.success(
            "🟢 Doanh nghiệp đã đáp ứng các tiêu chí "
            "sơ bộ được thiết lập."
        )


# =========================================================
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    st.subheader("📊 Nhập số liệu tài chính")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu,
            step=100.0
        )

        st.session_state.lnst = st.number_input(
            "Lợi nhuận sau thuế (LNST)",
            value=st.session_state.lnst,
            step=100.0
        )

        st.session_state.tong_tai_san = st.number_input(
            "Tổng tài sản",
            min_value=0.0,
            value=st.session_state.tong_tai_san,
            step=100.0
        )

    with c2:

        st.session_state.von_chu_so_huu = st.number_input(
            "Vốn chủ sở hữu",
            min_value=0.0,
            value=st.session_state.von_chu_so_huu,
            step=100.0
        )

        st.session_state.no_phai_tra = st.number_input(
            "Nợ phải trả",
            min_value=0.0,
            value=st.session_state.no_phai_tra,
            step=100.0
        )

        st.session_state.dong_tien = st.number_input(
            "Dòng tiền từ hoạt động kinh doanh",
            value=st.session_state.dong_tien,
            step=100.0
        )

    st.divider()

    if st.button(
        "📊 PHÂN TÍCH TÀI CHÍNH",
        type="primary"
    ):

        if st.session_state.tong_tai_san <= 0:

            st.error(
                "❌ Tổng tài sản phải lớn hơn 0."
            )

        elif st.session_state.von_chu_so_huu <= 0:

            st.error(
                "❌ Vốn chủ sở hữu phải lớn hơn 0."
            )

        elif st.session_state.no_phai_tra < 0:

            st.error(
                "❌ Nợ phải trả không được âm."
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

            st.session_state.tai_chinh_da_phan_tich = True

            st.success(
                "✅ Đã phân tích tài chính thành công."
            )

    if st.session_state.tai_chinh_da_phan_tich:

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
            "TỶ LỆ NỢ",
            f"{st.session_state.ty_le_no:.2f}%"
        )

        st.divider()

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

        if st.session_state.roa > 0:

            st.success(
                "🟢 ROA dương: Doanh nghiệp đang tạo ra lợi nhuận "
                "từ tài sản."
            )

        else:

            st.error(
                "🔴 ROA không dương: Cần xem xét hiệu quả sử dụng tài sản."
            )

        if st.session_state.roe > 0:

            st.success(
                "🟢 ROE dương: Vốn chủ sở hữu đang tạo ra lợi nhuận."
            )

        else:

            st.error(
                "🔴 ROE không dương: Cần xem xét hiệu quả sử dụng vốn."
            )

        if st.session_state.ty_le_no <= 70:

            st.success(
                "🟢 Tỷ lệ nợ không vượt mức 70% theo tiêu chí hỗ trợ."
            )

        else:

            st.warning(
                "🟡 Tỷ lệ nợ cao, cần xem xét thêm khả năng trả nợ."
            )


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title("💳 THÔNG TIN KHOẢN VAY")

    st.caption(
        "Đơn vị: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "Số tiền vay",
            min_value=0.0,
            value=st.session_state.so_tien_vay,
            step=100.0
        )

        st.session_state.thoi_gian_vay = st.number_input(
            "Thời hạn vay (tháng)",
            min_value=1,
            max_value=360,
            value=st.session_state.thoi_gian_vay,
            step=1
        )

    with c2:

        st.session_state.lai_suat = st.number_input(
            "Lãi suất (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat,
            step=0.1
        )

        st.session_state.nghia_vu_no_cu = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu,
            step=10.0
        )

    st.divider()

    if st.button(
        "💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ",
        type="primary"
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

            st.session_state.khoan_vay_da_phan_tich = True

            st.success(
                "✅ Đã tính toán nghĩa vụ trả nợ."
            )

    if st.session_state.khoan_vay_da_phan_tich:

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

        st.divider()

        st.subheader(
            "📊 KẾT QUẢ NGHĨA VỤ TRẢ NỢ"
        )

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

        st.info(
            f"Dòng tiền hoạt động kinh doanh hiện tại: "
            f"{st.session_state.dong_tien:,.2f} triệu đồng/tháng."
        )

        if st.session_state.dong_tien >= st.session_state.tong_nghia_vu:

            st.success(
                "🟢 Dòng tiền hiện tại có khả năng đáp ứng "
                "nghĩa vụ trả nợ theo tiêu chí hỗ trợ."
            )

        else:

            st.warning(
                "🟡 Dòng tiền hiện tại chưa đủ để đáp ứng "
                "toàn bộ nghĩa vụ trả nợ."
            )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title("🏠 TÀI SẢN BẢO ĐẢM")

    st.info(
        "LTV = Số tiền vay / Giá trị tài sản bảo đảm × 100%. "
        "Chỉ tiêu này được sử dụng để hỗ trợ đánh giá mức độ "
        "bảo đảm của khoản vay."
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
        value=st.session_state.gia_tri_tsdb,
        step=100.0
    )

    st.divider()

    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM",
        type="primary"
    ):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.error(
                "❌ Vui lòng xác định khoản vay có TSĐB hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.tsdb_da_phan_tich = True

            st.info(
                "Khoản vay không có tài sản bảo đảm."
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

            st.session_state.tsdb_da_phan_tich = True

            st.success(
                "✅ Đã phân tích tài sản bảo đảm."
            )

    if st.session_state.tsdb_da_phan_tich:

        st.divider()

        if st.session_state.ltv is None:

            st.metric(
                "LTV",
                "Không áp dụng"
            )

        else:

            st.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ≤ 70%: Mức tài trợ tương đối an toàn "
                    "theo tiêu chí hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 LTV từ 70% đến 100%: Cần xem xét thêm "
                    "chất lượng và tính thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 LTV > 100%: Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 11. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH")

    st.write(
        "Hệ thống tổng hợp các chỉ tiêu tài chính, "
        "khả năng trả nợ và tài sản bảo đảm."
    )

    # -----------------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # -----------------------------------------------------

    if not st.session_state.tai_chinh_da_phan_tich:

        st.warning(
            "⚠️ Chưa có dữ liệu phân tích tài chính."
        )

        st.info(
            "Vui lòng vào mục '💰 Phân tích tài chính' "
            "và thực hiện phân tích trước."
        )

    elif not st.session_state.khoan_vay_da_phan_tich:

        st.warning(
            "⚠️ Chưa có dữ liệu khoản vay."
        )

        st.info(
            "Vui lòng vào mục '💳 Thông tin khoản vay' "
            "và thực hiện phân tích khả năng trả nợ trước."
        )

    elif not st.session_state.tsdb_da_phan_tich:

        st.warning(
            "⚠️ Chưa có kết quả phân tích tài sản bảo đảm."
        )

        st.info(
            "Vui lòng vào mục '🏠 Tài sản bảo đảm' "
            "và thực hiện phân tích trước."
        )

    else:

        # -------------------------------------------------
        # TÍNH ĐIỂM
        # -------------------------------------------------

        diem = 0

        diem_toi_da = 90

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
                    "Khoản vay không có TSĐB"
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

        # -------------------------------------------------
        # TỶ LỆ ĐIỂM
        # -------------------------------------------------

        ty_le_diem = (
            diem
            / diem_toi_da
            * 100
        )

        # -------------------------------------------------
        # HIỂN THỊ TỔNG QUAN
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "🎯 TỔNG QUAN KẾT QUẢ"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🎯 ĐIỂM THẨM ĐỊNH",
            f"{diem}/{diem_toi_da}"
        )

        c2.metric(
            "📈 ROA",
            f"{st.session_state.roa:.2f}%"
        )

        c3.metric(
            "📊 ROE",
            f"{st.session_state.roe:.2f}%"
        )

        c4.metric(
            "🏠 LTV",
            (
                f"{st.session_state.ltv:.2f}%"
                if st.session_state.ltv is not None
                else "Không áp dụng"
            )
        )

        st.progress(
            min(ty_le_diem / 100, 1.0)
        )

        st.caption(
            f"Mức điểm đạt được: {ty_le_diem:.1f}%"
        )

        # -------------------------------------------------
        # KẾT LUẬN
        # -------------------------------------------------

        st.divider()

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH"
        )

        if ty_le_diem >= 80:

            st.success(
                "🟢 ĐỀ XUẤT CHO VAY"
            )

            st.write(
                f"Doanh nghiệp đạt mức đánh giá "
                f"{ty_le_diem:.1f}%."
            )

            st.info(
                "Hồ sơ có kết quả tương đối tích cực "
                "theo mô hình hỗ trợ. Có thể chuyển sang "
                "bước thẩm định tín dụng chi tiết."
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
                "lịch sử tín dụng, phương án sử dụng vốn "
                "và tài sản bảo đảm."
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
                "theo mô hình đánh giá. Cần xem xét "
                "bổ sung hoặc điều chỉnh phương án vay."
            )

        # -------------------------------------------------
        # BẢNG CHI TIẾT
        # -------------------------------------------------

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

        st.divider()

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả trên chỉ mang tính chất hỗ trợ thẩm định.

            ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu hỗ trợ
            phân tích tín dụng, không phải điều kiện pháp lý
            bắt buộc chung cho mọi doanh nghiệp.

            Quyết định cho vay thực tế cần dựa trên tổng thể hồ sơ,
            lịch sử tín dụng, dòng tiền, phương án kinh doanh,
            năng lực tài chính, tài sản bảo đảm và chính sách
            tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 12. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🏦 <b>CREDITVISION</b> |
        Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp
        <br>
        © 2026 - Ứng dụng phục vụ mục đích học tập và hỗ trợ phân tích
    </div>
    """,
    unsafe_allow_html=True
)
```
