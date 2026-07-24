import streamlit as st
import pandas as pd


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
# 2. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {

    # =========================
    # HỒ SƠ DOANH NGHIỆP
    # =========================
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # =========================
    # ĐIỀU KIỆN VAY
    # =========================
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_su_dung_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "su_dung_von_dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # =========================
    # TÀI CHÍNH
    # =========================
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # =========================
    # KẾT QUẢ TÀI CHÍNH
    # =========================
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # =========================
    # KHOẢN VAY
    # =========================
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # =========================
    # KHẢ NĂNG TRẢ NỢ
    # =========================
    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # =========================
    # TÀI SẢN BẢO ĐẢM
    # =========================
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # =========================
    # TRẠNG THÁI
    # =========================
    "da_luu_ho_so": False,
    "da_kiem_tra_dieu_kien": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False
}


for key, value in default_values.items():

    if key not in st.session_state:

        st.session_state[key] = value


# =========================================================
# 3. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       NỀN CHUNG
    ===================================================== */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f4f8fc 0%,
                #eef6fb 50%,
                #f8fbff 100%
            );
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #041b33 0%,
                #07345a 45%,
                #075b86 100%
            );

        border-right:
            1px solid
            rgba(255,255,255,0.1);
    }


    section[data-testid="stSidebar"] * {

        color: white !important;
    }


    section[data-testid="stSidebar"] hr {

        border-color:
            rgba(255,255,255,0.25);
    }


    /* =====================================================
       TIÊU ĐỀ
    ===================================================== */

    h1 {

        color:
            #062c4d !important;

        font-weight:
            800 !important;
    }


    h2 {

        color:
            #0a4d78 !important;

        font-weight:
            800 !important;
    }


    h3 {

        color:
            #12618f !important;

        font-weight:
            750 !important;
    }


    /* =====================================================
       METRIC
    ===================================================== */

    div[data-testid="stMetric"] {

        background:
            rgba(255,255,255,0.95);

        border:
            1px solid #d9e7f2;

        padding:
            18px;

        border-radius:
            18px;

        box-shadow:
            0 8px 25px
            rgba(7,55,90,0.08);

        transition:
            all 0.2s ease;
    }


    div[data-testid="stMetric"]:hover {

        transform:
            translateY(-3px);

        box-shadow:
            0 12px 30px
            rgba(7,55,90,0.14);
    }


    div[data-testid="stMetricLabel"] {

        color:
            #55718b !important;

        font-weight:
            650;
    }


    div[data-testid="stMetricValue"] {

        color:
            #07518a !important;

        font-weight:
            800;
    }


    /* =====================================================
       BUTTON
    ===================================================== */

    .stButton > button {

        width:
            100%;

        border:
            none;

        border-radius:
            12px;

        padding:
            0.75rem 1rem;

        font-weight:
            750;

        color:
            white;

        background:
            linear-gradient(
                135deg,
                #07518a,
                #0b8bc4
            );

        box-shadow:
            0 6px 18px
            rgba(7,81,138,0.2);

        transition:
            all 0.2s ease;
    }


    .stButton > button:hover {

        transform:
            translateY(-2px);

        box-shadow:
            0 10px 24px
            rgba(7,81,138,0.3);
    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero-card {

        background:
            linear-gradient(
                135deg,
                #032a4d,
                #075d8d,
                #0799ca
            );

        padding:
            38px;

        border-radius:
            24px;

        color:
            white;

        margin-bottom:
            25px;

        box-shadow:
            0 15px 35px
            rgba(5,55,90,0.22);
    }


    .hero-card h1 {

        color:
            white !important;

        font-size:
            30px;

        font-weight:
            850;

        margin-bottom:
            10px;
    }


    .hero-card p {

        color:
            rgba(255,255,255,0.9);

        font-size:
            16px;
    }


    /* =====================================================
       CARD
    ===================================================== */

    .section-card {

        background:
            white;

        padding:
            24px;

        border-radius:
            18px;

        border:
            1px solid #dce8f3;

        box-shadow:
            0 6px 20px
            rgba(8,43,76,0.06);

        margin-bottom:
            20px;
    }


    /* =====================================================
       STATUS
    ===================================================== */

    .status-good {

        background:
            linear-gradient(
                135deg,
                #e8f8ef,
                #f5fff9
            );

        border-left:
            7px solid #159957;

        padding:
            20px;

        border-radius:
            14px;

        color:
            #17663b;

        font-weight:
            750;

        font-size:
            19px;

        box-shadow:
            0 5px 15px
            rgba(21,153,87,0.08);
    }


    .status-warning {

        background:
            linear-gradient(
                135deg,
                #fff7df,
                #fffdf4
            );

        border-left:
            7px solid #e3a008;

        padding:
            20px;

        border-radius:
            14px;

        color:
            #765800;

        font-weight:
            750;

        font-size:
            19px;
    }


    .status-bad {

        background:
            linear-gradient(
                135deg,
                #fff0f0,
                #fffafa
            );

        border-left:
            7px solid #d43d3d;

        padding:
            20px;

        border-radius:
            14px;

        color:
            #852323;

        font-weight:
            750;

        font-size:
            19px;
    }


    /* =====================================================
       PROCESS
    ===================================================== */

    .process-card {

        background:
            white;

        padding:
            20px;

        border-radius:
            16px;

        text-align:
            center;

        border:
            1px solid #dce8f3;

        box-shadow:
            0 5px 15px
            rgba(8,43,76,0.05);
    }


    .process-number {

        font-size:
            28px;

        font-weight:
            800;

        color:
            #0876ad;
    }


    .process-title {

        font-weight:
            750;

        color:
            #174c70;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer {

        text-align:
            center;

        color:
            #71869b;

        padding:
            30px;

        font-size:
            13px;
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

    try:

        st.image(
            "logo.jpg",
            use_container_width=True
        )

    except Exception:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:60px;
                padding:20px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:20px;
            font-weight:800;
            line-height:1.5;
            margin-top:10px;
        ">

            HỆ THỐNG<br>
            THẨM ĐỊNH CHO VAY<br>
            DOANH NGHIỆP

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown(
        """
        <div style="
            font-size:15px;
            font-weight:800;
            margin-bottom:10px;
        ">

            📋 DANH MỤC THẨM ĐỊNH

        </div>
        """,
        unsafe_allow_html=True
    )


    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Tài chính & Khả năng trả nợ",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )


    st.divider()


    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:12px;
            color:#d5e9f5;
            line-height:1.6;
        ">

            Công cụ hỗ trợ<br>
            thẩm định tín dụng sơ bộ

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero-card">

            <h1>
                🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Công cụ hỗ trợ phân tích hồ sơ,
                đánh giá tài chính và khả năng trả nợ
                phục vụ thẩm định tín dụng sơ bộ.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("👋 Chào mừng bạn đến với hệ thống")


    st.write(
        """
        Hệ thống hỗ trợ cán bộ hoặc người sử dụng
        thực hiện đánh giá sơ bộ hồ sơ vay vốn của doanh nghiệp
        thông qua thông tin pháp lý, tài chính,
        khoản vay, khả năng trả nợ và tài sản bảo đảm.
        """
    )


    st.divider()


    # =====================================================
    # TRẠNG THÁI HỒ SƠ
    # =====================================================

    st.subheader("📊 TRẠNG THÁI HỒ SƠ")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "🏢 Hồ sơ doanh nghiệp",
            "Đã nhập"
            if st.session_state.da_luu_ho_so
            else "Chưa nhập"
        )


    with c2:

        st.metric(
            "⚖️ Điều kiện vay",
            "Đã kiểm tra"
            if st.session_state.da_kiem_tra_dieu_kien
            else "Chưa kiểm tra"
        )


    with c3:

        st.metric(
            "💰 Tài chính",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )


    with c4:

        if (
            st.session_state.da_luu_ho_so
            and st.session_state.da_phan_tich_tc
            and st.session_state.da_phan_tich_vay
            and st.session_state.da_phan_tich_dscr
        ):

            trang_thai = "Sẵn sàng"

        else:

            trang_thai = "Chưa đủ dữ liệu"


        st.metric(
            "📊 Kết quả",
            trang_thai
        )


    st.divider()


    # =====================================================
    # QUY TRÌNH
    # =====================================================

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:

        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    01
                </div>

                <div class="process-title">
                    🏢 HỒ SƠ
                </div>

                <p>
                    Thông tin doanh nghiệp
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    02
                </div>

                <div class="process-title">
                    ⚖️ ĐIỀU KIỆN
                </div>

                <p>
                    Kiểm tra điều kiện vay
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    03
                </div>

                <div class="process-title">
                    💰 TÀI CHÍNH
                </div>

                <p>
                    Phân tích chỉ tiêu tài chính
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    04
                </div>

                <div class="process-title">
                    💳 TRẢ NỢ
                </div>

                <p>
                    Đánh giá DSCR
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with c5:

        st.markdown(
            """
            <div class="process-card">

                <div class="process-number">
                    05
                </div>

                <div class="process-title">
                    📊 KẾT QUẢ
                </div>

                <p>
                    Tổng hợp thẩm định
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.divider()


    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ và không thay thế quyết định
        tín dụng chính thức của ngân hàng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY")


    # =====================================================
    # A. THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader("1️⃣ Thông tin doanh nghiệp")


    c1, c2 = st.columns(2)


    with c1:

        ten_dn = st.text_input(
            "Tên doanh nghiệp",
            value=st.session_state.ten_dn
        )


        ma_so = st.text_input(
            "Mã số doanh nghiệp",
            value=st.session_state.ma_so
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
            "Ngành nghề kinh doanh",
            danh_sach_nganh,
            index=danh_sach_nganh.index(
                st.session_state.nganh_nghe
            )
        )


        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )


    st.subheader("2️⃣ Mục đích và phương án vay")


    muc_dich_list = [

        "Bổ sung vốn lưu động",

        "Mua nguyên vật liệu",

        "Đầu tư máy móc thiết bị",

        "Mở rộng sản xuất",

        "Mua tài sản cố định",

        "Khác"

    ]


    muc_dich_vay = st.selectbox(

        "Mục đích sử dụng vốn",

        muc_dich_list,

        index=muc_dich_list.index(

            st.session_state.muc_dich_vay

        )

    )


    phuong_an = st.text_area(

        "Mô tả phương án sử dụng vốn",

        value=st.session_state.phuong_an,

        placeholder=
        "Nhập phương án kinh doanh, "
        "nhu cầu vay và cách sử dụng vốn..."

    )


    if st.button(
        "💾 LƯU HỒ SƠ DOANH NGHIỆP"
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


    st.divider()


    # =====================================================
    # B. ĐIỀU KIỆN VAY
    # =====================================================

    st.subheader("3️⃣ Kiểm tra điều kiện vay vốn")


    st.info(
        """
        Kiểm tra sơ bộ các điều kiện liên quan đến hồ sơ vay vốn.
        Việc đánh giá thực tế cần căn cứ hồ sơ pháp lý,
        mục đích vay, phương án sử dụng vốn,
        khả năng trả nợ và quy định nội bộ của tổ chức tín dụng.
        """
    )


    options = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(

            "Năng lực pháp lý phù hợp?",

            options,

            index=options.index(

                st.session_state.nang_luc_phap_ly

            )

        )


        st.session_state.muc_dich_hop_phap = st.selectbox(

            "Mục đích vay vốn hợp pháp?",

            options,

            index=options.index(

                st.session_state.muc_dich_hop_phap

            )

        )


        st.session_state.phuong_an_su_dung_von = st.selectbox(

            "Có phương án sử dụng vốn?",

            options,

            index=options.index(

                st.session_state.phuong_an_su_dung_von

            )

        )


        st.session_state.phuong_an_kha_thi = st.selectbox(

            "Phương án sử dụng vốn khả thi?",

            options,

            index=options.index(

                st.session_state.phuong_an_kha_thi

            )

        )


    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(

            "Có khả năng tài chính trả nợ?",

            options,

            index=options.index(

                st.session_state.kha_nang_tra_no

            )

        )


        st.session_state.su_dung_von_dung_muc_dich = st.selectbox(

            "Cam kết sử dụng vốn đúng mục đích?",

            options,

            index=options.index(

                st.session_state.su_dung_von_dung_muc_dich

            )

        )


        st.session_state.tra_no_dung_han = st.selectbox(

            "Cam kết trả nợ đúng hạn?",

            options,

            index=options.index(

                st.session_state.tra_no_dung_han

            )

        )


    if st.button(
        "🔍 KIỂM TRA ĐIỀU KIỆN VAY"
    ):

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich_hop_phap,

            st.session_state.phuong_an_su_dung_von,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no,

            st.session_state.su_dung_von_dung_muc_dich,

            st.session_state.tra_no_dung_han

        ]


        st.session_state.da_kiem_tra_dieu_kien = True


        if "Không" in dieu_kien:

            st.error(
                "🔴 Có ít nhất một điều kiện được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title(
        "💰 TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )


    # =====================================================
    # A. PHÂN TÍCH TÀI CHÍNH
    # =====================================================

    st.subheader(
        "1️⃣ Phân tích tài chính doanh nghiệp"
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

            "💧 Dòng tiền kinh doanh / tháng",

            value=st.session_state.dong_tien

        )


    if st.button(
        "📊 PHÂN TÍCH TÀI CHÍNH"
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

        st.subheader(
            "📈 KẾT QUẢ TÀI CHÍNH"
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


    st.divider()


    # =====================================================
    # B. THÔNG TIN KHOẢN VAY
    # =====================================================

    st.subheader(
        "2️⃣ Thông tin khoản vay"
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

            "💳 Nghĩa vụ trả nợ hiện tại/tháng",

            min_value=0.0,

            value=st.session_state.nghia_vu_no_cu

        )


    if st.button(
        "💳 TÍNH NGHĨA VỤ TRẢ NỢ"
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


    # =====================================================
    # C. KHẢ NĂNG TRẢ NỢ - DSCR
    # =====================================================

    st.subheader(
        "3️⃣ Khả năng trả nợ"
    )


    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

        c1, c2 = st.columns(2)


        c1.metric(

            "Dòng tiền kinh doanh/tháng",

            f"{st.session_state.dong_tien:,.2f}"

        )


        c2.metric(

            "Nghĩa vụ trả nợ/tháng",

            f"{st.session_state.tong_nghia_vu:,.2f}"

        )


        if st.button(
            "📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
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


                st.metric(

                    "DSCR",

                    f"{st.session_state.dscr:.2f} lần"

                )


                if st.session_state.dscr >= 1:

                    st.success(

                        "🟢 Dòng tiền hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."

                    )

                else:

                    st.warning(

                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."

                    )


    st.divider()


    # =====================================================
    # D. TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader(
        "4️⃣ Tài sản bảo đảm"
    )


    st.info(
        """
        Tài sản bảo đảm là yếu tố hỗ trợ trong thẩm định tín dụng.
        Cần xem xét loại tài sản, quyền sở hữu, giá trị định giá,
        khả năng thanh khoản và tỷ lệ cho vay trên giá trị tài sản.
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

        "🏠 Giá trị tài sản bảo đảm (triệu đồng)",

        min_value=0.0,

        value=st.session_state.gia_tri_tsdb

    )


    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
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

                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."

                )

            else:

                st.error(

                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."

                )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP"
    )


    st.info(
        """
        Kết quả được tổng hợp từ hồ sơ doanh nghiệp,
        điều kiện vay, tình hình tài chính,
        khả năng trả nợ và tài sản bảo đảm.
        Đây là kết quả hỗ trợ thẩm định sơ bộ.
        """
    )


    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    missing = []


    if not st.session_state.da_luu_ho_so:

        missing.append(
            "Hồ sơ doanh nghiệp"
        )


    if not st.session_state.da_phan_tich_tc:

        missing.append(
            "Phân tích tài chính"
        )


    if not st.session_state.da_phan_tich_vay:

        missing.append(
            "Thông tin khoản vay"
        )


    if not st.session_state.da_phan_tich_dscr:

        missing.append(
            "Phân tích khả năng trả nợ"
        )


    if not st.session_state.da_phan_tich_tsdb:

        missing.append(
            "Tài sản bảo đảm"
        )


    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận thẩm định."
        )


        st.write(
            "Vui lòng hoàn thành:"
        )


        for item in missing:

            st.write(
                f"🔸 {item}"
            )


        st.stop()


    # =====================================================
    # KIỂM TRA ĐIỀU KIỆN
    # =====================================================

    dieu_kien = [

        st.session_state.nang_luc_phap_ly,

        st.session_state.muc_dich_hop_phap,

        st.session_state.phuong_an_su_dung_von,

        st.session_state.phuong_an_kha_thi,

        st.session_state.kha_nang_tra_no,

        st.session_state.su_dung_von_dung_muc_dich,

        st.session_state.tra_no_dung_han

    ]


    co_dieu_kien_khong = (

        "Không"

        in dieu_kien

    )


    co_chua_danh_gia = (

        "Chưa đánh giá"

        in dieu_kien

    )


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader(
        "🏢 THÔNG TIN DOANH NGHIỆP"
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
    # CHỈ TIÊU
    # =====================================================

    st.subheader(
        "📊 CÁC CHỈ TIÊU THẨM ĐỊNH"
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

        f"{st.session_state.dscr:.2f} lần"

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
    # KẾT LUẬN
    # =====================================================

    st.subheader(
        "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
    )


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
            được đánh giá là Không.
            Cần xác định rõ nguyên nhân và bổ sung hồ sơ
            trước khi xem xét tiếp.
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
            Doanh nghiệp có kết quả kinh doanh dương,
            ROA và ROE dương, đồng thời dòng tiền hiện tại
            đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR.

            Hồ sơ có thể được chuyển sang bước thẩm định chi tiết,
            bao gồm kiểm tra hồ sơ pháp lý, CIC,
            lịch sử tín dụng, báo cáo tài chính,
            phương án kinh doanh, dòng tiền,
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
            Hồ sơ chưa có đủ các tín hiệu tích cực
            theo mô hình hỗ trợ hiện tại.
            Cần thẩm định bổ sung tình hình tài chính,
            dòng tiền, khả năng trả nợ,
            phương án kinh doanh,
            lịch sử tín dụng và tài sản bảo đảm.
            """

        )


    st.divider()


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.subheader(
        "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
    )


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
        ⚠️ LƯU Ý QUAN TRỌNG

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ
        chỉ là các chỉ tiêu hỗ trợ phân tích tín dụng,
        không phải là căn cứ duy nhất để quyết định cho vay.

        Quyết định tín dụng thực tế cần xem xét tổng thể:
        hồ sơ pháp lý doanh nghiệp, mục đích vay vốn,
        phương án kinh doanh, báo cáo tài chính,
        dòng tiền, lịch sử tín dụng, nghĩa vụ nợ,
        khả năng trả nợ, tài sản bảo đảm và chính sách
        tín dụng của ngân hàng.

        Kết quả của ứng dụng chỉ có giá trị
        hỗ trợ thẩm định sơ bộ.
        """

    )


# =========================================================
# 9. FOOTER
# =========================================================

st.divider()


st.markdown(

    """
    <div class="footer">

        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

        <br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

    </div>
    """,

    unsafe_allow_html=True

)
