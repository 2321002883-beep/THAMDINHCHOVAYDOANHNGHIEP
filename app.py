import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# 1. CẤU HÌNH
# =========================================================

st.set_page_config(
    page_title="Thẩm định doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. SESSION STATE
# =========================================================

DEFAULTS = {

    # Hồ sơ
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,

    # Điều kiện
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
    "tong_nghia_vu": None,

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,
}


for key, value in DEFAULTS.items():

    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown("""
<style>

/* ===== BODY ===== */

.stApp {
    background: #f8fafc;
}


/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #172554 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}


/* ===== HEADER ===== */

.hero {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e3a8a
    );

    padding: 30px 35px;
    border-radius: 22px;

    color: white;

    margin-bottom: 25px;

    box-shadow:
        0 10px 30px
        rgba(15, 23, 42, 0.15);
}

.hero-title {
    font-size: 32px;
    font-weight: 800;
}

.hero-sub {
    font-size: 15px;
    opacity: 0.85;
    margin-top: 8px;
}


/* ===== CARD ===== */

.card {
    background: white;

    padding: 22px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 5px 20px
        rgba(15, 23, 42, 0.06);

    margin-bottom: 18px;
}


/* ===== KPI ===== */

.kpi {
    background: white;

    padding: 20px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 5px 15px
        rgba(15, 23, 42, 0.05);

    text-align: center;
}

.kpi-title {
    font-size: 14px;
    color: #64748b;
}

.kpi-value {
    font-size: 28px;
    font-weight: 800;
    color: #0f172a;
}


/* ===== BUTTON ===== */

.stButton > button {

    border-radius: 12px;

    height: 48px;

    font-weight: 700;

    border: none;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        );

    color: white;

    box-shadow:
        0 5px 15px
        rgba(37, 99, 235, 0.25);
}


/* ===== RESULT ===== */

.result-success {

    background: #ecfdf5;

    border-left: 6px solid #10b981;

    padding: 25px;

    border-radius: 15px;

}

.result-warning {

    background: #fffbeb;

    border-left: 6px solid #f59e0b;

    padding: 25px;

    border-radius: 15px;

}

.result-danger {

    background: #fef2f2;

    border-left: 6px solid #ef4444;

    padding: 25px;

    border-radius: 15px;

}


/* ===== FOOTER ===== */

.footer {

    text-align: center;

    color: #64748b;

    padding: 30px;

    font-size: 13px;

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
        text-align:center;
        padding:20px 0;
        font-size:26px;
        font-weight:800;">
        🏦 CREDITCHECK
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "HỆ THỐNG HỖ TRỢ THẨM ĐỊNH TÍN DỤNG"
    )

    st.divider()

    menu = st.radio(
        "MENU",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay",
            "💰 Phân tích tài chính",
            "💳 Khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.markdown(
        "### 📌 TIẾN ĐỘ HỒ SƠ"
    )

    completed = 0

    if st.session_state.ten_dn:
        completed += 1

    if st.session_state.roa is not None:
        completed += 1

    if st.session_state.tong_nghia_vu is not None:
        completed += 1

    if st.session_state.ltv is not None:
        completed += 1

    progress = completed / 4

    st.progress(progress)

    st.caption(
        f"Đã hoàn thành {completed}/4 nhóm"
    )

    st.divider()

    st.caption("Version 2.0")
    st.caption("© 2026 CreditCheck")


# =========================================================
# 5. HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">

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


# =========================================================
# 6. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.title("👋 Xin chào!")

    st.write(
        "Chào mừng bạn đến với hệ thống hỗ trợ thẩm định "
        "cho vay doanh nghiệp."
    )

    st.divider()

    # KPI

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            """
            <div class="kpi">

            <div class="kpi-title">
            🏢 DOANH NGHIỆP
            </div>

            <div class="kpi-value">
            01
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="kpi">

            <div class="kpi-title">
            💰 PHÂN TÍCH TÀI CHÍNH
            </div>

            <div class="kpi-value">
            03
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="kpi">

            <div class="kpi-title">
            💳 KHOẢN VAY
            </div>

            <div class="kpi-value">
            01
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            """
            <div class="kpi">

            <div class="kpi-title">
            🏠 TÀI SẢN BẢO ĐẢM
            </div>

            <div class="kpi-value">
            01
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")

    st.subheader("🚀 Quy trình thẩm định")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.info(
            "### 01\n"
            "🏢 Hồ sơ doanh nghiệp\n\n"
            "Nhập thông tin pháp lý."
        )

    with c2:

        st.info(
            "### 02\n"
            "💰 Phân tích tài chính\n\n"
            "Đánh giá ROA, ROE, tỷ lệ nợ."
        )

    with c3:

        st.info(
            "### 03\n"
            "💳 Đánh giá khoản vay\n\n"
            "Phân tích khả năng trả nợ."
        )

    with c4:

        st.info(
            "### 04\n"
            "📊 Kết quả\n\n"
            "Tổng hợp và đề xuất."
        )


# =========================================================
# 7. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title("🏢 Hồ sơ doanh nghiệp")

    st.caption(
        "Nhập thông tin cơ bản của doanh nghiệp cần thẩm định."
    )

    st.subheader("📋 Thông tin doanh nghiệp")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp *",
            value=st.session_state.ten_dn
        )

        st.session_state.ma_so = st.text_input(
            "Mã số doanh nghiệp *",
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


    st.subheader("💳 Mục đích vay")

    muc_dich = st.selectbox(
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
        placeholder="Nhập mô tả ngắn gọn phương án sử dụng vốn..."
    )


    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
    ):

        if not st.session_state.ten_dn:

            st.error(
                "Vui lòng nhập tên doanh nghiệp."
            )

        else:

            st.success(
                f"✅ Đã lưu hồ sơ: "
                f"{st.session_state.ten_dn}"
            )


# =========================================================
# 8. ĐIỀU KIỆN VAY
# =========================================================

elif menu == "⚖️ Điều kiện vay":

    st.title("⚖️ Điều kiện vay vốn")

    st.caption(
        "Kiểm tra sơ bộ các điều kiện cơ bản của hồ sơ."
    )

    st.subheader("1️⃣ Điều kiện pháp lý")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Năng lực pháp luật dân sự",
            ["Chưa đánh giá", "Có", "Không"]
        )

        st.session_state.muc_dich = st.selectbox(
            "Mục đích vay hợp pháp",
            ["Chưa đánh giá", "Có", "Không"]
        )

        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn",
            ["Chưa đánh giá", "Có", "Không"]
        )

    with c2:

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn khả thi",
            ["Chưa đánh giá", "Có", "Không"]
        )

        st.session_state.kha_nang_tra_no = st.selectbox(
            "Có khả năng tài chính trả nợ",
            ["Chưa đánh giá", "Có", "Không"]
        )


    st.subheader("2️⃣ Cam kết khách hàng")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích",
            ["Chưa đánh giá", "Có", "Không"]
        )

    with c2:

        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết hoàn trả nợ đúng hạn",
            ["Chưa đánh giá", "Có", "Không"]
        )

    st.success(
        "✅ Thông tin điều kiện vay đã được cập nhật."
    )


# =========================================================
# 9. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 Phân tích tài chính")

    st.caption(
        "Đơn vị tính: triệu đồng"
    )

    st.subheader("📊 Nhập dữ liệu tài chính")

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
        "📊 PHÂN TÍCH NGAY"
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
                "✅ Phân tích tài chính hoàn tất."
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
# 10. KHOẢN VAY
# =========================================================

elif menu == "💳 Khoản vay":

    st.title("💳 Thông tin khoản vay")

    st.caption(
        "Nhập thông tin khoản vay và đánh giá nghĩa vụ trả nợ."
    )

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
            "💳 Nghĩa vụ nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu
        )


    if st.button(
        "💳 TÍNH KHẢ NĂNG TRẢ NỢ"
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

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc/tháng",
            f"{tien_goc:,.2f}"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{tien_lai:,.2f}"
        )

        c3.metric(
            "Tổng nghĩa vụ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )

        st.success(
            "✅ Đã hoàn thành tính toán nghĩa vụ trả nợ."
        )


# =========================================================
# 11. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title("🏠 Tài sản bảo đảm")

    st.caption(
        "Đánh giá sơ bộ tỷ lệ khoản vay trên giá trị tài sản bảo đảm."
    )

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "🏠 Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button(
        "🏠 PHÂN TÍCH TSĐB"
    ):

        if st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.info(
                "Khoản vay không có tài sản bảo đảm."
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

            st.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ở mức tương đối thấp "
                    "theo mô hình minh họa."
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
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 Kết quả thẩm định")

    st.caption(
        "Tổng hợp tự động các thông tin đã nhập và phân tích."
    )


    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    if (
        st.session_state.roa is None
        or st.session_state.tong_nghia_vu is None
    ):

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết quả cuối cùng."
        )

        st.info("""
        Vui lòng hoàn thành:

        1. 💰 Phân tích tài chính
        2. 💳 Phân tích khoản vay
        3. 🏠 Phân tích tài sản bảo đảm nếu có

        Sau đó quay lại trang này.
        """)


    else:

        # =================================================
        # TÍNH ĐIỂM
        # =================================================

        diem = 0
        tong_diem = 100

        ket_qua = []


        # Điều kiện pháp lý

        if st.session_state.nang_luc_phap_ly == "Có":
            diem += 15
            ket_qua.append(
                ["Năng lực pháp lý", "Đạt", "15/15"]
            )
        else:
            ket_qua.append(
                ["Năng lực pháp lý", "Không đạt", "0/15"]
            )


        # Mục đích vay

        if st.session_state.muc_dich == "Có":
            diem += 10
            ket_qua.append(
                ["Mục đích vay", "Đạt", "10/10"]
            )
        else:
            ket_qua.append(
                ["Mục đích vay", "Không đạt", "0/10"]
            )


        # Phương án

        if st.session_state.phuong_an_kha_thi == "Có":
            diem += 10
            ket_qua.append(
                ["Phương án sử dụng vốn", "Đạt", "10/10"]
            )
        else:
            ket_qua.append(
                ["Phương án sử dụng vốn", "Không đạt", "0/10"]
            )


        # LNST

        if st.session_state.lnst > 0:

            diem += 15

            ket_qua.append(
                ["LNST", "Đạt",
                 f"{st.session_state.lnst:,.0f} triệu"]
            )

        else:

            ket_qua.append(
                ["LNST", "Không đạt",
                 f"{st.session_state.lnst:,.0f} triệu"]
            )


        # ROA

        if st.session_state.roa > 0:

            diem += 10

            ket_qua.append(
                ["ROA", "Đạt",
                 f"{st.session_state.roa:.2f}%"]
            )

        else:

            ket_qua.append(
                ["ROA", "Không đạt",
                 f"{st.session_state.roa:.2f}%"]
            )


        # ROE

        if st.session_state.roe > 0:

            diem += 10

            ket_qua.append(
                ["ROE", "Đạt",
                 f"{st.session_state.roe:.2f}%"]
            )

        else:

            ket_qua.append(
                ["ROE", "Không đạt",
                 f"{st.session_state.roe:.2f}%"]
            )


        # Tỷ lệ nợ

        if st.session_state.ty_le_no <= 70:

            diem += 10

            ket_qua.append(
                ["Tỷ lệ nợ", "Đạt",
                 f"{st.session_state.ty_le_no:.2f}%"]
            )

        else:

            ket_qua.append(
                ["Tỷ lệ nợ", "Không đạt",
                 f"{st.session_state.ty_le_no:.2f}%"]
            )


        # Khả năng trả nợ

        if (
            st.session_state.dong_tien
            >= st.session_state.tong_nghia_vu
        ):

            diem += 10

            ket_qua.append(
                ["Khả năng trả nợ", "Đạt",
                 "Dòng tiền đáp ứng nghĩa vụ"]
            )

        else:

            ket_qua.append(
                ["Khả năng trả nợ", "Không đạt",
                 "Dòng tiền chưa đáp ứng"]
            )


        # LTV

        if st.session_state.ltv is not None:

            if st.session_state.ltv <= 70:

                diem += 10

                ket_qua.append(
                    ["LTV", "Đạt",
                     f"{st.session_state.ltv:.2f}%"]
                )

            else:

                ket_qua.append(
                    ["LTV", "Không đạt",
                     f"{st.session_state.ltv:.2f}%"]
                )

        else:

            diem += 10

            ket_qua.append(
                ["TSĐB", "Không áp dụng",
                 "Khoản vay không có TSĐB"]
            )


        # =================================================
        # HIỂN THỊ ĐIỂM
        # =================================================

        st.subheader(
            "🎯 KẾT QUẢ TỔNG HỢP"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "ĐIỂM THẨM ĐỊNH",
            f"{diem}/100"
        )

        c2.metric(
            "ROA",
            f"{st.session_state.roa:.2f}%"
        )

        c3.metric(
            "LTV",
            (
                f"{st.session_state.ltv:.2f}%"
                if st.session_state.ltv is not None
                else "N/A"
            )
        )


        st.progress(
            diem / 100
        )


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader(
            "📌 KẾT LUẬN"
        )


        if diem >= 80:

            st.markdown(
                """
                <div class="result-success">

                <h2>🟢 ĐỀ XUẤT CHO VAY</h2>

                <p>
                Hồ sơ có mức điểm thẩm định cao.
                Doanh nghiệp đáp ứng tương đối tốt các tiêu chí
                trong mô hình đánh giá.
                </p>

                <b>Khuyến nghị:</b>
                Có thể chuyển sang bước thẩm định tín dụng chi tiết.

                </div>
                """,
                unsafe_allow_html=True
            )


        elif diem >= 60:

            st.markdown(
                """
                <div class="result-warning">

                <h2>🟡 CẦN THẨM ĐỊNH BỔ SUNG</h2>

                <p>
                Hồ sơ có một số tiêu chí chưa đạt.
                Cần kiểm tra thêm dòng tiền, khả năng trả nợ,
                lịch sử tín dụng và tài sản bảo đảm.
                </p>

                <b>Khuyến nghị:</b>
                Chưa nên đưa ra quyết định cuối cùng.

                </div>
                """,
                unsafe_allow_html=True
            )


        else:

            st.markdown(
                """
                <div class="result-danger">

                <h2>🔴 KHÔNG ĐỀ XUẤT CHO VAY</h2>

                <p>
                Hồ sơ có mức điểm thấp và tồn tại nhiều yếu tố
                rủi ro theo mô hình đánh giá.
                </p>

                <b>Khuyến nghị:</b>
                Cần xem xét lại hồ sơ hoặc bổ sung điều kiện tín dụng.

                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # BẢNG CHI TIẾT
        # =================================================

        st.subheader(
            "📋 Chi tiết kết quả thẩm định"
        )

        df = pd.DataFrame(
            ket_qua,
            columns=[
                "Tiêu chí",
                "Kết quả",
                "Đánh giá"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


        st.info("""
        ⚠️ **Lưu ý:** Điểm số và ngưỡng phân loại trong ứng dụng
        là mô hình minh họa phục vụ mục đích học tập và hỗ trợ
        thẩm định. Không phải tiêu chuẩn pháp lý bắt buộc chung
        áp dụng cho mọi tổ chức tín dụng.
        """)


# =========================================================
# 13. FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    🏦 <b>CREDITCHECK</b> — HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
    CHO VAY DOANH NGHIỆP

    <br><br>

    Điều kiện vay • Tài chính • Khả năng trả nợ • TSĐB

    <br><br>

    © 2026

    </div>
    """,
    unsafe_allow_html=True
)
