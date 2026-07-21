import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="CreditVision - Thẩm định doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. ĐƯỜNG DẪN LOGO
# =========================================================

LOGO_PATH = Path(__file__).parent / "logo.png"


# =========================================================
# 3. CSS - THIẾT KẾ GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       NỀN CHUNG
    ============================== */

    .stApp {
        background-color: #f8fafc;
    }


    /* ==============================
       HEADER
    ============================== */

    .hero {
        padding: 30px 35px;
        border-radius: 20px;
        margin-bottom: 25px;

        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e3a8a 50%,
            #2563eb 100%
        );

        color: white;

        box-shadow:
            0 8px 25px
            rgba(15, 23, 42, 0.15);
    }

    .hero h1 {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 16px;
        margin-top: 5px;
        opacity: 0.9;
    }


    /* ==============================
       SECTION TITLE
    ============================== */

    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #0f172a;
        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* ==============================
       CARD
    ============================== */

    .info-card {
        background: white;
        padding: 22px;
        border-radius: 18px;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 4px 15px
            rgba(15, 23, 42, 0.05);

        margin-bottom: 20px;
    }


    /* ==============================
       KẾT QUẢ TỐT
    ============================== */

    .result-good {

        padding: 28px;

        border-radius: 20px;

        background-color: #ecfdf5;

        border: 2px solid #10b981;

        text-align: center;

        margin-top: 20px;

        box-shadow:
            0 5px 15px
            rgba(16, 185, 129, 0.10);
    }


    /* ==============================
       KẾT QUẢ CẦN XEM XÉT
    ============================== */

    .result-warning {

        padding: 28px;

        border-radius: 20px;

        background-color: #fffbeb;

        border: 2px solid #f59e0b;

        text-align: center;

        margin-top: 20px;

        box-shadow:
            0 5px 15px
            rgba(245, 158, 11, 0.10);
    }


    /* ==============================
       KẾT QUẢ RỦI RO
    ============================== */

    .result-bad {

        padding: 28px;

        border-radius: 20px;

        background-color: #fef2f2;

        border: 2px solid #ef4444;

        text-align: center;

        margin-top: 20px;

        box-shadow:
            0 5px 15px
            rgba(239, 68, 68, 0.10);
    }


    .result-title {

        font-size: 25px;

        font-weight: 800;

        margin-bottom: 10px;
    }


    /* ==============================
       SIDEBAR
    ============================== */

    section[data-testid="stSidebar"] {

        background-color: #f1f5f9;

        border-right:
            1px solid #e2e8f0;
    }


    /* ==============================
       BUTTON
    ============================== */

    .stButton > button {

        width: 100%;

        height: 52px;

        border-radius: 12px;

        font-size: 16px;

        font-weight: 700;

        background-color: #2563eb;

        color: white;

        border: none;

        transition: 0.2s;
    }


    .stButton > button:hover {

        background-color: #1d4ed8;

        transform: translateY(-1px);

    }


    /* ==============================
       METRIC
    ============================== */

    div[data-testid="stMetric"] {

        background-color: white;

        padding: 18px;

        border-radius: 16px;

        border:
            1px solid #e2e8f0;

        box-shadow:
            0 4px 12px
            rgba(15, 23, 42, 0.05);
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    # LOGO
    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    else:

        st.markdown(
            "# 🏦 CreditVision"
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
        "### 📌 Danh mục"
    )

    st.info(
        """
        🏢 Hồ sơ doanh nghiệp

        💰 Phân tích tài chính

        💳 Khoản vay

        🏠 Tài sản bảo đảm

        📊 Kết quả thẩm định
        """
    )

    st.divider()

    st.caption(
        "Phiên bản 1.0"
    )

    st.caption(
        "© 2026 CreditVision"
    )


# =========================================================
# 5. HEADER CHÍNH
# =========================================================

header_col1, header_col2 = st.columns(
    [1, 5]
)


with header_col1:

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            width=150
        )

    else:

        st.markdown(
            "# 🏦"
        )


with header_col2:

    st.markdown(
        """
        <div class="hero">

            <h1>
                CreditVision
            </h1>

            <p>
                HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                CHO VAY DOANH NGHIỆP
            </p>

            <p>
                Phân tích tài chính
                • Khả năng trả nợ
                • Tài sản bảo đảm
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 6. GIỚI THIỆU
# =========================================================

st.info(
    """
    💡 **Hướng dẫn sử dụng:**
    Nhập đầy đủ thông tin doanh nghiệp, tình hình tài chính,
    khoản vay và tài sản bảo đảm. Sau đó nhấn
    **THỰC HIỆN THẨM ĐỊNH** để hệ thống phân tích hồ sơ.
    """
)

st.warning(
    """
    ⚠️ **Lưu ý:** Kết quả của ứng dụng chỉ có mục đích
    hỗ trợ phân tích theo mô hình minh họa.
    Kết quả không thay thế quyết định tín dụng,
    quy trình thẩm định thực tế hoặc quy định nội bộ
    của tổ chức tín dụng.
    """
)


# =========================================================
# 7. THÔNG TIN DOANH NGHIỆP
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🏢 1. THÔNG TIN DOANH NGHIỆP'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    ten_dn = st.text_input(
        "Tên doanh nghiệp *",
        placeholder="VD: Công ty TNHH ABC"
    )


with col2:

    ma_so = st.text_input(
        "Mã số doanh nghiệp",
        placeholder="VD: 0312345678"
    )


with col3:

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


col4, col5 = st.columns(2)


with col4:

    thoi_gian_hd = st.number_input(
        "Thời gian hoạt động (năm)",
        min_value=0,
        value=3,
        step=1
    )


with col5:

    muc_dich_vay = st.selectbox(
        "Mục đích vay",
        [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Đầu tư mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]
    )


phuong_an = st.text_area(
    "📝 Phương án sử dụng vốn *",
    placeholder=(
        "Nhập mô tả chi tiết phương án "
        "sử dụng vốn của doanh nghiệp..."
    ),
    height=120
)


# =========================================================
# 8. TÌNH HÌNH TÀI CHÍNH
# =========================================================

st.markdown(
    '<div class="section-title">'
    '💰 2. PHÂN TÍCH TÀI CHÍNH'
    '</div>',
    unsafe_allow_html=True
)


st.caption(
    "Đơn vị nhập liệu: triệu đồng"
)


c1, c2, c3, c4 = st.columns(4)


with c1:

    doanh_thu = st.number_input(
        "Doanh thu",
        min_value=0.0,
        value=0.0
    )


with c2:

    lnst = st.number_input(
        "Lợi nhuận sau thuế (LNST)",
        value=0.0
    )


with c3:

    tong_tai_san = st.number_input(
        "Tổng tài sản",
        min_value=0.0,
        value=0.0
    )


with c4:

    von_chu_so_huu = st.number_input(
        "Vốn chủ sở hữu",
        min_value=0.0,
        value=0.0
    )


c5, c6 = st.columns(2)


with c5:

    no_phai_tra = st.number_input(
        "Nợ phải trả",
        min_value=0.0,
        value=0.0
    )


with c6:

    dong_tien = st.number_input(
        "Dòng tiền từ hoạt động kinh doanh",
        value=0.0
    )


# =========================================================
# 9. KHOẢN VAY
# =========================================================

st.markdown(
    '<div class="section-title">'
    '💳 3. THÔNG TIN KHOẢN VAY'
    '</div>',
    unsafe_allow_html=True
)


c7, c8, c9 = st.columns(3)


with c7:

    so_tien_vay = st.number_input(
        "Số tiền vay đề nghị",
        min_value=0.0,
        value=0.0
    )


with c8:

    thoi_gian_vay = st.number_input(
        "Thời hạn vay (tháng)",
        min_value=1,
        value=12
    )


with c9:

    lai_suat = st.number_input(
        "Lãi suất cho vay (%/năm)",
        min_value=0.0,
        value=0.0
    )


no_hien_tai = st.number_input(
    "Nghĩa vụ trả nợ hiện tại mỗi tháng",
    min_value=0.0,
    value=0.0
)


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🏠 4. TÀI SẢN BẢO ĐẢM'
    '</div>',
    unsafe_allow_html=True
)


c10, c11 = st.columns(2)


with c10:

    co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Có",
            "Không"
        ]
    )


with c11:

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0,
        value=0.0
    )


# =========================================================
# 11. NÚT THẨM ĐỊNH
# =========================================================

st.divider()


thuc_hien = st.button(
    "🔍  THỰC HIỆN THẨM ĐỊNH HỒ SƠ",
    type="primary",
    use_container_width=True
)


# =========================================================
# 12. XỬ LÝ THẨM ĐỊNH
# =========================================================

if thuc_hien:

    loi = []


    # ---------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # ---------------------------------------------

    if ten_dn.strip() == "":

        loi.append(
            "Chưa nhập tên doanh nghiệp."
        )


    if tong_tai_san <= 0:

        loi.append(
            "Tổng tài sản phải lớn hơn 0."
        )


    if von_chu_so_huu <= 0:

        loi.append(
            "Vốn chủ sở hữu phải lớn hơn 0."
        )


    if so_tien_vay <= 0:

        loi.append(
            "Số tiền vay phải lớn hơn 0."
        )


    if phuong_an.strip() == "":

        loi.append(
            "Chưa nhập phương án sử dụng vốn."
        )


    if (
        co_tsdb == "Có"
        and gia_tri_tsdb <= 0
    ):

        loi.append(
            "Đã chọn có TSĐB nhưng "
            "chưa nhập giá trị TSĐB."
        )


    # ---------------------------------------------
    # NẾU CÓ LỖI
    # ---------------------------------------------

    if loi:

        st.error(
            "⚠️ HỒ SƠ CHƯA ĐỦ DỮ LIỆU"
        )

        for x in loi:

            st.write(
                "❌",
                x
            )


    # ---------------------------------------------
    # NẾU DỮ LIỆU HỢP LỆ
    # ---------------------------------------------

    else:


        # =========================================
        # TÍNH ROA
        # =========================================

        roa = (
            lnst
            / tong_tai_san
            * 100
        )


        # =========================================
        # TÍNH ROE
        # =========================================

        roe = (
            lnst
            / von_chu_so_huu
            * 100
        )


        # =========================================
        # TỶ LỆ NỢ
        # =========================================

        ty_le_no = (
            no_phai_tra
            / tong_tai_san
            * 100
        )


        # =========================================
        # TÍNH LTV
        # =========================================

        if co_tsdb == "Có":

            ltv = (
                so_tien_vay
                / gia_tri_tsdb
                * 100
            )

        else:

            ltv = None


        # =========================================
        # TÍNH GỐC HÀNG THÁNG
        # =========================================

        tien_goc = (
            so_tien_vay
            / thoi_gian_vay
        )


        # =========================================
        # TÍNH LÃI THÁNG ĐẦU
        # =========================================

        tien_lai = (
            so_tien_vay
            * lai_suat
            / 100
            / 12
        )


        # =========================================
        # NGHĨA VỤ NỢ KHOẢN VAY MỚI
        # =========================================

        no_moi = (
            tien_goc
            + tien_lai
        )


        # =========================================
        # TỔNG NGHĨA VỤ NỢ
        # =========================================

        tong_no = (
            no_hien_tai
            + no_moi
        )


        # =========================================
        # TÍNH DTI MÔ HÌNH
        # =========================================

        if dong_tien > 0:

            dti = (
                tong_no
                / dong_tien
                * 100
            )

        else:

            dti = None


        # =========================================
        # CHẤM ĐIỂM
        # =========================================

        diem = 0


        # Tiêu chí 1:
        # Doanh nghiệp có lợi nhuận

        if lnst > 0:

            diem += 1


        # Tiêu chí 2:
        # ROA dương

        if roa > 0:

            diem += 1


        # Tiêu chí 3:
        # ROE dương

        if roe > 0:

            diem += 1


        # Tiêu chí 4:
        # Tỷ lệ nợ <= 70%
        # Đây là tiêu chí mô hình minh họa

        if ty_le_no <= 70:

            diem += 1


        # Tiêu chí 5:
        # DTI <= 70%
        # Đây là tiêu chí mô hình minh họa

        if (
            dti is not None
            and dti <= 70
        ):

            diem += 1


        # =========================================
        # HIỂN THỊ KẾT QUẢ
        # =========================================

        st.divider()

        st.markdown(
            "## 📊 KẾT QUẢ PHÂN TÍCH"
        )


        # -----------------------------------------
        # METRIC
        # -----------------------------------------

        m1, m2, m3, m4, m5 = st.columns(5)


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


        with m4:

            if ltv is not None:

                st.metric(
                    "LTV",
                    f"{ltv:.2f}%"
                )

            else:

                st.metric(
                    "LTV",
                    "N/A"
                )


        with m5:

            st.metric(
                "Điểm mô hình",
                f"{diem}/5"
            )


        # =========================================
        # BIỂU ĐỒ
        # =========================================

        st.markdown(
            "### 📈 BIỂU ĐỒ CHỈ TIÊU TÀI CHÍNH"
        )


        chart_data = pd.DataFrame(

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

            chart_data.set_index(
                "Chỉ tiêu"
            )

        )


        # =========================================
        # KHẢ NĂNG TRẢ NỢ
        # =========================================

        st.markdown(
            "### 💰 KHẢ NĂNG TRẢ NỢ"
        )


        p1, p2, p3 = st.columns(3)


        with p1:

            st.metric(
                "Trả gốc/tháng",
                f"{tien_goc:,.2f} triệu"
            )


        with p2:

            st.metric(
                "Lãi tháng đầu",
                f"{tien_lai:,.2f} triệu"
            )


        with p3:

            st.metric(
                "Tổng nghĩa vụ nợ",
                f"{tong_no:,.2f} triệu"
            )


        if dti is not None:


            if dti <= 50:

                st.success(
                    f"🟢 DTI = {dti:.2f}% — "
                    "Khả năng trả nợ tốt "
                    "theo tiêu chí mô hình."
                )


            elif dti <= 70:

                st.warning(
                    f"🟡 DTI = {dti:.2f}% — "
                    "Khả năng trả nợ cần "
                    "được xem xét thêm."
                )


            else:

                st.error(
                    f"🔴 DTI = {dti:.2f}% — "
                    "Áp lực trả nợ cao "
                    "theo tiêu chí mô hình."
                )


        else:

            st.warning(
                "Chưa thể tính DTI vì "
                "dòng tiền kinh doanh "
                "không lớn hơn 0."
            )


        # =========================================
        # ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM
        # =========================================

        st.markdown(
            "### 🏠 ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM"
        )


        if co_tsdb == "Có":


            if ltv <= 70:

                st.success(

                    f"🟢 LTV = {ltv:.2f}% — "
                    "Mức độ bảo đảm tương đối "
                    "tốt theo tiêu chí mô hình."

                )


            elif ltv <= 100:

                st.warning(

                    f"🟡 LTV = {ltv:.2f}% — "
                    "Cần xem xét thêm."

                )


            else:

                st.error(

                    f"🔴 LTV = {ltv:.2f}% — "
                    "Số tiền vay lớn hơn "
                    "giá trị TSĐB."

                )


        else:

            st.info(

                "Khoản vay không có tài sản bảo đảm. "
                "Cần đánh giá kỹ khả năng trả nợ "
                "và năng lực tài chính."

            )


        # =========================================
        # KẾT LUẬN
        # =========================================

        st.markdown(
            "## 🎯 KẾT LUẬN THẨM ĐỊNH"
        )


        if diem >= 4:


            st.markdown(

                """
                <div class="result-good">

                    <div class="result-title">
                        🟢 ĐỀ XUẤT XEM XÉT CHO VAY
                    </div>

                    <p>
                    Hồ sơ có các chỉ tiêu tích cực
                    theo mô hình hỗ trợ thẩm định.
                    </p>

                    <p>
                    Cần tiếp tục thực hiện thẩm định
                    thực tế và tuân thủ quy định
                    nội bộ của tổ chức tín dụng.
                    </p>

                </div>
                """,

                unsafe_allow_html=True

            )


        elif diem >= 2:


            st.markdown(

                """
                <div class="result-warning">

                    <div class="result-title">
                        🟡 CẦN THẨM ĐỊNH THÊM
                    </div>

                    <p>
                    Hồ sơ có một số chỉ tiêu tích cực
                    nhưng cần phân tích bổ sung
                    về khả năng trả nợ và rủi ro.
                    </p>

                </div>
                """,

                unsafe_allow_html=True

            )


        else:


            st.markdown(

                """
                <div class="result-bad">

                    <div class="result-title">
                        🔴 RỦI RO CAO THEO MÔ HÌNH
                    </div>

                    <p>
                    Hồ sơ chưa đáp ứng tốt các tiêu chí
                    của mô hình hỗ trợ thẩm định.
                    </p>

                    <p>
                    Kết quả này không đồng nghĩa với việc
                    pháp luật cấm cho vay.
                    </p>

                </div>
                """,

                unsafe_allow_html=True

            )


        # =========================================
        # BẢNG TỔNG HỢP
        # =========================================

        st.markdown(
            "### 📑 BẢNG TỔNG HỢP HỒ SƠ"
        )


        ket_qua = pd.DataFrame(

            {

                "Thông tin": [

                    "Tên doanh nghiệp",

                    "Mã số doanh nghiệp",

                    "Ngành nghề",

                    "Mục đích vay",

                    "Doanh thu",

                    "LNST",

                    "Tổng tài sản",

                    "Vốn chủ sở hữu",

                    "Nợ phải trả",

                    "ROA",

                    "ROE",

                    "Tỷ lệ nợ",

                    "Số tiền vay",

                    "Thời hạn vay",

                    "Lãi suất",

                    "Giá trị TSĐB",

                    "LTV",

                    "DTI",

                    "Điểm mô hình"

                ],


                "Kết quả": [

                    ten_dn,

                    ma_so,

                    nganh_nghe,

                    muc_dich_vay,

                    f"{doanh_thu:,.2f} triệu đồng",

                    f"{lnst:,.2f} triệu đồng",

                    f"{tong_tai_san:,.2f} triệu đồng",

                    f"{von_chu_so_huu:,.2f} triệu đồng",

                    f"{no_phai_tra:,.2f} triệu đồng",

                    f"{roa:.2f}%",

                    f"{roe:.2f}%",

                    f"{ty_le_no:.2f}%",

                    f"{so_tien_vay:,.2f} triệu đồng",

                    f"{thoi_gian_vay} tháng",

                    f"{lai_suat:.2f}%/năm",

                    f"{gia_tri_tsdb:,.2f} triệu đồng",

                    (
                        f"{ltv:.2f}%"
                        if ltv is not None
                        else "Không áp dụng"
                    ),

                    (
                        f"{dti:.2f}%"
                        if dti is not None
                        else "Không xác định"
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


        # =========================================
        # TẢI BÁO CÁO
        # =========================================

        st.markdown(
            "### 📥 XUẤT BÁO CÁO"
        )


        csv = ket_qua.to_csv(

            index=False

        ).encode(

            "utf-8-sig"

        )


        ten_file = (

            ten_dn.strip()
            if ten_dn.strip()
            else "doanh_nghiep"

        )


        st.download_button(

            label=(
                "📥 TẢI BÁO CÁO THẨM ĐỊNH "
                "DẠNG CSV"
            ),

            data=csv,

            file_name=(
                f"bao_cao_tham_dinh_"
                f"{ten_file}.csv"
            ),

            mime="text/csv",

            use_container_width=True

        )


# =========================================================
# 13. FOOTER
# =========================================================

st.divider()

st.markdown(

    """
    <div style="
        text-align: center;
        color: #64748b;
        padding: 20px;
    ">

        🏦 <b>CreditVision</b>
        <br>

        Hệ thống hỗ trợ thẩm định
        cho vay doanh nghiệp

        <br>

        <small>
        Kết quả chỉ mang tính chất hỗ trợ phân tích
        </small>

    </div>
    """,

    unsafe_allow_html=True

)
