import streamlit as st
import pandas as pd
from pathlib import Path


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {

    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # Điều kiện vay vốn
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
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

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "no_hien_tai": 0.0,

    # TSĐB
    "co_tsdb": "Có",
    "gia_tri_tsdb": 0.0,

    # Trạng thái
    "da_phan_tich_tai_chinh": False,
    "da_tinh_khoan_vay": False,
    "da_danh_gia_tsdb": False,
    "da_kiem_tra_dieu_kien": False
}


for key, value in default_values.items():

    if key not in st.session_state:

        st.session_state[key] = value


# =========================================================
# 3. CSS - GIỮ GIAO DIỆN ĐẸP
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
       TIÊU ĐỀ
    ========================= */

    .main-title {
        font-size: 32px;
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
       HEADER
    ========================= */

    .header-box {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 5px 15px rgba(15, 23, 42, 0.06);
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
        height: 48px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 15px;
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
# 4. LOGO
# =========================================================

LOGO_PATH = Path("logo.png")


# =========================================================
# 5. SIDEBAR
# =========================================================

with st.sidebar:

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    else:

        st.markdown(
            "## 🏦"
        )

    st.divider()

    st.markdown(
        "### 🏦 HỆ THỐNG THẨM ĐỊNH"
    )

    st.caption(
        "Hỗ trợ thẩm định cho vay doanh nghiệp"
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
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption(
        "Hệ thống hỗ trợ thẩm định"
    )

    st.caption(
        "© 2026"
    )


# =========================================================
# 6. HEADER
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

        st.markdown(
            "## 🏦"
        )


with col_header:

    st.markdown(
        '<div class="main-title">'
        '🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH '
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

    st.info(
        """
        👋 **Chào mừng bạn đến với Hệ thống hỗ trợ thẩm định
        cho vay doanh nghiệp**

        Hệ thống hỗ trợ cán bộ/người dùng nhập thông tin hồ sơ,
        kiểm tra điều kiện vay vốn, phân tích tài chính,
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
            "⚖️",
            "Điều kiện vay"
        )

    with c3:
        st.metric(
            "💰",
            "Phân tích tài chính"
        )

    with c4:
        st.metric(
            "📊",
            "Kết quả"
        )

    st.divider()

    st.markdown(
        "### 📋 Quy trình sử dụng"
    )

    st.write(
        """
        **Bước 1:** Nhập thông tin doanh nghiệp.

        **Bước 2:** Kiểm tra điều kiện vay vốn.

        **Bước 3:** Nhập và phân tích các chỉ tiêu tài chính.

        **Bước 4:** Nhập thông tin khoản vay và khả năng trả nợ.

        **Bước 5:** Nhập thông tin tài sản bảo đảm nếu có.

        **Bước 6:** Xem kết quả thẩm định tổng hợp.
        """
    )

    st.warning(
        """
        ⚠️ Kết quả của hệ thống chỉ mang tính chất hỗ trợ phân tích
        và minh họa. Không thay thế quyết định cấp tín dụng thực tế
        của tổ chức tín dụng.
        """
    )


# =========================================================
# 8. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.markdown(
        "## 🏢 Hồ sơ doanh nghiệp"
    )

    st.caption(
        "Nhập thông tin cơ bản của doanh nghiệp."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.session_state.ten_dn = st.text_input(
            "Tên doanh nghiệp",
            value=st.session_state.ten_dn,
            placeholder="Ví dụ: Công ty TNHH ABC"
        )

        st.session_state.ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so,
            placeholder="Ví dụ: 0312345678"
        )

        st.session_state.thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

    with col2:

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

        st.session_state.muc_dich_vay = st.selectbox(
            "Mục đích vay",
            [
                "Bổ sung vốn lưu động",
                "Mua nguyên vật liệu",
                "Đầu tư máy móc thiết bị",
                "Mở rộng sản xuất",
                "Mua tài sản cố định",
                "Khác"
            ],
            index=[
                "Bổ sung vốn lưu động",
                "Mua nguyên vật liệu",
                "Đầu tư máy móc thiết bị",
                "Mở rộng sản xuất",
                "Mua tài sản cố định",
                "Khác"
            ].index(st.session_state.muc_dich_vay)
        )

    st.session_state.phuong_an = st.text_area(
        "Phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        height=150,
        placeholder="Mô tả chi tiết phương án sử dụng vốn..."
    )

    if st.button(
        "💾 LƯU THÔNG TIN DOANH NGHIỆP"
    ):

        if not st.session_state.ten_dn.strip():

            st.error(
                "Vui lòng nhập tên doanh nghiệp."
            )

        elif not st.session_state.ma_so.strip():

            st.error(
                "Vui lòng nhập mã số doanh nghiệp."
            )

        elif not st.session_state.phuong_an.strip():

            st.error(
                "Vui lòng nhập phương án sử dụng vốn."
            )

        else:

            st.success(
                "✅ Đã lưu thông tin hồ sơ doanh nghiệp."
            )


# =========================================================
# 9. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.markdown(
        "## ⚖️ Điều kiện vay vốn"
    )

    st.info(
        """
        Phần này kiểm tra các điều kiện vay vốn cơ bản theo
        quy định pháp luật về hoạt động cho vay.

        ROA, ROE, LNST, tỷ lệ nợ và LTV được sử dụng ở phần
        phân tích tín dụng hỗ trợ, không phải điều kiện pháp lý
        bắt buộc chung cho mọi doanh nghiệp.
        """
    )

    st.markdown(
        "### 1️⃣ Điều kiện pháp lý và mục đích vay"
    )

    st.session_state.nang_luc_phap_ly = st.selectbox(
        "Doanh nghiệp có năng lực pháp luật dân sự?",
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

    st.session_state.muc_dich_hop_phap = st.selectbox(
        "Mục đích sử dụng vốn có hợp pháp?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ],
        index=[
            "Chưa đánh giá",
            "Có",
            "Không"
        ].index(st.session_state.muc_dich_hop_phap)
    )

    st.markdown(
        "### 2️⃣ Phương án sử dụng vốn"
    )

    st.session_state.co_phuong_an = st.selectbox(
        "Doanh nghiệp có phương án sử dụng vốn?",
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

    st.markdown(
        "### 3️⃣ Khả năng tài chính trả nợ"
    )

    st.session_state.kha_nang_tra_no = st.selectbox(
        "Doanh nghiệp có khả năng tài chính để trả nợ?",
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

    st.markdown(
        "### 4️⃣ Cam kết của doanh nghiệp"
    )

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

    st.session_state.tra_no_dung_han = st.selectbox(
        "Cam kết hoàn trả nợ gốc và lãi đúng hạn?",
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

    st.divider()

    if st.button(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    ):

        dieu_kien = [

            st.session_state.nang_luc_phap_ly == "Có",

            st.session_state.muc_dich_hop_phap == "Có",

            st.session_state.co_phuong_an == "Có",

            st.session_state.phuong_an_kha_thi == "Có",

            st.session_state.kha_nang_tra_no == "Có",

            st.session_state.dung_muc_dich == "Có",

            st.session_state.tra_no_dung_han == "Có"
        ]

        so_dieu_kien_dat = sum(dieu_kien)

        st.session_state.da_kiem_tra_dieu_kien = True

        st.metric(
            "Số điều kiện đạt",
            f"{so_dieu_kien_dat}/7"
        )

        if so_dieu_kien_dat == 7:

            st.success(
                """
                🟢 **ĐẠT ĐIỀU KIỆN SƠ BỘ**

                Các điều kiện được kiểm tra đều đáp ứng.
                Hồ sơ có thể tiếp tục được thẩm định tín dụng chi tiết.
                """
            )

        elif so_dieu_kien_dat >= 5:

            st.warning(
                """
                🟡 **CẦN XEM XÉT THÊM**

                Doanh nghiệp chưa đáp ứng đầy đủ các tiêu chí
                được kiểm tra. Cần bổ sung hoặc xác minh thêm hồ sơ.
                """
            )

        else:

            st.error(
                """
                🔴 **CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ**

                Doanh nghiệp chưa đáp ứng nhiều điều kiện
                trong mô hình kiểm tra.
                """
            )


# =========================================================
# 10. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.markdown(
        "## 💰 Phân tích tài chính"
    )

    st.caption(
        "Đơn vị: triệu đồng"
    )

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

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
        "📊 TÍNH CHỈ TIÊU TÀI CHÍNH"
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

            roa = (
                st.session_state.lnst
                / st.session_state.tong_tai_san
                * 100
            )

            roe = (
                st.session_state.lnst
                / st.session_state.von_chu_so_huu
                * 100
            )

            ty_le_no = (
                st.session_state.no_phai_tra
                / st.session_state.tong_tai_san
                * 100
            )

            st.session_state.da_phan_tich_tai_chinh = True

            c1, c2, c3 = st.columns(3)

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
                    "Tỷ lệ nợ",
                    f"{ty_le_no:.2f}%"
                )

            data = pd.DataFrame(
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
                data.set_index(
                    "Chỉ tiêu"
                )
            )


# =========================================================
# 11. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.markdown(
        "## 💳 Thông tin khoản vay"
    )

    st.caption(
        "Đơn vị: triệu đồng"
    )

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

        st.session_state.lai_suat = st.number_input(
            "Lãi suất cho vay (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )

        st.session_state.no_hien_tai = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.no_hien_tai
        )

    if st.button(
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ"
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

        no_moi = (
            tien_goc
            + tien_lai
        )

        tong_nghia_vu = (
            st.session_state.no_hien_tai
            + no_moi
        )

        st.session_state.da_tinh_khoan_vay = True

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
                "Tổng nghĩa vụ/tháng",
                f"{tong_nghia_vu:,.2f}"
            )

        st.info(
            """
            ℹ️ Đây là phép tính minh họa theo phương pháp
            chia đều gốc hàng tháng và tính lãi trên số tiền vay ban đầu.
            Lịch trả nợ thực tế phụ thuộc phương thức cấp tín dụng.
            """
        )


# =========================================================
# 12. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.markdown(
        "## 🏠 Tài sản bảo đảm"
    )

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm của khoản vay.
        Ngưỡng LTV cụ thể phụ thuộc chính sách tín dụng của từng tổ chức
        tín dụng và loại tài sản, không phải điều kiện pháp lý chung.
        """
    )

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Có",
            "Không"
        ],
        index=[
            "Có",
            "Không"
        ].index(st.session_state.co_tsdb)
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    if st.button(
        "🏠 ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM"
    ):

        if st.session_state.co_tsdb == "Không":

            st.session_state.da_danh_gia_tsdb = True

            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "Vui lòng nhập số tiền vay ở mục Thông tin khoản vay."
            )

        else:

            ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            st.session_state.da_danh_gia_tsdb = True

            st.metric(
                "LTV",
                f"{ltv:.2f}%"
            )

            if ltv <= 70:

                st.success(
                    "🟢 LTV ở mức tương đối thấp theo mô hình minh họa."
                )

            elif ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 13. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.markdown(
        "## 📊 KẾT QUẢ THẨM ĐỊNH"
    )

    # -----------------------------------------------------
    # THÔNG TIN DOANH NGHIỆP
    # -----------------------------------------------------

    st.markdown(
        "### 🏢 1. Thông tin doanh nghiệp"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Tên doanh nghiệp",
            st.session_state.ten_dn
            if st.session_state.ten_dn
            else "Chưa nhập"
        )

    with c2:
        st.metric(
            "Mã số",
            st.session_state.ma_so
            if st.session_state.ma_so
            else "Chưa nhập"
        )

    with c3:
        st.metric(
            "Thời gian hoạt động",
            f"{st.session_state.thoi_gian_hd} năm"
        )

    st.divider()

    # -----------------------------------------------------
    # ĐIỀU KIỆN VAY
    # -----------------------------------------------------

    st.markdown(
        "### ⚖️ 2. Điều kiện vay vốn"
    )

    dieu_kien = [

        st.session_state.nang_luc_phap_ly == "Có",

        st.session_state.muc_dich_hop_phap == "Có",

        st.session_state.co_phuong_an == "Có",

        st.session_state.phuong_an_kha_thi == "Có",

        st.session_state.kha_nang_tra_no == "Có",

        st.session_state.dung_muc_dich == "Có",

        st.session_state.tra_no_dung_han == "Có"
    ]

    so_dieu_kien_dat = sum(dieu_kien)

    st.metric(
        "Điều kiện đạt",
        f"{so_dieu_kien_dat}/7"
    )

    if so_dieu_kien_dat == 7:

        st.success(
            "🟢 Đạt đầy đủ các điều kiện sơ bộ được kiểm tra."
        )

    elif so_dieu_kien_dat >= 5:

        st.warning(
            "🟡 Cần xem xét và bổ sung thông tin."
        )

    else:

        st.error(
            "🔴 Chưa đáp ứng đầy đủ điều kiện sơ bộ."
        )

    st.divider()

    # -----------------------------------------------------
    # PHÂN TÍCH TÀI CHÍNH
    # -----------------------------------------------------

    st.markdown(
        "### 💰 3. Phân tích tài chính"
    )

    if st.session_state.tong_tai_san > 0:

        roa = (
            st.session_state.lnst
            / st.session_state.tong_tai_san
            * 100
        )

        if st.session_state.von_chu_so_huu > 0:

            roe = (
                st.session_state.lnst
                / st.session_state.von_chu_so_huu
                * 100
            )

        else:

            roe = 0

        ty_le_no = (
            st.session_state.no_phai_tra
            / st.session_state.tong_tai_san
            * 100
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "LNST",
                f"{st.session_state.lnst:,.2f}"
            )

        with c2:

            st.metric(
                "ROA",
                f"{roa:.2f}%"
            )

        with c3:

            st.metric(
                "ROE",
                f"{roe:.2f}%"
            )

        with c4:

            st.metric(
                "Tỷ lệ nợ",
                f"{ty_le_no:.2f}%"
            )

    else:

        st.warning(
            "Chưa đủ dữ liệu tài chính để tính các chỉ tiêu."
        )

    st.divider()

    # -----------------------------------------------------
    # KHOẢN VAY
    # -----------------------------------------------------

    st.markdown(
        "### 💳 4. Thông tin khoản vay"
    )

    if st.session_state.so_tien_vay > 0:

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
            st.session_state.no_hien_tai
            + tien_goc
            + tien_lai
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Số tiền vay",
                f"{st.session_state.so_tien_vay:,.2f}"
            )

        with c2:

            st.metric(
                "Thời hạn",
                f"{st.session_state.thoi_gian_vay} tháng"
            )

        with c3:

            st.metric(
                "Nghĩa vụ/tháng",
                f"{tong_nghia_vu:,.2f}"
            )

    else:

        st.warning(
            "Chưa nhập thông tin khoản vay."
        )

    st.divider()

    # -----------------------------------------------------
    # TÀI SẢN BẢO ĐẢM
    # -----------------------------------------------------

    st.markdown(
        "### 🏠 5. Tài sản bảo đảm"
    )

    if st.session_state.co_tsdb == "Có":

        if (
            st.session_state.gia_tri_tsdb > 0
            and st.session_state.so_tien_vay > 0
        ):

            ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Giá trị TSĐB",
                    f"{st.session_state.gia_tri_tsdb:,.2f}"
                )

            with c2:

                st.metric(
                    "LTV",
                    f"{ltv:.2f}%"
                )

        else:

            st.warning(
                "Chưa đủ dữ liệu để tính LTV."
            )

    else:

        st.info(
            "Khoản vay không có tài sản bảo đảm."
        )

    st.divider()

    # -----------------------------------------------------
    # KẾT LUẬN
    # -----------------------------------------------------

    st.markdown(
        "### 🎯 6. KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
    )

    # Điều kiện pháp lý/sơ bộ
    dieu_kien_phap_ly_dat = (
        so_dieu_kien_dat == 7
    )

    # Phân tích tài chính
    co_du_lieu_tai_chinh = (
        st.session_state.tong_tai_san > 0
        and st.session_state.von_chu_so_huu > 0
    )

    # Khoản vay
    co_du_lieu_khoan_vay = (
        st.session_state.so_tien_vay > 0
    )

    # Kết luận
    if (
        dieu_kien_phap_ly_dat
        and co_du_lieu_tai_chinh
        and co_du_lieu_khoan_vay
    ):

        st.success(
            """
            🟢 **ĐỀ XUẤT TIẾP TỤC THẨM ĐỊNH**

            Doanh nghiệp đáp ứng các điều kiện sơ bộ được kiểm tra
            và đã cung cấp các thông tin cơ bản để tiếp tục đánh giá.

            Hồ sơ cần được thẩm định chi tiết trước khi đưa ra
            quyết định cấp tín dụng.
            """
        )

    elif (
        so_dieu_kien_dat >= 5
        and co_du_lieu_khoan_vay
    ):

        st.warning(
            """
            🟡 **CẦN BỔ SUNG VÀ XEM XÉT THÊM**

            Hồ sơ đã có một số điều kiện đáp ứng nhưng chưa đủ cơ sở
            để đề xuất tiếp tục thẩm định đầy đủ.
            """
        )

    else:

        st.error(
            """
            🔴 **CHƯA ĐỦ CƠ SỞ ĐỀ XUẤT**

            Hồ sơ chưa đáp ứng đầy đủ các điều kiện sơ bộ
            hoặc chưa cung cấp đủ thông tin cần thiết.
            """
        )

    st.info(
        """
        ⚠️ **Lưu ý pháp lý và nghiệp vụ:**

        ROA, ROE, LNST, tỷ lệ nợ, LTV và giá trị tài sản bảo đảm
        là các chỉ tiêu hỗ trợ phân tích tín dụng. Các chỉ tiêu này
        không được sử dụng như các điều kiện pháp lý bắt buộc chung
        áp dụng cho mọi doanh nghiệp.

        Quyết định cho vay thực tế phải dựa trên hồ sơ, kết quả thẩm định,
        quy định pháp luật hiện hành và chính sách tín dụng của tổ chức
        tín dụng.
        """
    )


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
