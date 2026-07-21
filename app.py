import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="CreditVision",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. ĐƯỜNG DẪN LOGO
# =========================================================

LOGO_PATH = Path(__file__).parent / "logo.png"


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
        background-color: #f4f7fb;
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }


    /* =========================
       TIÊU ĐỀ CHÍNH
    ========================= */

    .main-title {
        font-size: 34px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 16px;
        color: #64748b;
        margin-bottom: 25px;
    }


    /* =========================
       KHỐI HEADER
    ========================= */

    .header-box {
        background-color: #0f172a;
        padding: 25px;
        border-radius: 18px;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.12);
    }


    /* =========================
       SECTION
    ========================= */

    .section-box {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        margin-top: 20px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
    }


    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 3px 10px rgba(15, 23, 42, 0.05);
    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 16px;
    }


    /* =========================
       KẾT QUẢ
    ========================= */

    .result-good {
        background-color: #ecfdf5;
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #10b981;
        margin-top: 20px;
    }

    .result-warning {
        background-color: #fffbeb;
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #f59e0b;
        margin-top: 20px;
    }

    .result-bad {
        background-color: #fef2f2;
        padding: 25px;
        border-radius: 16px;
        border: 2px solid #ef4444;
        margin-top: 20px;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;
        color: #64748b;
        padding: 25px;
        margin-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    # Logo

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    else:

        st.markdown(
            "## 🏦 CreditVision"
        )


    st.divider()


    st.markdown(
        "### 🏦 CreditVision"
    )


    st.caption(
        "Hệ thống hỗ trợ thẩm định "
        "cho vay doanh nghiệp"
    )


    st.divider()


    st.markdown(
        "### 📌 MENU"
    )


    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )


    st.divider()


    st.caption(
        "CreditVision v1.0"
    )


    st.caption(
        "© 2026"
    )


# =========================================================
# 5. HEADER
# =========================================================

col_logo, col_header = st.columns(
    [1, 5]
)


with col_logo:

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            width=140
        )

    else:

        st.write("🏦")


with col_header:

    st.markdown(
        '<div class="main-title">'
        'CreditVision'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 6. GIỚI THIỆU
# =========================================================

if menu == "🏠 Tổng quan":

    st.info(
        """
        👋 **Chào mừng bạn đến với CreditVision**

        Ứng dụng hỗ trợ phân tích hồ sơ vay vốn doanh nghiệp
        dựa trên các nhóm thông tin tài chính, khoản vay,
        khả năng trả nợ và tài sản bảo đảm.
        """
    )


    st.markdown(
        "## 📌 Các chức năng chính"
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "🏢",
            "Hồ sơ doanh nghiệp"
        )


    with c2:

        st.metric(
            "💰",
            "Tài chính"
        )


    with c3:

        st.metric(
            "💳",
            "Khoản vay"
        )


    with c4:

        st.metric(
            "📊",
            "Thẩm định"
        )


    st.divider()


    st.markdown(
        "### 📋 Quy trình sử dụng"
    )


    st.write(
        """
        **Bước 1:** Nhập thông tin doanh nghiệp.

        **Bước 2:** Nhập các chỉ tiêu tài chính.

        **Bước 3:** Nhập thông tin khoản vay.

        **Bước 4:** Nhập thông tin tài sản bảo đảm.

        **Bước 5:** Thực hiện thẩm định.

        **Bước 6:** Xem kết quả và tải báo cáo.
        """
    )


    st.warning(
        """
        ⚠️ Kết quả ứng dụng chỉ mang tính chất hỗ trợ phân tích
        theo mô hình minh họa, không thay thế quyết định tín dụng
        hoặc quy trình thẩm định thực tế của ngân hàng.
        """
    )


# =========================================================
# 7. NHẬP HỒ SƠ
# =========================================================

if menu == "🏢 Hồ sơ doanh nghiệp":

    st.markdown(
        "## 🏢 Hồ sơ doanh nghiệp"
    )


    st.caption(
        "Nhập thông tin cơ bản của doanh nghiệp."
    )


    ten_dn = st.text_input(
        "Tên doanh nghiệp",
        placeholder="Ví dụ: Công ty TNHH ABC"
    )


    ma_so = st.text_input(
        "Mã số doanh nghiệp",
        placeholder="Ví dụ: 0312345678"
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
        ]
    )


    thoi_gian_hd = st.number_input(
        "Thời gian hoạt động (năm)",
        min_value=0,
        value=3
    )


    muc_dich_vay = st.selectbox(
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


    phuong_an = st.text_area(
        "Phương án sử dụng vốn",
        height=150
    )


    st.success(
        "Thông tin hồ sơ đã được nhập."
    )


# =========================================================
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

if menu == "💰 Phân tích tài chính":

    st.markdown(
        "## 💰 Phân tích tài chính"
    )


    st.caption(
        "Đơn vị: triệu đồng"
    )


    c1, c2 = st.columns(2)


    with c1:

        doanh_thu = st.number_input(
            "Doanh thu",
            min_value=0.0
        )


        lnst = st.number_input(
            "Lợi nhuận sau thuế (LNST)"
        )


        tong_tai_san = st.number_input(
            "Tổng tài sản",
            min_value=0.0
        )


    with c2:

        von_chu_so_huu = st.number_input(
            "Vốn chủ sở hữu",
            min_value=0.0
        )


        no_phai_tra = st.number_input(
            "Nợ phải trả",
            min_value=0.0
        )


        dong_tien = st.number_input(
            "Dòng tiền từ hoạt động kinh doanh"
        )


    if st.button(
        "📊 TÍNH CHỈ TIÊU TÀI CHÍNH"
    ):


        if tong_tai_san <= 0:

            st.error(
                "Tổng tài sản phải lớn hơn 0."
            )

        elif von_chu_so_huu <= 0:

            st.error(
                "Vốn chủ sở hữu phải lớn hơn 0."
            )

        else:

            roa = (
                lnst
                / tong_tai_san
                * 100
            )


            roe = (
                lnst
                / von_chu_so_huu
                * 100
            )


            ty_le_no = (
                no_phai_tra
                / tong_tai_san
                * 100
            )


            m1, m2, m3 = st.columns(3)


            with m1:

                st.metric(
                    "ROA",
                    f"{roa:.2f}%"
                )


            with m2:

                st.metric(
                    "ROE",
                    f"{roe:.2f}%"
                )


            with m3:

                st.metric(
                    "Tỷ lệ nợ",
                    f"{ty_le_no:.2f}%"
                )


            chart = pd.DataFrame(
                {
                    "Chỉ tiêu": [
                        "ROA",
                        "ROE",
                        "Tỷ lệ nợ"
                    ],

                    "Giá trị": [
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


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

if menu == "💳 Thông tin khoản vay":

    st.markdown(
        "## 💳 Thông tin khoản vay"
    )


    c1, c2 = st.columns(2)


    with c1:

        so_tien_vay = st.number_input(
            "Số tiền vay",
            min_value=0.0
        )


        thoi_gian_vay = st.number_input(
            "Thời hạn vay (tháng)",
            min_value=1,
            value=12
        )


    with c2:

        lai_suat = st.number_input(
            "Lãi suất cho vay (%/năm)",
            min_value=0.0
        )


        no_hien_tai = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0
        )


    if st.button(
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ"
    ):


        tien_goc = (
            so_tien_vay
            / thoi_gian_vay
        )


        tien_lai = (
            so_tien_vay
            * lai_suat
            / 100
            / 12
        )


        tong_no_moi = (
            tien_goc
            + tien_lai
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Gốc/tháng",
                f"{tien_goc:,.2f}"
            )


        with c2:

            st.metric(
                "Lãi tháng đầu",
                f"{tien_lai:,.2f}"
            )


        with c3:

            st.metric(
                "Nợ mới/tháng",
                f"{tong_no_moi:,.2f}"
            )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

if menu == "🏠 Tài sản bảo đảm":

    st.markdown(
        "## 🏠 Tài sản bảo đảm"
    )


    co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Có",
            "Không"
        ]
    )


    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0
    )


    so_tien_vay_tsdb = st.number_input(
        "Số tiền vay để tính LTV",
        min_value=0.0
    )


    if st.button(
        "🏠 ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM"
    ):


        if co_tsdb == "Không":

            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )


        elif gia_tri_tsdb <= 0:

            st.error(
                "Giá trị TSĐB phải lớn hơn 0."
            )


        else:

            ltv = (
                so_tien_vay_tsdb
                / gia_tri_tsdb
                * 100
            )


            st.metric(
                "LTV",
                f"{ltv:.2f}%"
            )


            if ltv <= 70:

                st.success(
                    "🟢 LTV ở mức thấp theo "
                    "tiêu chí mô hình minh họa."
                )


            elif ltv <= 100:

                st.warning(
                    "🟡 LTV cần được xem xét thêm."
                )


            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 11. TRANG KẾT QUẢ THẨM ĐỊNH
# =========================================================

if menu == "📊 Kết quả thẩm định":

    st.markdown(
        "## 📊 Kết quả thẩm định"
    )


    st.info(
        """
        Để thực hiện thẩm định đầy đủ, vui lòng nhập
        thông tin doanh nghiệp, tài chính, khoản vay
        và tài sản bảo đảm.
        """
    )


    st.markdown(
        "### 🎯 Mô hình đánh giá minh họa"
    )


    st.write(
        """
        Hệ thống có thể đánh giá dựa trên các nhóm:

        🟢 Lợi nhuận doanh nghiệp

        🟢 ROA

        🟢 ROE

        🟢 Tỷ lệ nợ

        🟢 Khả năng trả nợ

        🟢 LTV

        🟢 Tài sản bảo đảm
        """
    )


    st.warning(
        """
        ⚠️ Các ngưỡng đánh giá trong ứng dụng là
        tiêu chí mô hình minh họa và cần được điều chỉnh
        theo chính sách tín dụng, quy định nội bộ
        và hồ sơ thực tế của từng ngân hàng.
        """
    )


# =========================================================
# 12. FOOTER
# =========================================================

st.divider()


st.markdown(
    """
    <div class="footer">

    🏦 CreditVision

    <br>

    Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp

    <br><br>

    © 2026 CreditVision

    </div>
    """,
    unsafe_allow_html=True
)
