import streamlit as st
import pandas as pd
from datetime import datetime


# ============================================================
# 1. CẤU HÌNH ỨNG DỤNG
# ============================================================

st.set_page_config(
    page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# 2. KHỞI TẠO SESSION STATE
# ============================================================

DEFAULT_VALUES = {
    # --------------------------------------------------------
    # ĐIỀU HƯỚNG
    # --------------------------------------------------------
    "buoc_hien_tai": 1,

    # --------------------------------------------------------
    # HỒ SƠ DOANH NGHIỆP
    # --------------------------------------------------------
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # --------------------------------------------------------
    # ĐIỀU KIỆN VAY
    # --------------------------------------------------------
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_su_dung_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "su_dung_von_dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # --------------------------------------------------------
    # TÀI CHÍNH
    # --------------------------------------------------------
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # --------------------------------------------------------
    # KẾT QUẢ TÀI CHÍNH
    # --------------------------------------------------------
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # --------------------------------------------------------
    # KHOẢN VAY
    # --------------------------------------------------------
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # --------------------------------------------------------
    # KHẢ NĂNG TRẢ NỢ
    # --------------------------------------------------------
    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # --------------------------------------------------------
    # TÀI SẢN BẢO ĐẢM
    # --------------------------------------------------------
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # --------------------------------------------------------
    # TRẠNG THÁI
    # --------------------------------------------------------
    "da_luu_ho_so": False,
    "da_kiem_tra_dieu_kien": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_dscr": False,
    "da_phan_tich_tsdb": False,

    # --------------------------------------------------------
    # MYSQL
    # --------------------------------------------------------
    "mysql_da_luu": False
}


for key, value in DEFAULT_VALUES.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# 3. CSS - GIAO DIỆN
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       NỀN CHUNG
    ====================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(26, 132, 196, 0.10),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #f5f9fd 0%,
                #edf5fb 50%,
                #f8fbff 100%
            );
    }


    /* ======================================================
       ẨN MENU MẶC ĐỊNH
    ====================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ======================================================
       HEADER
    ====================================================== */

    .main-header {
        background:
            linear-gradient(
                135deg,
                #06294b,
                #0a5685,
                #1496c7
            );

        padding: 28px 35px;
        border-radius: 22px;

        color: white;

        box-shadow:
            0 12px 30px
            rgba(5, 54, 91, 0.20);

        margin-bottom: 25px;
    }

    .main-header h1 {
        color: white !important;
        font-size: 30px !important;
        font-weight: 800 !important;
        margin-bottom: 8px !important;
    }

    .main-header p {
        color: rgba(255,255,255,0.90) !important;
        font-size: 16px;
        margin-bottom: 0;
    }


    /* ======================================================
       THANH TIẾN TRÌNH
    ====================================================== */

    .progress-box {
        background: white;
        border-radius: 18px;
        padding: 18px 22px;
        border: 1px solid #dbe8f2;
        box-shadow:
            0 5px 18px
            rgba(8,43,76,0.06);

        margin-bottom: 22px;
    }

    .step-active {
        background:
            linear-gradient(
                135deg,
                #07518a,
                #1193ca
            );

        color: white;

        padding: 12px;
        border-radius: 12px;

        text-align: center;
        font-weight: 800;
    }

    .step-done {
        background: #e8f7ef;
        color: #187343;

        padding: 12px;
        border-radius: 12px;

        text-align: center;
        font-weight: 700;
    }

    .step-normal {
        background: #f1f5f8;
        color: #71869b;

        padding: 12px;
        border-radius: 12px;

        text-align: center;
        font-weight: 600;
    }


    /* ======================================================
       CARD
    ====================================================== */

    .card {
        background: white;

        padding: 25px;

        border-radius: 20px;

        border: 1px solid #dce8f3;

        box-shadow:
            0 7px 22px
            rgba(8,43,76,0.07);

        margin-bottom: 22px;
    }


    /* ======================================================
       TIÊU ĐỀ
    ====================================================== */

    h1 {
        color: #082b4c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b416d !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #125d8e !important;
        font-weight: 750 !important;
    }


    /* ======================================================
       BUTTON
    ====================================================== */

    .stButton > button {
        width: 100%;

        min-height: 48px;

        border-radius: 12px;

        border: none;

        font-weight: 750;

        transition: all 0.2s ease;

        box-shadow:
            0 5px 15px
            rgba(7,81,138,0.15);
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 8px 20px
            rgba(7,81,138,0.22);
    }


    /* ======================================================
       METRIC
    ====================================================== */

    div[data-testid="stMetric"] {
        background: white;

        border: 1px solid #d7e5f2;

        padding: 18px;

        border-radius: 16px;

        box-shadow:
            0 5px 18px
            rgba(8,43,76,0.06);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3d66 !important;
        font-weight: 800;
    }


    /* ======================================================
       TRẠNG THÁI
    ====================================================== */

    .status-good {
        background: #e8f8ef;

        border-left: 6px solid #1c9b58;

        padding: 18px;

        border-radius: 12px;

        color: #17663b;

        font-weight: 750;

        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;

        border-left: 6px solid #e0a000;

        padding: 18px;

        border-radius: 12px;

        color: #765800;

        font-weight: 750;

        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;

        border-left: 6px solid #d43d3d;

        padding: 18px;

        border-radius: 12px;

        color: #852323;

        font-weight: 750;

        font-size: 18px;
    }


    /* ======================================================
       FOOTER
    ====================================================== */

    .footer {
        text-align: center;

        color: #71869b;

        padding: 25px;

        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. HEADER
# ============================================================

st.markdown(
    """
    <div class="main-header">
        <h1>🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</h1>
        <p>
            Hệ thống hỗ trợ nhập hồ sơ, phân tích tài chính,
            đánh giá khả năng trả nợ và tổng hợp kết quả thẩm định sơ bộ.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 5. THANH TIẾN TRÌNH
# ============================================================

steps = [
    "🏢 Hồ sơ",
    "⚖️ Điều kiện",
    "💰 Tài chính",
    "💳 Khoản vay",
    "🏠 TSĐB",
    "📊 Kết quả"
]

current_step = st.session_state.buoc_hien_tai

st.markdown(
    '<div class="progress-box">',
    unsafe_allow_html=True
)

progress_cols = st.columns(6)

for i, step in enumerate(steps, start=1):

    with progress_cols[i - 1]:

        if i < current_step:

            st.markdown(
                f"""
                <div class="step-done">
                    ✅ {i}. {step}
                </div>
                """,
                unsafe_allow_html=True
            )

        elif i == current_step:

            st.markdown(
                f"""
                <div class="step-active">
                    🔵 {i}. {step}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="step-normal">
                    {i}. {step}
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 6. HÀM ĐIỀU HƯỚNG
# ============================================================

def go_next():
    if st.session_state.buoc_hien_tai < 6:
        st.session_state.buoc_hien_tai += 1


def go_back():
    if st.session_state.buoc_hien_tai > 1:
        st.session_state.buoc_hien_tai -= 1


def go_home():
    st.session_state.buoc_hien_tai = 1


# ============================================================
# 7. BƯỚC 1 - HỒ SƠ DOANH NGHIỆP
# ============================================================

if current_step == 1:

    st.title("🏢 Bước 1: Hồ sơ doanh nghiệp")

    st.caption(
        "Nhập các thông tin cơ bản về doanh nghiệp và phương án sử dụng vốn."
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("🏢 Thông tin doanh nghiệp")

    c1, c2 = st.columns(2)

    with c1:

        ten_dn = st.text_input(
            "🏷️ Tên doanh nghiệp",
            value=st.session_state.ten_dn,
            placeholder="Ví dụ: Công ty TNHH ABC"
        )

        ma_so = st.text_input(
            "🆔 Mã số doanh nghiệp",
            value=st.session_state.ma_so,
            placeholder="Nhập mã số doanh nghiệp"
        )

        thoi_gian_hd = st.number_input(
            "📅 Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

    with c2:

        danh_sach_nganh = [
            "Sản xuất",
            "Thương mại",
            "Dịch vụ",
            "Xây dựng",
            "Vận tải",
            "Công nghệ",
            "Nông nghiệp",
            "Khác"
        ]

        nganh_nghe = st.selectbox(
            "🏭 Ngành nghề kinh doanh",
            danh_sach_nganh,
            index=danh_sach_nganh.index(
                st.session_state.nganh_nghe
            )
        )

        muc_dich_list = [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]

        muc_dich_vay = st.selectbox(
            "🎯 Mục đích sử dụng vốn",
            muc_dich_list,
            index=muc_dich_list.index(
                st.session_state.muc_dich_vay
            )
        )

    phuong_an = st.text_area(
        "📝 Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        height=150,
        placeholder=(
            "Nhập nội dung phương án kinh doanh, "
            "nhu cầu vay vốn, mục đích sử dụng vốn..."
        )
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([1, 1])

    with c1:

        if st.button(
            "💾 LƯU HỒ SƠ",
            key="save_profile"
        ):

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
                    "❌ Vui lòng nhập phương án sử dụng vốn."
                )

            else:

                st.session_state.ten_dn = ten_dn
                st.session_state.ma_so = ma_so
                st.session_state.nganh_nghe = nganh_nghe
                st.session_state.thoi_gian_hd = thoi_gian_hd
                st.session_state.muc_dich_vay = muc_dich_vay
                st.session_state.phuong_an = phuong_an
                st.session_state.da_luu_ho_so = True

                st.success(
                    "✅ Đã lưu hồ sơ doanh nghiệp."
                )

    with c2:

        if st.button(
            "TIẾP TỤC →",
            key="next_step_1"
        ):

            if ten_dn.strip() == "":

                st.error(
                    "❌ Vui lòng nhập tên doanh nghiệp trước khi tiếp tục."
                )

            elif ma_so.strip() == "":

                st.error(
                    "❌ Vui lòng nhập mã số doanh nghiệp trước khi tiếp tục."
                )

            elif phuong_an.strip() == "":

                st.error(
                    "❌ Vui lòng nhập phương án sử dụng vốn trước khi tiếp tục."
                )

            else:

                st.session_state.ten_dn = ten_dn
                st.session_state.ma_so = ma_so
                st.session_state.nganh_nghe = nganh_nghe
                st.session_state.thoi_gian_hd = thoi_gian_hd
                st.session_state.muc_dich_vay = muc_dich_vay
                st.session_state.phuong_an = phuong_an
                st.session_state.da_luu_ho_so = True

                go_next()


# ============================================================
# 8. BƯỚC 2 - ĐIỀU KIỆN VAY
# ============================================================

elif current_step == 2:

    st.title("⚖️ Bước 2: Kiểm tra điều kiện vay vốn")

    st.caption(
        "Đánh giá sơ bộ các điều kiện liên quan đến hồ sơ vay vốn."
    )

    options = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "⚖️ Năng lực pháp lý phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "🎯 Mục đích vay vốn hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.phuong_an_su_dung_von = st.selectbox(
            "💰 Có phương án sử dụng vốn?",
            options,
            index=options.index(
                st.session_state.phuong_an_su_dung_von
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "📈 Phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "💳 Có khả năng tài chính trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )

        st.session_state.su_dung_von_dung_muc_dich = st.selectbox(
            "🔐 Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.su_dung_von_dung_muc_dich
            )
        )

        st.session_state.tra_no_dung_han = st.selectbox(
            "⏰ Cam kết trả nợ đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    dieu_kien = [
        st.session_state.nang_luc_phap_ly,
        st.session_state.muc_dich_hop_phap,
        st.session_state.phuong_an_su_dung_von,
        st.session_state.phuong_an_kha_thi,
        st.session_state.kha_nang_tra_no,
        st.session_state.su_dung_von_dung_muc_dich,
        st.session_state.tra_no_dung_han
    ]

    co_khong = "Không" in dieu_kien
    co_chua_danh_gia = "Chưa đánh giá" in dieu_kien

    if st.button(
        "🔍 KIỂM TRA ĐIỀU KIỆN",
        key="check_condition"
    ):

        st.session_state.da_kiem_tra_dieu_kien = True

        if co_khong:

            st.error(
                "🔴 Có ít nhất một điều kiện được đánh giá là Không."
            )

        elif co_chua_danh_gia:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "← QUAY LẠI",
            key="back_step_2"
        ):

            go_back()

    with c2:

        if st.button(
            "TIẾP TỤC →",
            key="next_step_2"
        ):

            if co_khong:

                st.warning(
                    "⚠️ Hồ sơ đang có điều kiện được đánh giá là Không. "
                    "Bạn vẫn có thể tiếp tục để hoàn thiện phân tích."
                )

            go_next()


# ============================================================
# 9. BƯỚC 3 - PHÂN TÍCH TÀI CHÍNH
# ============================================================

elif current_step == 3:

    st.title("💰 Bước 3: Phân tích tài chính")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng."
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

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
            "💧 Dòng tiền từ hoạt động kinh doanh / tháng",
            value=st.session_state.dong_tien
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "📊 PHÂN TÍCH TÀI CHÍNH",
        key="analyze_finance"
    ):

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

        st.subheader("📈 Kết quả phân tích")

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

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "← QUAY LẠI",
            key="back_step_3"
        ):

            go_back()

    with c2:

        if st.button(
            "TIẾP TỤC →",
            key="next_step_3"
        ):

            if not st.session_state.da_phan_tich_tc:

                st.warning(
                    "⚠️ Vui lòng phân tích tài chính trước khi tiếp tục."
                )

            else:

                go_next()


# ============================================================
# 10. BƯỚC 4 - KHOẢN VAY & KHẢ NĂNG TRẢ NỢ
# ============================================================

elif current_step == 4:

    st.title("💳 Bước 4: Khoản vay & khả năng trả nợ")

    st.caption(
        "Tính nghĩa vụ trả nợ và đánh giá DSCR."
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader("💳 Thông tin khoản vay")

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

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ",
        key="calculate_debt"
    ):

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
                "✅ Đã tính nghĩa vụ trả nợ."
            )

    if st.session_state.tong_nghia_vu is not None:

        st.subheader("📌 Nghĩa vụ trả nợ dự kiến")

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

        st.divider()

        st.subheader("📈 Phân tích khả năng trả nợ")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )

        with c2:

            st.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

        if st.button(
            "📈 PHÂN TÍCH DSCR",
            key="analyze_dscr"
        ):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )

                st.session_state.da_phan_tich_dscr = True

                if st.session_state.dscr >= 1:

                    st.success(
                        f"🟢 DSCR = {st.session_state.dscr:.2f} lần. "
                        "Dòng tiền hiện tại đủ đáp ứng nghĩa vụ trả nợ theo chỉ tiêu hỗ trợ."
                    )

                else:

                    st.warning(
                        f"🟡 DSCR = {st.session_state.dscr:.2f} lần. "
                        "Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "← QUAY LẠI",
            key="back_step_4"
        ):

            go_back()

    with c2:

        if st.button(
            "TIẾP TỤC →",
            key="next_step_4"
        ):

            if not st.session_state.da_phan_tich_vay:

                st.warning(
                    "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
                )

            else:

                go_next()


# ============================================================
# 11. BƯỚC 5 - TÀI SẢN BẢO ĐẢM
# ============================================================

elif current_step == 5:

    st.title("🏠 Bước 5: Tài sản bảo đảm")

    st.caption(
        "Đánh giá sơ bộ tài sản bảo đảm và tỷ lệ LTV."
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    options_tsdb = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    st.session_state.co_tsdb = st.selectbox(
        "🏠 Khoản vay có tài sản bảo đảm?",
        options_tsdb,
        index=options_tsdb.index(
            st.session_state.co_tsdb
        )
    )

    st.session_state.gia_tri_tsdb = st.number_input(
        "💰 Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM",
        key="analyze_collateral"
    ):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được đánh giá là không có tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Vui lòng nhập số tiền vay trước."
            )

        else:

            st.session_state.ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            st.session_state.da_phan_tich_tsdb = True

            st.success(
                "✅ Phân tích tài sản bảo đảm thành công."
            )

            st.metric(
                "Tỷ lệ LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ở mức tương đối thấp theo tiêu chí hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng, tính pháp lý và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm theo dữ liệu nhập."
                )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "← QUAY LẠI",
            key="back_step_5"
        ):

            go_back()

    with c2:

        if st.button(
            "XEM KẾT QUẢ →",
            key="next_step_5"
        ):

            if not st.session_state.da_phan_tich_tsdb:

                st.warning(
                    "⚠️ Vui lòng phân tích tài sản bảo đảm trước."
                )

            else:

                go_next()


# ============================================================
# 12. BƯỚC 6 - KẾT QUẢ THẨM ĐỊNH
# ============================================================

elif current_step == 6:

    st.title("📊 Bước 6: Kết quả thẩm định")

    st.caption(
        "Tổng hợp kết quả phân tích hồ sơ, tài chính, khoản vay và TSĐB."
    )

    # --------------------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # --------------------------------------------------------

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
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:

            st.write(
                f"🔸 {item}"
            )

    else:

        # ----------------------------------------------------
        # ĐIỀU KIỆN
        # ----------------------------------------------------

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_su_dung_von,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.su_dung_von_dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        co_dieu_kien_khong = "Không" in dieu_kien

        co_chua_danh_gia = "Chưa đánh giá" in dieu_kien

        # ----------------------------------------------------
        # THÔNG TIN DOANH NGHIỆP
        # ----------------------------------------------------

        st.subheader("🏢 Thông tin doanh nghiệp")

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

        # ----------------------------------------------------
        # CHỈ TIÊU CHÍNH
        # ----------------------------------------------------

        st.subheader("📊 Các chỉ tiêu thẩm định")

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
            "Số tiền vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        st.divider()

        # ----------------------------------------------------
        # KẾT LUẬN
        # ----------------------------------------------------

        st.subheader("📌 Kết luận thẩm định sơ bộ")

        if co_dieu_kien_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 KHÔNG ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang có ít nhất một điều kiện vay vốn
                được đánh giá là Không. Cần xác định rõ nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước khi
                xem xét tiếp.
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
                Chưa đủ cơ sở để đưa ra kết luận thẩm định sơ bộ.
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
                    🟢 CÓ CƠ SỞ XEM XÉT CHO VAY SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đáp ứng các điều kiện sơ bộ đang được đánh giá.
                Doanh nghiệp có kết quả kinh doanh dương, ROA và ROE dương,
                đồng thời dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ
                theo chỉ tiêu DSCR.

                Hồ sơ có thể chuyển sang bước thẩm định chi tiết,
                bao gồm kiểm tra pháp lý, CIC, lịch sử tín dụng,
                báo cáo tài chính, phương án kinh doanh, dòng tiền,
                tài sản bảo đảm và chính sách tín dụng nội bộ.
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
                Hồ sơ chưa có đủ các tín hiệu tích cực theo mô hình
                hỗ trợ hiện tại. Cần thẩm định bổ sung tình hình tài chính,
                dòng tiền, khả năng trả nợ, phương án kinh doanh,
                lịch sử tín dụng và tài sản bảo đảm.
                """
            )

        st.divider()

        # ----------------------------------------------------
        # BẢNG TỔNG HỢP
        # ----------------------------------------------------

        st.subheader("📋 Bảng tổng hợp thẩm định")

        ket_qua = []

        ket_qua.append([
            "Năng lực pháp lý",
            "Đạt"
            if st.session_state.nang_luc_phap_ly == "Có"
            else "Cần xem xét",
            st.session_state.nang_luc_phap_ly
        ])

        ket_qua.append([
            "Mục đích vay vốn",
            "Đạt"
            if st.session_state.muc_dich_hop_phap == "Có"
            else "Cần xem xét",
            st.session_state.muc_dich_hop_phap
        ])

        ket_qua.append([
            "Phương án sử dụng vốn",
            "Đạt"
            if st.session_state.phuong_an_su_dung_von == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_su_dung_von
        ])

        ket_qua.append([
            "Tính khả thi phương án",
            "Đạt"
            if st.session_state.phuong_an_kha_thi == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_kha_thi
        ])

        ket_qua.append([
            "Khả năng tài chính trả nợ",
            "Đạt"
            if st.session_state.kha_nang_tra_no == "Có"
            else "Cần xem xét",
            st.session_state.kha_nang_tra_no
        ])

        ket_qua.append([
            "Lợi nhuận sau thuế",
            "Tích cực"
            if st.session_state.lnst > 0
            else "Cần xem xét",
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ])

        ket_qua.append([
            "ROA",
            "Tích cực"
            if st.session_state.roa > 0
            else "Cần xem xét",
            f"{st.session_state.roa:.2f}%"
        ])

        ket_qua.append([
            "ROE",
            "Tích cực"
            if st.session_state.roe > 0
            else "Cần xem xét",
            f"{st.session_state.roe:.2f}%"
        ])

        ket_qua.append([
            "Tỷ lệ nợ",
            "Tham khảo",
            f"{st.session_state.ty_le_no:.2f}%"
        ])

        if st.session_state.dscr is not None:

            ket_qua.append([
                "DSCR",
                "Tích cực"
                if st.session_state.dscr >= 1
                else "Cần xem xét",
                f"{st.session_state.dscr:.2f} lần"
            ])

        if st.session_state.ltv is not None:

            ket_qua.append([
                "LTV",
                "Tham khảo",
                f"{st.session_state.ltv:.2f}%"
            ])

        else:

            ket_qua.append([
                "Tài sản bảo đảm",
                "Không áp dụng",
                "Khoản vay không có TSĐB"
            ])

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

        st.divider()

        st.warning(
            """
            ⚠️ LƯU Ý

            ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ chỉ là các chỉ tiêu
            hỗ trợ phân tích tín dụng, không phải căn cứ duy nhất
            để quyết định cho vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể hồ sơ
            pháp lý doanh nghiệp, mục đích vay vốn, phương án kinh doanh,
            báo cáo tài chính, dòng tiền, lịch sử tín dụng,
            nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm và
            chính sách tín dụng của ngân hàng.

            Kết quả của ứng dụng chỉ có giá trị hỗ trợ thẩm định sơ bộ.
            """
        )

    st.divider()

    # --------------------------------------------------------
    # NÚT QUAY LẠI / VỀ ĐẦU
    # --------------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "← QUAY LẠI",
            key="back_step_6"
        ):

            go_back()

    with c2:

        if st.button(
            "🏠 VỀ BƯỚC ĐẦU",
            key="home_step_6"
        ):

            go_home()


# ============================================================
# 13. FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        🏦 Hệ thống hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng doanh nghiệp
    </div>
    """,
    unsafe_allow_html=True
)
