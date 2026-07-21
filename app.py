import streamlit as st

st.set_page_config(
    page_title="App thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 APP THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

st.write(
    "Nhập thông tin doanh nghiệp và khoản vay để thực hiện thẩm định."
)

# =========================
# THÔNG TIN DOANH NGHIỆP
# =========================

st.header("1. Thông tin doanh nghiệp")

ten_dn = st.text_input("Tên doanh nghiệp")

ma_so = st.text_input("Mã số doanh nghiệp")

nganh_nghe = st.text_input("Ngành nghề kinh doanh")

# =========================
# CHỈ TIÊU TÀI CHÍNH
# =========================

st.header("2. Thông tin tài chính")

col1, col2 = st.columns(2)

with col1:

    lnst = st.number_input(
        "Lợi nhuận sau thuế (triệu đồng)",
        min_value=0.0
    )

    tong_tai_san = st.number_input(
        "Tổng tài sản (triệu đồng)",
        min_value=0.0
    )

with col2:

    von_chu_so_huu = st.number_input(
        "Vốn chủ sở hữu (triệu đồng)",
        min_value=0.0
    )

    doanh_thu = st.number_input(
        "Doanh thu (triệu đồng)",
        min_value=0.0
    )

# =========================
# THÔNG TIN KHOẢN VAY
# =========================

st.header("3. Thông tin khoản vay")

so_tien_vay = st.number_input(
    "Số tiền vay (triệu đồng)",
    min_value=0.0
)

thoi_gian_vay = st.number_input(
    "Thời gian vay (tháng)",
    min_value=1
)

lai_suat = st.number_input(
    "Lãi suất cho vay (%/năm)",
    min_value=0.0
)

# =========================
# TÀI SẢN BẢO ĐẢM
# =========================

st.header("4. Tài sản bảo đảm")

gia_tri_tsdb = st.number_input(
    "Giá trị tài sản bảo đảm (triệu đồng)",
    min_value=0.0
)

# =========================
# NÚT THẨM ĐỊNH
# =========================

if st.button("THẨM ĐỊNH HỒ SƠ"):

    if tong_tai_san > 0:
        roa = lnst / tong_tai_san * 100
    else:
        roa = 0

    if von_chu_so_huu > 0:
        roe = lnst / von_chu_so_huu * 100
    else:
        roe = 0

    if gia_tri_tsdb > 0:
        ltv = so_tien_vay / gia_tri_tsdb * 100
    else:
        ltv = 0

    st.subheader("KẾT QUẢ THẨM ĐỊNH")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ROA", f"{roa:.2f}%")

    with col2:
        st.metric("ROE", f"{roe:.2f}%")

    with col3:
        st.metric("LTV", f"{ltv:.2f}%")

    # Đánh giá

    if roa >= 5:
        danh_gia_roa = "Đạt"
    else:
        danh_gia_roa = "Không đạt"

    if roe >= 10:
        danh_gia_roe = "Đạt"
    else:
        danh_gia_roe = "Không đạt"

    if ltv <= 70:
        danh_gia_ltv = "Đạt"
    else:
        danh_gia_ltv = "Không đạt"

    st.write("Đánh giá ROA:", danh_gia_roa)

    st.write("Đánh giá ROE:", danh_gia_roe)

    st.write("Đánh giá LTV:", danh_gia_ltv)

    # Kết luận

    if (
        roa >= 5
        and roe >= 10
        and ltv <= 70
    ):

        st.success(
            "HỒ SƠ ĐẠT TIÊU CHÍ THẨM ĐỊNH"
        )

    else:

        st.warning(
            "HỒ SƠ CẦN ĐƯỢC XEM XÉT THÊM"
        )
