import streamlit as st
import pandas as pd

# =========================================================
# 1. CẤU HÌNH TRANG
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

    # HỒ SƠ DOANH NGHIỆP
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "",
    "phuong_an": "",

    # ĐIỀU KIỆN VAY
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # TÀI CHÍNH
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # KHOẢN VAY
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

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
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False
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

    /* =========================
       NỀN
    ========================= */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #f5f8fc 0%,
            #eef4fb 50%,
            #f8fafc 100%
        );
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #071b35 0%,
            #0b2d52 50%,
            #123f68 100%
        );
    }


    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.2);
    }


    /* =========================
       TIÊU ĐỀ
    ========================= */

    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0d3b66 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155a8a !important;
        font-weight: 700 !important;
    }


    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {

        background: rgba(255,255,255,0.95);

        border: 1px solid #d9e4f0;

        padding: 18px;

        border-radius: 18px;

        box-shadow:
        0 8px 24px
        rgba(13,59,102,0.08);
    }


    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }


    div[data-testid="stMetricValue"] {
        color: #0b3761 !important;
        font-weight: 800;
    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {

        width: 100%;

        border-radius: 12px;

        border: none;

        padding: 0.7rem 1rem;

        font-weight: 700;

        color: white;

        background:
        linear-gradient(
            135deg,
            #0b4f8a,
            #1479b8
        );

        box-shadow:
        0 5px 15px
        rgba(11,79,138,0.22);

        transition: 0.25s;
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
        0 8px 20px
        rgba(11,79,138,0.3);
    }


    /* =========================
       HERO
    ========================= */

    .hero-card {

        background:
        linear-gradient(
            135deg,
            #08264a,
            #0d5287,
            #1581b8
        );

        padding: 35px;

        border-radius: 24px;

        color: white;

        box-shadow:
        0 15px 35px
        rgba(8,38,74,0.22);

        margin-bottom: 25px;
    }


    .hero-card h1 {

        color: white !important;

        font-size: 32px;

        margin-bottom: 8px;
    }


    .hero-card p {

        color:
        rgba(255,255,255,0.9);

        font-size: 16px;

        margin-bottom: 0;
    }


    /* =========================
       CARD
    ========================= */

    .section-card {

        background:
        rgba(255,255,255,0.9);

        padding: 22px;

        border-radius: 18px;

        border:
        1px solid #dce7f2;

        box-shadow:
        0 6px 20px
        rgba(13,59,102,0.06);

        margin-bottom: 18px;
    }


    /* =========================
       STATUS
    ========================= */

    .status-good {

        background: #e9f8ef;

        border-left:
        5px solid #1e9e58;

        padding: 15px;

        border-radius: 12px;

        color: #176b3c;

        font-weight: 700;
    }


    .status-warning {

        background: #fff7df;

        border-left:
        5px solid #e4a400;

        padding: 15px;

        border-radius: 12px;

        color: #805f00;

        font-weight: 700;
    }


    .status-bad {

        background: #fff0f0;

        border-left:
        5px solid #d64545;

        padding: 15px;

        border-radius: 12px;

        color: #8c2525;

        font-weight: 700;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {

        text-align: center;

        color: #70849a;

        padding: 20px;

        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR - DANH MỤC RÚT GỌN
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">

            <div style="
                font-size:42px;
            ">
                🏦
            </div>

            <div style="
                font-size:19px;
                font-weight:800;
                line-height:1.4;
            ">
                HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH
            </div>

            <div style="
                font-size:15px;
                font-weight:600;
                opacity:0.85;
                margin-top:5px;
            ">
                CHO VAY DOANH NGHIỆP
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # =====================================================
    # MENU RÚT GỌN CÒN 5 MỤC
    # =====================================================

    menu = st.radio(
        "📌 DANH MỤC CHỨC NĂNG",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & Khả năng trả nợ",
            "📊 Kết quả thẩm định"
        ]
    )


    st.divider()


    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )


# =========================================================
# 5. TỔNG QUAN
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
                Phân tích hồ sơ • Đánh giá tài chính •
                Khả năng trả nợ • Tài sản bảo đảm •
                Hỗ trợ quyết định tín dụng
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("👋 Chào mừng bạn đến với hệ thống")


    st.write(
        """
        Ứng dụng hỗ trợ thực hiện quy trình thẩm định sơ bộ
        đối với hồ sơ vay vốn của doanh nghiệp.
        """
    )


    st.divider()


    st.subheader("📊 TÌNH TRẠNG HỒ SƠ")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "🏢 Hồ sơ",
            "Đã nhập"
            if st.session_state.da_luu_ho_so
            else "Chưa nhập"
        )


    with c2:

        st.metric(
            "💰 Tài chính",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )


    with c3:

        st.metric(
            "💳 Khoản vay",
            "Đã tính"
            if st.session_state.da_phan_tich_vay
            else "Chưa tính"
        )


    with c4:

        st.metric(
            "🏠 TSĐB",
            "Đã phân tích"
            if st.session_state.da_phan_tich_tsdb
            else "Chưa phân tích"
        )


    st.divider()


    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.info(
            """
            **01 | HỒ SƠ**

            Nhập thông tin doanh nghiệp
            và kiểm tra điều kiện vay.
            """
        )


    with c2:

        st.info(
            """
            **02 | TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )


    with c3:

        st.info(
            """
            **03 | KHOẢN VAY**

            Tính nghĩa vụ trả nợ,
            DSCR và LTV.
            """
        )


    with c4:

        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu
            và đưa ra kết luận sơ bộ.
            """
        )


    st.warning(
        """
        ⚠️ Lưu ý: Ứng dụng chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ. Kết quả không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    st.subheader("📋 1. Thông tin doanh nghiệp")


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


    st.subheader("💳 2. Mục đích vay vốn")


    muc_dich_vay = st.selectbox(
        "Mục đích sử dụng vốn",
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
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder=
        "Nhập mô tả phương án kinh doanh..."
    )


    if st.button("💾 LƯU HỒ SƠ"):

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
                "❌ Vui lòng mô tả phương án sử dụng vốn."
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
    # ĐIỀU KIỆN VAY
    # =====================================================

    st.subheader("⚖️ 3. Kiểm tra điều kiện vay vốn")


    st.info(
        """
        Đánh giá sơ bộ theo các nhóm điều kiện vay vốn.
        Đây không phải là quyết định tín dụng chính thức.
        """
    )


    lua_chon = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Doanh nghiệp có năng lực pháp lý phù hợp?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.nang_luc_phap_ly
            )
        )


        st.session_state.muc_dich = st.selectbox(
            "Mục đích vay vốn có hợp pháp?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.muc_dich
            )
        )


        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.co_phuong_an
            )
        )


        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn có khả thi?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.phuong_an_kha_thi
            )
        )


    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "Doanh nghiệp có khả năng trả nợ?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.kha_nang_tra_no
            )
        )


        st.session_state.dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.dung_muc_dich
            )
        )


        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết trả nợ đúng hạn?",
            lua_chon,
            index=lua_chon.index(
                st.session_state.tra_no_dung_han
            )
        )


    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich,

            st.session_state.co_phuong_an,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no,

            st.session_state.dung_muc_dich,

            st.session_state.tra_no_dung_han
        ]


        if "Không" in dieu_kien:

            st.error(
                "🔴 Có ít nhất một điều kiện đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Tất cả điều kiện sơ bộ đang được đánh giá là Có."
            )


# =========================================================
# 7. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH")


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )


    c1, c2 = st.columns(2)


    with c1:

        st.session_state.doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )


        st.session_state.lnst = st.number_input(
            "📈 Lợi nhuận sau thuế",
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
            "💧 Dòng tiền từ hoạt động kinh doanh",
            value=st.session_state.dong_tien
        )


    if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

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

        st.divider()


        st.subheader("📈 KẾT QUẢ")


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


        chart = pd.DataFrame(
            {
                "Chỉ tiêu": [
                    "ROA",
                    "ROE",
                    "Tỷ lệ nợ"
                ],

                "Giá trị": [
                    st.session_state.roa,
                    st.session_state.roe,
                    st.session_state.ty_le_no
                ]
            }
        )


        st.bar_chart(
            chart.set_index("Chỉ tiêu")
        )


        st.info(
            """
            💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu hỗ trợ
            phân tích tài chính. Việc đánh giá cần kết hợp
            với ngành nghề, quy mô, lịch sử hoạt động và
            chính sách tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 8. KHOẢN VAY & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💳 Khoản vay & Khả năng trả nợ":

    st.title(
        "💳 KHOẢN VAY & KHẢ NĂNG TRẢ NỢ"
    )


    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )


    # =====================================================
    # THÔNG TIN KHOẢN VAY
    # =====================================================

    st.subheader("💳 1. Thông tin khoản vay")


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


    if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

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

        st.divider()


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
    # DSCR
    # =====================================================

    st.subheader("📈 2. Khả năng trả nợ - DSCR")


    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

        if st.button("📈 PHÂN TÍCH DSCR"):

            if st.session_state.tong_nghia_vu <= 0:

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )


                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )


                if st.session_state.dscr >= 1:

                    st.success(
                        "🟢 Dòng tiền hiện tại đủ để đáp ứng nghĩa vụ trả nợ theo mô hình hỗ trợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


    st.divider()


    # =====================================================
    # TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader("🏠 3. Tài sản bảo đảm")


    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Chưa đánh giá",
            "Có",
            "Không"
        ],
        index=[
            "Chưa đánh giá",
            "Có",
            "Không"
        ].index(
            st.session_state.co_tsdb
        )
    )


    st.session_state.gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )


    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
    ):

        if st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None

            st.session_state.da_phan_tich_tsdb = True


            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )


        elif st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định có tài sản bảo đảm hay không."
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
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )


            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV tương đối thấp theo mô hình hỗ trợ."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 9. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ"
    )


    st.info(
        """
        Kết quả được tổng hợp từ thông tin người dùng nhập.
        Đây là công cụ hỗ trợ thẩm định sơ bộ và không thay thế
        quyết định tín dụng chính thức.
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


    if not st.session_state.da_phan_tich_tsdb:

        missing.append(
            "Tài sản bảo đảm"
        )


    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để kết luận."
        )


        st.write(
            "Các nội dung còn thiếu:"
        )


        for item in missing:

            st.write(
                f"• {item}"
            )


    else:

        # =================================================
        # ĐIỀU KIỆN VAY
        # =================================================

        dieu_kien = [

            st.session_state.nang_luc_phap_ly,

            st.session_state.muc_dich,

            st.session_state.co_phuong_an,

            st.session_state.phuong_an_kha_thi,

            st.session_state.kha_nang_tra_no,

            st.session_state.dung_muc_dich,

            st.session_state.tra_no_dung_han
        ]


        co_dieu_kien_khong = (
            "Không" in dieu_kien
        )


        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )


        # =================================================
        # THÔNG TIN KHÁCH HÀNG
        # =================================================

        st.subheader(
            "🏢 THÔNG TIN KHÁCH HÀNG"
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


        # =================================================
        # CHỈ TIÊU
        # =================================================

        st.subheader(
            "📊 CÁC CHỈ TIÊU CHÍNH"
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


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )


        if co_dieu_kien_khong:

            st.markdown(
                """
                <div class="status-bad">

                🔴 CHƯA ĐỦ ĐIỀU KIỆN SƠ BỘ

                </div>
                """,
                unsafe_allow_html=True
            )


            st.write(
                """
                Có ít nhất một điều kiện vay vốn cơ bản
                đang được đánh giá là Không.
                Hồ sơ cần được xem xét hoặc bổ sung.
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
                Một hoặc nhiều điều kiện vay vốn
                chưa được đánh giá.
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

                🟢 ĐỦ ĐIỀU KIỆN SƠ BỘ
                ĐỂ XEM XÉT CHO VAY

                </div>
                """,
                unsafe_allow_html=True
            )


            st.write(
                """
                Các điều kiện vay vốn cơ bản đang được đánh giá là đạt.
                Chỉ tiêu tài chính và khả năng trả nợ có tín hiệu tích cực.
                Hồ sơ có thể chuyển sang bước thẩm định chi tiết.
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
                Hồ sơ chưa thể kết luận đủ điều kiện sơ bộ.
                Cần xem xét thêm tài chính, dòng tiền,
                phương án kinh doanh, lịch sử tín dụng
                và các yếu tố liên quan.
                """
            )


        st.divider()


        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader(
            "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
        )


        ket_qua = []


        # ĐIỀU KIỆN 1
        ket_qua.append(
            [
                "Năng lực pháp lý",
                "Đạt"
                if st.session_state.nang_luc_phap_ly == "Có"
                else "Cần xem xét",
                st.session_state.nang_luc_phap_ly
            ]
        )


        # ĐIỀU KIỆN 2
        ket_qua.append(
            [
                "Mục đích vay",
                "Đạt"
                if st.session_state.muc_dich == "Có"
                else "Cần xem xét",
                st.session_state.muc_dich
            ]
        )


        # ĐIỀU KIỆN 3
        ket_qua.append(
            [
                "Phương án sử dụng vốn",
                "Đạt"
                if st.session_state.co_phuong_an == "Có"
                else "Cần xem xét",
                st.session_state.co_phuong_an
            ]
        )


        # ĐIỀU KIỆN 4
        ket_qua.append(
            [
                "Tính khả thi",
                "Đạt"
                if st.session_state.phuong_an_kha_thi == "Có"
                else "Cần xem xét",
                st.session_state.phuong_an_kha_thi
            ]
        )


        # ĐIỀU KIỆN 5
        ket_qua.append(
            [
                "Khả năng trả nợ",
                "Đạt"
                if st.session_state.kha_nang_tra_no == "Có"
                else "Cần xem xét",
                st.session_state.kha_nang_tra_no
            ]
        )


        # LNST
        ket_qua.append(
            [
                "LNST",
                "Tích cực"
                if st.session_state.lnst > 0
                else "Cần xem xét",
                f"{st.session_state.lnst:,.2f} triệu đồng"
            ]
        )


        # ROA
        ket_qua.append(
            [
                "ROA",
                "Tích cực"
                if st.session_state.roa > 0
                else "Cần xem xét",
                f"{st.session_state.roa:.2f}%"
            ]
        )


        # ROE
        ket_qua.append(
            [
                "ROE",
                "Tích cực"
                if st.session_state.roe > 0
                else "Cần xem xét",
                f"{st.session_state.roe:.2f}%"
            ]
        )


        # DSCR
        if st.session_state.dscr is not None:

            ket_qua.append(
                [
                    "DSCR",
                    "Tích cực"
                    if st.session_state.dscr >= 1
                    else "Cần xem xét",
                    f"{st.session_state.dscr:.2f} lần"
                ]
            )


        # LTV
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


        st.warning(
            """
            ⚠️ LƯU Ý:

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu
            hỗ trợ phân tích tín dụng. Không sử dụng riêng lẻ
            các chỉ tiêu này để kết luận doanh nghiệp chắc chắn
            được vay vốn.

            Quyết định cho vay thực tế còn phụ thuộc vào hồ sơ
            pháp lý, mục đích sử dụng vốn, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách
            tín dụng của từng tổ chức tín dụng.
            """
        )


# =========================================================
# 10. FOOTER
# =========================================================

st.divider()


st.markdown(
    """
    <div class="footer">

        🏦
        <b>
        HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP
        </b>

        <br>

        Công cụ hỗ trợ phân tích
        và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo
        và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
