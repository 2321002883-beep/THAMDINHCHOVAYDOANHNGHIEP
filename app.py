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

DEFAULTS = {
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

    # Kết quả tài chính
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
    "da_phan_tich_dscr": False
}

for key, value in DEFAULTS.items():
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
            #061a33 0%,
            #0a3158 50%,
            #0d4d78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }


    /* ================================
       TIÊU ĐỀ
    ================================= */

    h1 {
        color: #082c52 !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b426f !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155d8c !important;
        font-weight: 700 !important;
    }


    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            135deg,
            #0866a6,
            #0d8bc5
        );
        box-shadow: 0 5px 15px rgba(8,102,166,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(8,102,166,0.32);
    }


    /* ================================
       METRIC
    ================================= */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d8e5f0;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(13,59,102,0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #5b7188 !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #083b66 !important;
        font-weight: 800;
    }


    /* ================================
       CARD
    ================================= */

    .hero-card {
        background: linear-gradient(
            135deg,
            #06264a,
            #08669d,
            #0c9bc7
        );
        padding: 35px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 15px 35px rgba(8,38,74,0.22);
        margin-bottom: 25px;
    }

    .hero-card h1 {
        color: white !important;
        font-size: 31px;
        margin-bottom: 10px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        margin-bottom: 0;
    }


    .section-card {
        background: rgba(255,255,255,0.96);
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #dce8f2;
        box-shadow: 0 6px 20px rgba(13,59,102,0.06);
        margin-bottom: 20px;
    }


    /* ================================
       KẾT QUẢ
    ================================= */

    .result-good {
        background: #e8f8ef;
        border-left: 6px solid #159957;
        padding: 18px;
        border-radius: 14px;
        color: #126b3d;
        font-weight: 800;
        font-size: 18px;
    }

    .result-warning {
        background: #fff7df;
        border-left: 6px solid #e4a400;
        padding: 18px;
        border-radius: 14px;
        color: #7c5d00;
        font-weight: 800;
        font-size: 18px;
    }

    .result-bad {
        background: #fff0f0;
        border-left: 6px solid #d64545;
        padding: 18px;
        border-radius: 14px;
        color: #8d2424;
        font-weight: 800;
        font-size: 18px;
    }


    /* ================================
       SIDEBAR MENU
    ================================= */

    div[data-testid="stRadio"] label {
        background: rgba(255,255,255,0.08);
        padding: 10px 12px;
        border-radius: 10px;
        margin-bottom: 6px;
    }


    /* ================================
       FOOTER
    ================================= */

    .footer {
        text-align: center;
        color: #70849a;
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
            use_container_width=True
        )
    except:
        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:55px;
                padding:10px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )

    # TÊN HỆ THỐNG
    st.markdown(
        """
        <div style="
            text-align:center;
            padding:5px 5px 15px 5px;
        ">
            <div style="
                font-size:19px;
                font-weight:800;
                line-height:1.4;
            ">
                THẨM ĐỊNH
                <br>
                CHO VAY DOANH NGHIỆP
            </div>

            <div style="
                font-size:13px;
                opacity:0.85;
                margin-top:7px;
            ">
                HỖ TRỢ PHÂN TÍCH TÍN DỤNG
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "### 📌 MENU THẨM ĐỊNH"
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
        "🏦 Phiên bản hỗ trợ thẩm định sơ bộ"
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
        hồ sơ vay vốn doanh nghiệp thông qua việc tổng hợp thông tin
        pháp lý, mục đích vay, tình hình tài chính, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )

    st.divider()

    st.subheader("📊 TIẾN ĐỘ THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 Hồ sơ",
            "Đã nhập" if st.session_state.da_luu_ho_so
            else "Chưa nhập"
        )

    with c2:
        st.metric(
            "💰 Tài chính",
            "Đã phân tích" if st.session_state.da_phan_tich_tc
            else "Chưa phân tích"
        )

    with c3:
        st.metric(
            "📈 Trả nợ",
            "Đã phân tích" if st.session_state.da_phan_tich_dscr
            else "Chưa phân tích"
        )

    with c4:
        st.metric(
            "🏠 TSĐB",
            "Đã phân tích" if st.session_state.da_phan_tich_tsdb
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
            và mục đích vay vốn.
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

            Phân tích LNST, ROA,
            ROE, tỷ lệ nợ và DSCR.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu và đưa ra
            kết luận thẩm định sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ, không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY")

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
            ].index(st.session_state.nganh_nghe)
        )

    with c2:

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=int(st.session_state.thoi_gian_hd)
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

    if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

        if ten_dn.strip() == "":
            st.error("❌ Vui lòng nhập tên doanh nghiệp.")

        elif ma_so.strip() == "":
            st.error("❌ Vui lòng nhập mã số doanh nghiệp.")

        elif phuong_an.strip() == "":
            st.error("❌ Vui lòng nhập phương án sử dụng vốn.")

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

    st.subheader("⚖️ 2. Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ
        điều kiện vay vốn. Việc chấp thuận cho vay thực tế còn
        phụ thuộc quy định pháp luật, hồ sơ khách hàng và chính sách
        tín dụng của từng tổ chức tín dụng.
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
            "1. Có năng lực pháp lý phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "2. Mục đích vay vốn hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.co_phuong_an = st.selectbox(
            "3. Có phương án sử dụng vốn?",
            options,
            index=options.index(
                st.session_state.co_phuong_an
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "4. Phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "5. Có khả năng tài chính trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )

        st.session_state.dung_muc_dich = st.selectbox(
            "6. Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.dung_muc_dich
            )
        )

        st.session_state.tra_no_dung_han = st.selectbox(
            "7. Cam kết trả nợ đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )

    st.divider()

    # =====================================================
    # TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader("🏠 3. Tài sản bảo đảm")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.co_tsdb = st.selectbox(
            "Khoản vay có tài sản bảo đảm?",
            options,
            index=options.index(
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

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN & TSĐB"):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        if "Không" in dieu_kien:

            st.error(
                "🔴 Có ít nhất một điều kiện vay vốn đang được đánh giá là Không."
            )

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 Các điều kiện vay vốn hiện đang được đánh giá là Có."
            )

        # Xử lý TSĐB

        if st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được xác định là không có tài sản bảo đảm."
            )

        elif st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Chưa xác định tình trạng tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.warning(
                "⚠️ Chưa nhập số tiền vay. Vui lòng nhập khoản vay "
                "tại mục 'Tài chính & Khả năng trả nợ'."
            )

        else:

            st.session_state.ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            st.session_state.da_phan_tich_tsdb = True

            st.success(
                f"✅ Đã tính LTV: {st.session_state.ltv:.2f}%"
            )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ")

    # =====================================================
    # TÀI CHÍNH
    # =====================================================

    st.subheader("📊 1. Phân tích tình hình tài chính")

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
            "📈 Lợi nhuận sau thuế (LNST)",
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
                "✅ Đã phân tích tình hình tài chính."
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
    # KHOẢN VAY
    # =====================================================

    st.subheader("💳 2. Thông tin khoản vay")

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

    st.subheader("📈 3. Phân tích khả năng trả nợ")

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
                "Tổng nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )

        if st.button("📈 TÍNH DSCR"):

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
                        "🟢 Dòng tiền hiện tại đủ hoặc lớn hơn nghĩa vụ trả nợ."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                    )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả dưới đây là kết quả thẩm định sơ bộ dựa trên
        thông tin được nhập vào hệ thống. Quyết định cho vay
        thực tế phải được thực hiện theo quy trình và chính sách
        tín dụng của tổ chức tín dụng.
        """
    )

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append("Hồ sơ doanh nghiệp")

    if not st.session_state.da_phan_tich_tc:
        missing.append("Phân tích tài chính")

    if not st.session_state.da_phan_tich_vay:
        missing.append("Thông tin khoản vay")

    if not st.session_state.da_phan_tich_dscr:
        missing.append("Khả năng trả nợ")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Tài sản bảo đảm")


    # =====================================================
    # THÔNG TIN KHÁCH HÀNG
    # =====================================================

    if st.session_state.da_luu_ho_so:

        st.subheader("🏢 THÔNG TIN DOANH NGHIỆP")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Tên doanh nghiệp",
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
    # CHỈ TIÊU CHÍNH
    # =====================================================

    st.subheader("📊 CÁC CHỈ TIÊU THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "LNST",
        f"{st.session_state.lnst:,.2f}"
    )

    c2.metric(
        "ROA",
        (
            f"{st.session_state.roa:.2f}%"
            if st.session_state.roa is not None
            else "Chưa tính"
        )
    )

    c3.metric(
        "ROE",
        (
            f"{st.session_state.roe:.2f}%"
            if st.session_state.roe is not None
            else "Chưa tính"
        )
    )

    c4.metric(
        "Tỷ lệ nợ",
        (
            f"{st.session_state.ty_le_no:.2f}%"
            if st.session_state.ty_le_no is not None
            else "Chưa tính"
        )
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


    # =====================================================
    # NẾU THIẾU DỮ LIỆU
    # =====================================================

    if len(missing) > 0:

        st.divider()

        st.warning(
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN THẨM ĐỊNH."
        )

        st.write(
            "Vui lòng hoàn thành các nội dung sau:"
        )

        for item in missing:
            st.write(
                f"🔸 {item}"
            )

    else:

        # =================================================
        # KIỂM TRA ĐIỀU KIỆN
        # =================================================

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
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
        # ĐÁNH GIÁ TÀI CHÍNH
        # =================================================

        tai_chinh_tot = (
            st.session_state.lnst > 0
            and st.session_state.roa is not None
            and st.session_state.roa > 0
            and st.session_state.roe is not None
            and st.session_state.roe > 0
        )

        tra_no_tot = (
            st.session_state.dscr is not None
            and st.session_state.dscr >= 1
        )


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.divider()

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")


        if co_dieu_kien_khong:

            st.markdown(
                """
                <div class="result-bad">
                    🔴 CHƯA ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ có ít nhất một điều kiện vay vốn cơ bản
                đang được đánh giá là Không. Cần xác minh nguyên nhân,
                bổ sung hồ sơ hoặc điều chỉnh phương án trước khi
                tiếp tục thẩm định.
                """
            )


        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="result-warning">
                    🟡 CHƯA ĐỦ CƠ SỞ ĐỂ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ vẫn còn điều kiện vay vốn chưa được đánh giá.
                Chưa nên đưa ra kết luận cuối cùng về việc cấp tín dụng.
                """
            )


        elif tai_chinh_tot and tra_no_tot:

            st.markdown(
                """
                <div class="result-good">
                    🟢 ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ TIẾP TỤC XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đáp ứng các điều kiện sơ bộ đã được nhập và đánh giá.
                Tình hình lợi nhuận có tín hiệu tích cực, khả năng sinh lời
                dương và DSCR đạt từ 1 lần trở lên theo dữ liệu đầu vào.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
                chi tiết, bao gồm xác minh hồ sơ pháp lý, CIC/lịch sử tín dụng,
                kiểm tra phương án kinh doanh, dòng tiền thực tế,
                định giá tài sản bảo đảm và các nội dung khác theo quy định
                của tổ chức tín dụng.
                """
            )


        else:

            st.markdown(
                """
                <div class="result-warning">
                    🟡 CẦN THẨM ĐỊNH BỔ SUNG TRƯỚC KHI QUYẾT ĐỊNH
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ chưa có đủ tín hiệu tích cực trên các chỉ tiêu
                tài chính và khả năng trả nợ được sử dụng trong mô hình
                hỗ trợ. Cần tiếp tục xem xét dòng tiền, tình hình tài chính,
                phương án kinh doanh, lịch sử tín dụng, nghĩa vụ nợ và
                tài sản bảo đảm trước khi quyết định cấp tín dụng.
                """)


        # =================================================
        # BẢNG THẨM ĐỊNH CHI TIẾT
        # =================================================

        st.divider()

        st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []


        # Điều kiện vay

        dieu_kien_data = [
            (
                "Năng lực pháp lý",
                st.session_state.nang_luc_phap_ly
            ),
            (
                "Mục đích vay hợp pháp",
                st.session_state.muc_dich_hop_phap
            ),
            (
                "Phương án sử dụng vốn",
                st.session_state.co_phuong_an
            ),
            (
                "Tính khả thi phương án",
                st.session_state.phuong_an_kha_thi
            ),
            (
                "Khả năng tài chính trả nợ",
                st.session_state.kha_nang_tra_no
            ),
            (
                "Cam kết sử dụng vốn đúng mục đích",
                st.session_state.dung_muc_dich
            ),
            (
                "Cam kết trả nợ đúng hạn",
                st.session_state.tra_no_dung_han
            )
        ]


        for ten, gia_tri in dieu_kien_data:

            if gia_tri == "Có":

                ket_qua.append(
                    [
                        ten,
                        "Đạt",
                        "Đang được đánh giá là Có"
                    ]
                )

            elif gia_tri == "Không":

                ket_qua.append(
                    [
                        ten,
                        "Không đạt",
                        "Đang được đánh giá là Không"
                    ]
                )

            else:

                ket_qua.append(
                    [
                        ten,
                        "Chưa đánh giá",
                        "Cần bổ sung thông tin"
                    ]
                )


        # Tài chính

        if st.session_state.lnst > 0:

            ket_qua.append(
                [
                    "Lợi nhuận sau thuế",
                    "Tích cực",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Lợi nhuận sau thuế",
                    "Cần xem xét",
                    f"{st.session_state.lnst:,.2f} triệu đồng"
                ]
            )


        if st.session_state.roa > 0:

            ket_qua.append(
                [
                    "ROA",
                    "Tích cực",
                    f"{st.session_state.roa:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "ROA",
                    "Cần xem xét",
                    f"{st.session_state.roa:.2f}%"
                ]
            )


        if st.session_state.roe > 0:

            ket_qua.append(
                [
                    "ROE",
                    "Tích cực",
                    f"{st.session_state.roe:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "ROE",
                    "Cần xem xét",
                    f"{st.session_state.roe:.2f}%"
                ]
            )


        # DSCR

        if st.session_state.dscr >= 1:

            ket_qua.append(
                [
                    "DSCR",
                    "Tích cực",
                    f"{st.session_state.dscr:.2f} lần"
                ]
            )

        else:

            ket_qua.append(
                [
                    "DSCR",
                    "Cần xem xét",
                    f"{st.session_state.dscr:.2f} lần"
                ]
            )


        # TSĐB

        if st.session_state.co_tsdb == "Không":

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Không có TSĐB",
                    "Khoản vay không có tài sản bảo đảm"
                ]
            )

        elif st.session_state.ltv is not None:

            ket_qua.append(
                [
                    "Tỷ lệ LTV",
                    "Tham khảo",
                    f"{st.session_state.ltv:.2f}%"
                ]
            )

        else:

            ket_qua.append(
                [
                    "Tài sản bảo đảm",
                    "Chưa đánh giá",
                    "Chưa đủ dữ liệu đánh giá"
                ]
            )


        df = pd.DataFrame(
            ket_qua,
            columns=[
                "Tiêu chí thẩm định",
                "Kết quả",
                "Chi tiết"
            ]
        )


        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


        # =================================================
        # LƯU Ý
        # =================================================

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu
            hỗ trợ phân tích tín dụng, không phải là điều kiện
            pháp lý duy nhất để quyết định cho vay.

            Quyết định tín dụng thực tế cần xem xét tổng thể:
            hồ sơ pháp lý, mục đích vay, phương án kinh doanh,
            tình hình tài chính, dòng tiền, lịch sử tín dụng,
            nghĩa vụ nợ, tài sản bảo đảm, khả năng trả nợ và
            chính sách tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 9. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

        🏦 <b>HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP</b>

        <br><br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ
        ra quyết định tín dụng.

    </div>
    """,
    unsafe_allow_html=True
)
