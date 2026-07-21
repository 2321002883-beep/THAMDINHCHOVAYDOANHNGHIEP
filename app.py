import streamlit as st
import pandas as pd
from pathlib import Path

# =====================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =====================================================

st.set_page_config(
    page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# 2. LOGO
# =====================================================

logo = Path(__file__).parent / "logo.png"

# =====================================================
# 3. GIAO DIỆN
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

h1 {
    color: #0f172a;
}

h2, h3 {
    color: #1e293b;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 3px 12px rgba(0,0,0,.06);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 4. SIDEBAR
# =====================================================

with st.sidebar:

    if logo.exists():
        st.image(
            str(logo),
            use_container_width=True
        )

    st.title(
        "🏦 Thẩm định tín dụng"
    )

    st.caption(
        "Hệ thống hỗ trợ thẩm định "
        "cho vay doanh nghiệp"
    )

    st.divider()

    st.info("""
    **QUY TRÌNH THẨM ĐỊNH**

    1️⃣ Nhập hồ sơ doanh nghiệp

    2️⃣ Nhập thông tin tài chính

    3️⃣ Nhập khoản vay

    4️⃣ Nhập tài sản bảo đảm

    5️⃣ Thực hiện thẩm định

    6️⃣ Xem kết quả
    """)

    st.divider()

    st.caption(
        "© 2026 - Hệ thống hỗ trợ thẩm định"
    )

# =====================================================
# 5. HEADER
# =====================================================

col_logo, col_title = st.columns([1, 6])

with col_logo:

    if logo.exists():

        st.image(
            str(logo),
            width=110
        )

    else:

        st.write("🏦")


with col_title:

    st.title(
        "🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH "
        "CHO VAY DOANH NGHIỆP"
    )

    st.caption(
        "Phân tích tài chính • Khả năng trả nợ • "
        "Tài sản bảo đảm"
    )


st.divider()

# =====================================================
# 6. THÔNG TIN DOANH NGHIỆP
# =====================================================

st.subheader(
    "🏢 1. THÔNG TIN DOANH NGHIỆP"
)

c1, c2, c3 = st.columns(3)

with c1:

    ten_dn = st.text_input(
        "Tên doanh nghiệp",
        placeholder="Ví dụ: Công ty TNHH ABC"
    )

with c2:

    ma_so = st.text_input(
        "Mã số doanh nghiệp",
        placeholder="Ví dụ: 0312345678"
    )

with c3:

    nganh = st.selectbox(
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

# =====================================================
# 7. TÌNH HÌNH TÀI CHÍNH
# =====================================================

st.subheader(
    "💰 2. TÌNH HÌNH TÀI CHÍNH"
)

st.caption(
    "Đơn vị nhập liệu: triệu đồng"
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    doanh_thu = st.number_input(
        "Doanh thu",
        min_value=0.0
    )

with c2:

    lnst = st.number_input(
        "Lợi nhuận sau thuế (LNST)",
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

# =====================================================
# 8. THÔNG TIN KHOẢN VAY
# =====================================================

st.subheader(
    "💳 3. THÔNG TIN KHOẢN VAY"
)

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
        "Lãi suất cho vay (%/năm)",
        min_value=0.0
    )

# =====================================================
# 9. TÀI SẢN BẢO ĐẢM
# =====================================================

st.subheader(
    "🏠 4. TÀI SẢN BẢO ĐẢM"
)

c1, c2 = st.columns(2)

with c1:

    co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Có",
            "Không"
        ]
    )

with c2:

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0
    )

# =====================================================
# 10. NÚT THẨM ĐỊNH
# =====================================================

st.divider()

thuc_hien = st.button(
    "🔍 THỰC HIỆN THẨM ĐỊNH",
    type="primary",
    use_container_width=True
)

# =====================================================
# 11. TÍNH TOÁN VÀ THẨM ĐỊNH
# =====================================================

if thuc_hien:

    # Kiểm tra dữ liệu

    if not ten_dn:

        st.error(
            "⚠️ Vui lòng nhập tên doanh nghiệp."
        )

        st.stop()

    if tong_ts <= 0:

        st.error(
            "⚠️ Tổng tài sản phải lớn hơn 0."
        )

        st.stop()

    if von_csh <= 0:

        st.error(
            "⚠️ Vốn chủ sở hữu phải lớn hơn 0."
        )

        st.stop()

    if so_tien_vay <= 0:

        st.error(
            "⚠️ Số tiền vay phải lớn hơn 0."
        )

        st.stop()

    # =================================================
    # TÍNH ROA
    # =================================================

    roa = (
        lnst
        / tong_ts
        * 100
    )

    # =================================================
    # TÍNH ROE
    # =================================================

    roe = (
        lnst
        / von_csh
        * 100
    )

    # =================================================
    # TÍNH NỢ PHẢI TRẢ
    # =================================================

    no_phai_tra = (
        tong_ts
        - von_csh
    )

    # =================================================
    # TỶ LỆ NỢ
    # =================================================

    ty_le_no = (
        no_phai_tra
        / tong_ts
        * 100
    )

    # =================================================
    # TÍNH LTV
    # =================================================

    if (
        co_tsdb == "Có"
        and gia_tri_tsdb > 0
    ):

        ltv = (
            so_tien_vay
            / gia_tri_tsdb
            * 100
        )

    else:

        ltv = None

    # =================================================
    # TÍNH TRẢ NỢ HÀNG THÁNG
    # =================================================

    tien_goc = (
        so_tien_vay
        / thoi_han
    )

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

    # =================================================
    # CHẤM ĐIỂM MÔ HÌNH
    # =================================================

    diem = 0

    if lnst > 0:
        diem += 1

    if roa > 0:
        diem += 1

    if roe > 0:
        diem += 1

    if ty_le_no <= 70:
        diem += 1

    if (
        ltv is None
        or ltv <= 70
    ):
        diem += 1

    # =================================================
    # KẾT QUẢ
    # =================================================

    st.divider()

    st.header(
        "📊 5. KẾT QUẢ THẨM ĐỊNH"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        st.metric(
            "ROA",
            f"{roa:.2f}%"
        )

    with c2:

        st.metric(
            "ROE",
            f"{roe:.2f}%"
        )

    with c3:

        st.metric(
            "TỶ LỆ NỢ",
            f"{ty_le_no:.2f}%"
        )

    with c4:

        st.metric(
            "LTV",
            (
                f"{ltv:.2f}%"
                if ltv is not None
                else "N/A"
            )
        )

    with c5:

        st.metric(
            "ĐIỂM ĐÁNH GIÁ",
            f"{diem}/5"
        )

    # =================================================
    # BIỂU ĐỒ
    # =================================================

    st.subheader(
        "📈 Phân tích các chỉ tiêu"
    )

    chart = pd.DataFrame(

        {
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
        }

    )

    st.bar_chart(
        chart.set_index(
            "Chỉ tiêu"
        )
    )

    # =================================================
    # KHẢ NĂNG TRẢ NỢ
    # =================================================

    st.subheader(
        "💰 Khả năng trả nợ"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Gốc trả/tháng",
            f"{tien_goc:,.2f} triệu"
        )

    with c2:

        st.metric(
            "Lãi tháng đầu",
            f"{tien_lai:,.2f} triệu"
        )

    with c3:

        st.metric(
            "Tổng trả/tháng",
            f"{no_hang_thang:,.2f} triệu"
        )

    # =================================================
    # KẾT LUẬN
    # =================================================

    st.subheader(
        "🎯 KẾT LUẬN"
    )

    if diem >= 4:

        st.success(
            "🟢 ĐỀ XUẤT XEM XÉT CHO VAY\n\n"
            "Hồ sơ có các chỉ tiêu tương đối tích cực "
            "theo mô hình hỗ trợ thẩm định."
        )

    elif diem >= 2:

        st.warning(
            "🟡 CẦN THẨM ĐỊNH THÊM\n\n"
            "Hồ sơ cần được phân tích bổ sung "
            "về khả năng trả nợ và rủi ro."
        )

    else:

        st.error(
            "🔴 RỦI RO CAO THEO MÔ HÌNH\n\n"
            "Hồ sơ chưa đáp ứng tốt các tiêu chí "
            "của mô hình hỗ trợ."
        )

    # =================================================
    # BẢNG TỔNG HỢP
    # =================================================

    st.subheader(
        "📋 BẢNG TỔNG HỢP HỒ SƠ"
    )

    ket_qua = pd.DataFrame(

        {
            "Chỉ tiêu": [

                "Tên doanh nghiệp",

                "Mã số doanh nghiệp",

                "Ngành nghề",

                "Doanh thu",

                "LNST",

                "Tổng tài sản",

                "Vốn chủ sở hữu",

                "ROA",

                "ROE",

                "Tỷ lệ nợ",

                "Số tiền vay",

                "Thời hạn vay",

                "Lãi suất",

                "Giá trị TSĐB",

                "LTV",

                "Điểm đánh giá"

            ],

            "Kết quả": [

                ten_dn,

                ma_so,

                nganh,

                f"{doanh_thu:,.2f} triệu đồng",

                f"{lnst:,.2f} triệu đồng",

                f"{tong_ts:,.2f} triệu đồng",

                f"{von_csh:,.2f} triệu đồng",

                f"{roa:.2f}%",

                f"{roe:.2f}%",

                f"{ty_le_no:.2f}%",

                f"{so_tien_vay:,.2f} triệu đồng",

                f"{thoi_han} tháng",

                f"{lai_suat:.2f}%/năm",

                f"{gia_tri_tsdb:,.2f} triệu đồng",

                (
                    f"{ltv:.2f}%"
                    if ltv is not None
                    else "Không áp dụng"
                ),

                f"{diem}/5"

            ]

        }

    )

    st.dataframe(
        ket_qua,
        use_container_width=True,
        hide_index=True
    )

    # =================================================
    # TẢI BÁO CÁO
    # =================================================

    csv = ket_qua.to_csv(
        index=False
    ).encode(
        "utf-8-sig"
    )

    st.download_button(
        "📥 TẢI BÁO CÁO THẨM ĐỊNH",
        csv,
        f"bao_cao_tham_dinh_{ten_dn}.csv",
        "text/csv",
        use_container_width=True
    )

# =====================================================
# 12. FOOTER
# =====================================================

st.divider()

st.caption(
    "🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP "
    "| Phiên bản 1.0 | 2026"
)
