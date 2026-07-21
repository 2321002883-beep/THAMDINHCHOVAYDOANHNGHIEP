import streamlit as st

st.set_page_config(
    page_title="App thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

# =========================
# TIÊU ĐỀ
# =========================

st.title("🏦 APP THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

st.write(
    "Nhập thông tin doanh nghiệp và khoản vay để thực hiện thẩm định."
)

# =========================
# CHÈN HÌNH ẢNH
# =========================

st.image("logo.png", width=200)

# =========================
# 1. THÔNG TIN DOANH NGHIỆP
# =========================

st.header("1️⃣ Thông tin doanh nghiệp")

ten_dn = st.text_input(
    "Tên doanh nghiệp"
)

ma_so = st.text_input(
    "Mã số doanh nghiệp"
)

nganh_nghe = st.text_input(
    "Ngành nghề kinh doanh"
)

# =========================
# 2. THÔNG TIN TÀI CHÍNH
# =========================

st.header("2️⃣ Thông tin tài chính")

col1, col2 = st.columns(2)

with col1:

    lnst = st.number_input(
        "Lợi nhuận sau thuế - LNST (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

    tong_tai_san = st.number_input(
        "Tổng tài sản (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

with col2:

    von_chu_so_huu = st.number_input(
        "Vốn chủ sở hữu (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

    doanh_thu = st.number_input(
        "Doanh thu (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

# =========================
# 3. THÔNG TIN KHOẢN VAY
# =========================

st.header("3️⃣ Thông tin khoản vay")

col3, col4 = st.columns(2)

with col3:

    so_tien_vay = st.number_input(
        "Số tiền vay (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

    thoi_gian_vay = st.number_input(
        "Thời gian vay (tháng)",
        min_value=1,
        value=12
    )

with col4:

    lai_suat = st.number_input(
        "Lãi suất cho vay (%/năm)",
        min_value=0.0,
        value=0.0
    )

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm - TSĐB (triệu đồng)",
        min_value=0.0,
        value=0.0
    )

# =========================
# 4. NÚT THẨM ĐỊNH
# =========================

st.header("4️⃣ Thẩm định hồ sơ")

if st.button(
    "🔍 THẨM ĐỊNH HỒ SƠ",
    type="primary"
):

    # Tính ROA
    if tong_tai_san > 0:
        roa = lnst / tong_tai_san * 100
    else:
        roa = 0

    # Tính ROE
    if von_chu_so_huu > 0:
        roe = lnst / von_chu_so_huu * 100
    else:
        roe = 0

    # Tính LTV
    if gia_tri_tsdb > 0:
        ltv = so_tien_vay / gia_tri_tsdb * 100
    else:
        ltv = 0

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.subheader("📊 KẾT QUẢ THẨM ĐỊNH")

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric(
            "ROA",
            f"{roa:.2f}%"
        )

    with col6:
        st.metric(
            "ROE",
            f"{roe:.2f}%"
        )

    with col7:
        st.metric(
            "LTV",
            f"{ltv:.2f}%"
        )

    # =========================
    # ĐÁNH GIÁ
    # =========================

    st.subheader("📋 Đánh giá")

    if roa >= 5:
        st.success("✅ ROA: ĐẠT")
    else:
        st.warning("⚠️ ROA: KHÔNG ĐẠT")

    if roe >= 10:
        st.success("✅ ROE: ĐẠT")
    else:
        st.warning("⚠️ ROE: KHÔNG ĐẠT")

    if ltv <= 70:
        st.success("✅ LTV: ĐẠT")
    else:
        st.warning("⚠️ LTV: KHÔNG ĐẠT")

    # =========================
    # KẾT LUẬN
    # =========================

    if (
        roa >= 5
        and roe >= 10
        and ltv <= 70
    ):

        st.success(
            "🎉 KẾT LUẬN: HỒ SƠ ĐẠT TIÊU CHÍ THẨM ĐỊNH"
        )

    else:

        st.error(
            "❌ KẾT LUẬN: HỒ SƠ CẦN ĐƯỢC XEM XÉT THÊM"
        )
