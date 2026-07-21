import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# CẤU HÌNH
# =========================
st.set_page_config(
    page_title="CreditVision",
    page_icon="🏦",
    layout="wide"
)

# =========================
# LOGO
# =========================
logo = Path(__file__).parent / "logo.png"

# =========================
# CSS NGẮN GỌN
# =========================
st.markdown("""
<style>
.stApp {
    background:#f5f7fb;
}
section[data-testid="stSidebar"] {
    background:#0f172a;
}
.block-container {
    max-width:1200px;
    padding-top:2rem;
}
h1 {
    color:#0f172a;
}
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #e2e8f0;
    box-shadow:0 3px 12px rgba(0,0,0,.06);
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    if logo.exists():
        st.image(str(logo), use_container_width=True)

    st.title("🏦 CreditVision")
    st.caption("Hệ thống hỗ trợ thẩm định tín dụng doanh nghiệp")

    st.divider()

    st.info("""
    **Quy trình**

    1️⃣ Nhập hồ sơ  
    2️⃣ Nhập tài chính  
    3️⃣ Nhập khoản vay  
    4️⃣ Nhập TSĐB  
    5️⃣ Thẩm định
    """)

# =========================
# HEADER
# =========================
c1, c2 = st.columns([1, 6])

with c1:
    if logo.exists():
        st.image(str(logo), width=110)
    else:
        st.write("🏦")

with c2:
    st.title("CreditVision")
    st.caption(
        "HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP"
    )

st.divider()

# =========================
# 1. THÔNG TIN DOANH NGHIỆP
# =========================
st.subheader("🏢 Thông tin doanh nghiệp")

c1, c2, c3 = st.columns(3)

with c1:
    ten_dn = st.text_input(
        "Tên doanh nghiệp",
        "Công ty TNHH ABC"
    )

with c2:
    ma_so = st.text_input(
        "Mã số doanh nghiệp"
    )

with c3:
    nganh = st.selectbox(
        "Ngành nghề",
        [
            "Sản xuất",
            "Thương mại",
            "Dịch vụ",
            "Xây dựng",
            "Vận tải",
            "Công nghệ",
            "Khác"
        ]
    )

# =========================
# 2. TÀI CHÍNH
# =========================
st.subheader("💰 Tình hình tài chính")
st.caption("Đơn vị: triệu đồng")

c1, c2, c3, c4 = st.columns(4)

with c1:
    doanh_thu = st.number_input(
        "Doanh thu",
        min_value=0.0
    )

with c2:
    lnst = st.number_input(
        "LNST",
        value=0.0
    )

with c3:
    tong_ts = st.number_input(
        "Tổng tài sản",
        min_value=0.0
    )

with c4:
    von_csh = st.number_input(
        "Vốn chủ sở hữu",
        min_value=0.0
    )

# =========================
# 3. KHOẢN VAY
# =========================
st.subheader("💳 Thông tin khoản vay")

c1, c2, c3 = st.columns(3)

with c1:
    so_tien_vay = st.number_input(
        "Số tiền vay",
        min_value=0.0
    )

with c2:
    thoi_han = st.number_input(
        "Thời hạn vay (tháng)",
        min_value=1,
        value=12
    )

with c3:
    lai_suat = st.number_input(
        "Lãi suất (%/năm)",
        min_value=0.0
    )

# =========================
# 4. TSĐB
# =========================
st.subheader("🏠 Tài sản bảo đảm")

c1, c2 = st.columns(2)

with c1:
    co_tsdb = st.selectbox(
        "Có tài sản bảo đảm?",
        ["Có", "Không"]
    )

with c2:
    gia_tri_tsdb = st.number_input(
        "Giá trị TSĐB",
        min_value=0.0
    )

# =========================
# 5. THẨM ĐỊNH
# =========================
st.divider()

if st.button(
    "🔍 THỰC HIỆN THẨM ĐỊNH",
    type="primary",
    use_container_width=True
):

    # Kiểm tra dữ liệu
    if tong_ts <= 0 or von_csh <= 0 or so_tien_vay <= 0:

        st.error(
            "⚠️ Vui lòng nhập đầy đủ Tổng tài sản, "
            "Vốn chủ sở hữu và Số tiền vay."
        )

        st.stop()

    # =====================
    # TÍNH ROA - ROE
    # =====================
    roa = lnst / tong_ts * 100
    roe = lnst / von_csh * 100

    # =====================
    # TỶ LỆ NỢ
    # =====================
    # Tạm thời dùng tổng tài sản - VCSH
    no_phai_tra = tong_ts - von_csh

    ty_le_no = no_phai_tra / tong_ts * 100

    # =====================
    # LTV
    # =====================
    if co_tsdb == "Có" and gia_tri_tsdb > 0:
        ltv = so_tien_vay / gia_tri_tsdb * 100
    else:
        ltv = None

    # =====================
    # TRẢ NỢ
    # =====================
    tien_goc = so_tien_vay / thoi_han

    tien_lai = (
        so_tien_vay
        * lai_suat
        / 100
        / 12
    )

    no_hang_thang = (
        tien_goc
        + tien_lai
    )

    # =====================
    # CHẤM ĐIỂM
    # =====================
    diem = 0

    if lnst > 0:
        diem += 1

    if roa > 0:
        diem += 1

    if roe > 0:
        diem += 1

    if ty_le_no <= 70:
        diem += 1

    if ltv is None or ltv <= 70:
        diem += 1

    # =====================
    # KẾT QUẢ
    # =====================
    st.subheader("📊 Kết quả thẩm định")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("ROA", f"{roa:.2f}%")
    c2.metric("ROE", f"{roe:.2f}%")
    c3.metric("Tỷ lệ nợ", f"{ty_le_no:.2f}%")
    c4.metric(
        "LTV",
        f"{ltv:.2f}%" if ltv is not None else "N/A"
    )
    c5.metric("Điểm", f"{diem}/5")

    # =====================
    # BIỂU ĐỒ
    # =====================
    chart = pd.DataFrame({
        "Chỉ tiêu": [
            "ROA",
            "ROE",
            "Tỷ lệ nợ"
        ],
        "Giá trị (%)": [
            roa,
            roe,
            ty_le_no
        ]
    })

    st.bar_chart(
        chart.set_index("Chỉ tiêu")
    )

    # =====================
    # KHẢ NĂNG TRẢ NỢ
    # =====================
    st.subheader("💰 Khả năng trả nợ")

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
        "Tổng trả/tháng",
        f"{no_hang_thang:,.2f}"
    )

    # =====================
    # KẾT LUẬN
    # =====================
    if diem >= 4:

        st.success(
            "🟢 ĐỀ XUẤT XEM XÉT CHO VAY\n\n"
            "Hồ sơ có các chỉ tiêu tương đối tích cực "
            "theo mô hình hỗ trợ."
        )

    elif diem >= 2:

        st.warning(
            "🟡 CẦN THẨM ĐỊNH THÊM\n\n"
            "Hồ sơ còn một số yếu tố cần phân tích "
            "bổ sung."
        )

    else:

        st.error(
            "🔴 RỦI RO CAO THEO MÔ HÌNH\n\n"
            "Hồ sơ chưa đáp ứng tốt các tiêu chí "
            "của mô hình."
        )

    # =====================
    # BẢNG KẾT QUẢ
    # =====================
    ket_qua = pd.DataFrame({
        "Chỉ tiêu": [
            "Doanh nghiệp",
            "Mã số",
            "Ngành nghề",
            "ROA",
            "ROE",
            "Tỷ lệ nợ",
            "Số tiền vay",
            "Thời hạn vay",
            "Lãi suất",
            "Giá trị TSĐB",
            "LTV",
            "Điểm"
        ],
        "Kết quả": [
            ten_dn,
            ma_so,
            nganh,
            f"{roa:.2f}%",
            f"{roe:.2f}%",
            f"{ty_le_no:.2f}%",
            f"{so_tien_vay:,.2f}",
            f"{thoi_han} tháng",
            f"{lai_suat:.2f}%",
            f"{gia_tri_tsdb:,.2f}",
            f"{ltv:.2f}%" if ltv else "N/A",
            f"{diem}/5"
        ]
    })

    st.subheader("📋 Tổng hợp hồ sơ")

    st.dataframe(
        ket_qua,
        use_container_width=True,
        hide_index=True
    )

    # =====================
    # TẢI BÁO CÁO
    # =====================
    csv = ket_qua.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        "📥 TẢI BÁO CÁO CSV",
        csv,
        f"bao_cao_{ten_dn}.csv",
        "text/csv",
        use_container_width=True
    )

# =========================
# FOOTER
# =========================
st.divider()

st.caption(
    "🏦 CreditVision | Hệ thống hỗ trợ thẩm định "
    "cho vay doanh nghiệp | 2026"
)
