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

defaults = {
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 0,
    "muc_dich_vay": "",
    "phuong_an": "",

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no_dk": "Chưa đánh giá",
    "cam_ket_dung_muc_dich": "Chưa đánh giá",
    "cam_ket_tra_no": "Chưa đánh giá",

    # Tài chính
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    # Chỉ tiêu tài chính
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # Khả năng trả nợ
    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,
    "dscr": None,

    # Tài sản bảo đảm
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_kiem_tra_dieu_kien": False
}


for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       NỀN CHUNG
    ================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eef5fb 50%,
            #f8fbff 100%
        );
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #061b35 0%,
            #0a3158 50%,
            #0d4c78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #07315c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b4775 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #12608f !important;
        font-weight: 700 !important;
    }


    /* ================================
       HERO
    ================================= */

    .hero {
        background: linear-gradient(
            135deg,
            #06264a,
            #0b5688,
            #1685b9
        );

        padding: 35px;
        border-radius: 25px;
        color: white;
        margin-bottom: 25px;

        box-shadow:
            0 15px 35px
            rgba(6, 38, 74, 0.25);
    }

    .hero h1 {
        color: white !important;
        font-size: 32px;
        margin-bottom: 12px;
    }

    .hero p {
        color: rgba(255,255,255,0.9);
        font-size: 16px;
    }


    /* ================================
       CARD
    ================================= */

    .card {
        background: rgba(255,255,255,0.95);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #dce7f2;

        box-shadow:
            0 7px 22px
            rgba(13,59,102,0.08);

        margin-bottom: 20px;
    }


    /* ================================
       MENU CARD
    ================================= */

    .menu-title {
        font-size: 17px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .menu-sub {
        font-size: 13px;
        opacity: 0.85;
    }


    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 12px;

        padding: 0.7rem 1rem;

        font-weight: 700;
        color: white;

        background: linear-gradient(
            135deg,
            #07518d,
            #1385bd
        );

        box-shadow:
            0 5px 15px
            rgba(7,81,141,0.25);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }


    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background: white;
        padding: 18px;
        border-radius: 17px;

        border: 1px solid #dce7f2;

        box-shadow:
            0 7px 20px
            rgba(13,59,102,0.07);
    }


    /* ================================
       KẾT QUẢ
    ================================= */

    .good {
        background: #e9f8ef;
        border-left: 6px solid #20a05a;

        padding: 18px;
        border-radius: 12px;

        color: #176b3c;
        font-weight: 700;
    }

    .warning {
        background: #fff7df;
        border-left: 6px solid #e4a400;

        padding: 18px;
        border-radius: 12px;

        color: #805f00;
        font-weight: 700;
    }

    .bad {
        background: #fff0f0;
        border-left: 6px solid #d64545;

        padding: 18px;
        border-radius: 12px;

        color: #8c2525;
        font-weight: 700;
    }


    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        color: #71859a;
        padding: 25px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 4. SIDEBAR - MENU CHÍNH
# =========================================================

with st.sidebar:

    # LOGO
    try:
        st.image(
            "logo.jpg",
            width=130
        )
    except:
        st.markdown(
            "<div style='font-size:65px;text-align:center;'>🏦</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:20px;
            font-weight:800;
            margin-top:5px;
            margin-bottom:10px;
        ">
            THẨM ĐỊNH CHO VAY
            <br>
            DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "<b>📌 DANH MỤC THẨM ĐỊNH</b>",
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

    st.caption(
        "Hệ thống hỗ trợ thẩm định sơ bộ"
    )


# =========================================================
# 5. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero">

            <h1>
                🏦 HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Phân tích hồ sơ • Kiểm tra điều kiện vay •
                Đánh giá tài chính • Khả năng trả nợ •
                Tài sản bảo đảm • Tổng hợp kết quả
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👋 Chào mừng bạn đến với hệ thống")

    st.write(
        """
        Hệ thống hỗ trợ cán bộ tín dụng thực hiện thẩm định sơ bộ
        hồ sơ vay vốn doanh nghiệp dựa trên thông tin doanh nghiệp,
        điều kiện vay vốn, tình hình tài chính, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )

    st.divider()

    st.subheader("📊 TRẠNG THÁI HỒ SƠ")

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
            "⚖️ Điều kiện",
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
        st.metric(
            "💳 Khoản vay",
            "Đã tính"
            if st.session_state.da_phan_tich_vay
            else "Chưa tính"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(
            """
            **01 | HỒ SƠ**

            Nhập thông tin doanh nghiệp,
            mục đích vay và phương án sử dụng vốn.
            """
        )

    with c2:
        st.info(
            """
            **02 | ĐIỀU KIỆN**

            Kiểm tra điều kiện vay vốn
            và tài sản bảo đảm.
            """
        )

    with c3:
        st.info(
            """
            **03 | TÀI CHÍNH**

            Phân tích LNST, ROA, ROE,
            tỷ lệ nợ và DSCR.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp thông tin và
            đưa ra kết luận sơ bộ.
            """
        )

    st.warning(
        """
        ⚠️ Lưu ý: Đây là công cụ hỗ trợ thẩm định sơ bộ.
        Kết quả không thay thế quyết định tín dụng chính thức
        của ngân hàng hoặc tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")

    # -----------------------------------------------------
    # HỒ SƠ DOANH NGHIỆP
    # -----------------------------------------------------

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
            ].index(
                st.session_state.nganh_nghe
            )
        )

    with c2:

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=int(
                st.session_state.thoi_gian_hd
            )
        )

        muc_dich_vay = st.selectbox(
            "Mục đích vay vốn",
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
        placeholder="Nhập phương án kinh doanh và nhu cầu sử dụng vốn..."
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

    # -----------------------------------------------------
    # ĐIỀU KIỆN VAY
    # -----------------------------------------------------

    st.subheader("2️⃣ Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Việc kiểm tra dưới đây nhằm hỗ trợ rà soát sơ bộ hồ sơ.
        Điều kiện và quy trình thực tế phải căn cứ quy định pháp luật
        hiện hành và chính sách tín dụng của từng ngân hàng.
        """
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Doanh nghiệp có năng lực pháp lý phù hợp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "Mục đích vay vốn hợp pháp?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn khả thi?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no_dk = st.selectbox(
            "Doanh nghiệp có khả năng tài chính trả nợ?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.kha_nang_tra_no_dk
            )
        )

        st.session_state.cam_ket_dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.cam_ket_dung_muc_dich
            )
        )

        st.session_state.cam_ket_tra_no = st.selectbox(
            "Cam kết trả nợ đúng hạn?",
            ["Chưa đánh giá", "Có", "Không"],
            index=[
                "Chưa đánh giá",
                "Có",
                "Không"
            ].index(
                st.session_state.cam_ket_tra_no
            )
        )

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_dk,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        st.session_state.da_kiem_tra_dieu_kien = True

        if "Không" in dieu_kien:

            st.error(
                "🔴 Hồ sơ có ít nhất một điều kiện đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
            )

    st.divider()

    # -----------------------------------------------------
    # TÀI SẢN BẢO ĐẢM
    # -----------------------------------------------------

    st.subheader("3️⃣ Tài sản bảo đảm")

    c1, c2 = st.columns(2)

    with c1:

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

    with c2:

        st.session_state.gia_tri_tsdb = st.number_input(
            "Giá trị tài sản bảo đảm (triệu đồng)",
            min_value=0.0,
            value=float(
                st.session_state.gia_tri_tsdb
            )
        )

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định tình trạng tài sản bảo đảm."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được xác định là không có tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.warning(
                "⚠️ Vui lòng nhập số tiền vay tại mục "
                "'Tài chính & Khả năng trả nợ' trước."
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
                    "🟢 Tỷ lệ LTV ở mức thấp theo ngưỡng tham khảo."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng, khả năng thanh khoản "
                    "và giá trị định giá tài sản."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm."
                )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title("💰 TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ")

    # =====================================================
    # PHÂN TÍCH TÀI CHÍNH
    # =====================================================

    st.subheader("1️⃣ Phân tích tài chính")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=float(
                st.session_state.doanh_thu
            )
        )

        st.session_state.lnst = st.number_input(
            "📈 Lợi nhuận sau thuế",
            value=float(
                st.session_state.lnst
            )
        )

        st.session_state.tong_tai_san = st.number_input(
            "🏢 Tổng tài sản",
            min_value=0.0,
            value=float(
                st.session_state.tong_tai_san
            )
        )

    with c2:

        st.session_state.von_chu_so_huu = st.number_input(
            "💼 Vốn chủ sở hữu",
            min_value=0.0,
            value=float(
                st.session_state.von_chu_so_huu
            )
        )

        st.session_state.no_phai_tra = st.number_input(
            "📌 Nợ phải trả",
            min_value=0.0,
            value=float(
                st.session_state.no_phai_tra
            )
        )

        st.session_state.dong_tien = st.number_input(
            "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
            value=float(
                st.session_state.dong_tien
            )
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
                "✅ Đã phân tích các chỉ tiêu tài chính."
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
    # THÔNG TIN KHOẢN VAY
    # =====================================================

    st.subheader("2️⃣ Thông tin khoản vay")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "💰 Số tiền vay (triệu đồng)",
            min_value=0.0,
            value=float(
                st.session_state.so_tien_vay
            )
        )

        st.session_state.thoi_gian_vay = st.number_input(
            "📅 Thời hạn vay (tháng)",
            min_value=1,
            value=int(
                st.session_state.thoi_gian_vay
            )
        )

    with c2:

        st.session_state.lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=float(
                st.session_state.lai_suat
            )
        )

        st.session_state.nghia_vu_no_cu = st.number_input(
            "💳 Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=float(
                st.session_state.nghia_vu_no_cu
            )
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

    st.subheader("3️⃣ Khả năng trả nợ")

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

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

        if st.button("📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"):

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
                        "🟢 Dòng tiền hiện tại đủ để đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại chưa đủ đáp ứng nghĩa vụ trả nợ."
                    )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả được tổng hợp từ dữ liệu đã nhập.
        Đây là kết quả hỗ trợ thẩm định sơ bộ, không phải quyết định
        phê duyệt tín dụng chính thức.
        """
    )

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append("Hồ sơ doanh nghiệp")

    if not st.session_state.da_kiem_tra_dieu_kien:
        missing.append("Kiểm tra điều kiện vay")

    if not st.session_state.da_phan_tich_tc:
        missing.append("Phân tích tài chính")

    if not st.session_state.da_phan_tich_vay:
        missing.append("Thông tin khoản vay")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Tài sản bảo đảm")

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết quả thẩm định sơ bộ."
        )

        st.write(
            "Vui lòng hoàn thành:"
        )

        for item in missing:
            st.write(
                f"• {item}"
            )

    else:

        # =================================================
        # THÔNG TIN DOANH NGHIỆP
        # =================================================

        st.subheader("🏢 THÔNG TIN KHÁCH HÀNG")

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

        st.subheader("📊 CÁC CHỈ TIÊU THẨM ĐỊNH")

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
        # KIỂM TRA ĐIỀU KIỆN
        # =================================================

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no_dk,
            st.session_state.cam_ket_dung_muc_dich,
            st.session_state.cam_ket_tra_no
        ]

        co_khong = "Không" in dieu_kien

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

        # =================================================
        # KẾT LUẬN
        # =================================================

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

        # 1. Có điều kiện không đạt
        if co_khong:

            st.markdown(
                """
                <div class="bad">
                    🔴 CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang có ít nhất một điều kiện vay vốn được đánh giá
                là Không. Chưa nên đề xuất cấp tín dụng tại bước thẩm định
                sơ bộ cho đến khi nguyên nhân được làm rõ và xử lý.
                """
            )

        # 2. Chưa đánh giá đủ
        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="warning">
                    🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ chưa được đánh giá đầy đủ các điều kiện vay vốn.
                Cần bổ sung thông tin trước khi đưa ra kết luận.
                """
            )

        # 3. Điều kiện đạt nhưng khả năng tài chính yếu
        elif (
            st.session_state.lnst <= 0
            or st.session_state.roa <= 0
            or st.session_state.roe <= 0
            or st.session_state.dscr is None
            or st.session_state.dscr < 1
        ):

            st.markdown(
                """
                <div class="warning">
                    🟡 CẦN THẨM ĐỊNH BỔ SUNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Các điều kiện hồ sơ cơ bản đang được đánh giá là đạt,
                tuy nhiên một hoặc nhiều chỉ tiêu tài chính hoặc khả năng
                trả nợ chưa đạt mức tích cực. Cần xem xét thêm dòng tiền,
                nguồn trả nợ, lịch sử tín dụng, phương án kinh doanh,
                tình hình tài chính và các yếu tố rủi ro khác.
                """
            )

        # 4. Hồ sơ đạt sơ bộ
        else:

            st.markdown(
                """
                <div class="good">
                    🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CẤP TÍN DỤNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang đáp ứng các điều kiện sơ bộ được kiểm tra.
                Tình hình lợi nhuận, hiệu quả tài sản, hiệu quả vốn chủ sở hữu
                và khả năng trả nợ theo DSCR đang có tín hiệu tích cực.
                Hồ sơ có thể được chuyển sang bước thẩm định chi tiết,
                phê duyệt tín dụng theo quy trình của ngân hàng.
                """
            )

        st.divider()

        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []

        # Điều kiện pháp lý
        ket_qua.append(
            [
                "Năng lực pháp lý",
                st.session_state.nang_luc_phap_ly,
                "Điều kiện hồ sơ"
            ]
        )

        ket_qua.append(
            [
                "Mục đích vay vốn",
                st.session_state.muc_dich_hop_phap,
                "Mục đích sử dụng vốn"
            ]
        )

        ket_qua.append(
            [
                "Tính khả thi phương án",
                st.session_state.phuong_an_kha_thi,
                "Phương án kinh doanh"
            ]
        )

        ket_qua.append(
            [
                "Khả năng tài chính trả nợ",
                st.session_state.kha_nang_tra_no_dk,
                "Điều kiện vay"
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

        # Tỷ lệ nợ
        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Tham khảo",
                f"{st.session_state.ty_le_no:.2f}%"
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
                "Đánh giá",
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

            Kết quả "Đạt điều kiện sơ bộ" KHÔNG đồng nghĩa với việc
            doanh nghiệp chắc chắn được ngân hàng phê duyệt khoản vay.

            ROA, ROE, LNST, DSCR, LTV chỉ là các chỉ tiêu hỗ trợ phân tích.
            Quyết định tín dụng thực tế còn phải xem xét hồ sơ pháp lý,
            mục đích vay, phương án kinh doanh, dòng tiền, lịch sử tín dụng,
            nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm, định giá tài sản,
            ngành nghề, rủi ro doanh nghiệp và chính sách tín dụng của
            từng ngân hàng.
            """
        )


# =========================================================
# 9. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</b>

        <br><br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
