import streamlit as st
import pandas as pd
from pathlib import Path


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
# 2. LOGO
# =========================================================

LOGO_PATH = Path(__file__).parent / "logo.png"


# =========================================================
# 3. CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

section[data-testid="stSidebar"] * {
    color: white;
}

.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
}

.sub-title {
    font-size: 16px;
    color: #64748b;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 3px 10px rgba(15,23,42,.05);
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 4. KHỞI TẠO SESSION STATE
# =========================================================

# Hồ sơ doanh nghiệp
if "ten_dn" not in st.session_state:
    st.session_state.ten_dn = ""

if "ma_so" not in st.session_state:
    st.session_state.ma_so = ""

# Điều kiện vay vốn
if "nang_luc_phap_ly" not in st.session_state:
    st.session_state.nang_luc_phap_ly = "Chưa đánh giá"

if "muc_dich" not in st.session_state:
    st.session_state.muc_dich = "Chưa đánh giá"

if "co_phuong_an" not in st.session_state:
    st.session_state.co_phuong_an = "Chưa đánh giá"

if "phuong_an_kha_thi" not in st.session_state:
    st.session_state.phuong_an_kha_thi = "Chưa đánh giá"

if "kha_nang_tra_no" not in st.session_state:
    st.session_state.kha_nang_tra_no = "Chưa đánh giá"

if "dung_muc_dich" not in st.session_state:
    st.session_state.dung_muc_dich = "Chưa đánh giá"

if "tra_no_dung_han" not in st.session_state:
    st.session_state.tra_no_dung_han = "Chưa đánh giá"


# Phân tích tài chính
if "doanh_thu" not in st.session_state:
    st.session_state.doanh_thu = 0.0

if "lnst" not in st.session_state:
    st.session_state.lnst = 0.0

if "tong_tai_san" not in st.session_state:
    st.session_state.tong_tai_san = 0.0

if "von_chu_so_huu" not in st.session_state:
    st.session_state.von_chu_so_huu = 0.0

if "no_phai_tra" not in st.session_state:
    st.session_state.no_phai_tra = 0.0

if "dong_tien" not in st.session_state:
    st.session_state.dong_tien = 0.0

if "roa" not in st.session_state:
    st.session_state.roa = None

if "roe" not in st.session_state:
    st.session_state.roe = None

if "ty_le_no" not in st.session_state:
    st.session_state.ty_le_no = None


# Khoản vay
if "so_tien_vay" not in st.session_state:
    st.session_state.so_tien_vay = 0.0

if "thoi_gian_vay" not in st.session_state:
    st.session_state.thoi_gian_vay = 12

if "lai_suat" not in st.session_state:
    st.session_state.lai_suat = 0.0

if "nghia_vu_no_cu" not in st.session_state:
    st.session_state.nghia_vu_no_cu = 0.0

if "tong_nghia_vu" not in st.session_state:
    st.session_state.tong_nghia_vu = None


# Tài sản bảo đảm
if "co_tsdb" not in st.session_state:
    st.session_state.co_tsdb = "Chưa đánh giá"

if "gia_tri_tsdb" not in st.session_state:
    st.session_state.gia_tri_tsdb = 0.0

if "ltv" not in st.session_state:
    st.session_state.ltv = None


# =========================================================
# 5. SIDEBAR
# =========================================================

with st.sidebar:

    if LOGO_PATH.exists():
        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    st.divider()

    st.markdown(
        "### 🏦 HỆ THỐNG THẨM ĐỊNH"
    )

    st.caption(
        "Hỗ trợ thẩm định cho vay doanh nghiệp"
    )

    st.divider()

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

    st.caption("Phiên bản 1.0")
    st.caption("© 2026")


# =========================================================
# 6. HEADER
# =========================================================

col_logo, col_header = st.columns([1, 5])

with col_logo:

    if LOGO_PATH.exists():
        st.image(
            str(LOGO_PATH),
            width=130
        )
    else:
        st.write("🏦")


with col_header:

    st.markdown(
        '<div class="main-title">'
        '🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH'
        '<br>'
        'CHO VAY DOANH NGHIỆP'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Điều kiện vay vốn • Phân tích tài chính • '
        'Khả năng trả nợ • Tài sản bảo đảm'
        '</div>',
        unsafe_allow_html=True
    )


st.divider()


# =========================================================
# 7. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.info("""
    👋 **Chào mừng bạn đến với Hệ thống hỗ trợ thẩm định
    cho vay doanh nghiệp**

    Hệ thống hỗ trợ kiểm tra điều kiện vay vốn,
    phân tích tình hình tài chính, đánh giá khả năng trả nợ
    và phân tích tài sản bảo đảm.
    """)

    st.subheader("📌 Các nhóm đánh giá")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("⚖️", "Điều kiện vay")
    c2.metric("💰", "Tài chính")
    c3.metric("💳", "Khả năng trả nợ")
    c4.metric("🏠", "TSĐB")

    st.divider()

    st.subheader("📋 Quy trình")

    st.write("""
    **Bước 1:** Kiểm tra thông tin pháp lý doanh nghiệp.

    **Bước 2:** Kiểm tra mục đích vay và phương án sử dụng vốn.

    **Bước 3:** Phân tích khả năng tài chính và trả nợ.

    **Bước 4:** Đánh giá tài sản bảo đảm nếu có.

    **Bước 5:** Tổng hợp kết quả thẩm định.

    **Bước 6:** Đưa ra kết luận hỗ trợ.
    """)

    st.warning("""
    ⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ thẩm định.
    Quyết định cho vay thực tế thuộc thẩm quyền của tổ chức tín dụng
    và phải tuân thủ quy định pháp luật, chính sách tín dụng nội bộ
    và kết quả thẩm định hồ sơ thực tế.
    """)


# =========================================================
# 8. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.header("🏢 Hồ sơ doanh nghiệp")

    st.subheader("Thông tin pháp lý")

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

        st.selectbox(
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

        st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=3
        )

    st.subheader("Thông tin khoản vay")

    st.selectbox(
        "Mục đích vay",
        [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]
    )

    st.success(
        "Thông tin doanh nghiệp đã được nhập."
    )


# =========================================================
# 9. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.header("⚖️ Kiểm tra điều kiện vay vốn")

    st.info("""
    Điều kiện vay vốn được sử dụng để kiểm tra sơ bộ hồ sơ.
    Các chỉ tiêu ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu
    hỗ trợ phân tích tín dụng, không phải điều kiện pháp lý
    bắt buộc chung cho mọi doanh nghiệp.
    """)

    st.subheader("1️⃣ Điều kiện pháp lý và mục đích vay")

    st.session_state.nang_luc_phap_ly = st.selectbox(
        "Doanh nghiệp có năng lực pháp luật dân sự?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.muc_dich = st.selectbox(
        "Mục đích sử dụng vốn có hợp pháp?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.co_phuong_an = st.selectbox(
        "Có phương án sử dụng vốn?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.phuong_an_kha_thi = st.selectbox(
        "Phương án sử dụng vốn có khả thi?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.kha_nang_tra_no = st.selectbox(
        "Có khả năng tài chính để trả nợ?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.subheader("2️⃣ Cam kết của khách hàng")

    st.session_state.dung_muc_dich = st.selectbox(
        "Cam kết sử dụng vốn đúng mục đích?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.tra_no_dung_han = st.selectbox(
        "Có khả năng và cam kết hoàn trả nợ đúng hạn?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.success(
        "Đã lưu thông tin điều kiện vay vốn."
    )


# =========================================================
# 10. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.header("💰 Phân tích tài chính")

    st.caption("Đơn vị: triệu đồng")

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

    if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

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
# 11. KHOẢN VAY VÀ KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.header("💳 Thông tin khoản vay")

    st.caption("Đơn vị: triệu đồng")

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

    if st.button("💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"):

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

        no_moi = tien_goc + tien_lai

        st.session_state.tong_nghia_vu = (
            st.session_state.nghia_vu_no_cu
            + no_moi
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


# =========================================================
# 12. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.header("🏠 Tài sản bảo đảm")

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        ["Chưa đánh giá", "Có", "Không"]
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

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
                "Vui lòng nhập số tiền vay ở mục "
                "'Thông tin khoản vay' trước."
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
# 13. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.header("🎯 KẾT QUẢ THẨM ĐỊNH")

    st.info(
        "Kết quả dưới đây được tổng hợp tự động từ các thông tin "
        "đã nhập trong các mục: Điều kiện vay vốn, Phân tích tài chính, "
        "Thông tin khoản vay và Tài sản bảo đảm."
    )

    ket_qua = []

    # =====================================================
    # A. ĐIỀU KIỆN VAY VỐN
    # =====================================================

    dieu_kien = [
        st.session_state.nang_luc_phap_ly,
        st.session_state.muc_dich,
        st.session_state.co_phuong_an,
        st.session_state.phuong_an_kha_thi,
        st.session_state.kha_nang_tra_no,
        st.session_state.dung_muc_dich,
        st.session_state.tra_no_dung_han
    ]

    ten_dieu_kien = [
        "Năng lực pháp lý",
        "Mục đích vay hợp pháp",
        "Có phương án sử dụng vốn",
        "Phương án sử dụng vốn khả thi",
        "Có khả năng tài chính trả nợ",
        "Cam kết sử dụng vốn đúng mục đích",
        "Cam kết hoàn trả nợ đúng hạn"
    ]

    for ten, gia_tri in zip(ten_dieu_kien, dieu_kien):

        if gia_tri == "Có":

            ket_qua.append(
                (ten, "Đạt", "Đáp ứng điều kiện")
            )

        elif gia_tri == "Không":

            ket_qua.append(
                (ten, "Không đạt", "Chưa đáp ứng điều kiện")
            )

        else:

            ket_qua.append(
                (ten, "Chưa đánh giá", "Chưa có dữ liệu")
            )


    # =====================================================
    # B. PHÂN TÍCH TÀI CHÍNH
    # =====================================================

    if st.session_state.roa is not None:

        if st.session_state.roa > 0:

            ket_qua.append(
                (
                    "ROA",
                    "Đạt",
                    f"ROA = {st.session_state.roa:.2f}%"
                )
            )

        else:

            ket_qua.append(
                (
                    "ROA",
                    "Không đạt",
                    f"ROA = {st.session_state.roa:.2f}%"
                )
            )

    else:

        ket_qua.append(
            (
                "ROA",
                "Chưa đánh giá",
                "Chưa thực hiện phân tích tài chính"
            )
        )


    if st.session_state.roe is not None:

        if st.session_state.roe > 0:

            ket_qua.append(
                (
                    "ROE",
                    "Đạt",
                    f"ROE = {st.session_state.roe:.2f}%"
                )
            )

        else:

            ket_qua.append(
                (
                    "ROE",
                    "Không đạt",
                    f"ROE = {st.session_state.roe:.2f}%"
                )
            )

    else:

        ket_qua.append(
            (
                "ROE",
                "Chưa đánh giá",
                "Chưa thực hiện phân tích tài chính"
            )
        )


    if st.session_state.ty_le_no is not None:

        if st.session_state.ty_le_no <= 70:

            ket_qua.append(
                (
                    "Tỷ lệ nợ",
                    "Đạt",
                    f"{st.session_state.ty_le_no:.2f}%"
                )
            )

        else:

            ket_qua.append(
                (
                    "Tỷ lệ nợ",
                    "Không đạt",
                    f"{st.session_state.ty_le_no:.2f}% - Mức nợ cao"
                )
            )

    else:

        ket_qua.append(
            (
                "Tỷ lệ nợ",
                "Chưa đánh giá",
                "Chưa thực hiện phân tích tài chính"
            )
        )


    # =====================================================
    # C. LNST
    # =====================================================

    if st.session_state.lnst > 0:

        ket_qua.append(
            (
                "LNST",
                "Đạt",
                f"LNST = {st.session_state.lnst:,.2f} triệu đồng"
            )
        )

    elif st.session_state.lnst < 0:

        ket_qua.append(
            (
                "LNST",
                "Không đạt",
                f"LNST = {st.session_state.lnst:,.2f} triệu đồng"
            )
        )

    else:

        ket_qua.append(
            (
                "LNST",
                "Chưa đánh giá",
                "Chưa nhập dữ liệu LNST"
            )
        )


    # =====================================================
    # D. KHẢ NĂNG TRẢ NỢ
    # =====================================================

    if st.session_state.tong_nghia_vu is not None:

        if st.session_state.dong_tien >= st.session_state.tong_nghia_vu:

            ket_qua.append(
                (
                    "Khả năng trả nợ",
                    "Đạt",
                    "Dòng tiền đủ đáp ứng nghĩa vụ trả nợ"
                )
            )

        else:

            ket_qua.append(
                (
                    "Khả năng trả nợ",
                    "Không đạt",
                    "Dòng tiền chưa đủ đáp ứng nghĩa vụ trả nợ"
                )
            )

    else:

        ket_qua.append(
            (
                "Khả năng trả nợ",
                "Chưa đánh giá",
                "Chưa phân tích khoản vay"
            )
        )


    # =====================================================
    # E. LTV
    # =====================================================

    if st.session_state.co_tsdb == "Không":

        ket_qua.append(
            (
                "LTV",
                "Không áp dụng",
                "Khoản vay không có tài sản bảo đảm"
            )
        )

    elif st.session_state.ltv is not None:

        if st.session_state.ltv <= 70:

            ket_qua.append(
                (
                    "LTV",
                    "Đạt",
                    f"LTV = {st.session_state.ltv:.2f}%"
                )
            )

        else:

            ket_qua.append(
                (
                    "LTV",
                    "Không đạt",
                    f"LTV = {st.session_state.ltv:.2f}%"
                )
            )

    else:

        ket_qua.append(
            (
                "LTV",
                "Chưa đánh giá",
                "Chưa phân tích tài sản bảo đảm"
            )
        )


    # =====================================================
    # F. HIỂN THỊ BẢNG
    # =====================================================

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


    # =====================================================
    # G. TỔNG HỢP
    # =====================================================

    so_dat = sum(
        1 for item in ket_qua
        if item[1] == "Đạt"
    )

    so_khong_dat = sum(
        1 for item in ket_qua
        if item[1] == "Không đạt"
    )

    so_chua_danh_gia = sum(
        1 for item in ket_qua
        if item[1] == "Chưa đánh giá"
    )

    tong_tieu_chi = len(ket_qua)


    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Tổng tiêu chí",
        tong_tieu_chi
    )

    c2.metric(
        "Tiêu chí đạt",
        so_dat
    )

    c3.metric(
        "Không đạt",
        so_khong_dat
    )

    c4.metric(
        "Chưa đánh giá",
        so_chua_danh_gia
    )


    # =====================================================
    # H. KẾT LUẬN THẨM ĐỊNH
    # =====================================================

    st.subheader("📌 KẾT LUẬN THẨM ĐỊNH")


    # Nếu có điều kiện pháp lý không đạt
    dieu_kien_phap_ly_khong_dat = (
        st.session_state.nang_luc_phap_ly == "Không"
        or st.session_state.muc_dich == "Không"
        or st.session_state.co_phuong_an == "Không"
        or st.session_state.phuong_an_kha_thi == "Không"
        or st.session_state.dung_muc_dich == "Không"
    )


    if dieu_kien_phap_ly_khong_dat:

        st.error(
            "🔴 KHÔNG ĐỀ XUẤT CHO VAY"
        )

        st.write(
            "Hồ sơ chưa đáp ứng một hoặc nhiều điều kiện "
            "cơ bản về pháp lý, mục đích hoặc phương án sử dụng vốn."
        )


    elif so_khong_dat > 0:

        st.warning(
            "🟡 CẦN THẨM ĐỊNH BỔ SUNG"
        )

        st.write(
            "Hồ sơ còn một số tiêu chí chưa đạt hoặc có yếu tố rủi ro. "
            "Cần xem xét bổ sung hồ sơ tài chính, dòng tiền, "
            "khả năng trả nợ và tài sản bảo đảm."
        )


    elif so_chua_danh_gia > 0:

        st.warning(
            "🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN"
        )

        st.write(
            "Vui lòng nhập đầy đủ thông tin và thực hiện phân tích "
            "tài chính, khoản vay và tài sản bảo đảm trước khi "
            "đưa ra kết luận."
        )


    else:

        st.success(
            "🟢 ĐỀ XUẤT CHO VAY / CHUYỂN THẨM ĐỊNH CHI TIẾT"
        )

        st.write(
            "Hồ sơ đáp ứng các tiêu chí được xây dựng trong mô hình "
            "thẩm định sơ bộ. Có thể chuyển sang bước thẩm định tín dụng "
            "chi tiết theo chính sách của tổ chức tín dụng."
        )


    st.info("""
    ⚠️ **Lưu ý:** Kết quả trên là kết quả hỗ trợ thẩm định theo
    mô hình minh họa của ứng dụng, không phải quyết định cấp tín dụng.
    Quyết định cho vay thực tế cần căn cứ hồ sơ, chính sách tín dụng,
    lịch sử tín dụng, dòng tiền, khả năng trả nợ và các quy định
    của tổ chức tín dụng.
    """)


# =========================================================
# 14. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

    <br>

    Điều kiện vay vốn • Phân tích tài chính •
    Khả năng trả nợ • Tài sản bảo đảm

    <br><br>

    © 2026

    </div>
    """,
    unsafe_allow_html=True
)
