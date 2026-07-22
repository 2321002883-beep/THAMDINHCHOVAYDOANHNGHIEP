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
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,

    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN HIỆN ĐẠI
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       NỀN CHUNG
    ========================= */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f5f8fc 0%,
                #eef4fb 50%,
                #f8fafc 100%
            );
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #071b35 0%,
                #0b2d52 50%,
                #123f68 100%
            );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.2);
    }

    /* =========================
       TIÊU ĐỀ
    ========================= */

    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        color: #0d3b66 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155a8a !important;
        font-weight: 700 !important;
    }

    /* =========================
       METRIC CARD
    ========================= */

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.95);
        border: 1px solid #d9e4f0;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(13,59,102,0.08);
        transition: 0.25s;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px rgba(13,59,102,0.14);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
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
        background:
            linear-gradient(
                135deg,
                #0b4f8a,
                #1479b8
            );
        box-shadow: 0 5px 15px rgba(11,79,138,0.22);
        transition: 0.25s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(11,79,138,0.3);
    }

    /* =========================
       INPUT
    ========================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"],
    textarea {
        border-radius: 10px !important;
    }

    /* =========================
       INFO / WARNING / SUCCESS
    ========================= */

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }

    /* =========================
       CARD TÙY CHỈNH
    ========================= */

    .hero-card {
        background:
            linear-gradient(
                135deg,
                #08264a,
                #0d5287,
                #1581b8
            );
        padding: 35px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 15px 35px rgba(8,38,74,0.22);
        margin-bottom: 25px;
    }

    .hero-card h1 {
        color: white !important;
        font-size: 32px;
        margin-bottom: 8px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.9);
        font-size: 16px;
        margin-bottom: 0;
    }

    .section-card {
        background: rgba(255,255,255,0.9);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #dce7f2;
        box-shadow: 0 6px 20px rgba(13,59,102,0.06);
        margin-bottom: 18px;
    }

    .status-good {
        background: #e9f8ef;
        border-left: 5px solid #1e9e58;
        padding: 15px;
        border-radius: 12px;
        color: #176b3c;
        font-weight: 700;
    }

    .status-warning {
        background: #fff7df;
        border-left: 5px solid #e4a400;
        padding: 15px;
        border-radius: 12px;
        color: #805f00;
        font-weight: 700;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 5px solid #d64545;
        padding: 15px;
        border-radius: 12px;
        color: #8c2525;
        font-weight: 700;
    }

    .footer {
        text-align: center;
        color: #70849a;
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
                HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH
            </div>
            <div style="
                font-size:15px;
                font-weight:600;
                opacity:0.85;
                margin-top:5px;
            ">
                CHO VAY DOANH NGHIỆP
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "📌 DANH MỤC CHỨC NĂNG",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "📈 Khả năng trả nợ",
            "🏠 Tài sản bảo đảm",
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
            <h1>🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</h1>
            <p>
                Phân tích hồ sơ • Đánh giá tài chính •
                Khả năng trả nợ • Tài sản bảo đảm •
                Hỗ trợ quyết định tín dụng
            </p>
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

    st.subheader("📊 TỔNG QUAN HỒ SƠ")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 Hồ sơ doanh nghiệp",
            "Đã nhập" if st.session_state.da_luu_ho_so else "Chưa nhập"
        )

    with c2:
        st.metric(
            "💰 Phân tích tài chính",
            "Đã phân tích" if st.session_state.da_phan_tich_tc else "Chưa phân tích"
        )

    with c3:
        st.metric(
            "💳 Khoản vay",
            "Đã tính" if st.session_state.da_phan_tich_vay else "Chưa tính"
        )

    with c4:
        st.metric(
            "🏠 Tài sản bảo đảm",
            "Đã phân tích" if st.session_state.da_phan_tich_tsdb else "Chưa phân tích"
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
            **02 | TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )

    with c3:
        st.info(
            """
            **03 | TRẢ NỢ**

            Phân tích dòng tiền,
            nghĩa vụ trả nợ và DSCR.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp điều kiện,
            chỉ tiêu và kết luận sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Ứng dụng chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ. Kết quả không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title("🏢 HỒ SƠ DOANH NGHIỆP")

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True
    )

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

    with c2:

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

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

    st.subheader("💳 Mục đích vay vốn")

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
        placeholder="Nhập mô tả chi tiết phương án kinh doanh và nhu cầu sử dụng vốn..."
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
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
            st.session_state.da_luu_ho_so = True

            st.success(
                "✅ Đã lưu thông tin hồ sơ doanh nghiệp."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title("⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN")

    st.info(
        """
        Phần này kiểm tra sơ bộ các nhóm điều kiện vay vốn.
        Đây là bước kiểm tra điều kiện, không phải mô hình
        chấm điểm tín dụng thay thế chính sách của ngân hàng.
        """
    )

    st.subheader("1️⃣ Điều kiện cơ bản")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Doanh nghiệp có năng lực pháp lý phù hợp?",
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

        st.session_state.muc_dich = st.selectbox(
            "Mục đích vay vốn có hợp pháp?",
            [
                "Chưa đánh giá",
                "Có",
                "Không"
            ],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(st.session_state.muc_dich)
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
            "Phương án sử dụng vốn có khả thi?",
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
            "Doanh nghiệp có khả năng tài chính trả nợ?",
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

    st.subheader("2️⃣ Cam kết của khách hàng")

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
# 8. PHÂN TÍCH TÀI CHÍNH
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
            💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu phân tích
            tài chính hỗ trợ thẩm định. Ngưỡng đánh giá cụ thể
            cần căn cứ vào ngành nghề, quy mô doanh nghiệp,
            lịch sử hoạt động và chính sách tín dụng của từng
            tổ chức tín dụng.
            """
        )


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title("💳 THÔNG TIN KHOẢN VAY")

    st.caption("Đơn vị nhập liệu: triệu đồng")

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
                "✅ Đã tính toán nghĩa vụ trả nợ."
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


# =========================================================
# 10. KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "📈 Khả năng trả nợ":

    st.title("📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ")

    st.info(
        """
        DSCR được sử dụng như một chỉ tiêu hỗ trợ để so sánh
        dòng tiền tạo ra với nghĩa vụ trả nợ. Ngưỡng cụ thể
        cần căn cứ chính sách tín dụng của từng ngân hàng.
        """
    )

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng nhập và tính khoản vay trước."
        )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Dòng tiền kinh doanh",
                f"{st.session_state.dong_tien:,.2f} triệu đồng/tháng"
            )

        with c2:

            st.metric(
                "Nghĩa vụ trả nợ",
                f"{st.session_state.tong_nghia_vu:,.2f} triệu đồng/tháng"
            )

        if st.button("📈 PHÂN TÍCH DSCR"):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )

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


# =========================================================
# 11. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title("🏠 TÀI SẢN BẢO ĐẢM")

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm của khoản vay.
        Tỷ lệ chấp nhận thực tế phụ thuộc vào loại tài sản, giá trị
        định giá, khả năng thanh khoản và chính sách của ngân hàng.
        """
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
                "Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "Giá trị tài sản bảo đảm phải lớn hơn 0."
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

            st.session_state.da_phan_tich_tsdb = True

            st.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "Mức LTV tương đối thấp theo mô hình hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả dưới đây được tổng hợp từ dữ liệu người dùng nhập.
        Ứng dụng không thay thế quy trình thẩm định tín dụng chính thức.
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

        # =================================================
        # KIỂM TRA ĐIỀU KIỆN VAY
        # =================================================

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        co_dieu_kien_khong = "Không" in dieu_kien
        co_chua_danh_gia = "Chưa đánh giá" in dieu_kien

        # =================================================
        # TỔNG HỢP
        # =================================================

        st.subheader("🏢 THÔNG TIN KHÁCH HÀNG")

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
            "Khoản vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        st.divider()

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

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
                và chính sách của tổ chức tín dụng.
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

        # =================================================
        # BẢNG CHI TIẾT
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        if st.session_state.nang_luc_phap_ly == "Có":
            ket_qua.append(
                ["Năng lực pháp lý", "Đạt", "Đang được đánh giá là Có"]
            )
        else:
            ket_qua.append(
                ["Năng lực pháp lý", "Cần xem xét", st.session_state.nang_luc_phap_ly]
            )

        if st.session_state.muc_dich == "Có":
            ket_qua.append(
                ["Mục đích vay", "Đạt", "Mục đích được đánh giá là hợp pháp"]
            )
        else:
            ket_qua.append(
                ["Mục đích vay", "Cần xem xét", st.session_state.muc_dich]
            )

        if st.session_state.co_phuong_an == "Có":
            ket_qua.append(
                ["Phương án sử dụng vốn", "Đạt", "Có phương án"]
            )
        else:
            ket_qua.append(
                ["Phương án sử dụng vốn", "Cần xem xét", st.session_state.co_phuong_an]
            )

        if st.session_state.phuong_an_kha_thi == "Có":
            ket_qua.append(
                ["Tính khả thi", "Đạt", "Phương án được đánh giá là khả thi"]
            )
        else:
            ket_qua.append(
                ["Tính khả thi", "Cần xem xét", st.session_state.phuong_an_kha_thi]
            )

        if st.session_state.kha_nang_tra_no == "Có":
            ket_qua.append(
                ["Khả năng tài chính trả nợ", "Đạt", "Được đánh giá là Có"]
            )
        else:
            ket_qua.append(
                ["Khả năng tài chính trả nợ", "Cần xem xét", st.session_state.kha_nang_tra_no]
            )

        if st.session_state.lnst > 0:
            ket_qua.append(
                ["LNST", "Tích cực", f"{st.session_state.lnst:,.2f} triệu đồng"]
            )
        else:
            ket_qua.append(
                ["LNST", "Cần xem xét", "LNST không dương"]
            )

        if st.session_state.roa > 0:
            ket_qua.append(
                ["ROA", "Tích cực", f"{st.session_state.roa:.2f}%"]
            )
        else:
            ket_qua.append(
                ["ROA", "Cần xem xét", f"{st.session_state.roa:.2f}%"]
            )

        if st.session_state.roe > 0:
            ket_qua.append(
                ["ROE", "Tích cực", f"{st.session_state.roe:.2f}%"]
            )
        else:
            ket_qua.append(
                ["ROE", "Cần xem xét", f"{st.session_state.roe:.2f}%"]
            )

        if st.session_state.dscr is not None:

            if st.session_state.dscr >= 1:
                ket_qua.append(
                    ["DSCR", "Tích cực", f"{st.session_state.dscr:.2f} lần"]
                )
            else:
                ket_qua.append(
                    ["DSCR", "Cần xem xét", f"{st.session_state.dscr:.2f} lần"]
                )

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
# 13. FOOTER
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
st.image("logo.png")
