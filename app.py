import streamlit as st
import pandas as pd

# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# 2. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {
    # HỒ SƠ DOANH NGHIỆP
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # ĐIỀU KIỆN VAY
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_su_dung_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "su_dung_von_dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # TÀI CHÍNH
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # CHỈ TIÊU TÀI CHÍNH
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # KHOẢN VAY
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # KHẢ NĂNG TRẢ NỢ
    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # TÀI SẢN BẢO ĐẢM
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # TRẠNG THÁI
    "da_luu_ho_so": False,
    "da_kiem_tra_dieu_kien": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,

    # BƯỚC HIỆN TẠI
    "step": 1
}


for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       NỀN CHUNG
    ============================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eef6fb 50%,
            #f9fcff 100%
        );
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ==============================
       HEADER
    ============================== */

    .header-card {
        background: linear-gradient(
            135deg,
            #052b4d,
            #07598a,
            #079bd0
        );

        padding: 30px;

        border-radius: 24px;

        color: white;

        min-height: 220px;

        display: flex;

        flex-direction: column;

        justify-content: center;

        box-shadow:
        0 12px 35px
        rgba(5, 43, 77, 0.18);
    }

    .header-card h1 {
        color: white !important;

        font-size: 30px !important;

        font-weight: 800 !important;

        margin-bottom: 12px !important;
    }

    .header-card p {
        color: rgba(255,255,255,0.92);

        font-size: 16px;

        line-height: 1.6;

        margin: 0;
    }


    /* ==============================
       LOGO CARD
    ============================== */

    .logo-card {
        background: white;

        padding: 15px;

        border-radius: 24px;

        min-height: 220px;

        display: flex;

        align-items: center;

        justify-content: center;

        border:
        1px solid #dce8f3;

        box-shadow:
        0 12px 35px
        rgba(5,43,77,0.12);
    }


    /* ==============================
       CARD
    ============================== */

    .card {
        background: white;

        padding: 25px;

        border-radius: 20px;

        border:
        1px solid #dce8f3;

        box-shadow:
        0 8px 25px
        rgba(8,43,76,0.06);

        margin-bottom: 20px;
    }


    /* ==============================
       STEP
    ============================== */

    .step-card {
        background: white;

        padding: 15px 10px;

        border-radius: 16px;

        text-align: center;

        border:
        1px solid #dce8f3;

        box-shadow:
        0 5px 15px
        rgba(8,43,76,0.05);

        font-weight: 600;

        color: #55708d;
    }

    .step-active {
        background: linear-gradient(
            135deg,
            #07518a,
            #0a9bd0
        );

        color: white !important;

        border: none;

        box-shadow:
        0 8px 20px
        rgba(7,81,138,0.22);
    }

    .step-done {
        border:
        2px solid #1c9b58;

        color: #17663b;
    }


    /* ==============================
       BUTTON
    ============================== */

    .stButton > button {

        width: 100%;

        min-height: 46px;

        border-radius: 12px;

        border: none;

        font-weight: 700;

        color: white;

        background: linear-gradient(
            135deg,
            #07518a,
            #0a9bd0
        );

        box-shadow:
        0 5px 15px
        rgba(7,81,138,0.18);

        transition: 0.2s;
    }

    .stButton > button:hover {

        transform:
        translateY(-2px);

        box-shadow:
        0 8px 20px
        rgba(7,81,138,0.28);
    }


    /* ==============================
       METRIC
    ============================== */

    div[data-testid="stMetric"] {

        background: white;

        border:
        1px solid #dce8f3;

        padding: 18px;

        border-radius: 16px;

        box-shadow:
        0 5px 18px
        rgba(8,43,76,0.06);
    }

    div[data-testid="stMetricLabel"] {

        color:
        #58718b !important;

        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {

        color:
        #07518a !important;

        font-weight: 800;
    }


    /* ==============================
       STATUS
    ============================== */

    .status-good {

        background: #e9f8ef;

        border-left:
        6px solid #1c9b58;

        padding: 20px;

        border-radius: 14px;

        color: #17663b;

        font-weight: 700;

        font-size: 19px;
    }


    .status-warning {

        background: #fff7df;

        border-left:
        6px solid #e0a000;

        padding: 20px;

        border-radius: 14px;

        color: #765800;

        font-weight: 700;

        font-size: 19px;
    }


    .status-bad {

        background: #fff0f0;

        border-left:
        6px solid #d43d3d;

        padding: 20px;

        border-radius: 14px;

        color: #852323;

        font-weight: 700;

        font-size: 19px;
    }


    /* ==============================
       FOOTER
    ============================== */

    .footer {

        text-align: center;

        color: #71869b;

        padding: 30px;

        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. HEADER
# ẢNH LOGO BÊN PHẢI TIÊU ĐỀ
# =========================================================

col_left, col_right = st.columns(
    [3, 1],
    vertical_alignment="center"
)


with col_left:

    st.markdown(
        """
        <div class="header-card">

            <div style="
                font-size:14px;
                font-weight:700;
                letter-spacing:1px;
                color:#bfe7ff;
                margin-bottom:10px;
            ">
                🏦 CREDIT APPRAISAL SYSTEM
            </div>

            <h1>
                HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Hỗ trợ thu thập thông tin doanh nghiệp,
                phân tích tài chính, đánh giá khả năng trả nợ
                và tổng hợp kết quả thẩm định sơ bộ.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col_right:

    st.markdown(
        """
        <div class="logo-card">
        """,
        unsafe_allow_html=True
    )

    try:

        st.image(
            "logo.jpg",
            use_container_width=True
        )

    except Exception:

        st.markdown(
            """
            <div style="
                font-size:80px;
                text-align:center;
                padding:30px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# 5. THANH TIẾN TRÌNH
# =========================================================

current_step = st.session_state.step

step_names = [
    "🏢 Hồ sơ",
    "⚖️ Điều kiện",
    "💰 Phân tích",
    "📊 Kết quả"
]

cols = st.columns(4)

for i, name in enumerate(step_names, start=1):

    with cols[i - 1]:

        if i == current_step:

            st.markdown(
                f"""
                <div class="step-card step-active">
                    BƯỚC {i}<br>
                    {name}
                </div>
                """,
                unsafe_allow_html=True
            )

        elif i < current_step:

            st.markdown(
                f"""
                <div class="step-card step-done">
                    ✓ BƯỚC {i}<br>
                    {name}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="step-card">
                    BƯỚC {i}<br>
                    {name}
                </div>
                """,
                unsafe_allow_html=True
            )


st.progress(
    current_step / 4
)


# =========================================================
# 6. HÀM KIỂM TRA ĐIỀU KIỆN
# =========================================================

def kiem_tra_dieu_kien():

    dieu_kien = [

        st.session_state.nang_luc_phap_ly,

        st.session_state.muc_dich_hop_phap,

        st.session_state.phuong_an_su_dung_von,

        st.session_state.phuong_an_kha_thi,

        st.session_state.kha_nang_tra_no,

        st.session_state.su_dung_von_dung_muc_dich,

        st.session_state.tra_no_dung_han
    ]

    if "Không" in dieu_kien:

        return "khong"

    if "Chưa đánh giá" in dieu_kien:

        return "chua"

    return "co"


# =========================================================
# 7. BƯỚC 1 - HỒ SƠ DOANH NGHIỆP
# =========================================================

if current_step == 1:

    st.title(
        "🏢 BƯỚC 1 - HỒ SƠ DOANH NGHIỆP"
    )

    st.caption(
        "Nhập thông tin cơ bản của doanh nghiệp và phương án sử dụng vốn."
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.subheader(
        "🏢 Thông tin doanh nghiệp"
    )

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

        thoi_gian_hd = st.number_input(
            "📅 Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

    st.subheader(
        "💳 Mục đích và phương án vay"
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
        "📝 Phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        height=150,
        placeholder=(
            "Nhập nhu cầu vay vốn, mục đích sử dụng vốn, "
            "phương án kinh doanh và nguồn trả nợ..."
        )
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    c1, c2 = st.columns(2)

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
                    "✅ Đã lưu hồ sơ doanh nghiệp thành công."
                )


    with c2:

        if st.button(
            "➡️ TIẾP TỤC BƯỚC 2",
            key="next_step_1"
        ):

            if not st.session_state.da_luu_ho_so:

                st.error(
                    "❌ Vui lòng lưu hồ sơ trước khi tiếp tục."
                )

            else:

                st.session_state.step = 2

                st.rerun()


# =========================================================
# 8. BƯỚC 2 - ĐIỀU KIỆN VAY
# =========================================================

elif current_step == 2:

    st.title(
        "⚖️ BƯỚC 2 - ĐIỀU KIỆN VAY VỐN"
    )

    st.caption(
        "Đánh giá sơ bộ các điều kiện liên quan đến khoản vay."
    )

    st.info(
        """
        🔍 Hãy đánh giá từng điều kiện dựa trên hồ sơ và thông tin thực tế.
        """
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
        "</div>",
        unsafe_allow_html=True
    )


    if st.button(
        "🔍 KIỂM TRA ĐIỀU KIỆN VAY",
        key="check_conditions"
    ):

        st.session_state.da_kiem_tra_dieu_kien = True

        ket_qua = kiem_tra_dieu_kien()


        if ket_qua == "khong":

            st.error(
                "🔴 Có ít nhất một điều kiện được đánh giá là Không."
            )


        elif ket_qua == "chua":

            st.warning(
                "🟡 Vẫn còn điều kiện chưa được đánh giá."
            )


        else:

            st.success(
                "🟢 Tất cả điều kiện hiện đang được đánh giá là Có."
            )


    st.divider()


    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "⬅️ QUAY LẠI BƯỚC 1",
            key="back_step_2"
        ):

            st.session_state.step = 1

            st.rerun()


    with c2:

        if st.button(
            "➡️ TIẾP TỤC BƯỚC 3",
            key="next_step_2"
        ):

            if not st.session_state.da_kiem_tra_dieu_kien:

                st.warning(
                    "⚠️ Vui lòng kiểm tra điều kiện vay trước."
                )

            else:

                st.session_state.step = 3

                st.rerun()


# =========================================================
# 9. BƯỚC 3 - PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif current_step == 3:

    st.title(
        "💰 BƯỚC 3 - PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )

    st.caption(
        "Đơn vị nhập liệu: triệu đồng."
    )


    # =====================================================
    # A. TÀI CHÍNH
    # =====================================================

    st.subheader(
        "📊 1. Phân tích tài chính doanh nghiệp"
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
        "</div>",
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


    # =====================================================
    # B. KHOẢN VAY
    # =====================================================

    st.subheader(
        "💳 2. Thông tin khoản vay"
    )


    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )


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
            "💳 Nghĩa vụ trả nợ hiện tại / tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu
        )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


    if st.button(
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ",
        key="calculate_loan"
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

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc / tháng",
            f"{st.session_state.tien_goc_thang:,.2f}"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{st.session_state.tien_lai_thang:,.2f}"
        )

        c3.metric(
            "Tổng nghĩa vụ / tháng",
            f"{st.session_state.tong_nghia_vu:,.2f}"
        )


    st.divider()


    # =====================================================
    # C. DSCR
    # =====================================================

    st.subheader(
        "📈 3. Khả năng trả nợ - DSCR"
    )


    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )


    else:

        c1, c2 = st.columns(2)


        with c1:

            st.metric(
                "Dòng tiền kinh doanh / tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )


        with c2:

            st.metric(
                "Nghĩa vụ trả nợ / tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )


        if st.button(
            "📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ",
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


                if st.session_state.dscr >= 1:

                    st.success(
                        f"🟢 DSCR = {st.session_state.dscr:.2f} lần. "
                        "Dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ."
                    )

                else:

                    st.warning(
                        f"🟡 DSCR = {st.session_state.dscr:.2f} lần. "
                        "Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


    st.divider()


    # =====================================================
    # D. TSĐB
    # =====================================================

    st.subheader(
        "🏠 4. Tài sản bảo đảm"
    )


    st.info(
        """
        TSĐB là nội dung hỗ trợ trong thẩm định. 
        Cần xem xét loại tài sản, quyền sở hữu, giá trị định giá,
        khả năng thanh khoản và chính sách cho vay của ngân hàng.
        """
    )


    options_tsdb = [

        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        options_tsdb,
        index=options_tsdb.index(
            st.session_state.co_tsdb
        )
    )


    st.session_state.gia_tri_tsdb = st.number_input(
        "🏠 Giá trị tài sản bảo đảm",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM",
        key="analyze_collateral"
    ):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định có tài sản bảo đảm hay không."
            )


        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được đánh giá là không có TSĐB."
            )


        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị TSĐB phải lớn hơn 0."
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


            if st.session_state.ltv <= 70:

                st.success(
                    f"🟢 LTV = {st.session_state.ltv:.2f}%. "
                    "Tỷ lệ vay trên giá trị TSĐB ở mức tương đối thấp."
                )


            elif st.session_state.ltv <= 100:

                st.warning(
                    f"🟡 LTV = {st.session_state.ltv:.2f}%. "
                    "Cần xem xét thêm chất lượng và khả năng thanh khoản TSĐB."
                )


            else:

                st.error(
                    f"🔴 LTV = {st.session_state.ltv:.2f}%. "
                    "Số tiền vay lớn hơn giá trị TSĐB."
                )


    st.divider()


    # =====================================================
    # NÚT ĐIỀU HƯỚNG
    # =====================================================

    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "⬅️ QUAY LẠI BƯỚC 2",
            key="back_step_3"
        ):

            st.session_state.step = 2

            st.rerun()


    with c2:

        if st.button(
            "➡️ XEM KẾT QUẢ THẨM ĐỊNH",
            key="next_step_3"
        ):

            missing = []


            if not st.session_state.da_phan_tich_tc:

                missing.append(
                    "Phân tích tài chính"
                )


            if not st.session_state.da_phan_tich_vay:

                missing.append(
                    "Tính nghĩa vụ trả nợ"
                )


            if not st.session_state.da_phan_tich_tsdb:

                missing.append(
                    "Phân tích tài sản bảo đảm"
                )


            if len(missing) > 0:

                st.warning(
                    "⚠️ Vui lòng hoàn thành: "
                    + ", ".join(missing)
                )

            else:

                st.session_state.step = 4

                st.rerun()


# =========================================================
# 10. BƯỚC 4 - KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif current_step == 4:

    st.title(
        "📊 BƯỚC 4 - KẾT QUẢ THẨM ĐỊNH"
    )


    st.caption(
        "Tổng hợp thông tin và đưa ra kết luận hỗ trợ thẩm định sơ bộ."
    )


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader(
        "🏢 Thông tin doanh nghiệp"
    )


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


    # =====================================================
    # CÁC CHỈ TIÊU
    # =====================================================

    st.subheader(
        "📊 Các chỉ tiêu chính"
    )


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


    # =====================================================
    # ĐIỀU KIỆN VAY
    # =====================================================

    ket_qua_dieu_kien = kiem_tra_dieu_kien()


    # =====================================================
    # KẾT LUẬN
    # =====================================================

    st.subheader(
        "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
    )


    if ket_qua_dieu_kien == "khong":

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
            Hồ sơ có ít nhất một điều kiện vay vốn được đánh giá là Không.
            Cần xác định nguyên nhân, bổ sung hồ sơ hoặc điều chỉnh phương án
            trước khi tiếp tục xem xét.
            """
        )


    elif ket_qua_dieu_kien == "chua":

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
            Hồ sơ đang có các tín hiệu tích cực theo mô hình hỗ trợ.
            Doanh nghiệp có lợi nhuận sau thuế dương, ROA và ROE dương,
            đồng thời dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ theo DSCR.

            Hồ sơ có thể được chuyển sang bước thẩm định chi tiết.
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
            Hồ sơ chưa có đủ các tín hiệu tích cực theo mô hình hỗ trợ.
            Cần thẩm định bổ sung tình hình tài chính, dòng tiền,
            khả năng trả nợ, phương án kinh doanh, lịch sử tín dụng
            và tài sản bảo đảm.
            """
        )


    st.divider()


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.subheader(
        "📋 Bảng tổng hợp thẩm định"
    )


    ket_qua = []


    ket_qua.append(
        [
            "Năng lực pháp lý",
            "Đạt"
            if st.session_state.nang_luc_phap_ly == "Có"
            else "Cần xem xét",
            st.session_state.nang_luc_phap_ly
        ]
    )


    ket_qua.append(
        [
            "Mục đích vay vốn",
            "Đạt"
            if st.session_state.muc_dich_hop_phap == "Có"
            else "Cần xem xét",
            st.session_state.muc_dich_hop_phap
        ]
    )


    ket_qua.append(
        [
            "Phương án sử dụng vốn",
            "Đạt"
            if st.session_state.phuong_an_su_dung_von == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_su_dung_von
        ]
    )


    ket_qua.append(
        [
            "Tính khả thi phương án",
            "Đạt"
            if st.session_state.phuong_an_kha_thi == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_kha_thi
        ]
    )


    ket_qua.append(
        [
            "Khả năng tài chính trả nợ",
            "Đạt"
            if st.session_state.kha_nang_tra_no == "Có"
            else "Cần xem xét",
            st.session_state.kha_nang_tra_no
        ]
    )


    ket_qua.append(
        [
            "Lợi nhuận sau thuế",
            "Tích cực"
            if st.session_state.lnst > 0
            else "Cần xem xét",
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ]
    )


    ket_qua.append(
        [
            "ROA",
            "Tích cực"
            if st.session_state.roa > 0
            else "Cần xem xét",
            f"{st.session_state.roa:.2f}%"
        ]
    )


    ket_qua.append(
        [
            "ROE",
            "Tích cực"
            if st.session_state.roe > 0
            else "Cần xem xét",
            f"{st.session_state.roe:.2f}%"
        ]
    )


    ket_qua.append(
        [
            "Tỷ lệ nợ",
            "Tham khảo",
            f"{st.session_state.ty_le_no:.2f}%"
        ]
    )


    ket_qua.append(
        [
            "DSCR",
            (
                "Tích cực"
                if st.session_state.dscr is not None
                and st.session_state.dscr >= 1
                else "Cần xem xét"
            ),
            (
                f"{st.session_state.dscr:.2f} lần"
                if st.session_state.dscr is not None
                else "Chưa tính"
            )
        ]
    )


    if st.session_state.ltv is not None:

        ket_qua.append(
            [
                "LTV",
                "Tham khảo",
                f"{st.session_state.ltv:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "Tài sản bảo đảm",
                "Không áp dụng",
                "Khoản vay không có TSĐB"
            ]
        )


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


    # =====================================================
    # NÚT ĐIỀU HƯỚNG
    # =====================================================

    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "⬅️ QUAY LẠI PHÂN TÍCH",
            key="back_step_4"
        ):

            st.session_state.step = 3

            st.rerun()


    with c2:

        if st.button(
            "🔄 TẠO HỒ SƠ MỚI",
            key="reset_application"
        ):

            for key, value in default_values.items():

                st.session_state[key] = value

            st.rerun()


    st.divider()


    st.warning(
        """
        ⚠️ LƯU Ý QUAN TRỌNG

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ chỉ là các chỉ tiêu
        hỗ trợ phân tích tín dụng, không phải là căn cứ duy nhất
        để quyết định cho vay.

        Quyết định tín dụng thực tế cần xem xét tổng thể:
        hồ sơ pháp lý doanh nghiệp, mục đích vay vốn, phương án
        kinh doanh, báo cáo tài chính, dòng tiền, lịch sử tín dụng,
        nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm và chính sách
        tín dụng của ngân hàng.

        Kết quả của ứng dụng chỉ có giá trị hỗ trợ thẩm định sơ bộ.
        """
    )


# =========================================================
# 11. FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

        <br><br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

    </div>
    """,
    unsafe_allow_html=True
)
