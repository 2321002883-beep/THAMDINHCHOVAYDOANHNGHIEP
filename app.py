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

DEFAULT_VALUES = {
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "",
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

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

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
}


for key, value in DEFAULT_VALUES.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. CSS GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* NỀN */
    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #eef5fb 50%,
            #f8fbff 100%
        );
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #061a33 0%,
            #0b3158 50%,
            #0f4d78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.25);
    }

    /* TIÊU ĐỀ */
    h1 {
        color: #082b4c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0d426d !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #155a86 !important;
        font-weight: 700 !important;
    }

    /* HERO */
    .hero-card {
        background: linear-gradient(
            135deg,
            #06284d,
            #0b5b91,
            #168ac1
        );
        padding: 38px;
        border-radius: 25px;
        color: white;
        box-shadow: 0 15px 35px rgba(6,40,77,0.25);
        margin-bottom: 25px;
    }

    .hero-card h1 {
        color: white !important;
        font-size: 32px;
        margin-bottom: 10px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        margin: 0;
    }

    /* CARD */
    .card {
        background: rgba(255,255,255,0.95);
        padding: 24px;
        border-radius: 20px;
        border: 1px solid #d9e6f2;
        box-shadow: 0 8px 24px rgba(13,59,102,0.08);
        margin-bottom: 20px;
    }

    /* METRIC */
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d9e6f2;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(13,59,102,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3761 !important;
        font-weight: 800;
    }

    /* BUTTON */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(
            135deg,
            #0b4f8a,
            #1688c5
        );
        box-shadow: 0 5px 15px rgba(11,79,138,0.22);
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(11,79,138,0.30);
    }

    /* STATUS */
    .status-good {
        background: #e9f8ef;
        border-left: 6px solid #1e9e58;
        padding: 18px;
        border-radius: 12px;
        color: #176b3c;
        font-weight: 700;
        font-size: 17px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 6px solid #e4a400;
        padding: 18px;
        border-radius: 12px;
        color: #805f00;
        font-weight: 700;
        font-size: 17px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 6px solid #d64545;
        padding: 18px;
        border-radius: 12px;
        color: #8c2525;
        font-weight: 700;
        font-size: 17px;
    }

    /* FOOTER */
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
# 4. SIDEBAR - DANH MỤC CHÍNH
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:8px 5px 18px 5px;
        ">
            <div style="font-size:42px;">🏦</div>

            <div style="
                font-size:20px;
                font-weight:800;
                line-height:1.4;
            ">
                THẨM ĐỊNH
            </div>

            <div style="
                font-size:15px;
                font-weight:600;
                opacity:0.9;
            ">
                CHO VAY DOANH NGHIỆP
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "📌 DANH MỤC CHÍNH",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện vay",
            "💰 Tài chính, Khoản vay & TSĐB",
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
        Hệ thống hỗ trợ cán bộ tín dụng hoặc người sử dụng
        thực hiện thẩm định sơ bộ hồ sơ vay vốn của doanh nghiệp.
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
            và phương án vay vốn.
            """
        )

    with c2:
        st.info(
            """
            **02 | ĐIỀU KIỆN**

            Kiểm tra các điều kiện
            vay vốn cơ bản.
            """
        )

    with c3:
        st.info(
            """
            **03 | TÀI CHÍNH**

            Phân tích tài chính,
            dòng tiền, khoản vay
            và TSĐB.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp dữ liệu và
            đưa ra kết luận sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ và không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY VỐN")

    tab1, tab2 = st.tabs(
        [
            "📋 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn"
        ]
    )

    # -----------------------------------------------------
    # TAB 1: HỒ SƠ
    # -----------------------------------------------------

    with tab1:

        st.subheader("📋 THÔNG TIN DOANH NGHIỆP")

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
                value=int(
                    st.session_state.thoi_gian_hd
                )
            )

        st.subheader("💳 PHƯƠNG ÁN VAY VỐN")

        muc_dich_options = [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]

        muc_dich_vay = st.selectbox(
            "Mục đích sử dụng vốn",
            muc_dich_options
        )

        phuong_an = st.text_area(
            "Mô tả phương án sử dụng vốn",
            value=st.session_state.phuong_an,
            placeholder="Nhập phương án kinh doanh và nhu cầu sử dụng vốn..."
        )

        if st.button(
            "💾 LƯU HỒ SƠ DOANH NGHIỆP",
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

    # -----------------------------------------------------
    # TAB 2: ĐIỀU KIỆN VAY
    # -----------------------------------------------------

    with tab2:

        st.subheader(
            "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
        )

        st.info(
            """
            Các tiêu chí dưới đây dùng để kiểm tra sơ bộ.
            Quyết định cho vay thực tế phải căn cứ quy định pháp luật
            hiện hành, hồ sơ khách hàng và chính sách tín dụng của
            từng tổ chức tín dụng.
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
                "1. Doanh nghiệp có năng lực pháp lý phù hợp?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.nang_luc_phap_ly
                )
            )

            st.session_state.muc_dich_hop_phap = st.selectbox(
                "2. Mục đích vay vốn có hợp pháp?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.muc_dich_hop_phap
                )
            )

            st.session_state.co_phuong_an = st.selectbox(
                "3. Có phương án sử dụng vốn?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.co_phuong_an
                )
            )

            st.session_state.phuong_an_kha_thi = st.selectbox(
                "4. Phương án sử dụng vốn có khả thi?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.phuong_an_kha_thi
                )
            )

        with c2:

            st.session_state.kha_nang_tra_no = st.selectbox(
                "5. Có khả năng tài chính để trả nợ?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.kha_nang_tra_no
                )
            )

            st.session_state.dung_muc_dich = st.selectbox(
                "6. Cam kết sử dụng vốn đúng mục đích?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.dung_muc_dich
                )
            )

            st.session_state.tra_no_dung_han = st.selectbox(
                "7. Cam kết trả nợ đúng hạn?",
                lua_chon,
                index=lua_chon.index(
                    st.session_state.tra_no_dung_han
                )
            )

        if st.button(
            "🔍 KIỂM TRA ĐIỀU KIỆN VAY",
            key="check_conditions"
        ):

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
                    "🔴 Có ít nhất một điều kiện đang được đánh giá là Không."
                )

            elif "Chưa đánh giá" in dieu_kien:

                st.warning(
                    "🟡 Chưa thể kết luận vì còn điều kiện chưa được đánh giá."
                )

            else:

                st.success(
                    "🟢 Tất cả điều kiện sơ bộ hiện đang được đánh giá là Có."
                )


# =========================================================
# 7. TÀI CHÍNH - KHOẢN VAY - KHẢ NĂNG TRẢ NỢ - TSĐB
# =========================================================

elif menu == "💰 Tài chính, Khoản vay & TSĐB":

    st.title(
        "💰 TÀI CHÍNH, KHOẢN VAY & TÀI SẢN BẢO ĐẢM"
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "📈 Phân tích tài chính",
            "💳 Khoản vay & Khả năng trả nợ",
            "🏠 Tài sản bảo đảm"
        ]
    )

    # =====================================================
    # TAB 1: TÀI CHÍNH
    # =====================================================

    with tab1:

        st.subheader("📈 PHÂN TÍCH TÀI CHÍNH")

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
                ),
                key="input_doanh_thu"
            )

            st.session_state.lnst = st.number_input(
                "📈 Lợi nhuận sau thuế (LNST)",
                value=float(
                    st.session_state.lnst
                ),
                key="input_lnst"
            )

            st.session_state.tong_tai_san = st.number_input(
                "🏢 Tổng tài sản",
                min_value=0.0,
                value=float(
                    st.session_state.tong_tai_san
                ),
                key="input_tts"
            )

        with c2:

            st.session_state.von_chu_so_huu = st.number_input(
                "💼 Vốn chủ sở hữu",
                min_value=0.0,
                value=float(
                    st.session_state.von_chu_so_huu
                ),
                key="input_vcsh"
            )

            st.session_state.no_phai_tra = st.number_input(
                "📌 Nợ phải trả",
                min_value=0.0,
                value=float(
                    st.session_state.no_phai_tra
                ),
                key="input_npt"
            )

            st.session_state.dong_tien = st.number_input(
                "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
                value=float(
                    st.session_state.dong_tien
                ),
                key="input_dong_tien"
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

            st.divider()

            st.subheader(
                "📊 KẾT QUẢ PHÂN TÍCH"
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

    # =====================================================
    # TAB 2: KHOẢN VAY & DSCR
    # =====================================================

    with tab2:

        st.subheader(
            "💳 THÔNG TIN KHOẢN VAY"
        )

        st.caption(
            "Đơn vị nhập liệu: triệu đồng"
        )

        c1, c2 = st.columns(2)

        with c1:

            st.session_state.so_tien_vay = st.number_input(
                "💰 Số tiền vay",
                min_value=0.0,
                value=float(
                    st.session_state.so_tien_vay
                ),
                key="input_loan"
            )

            st.session_state.thoi_gian_vay = st.number_input(
                "📅 Thời hạn vay (tháng)",
                min_value=1,
                value=int(
                    st.session_state.thoi_gian_vay
                ),
                key="input_term"
            )

        with c2:

            st.session_state.lai_suat = st.number_input(
                "📈 Lãi suất (%/năm)",
                min_value=0.0,
                value=float(
                    st.session_state.lai_suat
                ),
                key="input_rate"
            )

            st.session_state.nghia_vu_no_cu = st.number_input(
                "💳 Nghĩa vụ trả nợ hiện tại/tháng",
                min_value=0.0,
                value=float(
                    st.session_state.nghia_vu_no_cu
                ),
                key="input_old_debt"
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

            st.subheader(
                "📈 KHẢ NĂNG TRẢ NỢ - DSCR"
            )

            st.info(
                """
                DSCR là chỉ tiêu hỗ trợ đánh giá khả năng tạo dòng tiền
                để đáp ứng nghĩa vụ trả nợ. Ngưỡng đánh giá thực tế
                phụ thuộc vào phương pháp tính dòng tiền và chính sách
                tín dụng của từng tổ chức tín dụng.
                """
            )

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
                "📈 TÍNH DSCR",
                key="calculate_dscr"
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

    # =====================================================
    # TAB 3: TSĐB
    # =====================================================

    with tab3:

        st.subheader(
            "🏠 TÀI SẢN BẢO ĐẢM"
        )

        st.info(
            """
            Tài sản bảo đảm là yếu tố hỗ trợ đánh giá mức độ bảo đảm
            cho khoản vay. Việc có hay không có TSĐB và tỷ lệ LTV phù hợp
            phụ thuộc vào sản phẩm tín dụng, loại tài sản, giá trị định giá,
            khả năng thanh khoản và chính sách của tổ chức tín dụng.
            """
        )

        lua_chon_tsdb = [
            "Chưa đánh giá",
            "Có",
            "Không"
        ]

        st.session_state.co_tsdb = st.selectbox(
            "Khoản vay có tài sản bảo đảm?",
            lua_chon_tsdb,
            index=lua_chon_tsdb.index(
                st.session_state.co_tsdb
            )
        )

        st.session_state.gia_tri_tsdb = st.number_input(
            "🏠 Giá trị tài sản bảo đảm (triệu đồng)",
            min_value=0.0,
            value=float(
                st.session_state.gia_tri_tsdb
            ),
            key="input_collateral"
        )

        if st.button(
            "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM",
            key="analyze_collateral"
        ):

            if st.session_state.co_tsdb == "Chưa đánh giá":

                st.warning(
                    "⚠️ Vui lòng xác định tình trạng tài sản bảo đảm."
                )

            elif st.session_state.co_tsdb == "Không":

                st.session_state.ltv = None
                st.session_state.da_phan_tich_tsdb = True

                st.info(
                    "ℹ️ Khoản vay được xác định là không có tài sản bảo đảm."
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
                        "🟢 LTV ở mức tương đối thấp theo mô hình hỗ trợ."
                    )

                elif st.session_state.ltv <= 100:

                    st.warning(
                        "🟡 Cần xem xét thêm loại tài sản, giá trị định giá và khả năng thanh khoản."
                    )

                else:

                    st.error(
                        "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                    )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ"
    )

    st.info(
        """
        Kết quả được tổng hợp từ thông tin hồ sơ, điều kiện vay,
        tình hình tài chính, khả năng trả nợ và tài sản bảo đảm.
        Đây là kết quả hỗ trợ thẩm định sơ bộ, không phải quyết định
        cấp tín dụng chính thức.
        """
    )

    # -----------------------------------------------------
    # KIỂM TRA DỮ LIỆU BẮT BUỘC
    # -----------------------------------------------------

    missing = []

    if not st.session_state.da_luu_ho_so:
        missing.append("Hồ sơ doanh nghiệp")

    if not st.session_state.da_phan_tich_tc:
        missing.append("Phân tích tài chính")

    if not st.session_state.da_phan_tich_vay:
        missing.append("Thông tin khoản vay")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Phân tích tài sản bảo đảm")

    if len(missing) > 0:

        st.warning(
            "⚠️ Chưa đủ dữ liệu để đưa ra kết quả thẩm định sơ bộ."
        )

        st.write(
            "Các nội dung còn thiếu:"
        )

        for item in missing:
            st.write(
                f"• {item}"
            )

    else:

        # -------------------------------------------------
        # THÔNG TIN DOANH NGHIỆP
        # -------------------------------------------------

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

        # -------------------------------------------------
        # CHỈ TIÊU TÀI CHÍNH
        # -------------------------------------------------

        st.subheader(
            "📊 CHỈ TIÊU TÀI CHÍNH & TÍN DỤNG"
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

        # -------------------------------------------------
        # KIỂM TRA ĐIỀU KIỆN
        # -------------------------------------------------

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich_hop_phap,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        co_khong = "Không" in dieu_kien

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )

        # -------------------------------------------------
        # KẾT LUẬN
        # -------------------------------------------------

        st.subheader(
            "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
        )

        # TRƯỜNG HỢP 1
        if co_khong:

            st.markdown(
                """
                <div class="status-bad">
                    🔴 CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ đang có ít nhất một điều kiện vay vốn cơ bản
                được đánh giá là "Không". Hồ sơ chưa phù hợp để
                chuyển sang kết luận tích cực ở thời điểm hiện tại.
                Cần xác định nguyên nhân và xem xét bổ sung hoặc
                điều chỉnh hồ sơ.
                """
            )

        # TRƯỜNG HỢP 2
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
                Cần hoàn thiện thông tin trước khi đưa ra kết luận
                thẩm định sơ bộ.
                """
            )

        # TRƯỜNG HỢP 3
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
                    🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CẤP TÍN DỤNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Dữ liệu nhập cho thấy doanh nghiệp đang đáp ứng các
                điều kiện sơ bộ được kiểm tra và có một số tín hiệu
                tích cực về lợi nhuận, hiệu quả tài sản, hiệu quả vốn
                chủ sở hữu và khả năng đáp ứng nghĩa vụ trả nợ.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
                chi tiết. Kết quả này không đồng nghĩa với việc khoản
                vay chắc chắn được phê duyệt.
                """
            )

        # TRƯỜNG HỢP 4
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
                Hồ sơ chưa có đủ tín hiệu tích cực để đưa ra kết luận
                đạt điều kiện sơ bộ. Cần xem xét thêm tình hình tài chính,
                dòng tiền, khả năng trả nợ, lịch sử tín dụng, phương án
                kinh doanh, nghĩa vụ nợ hiện tại và các yếu tố liên quan.
                """
            )

        st.divider()

        # -------------------------------------------------
        # BẢNG TỔNG HỢP
        # -------------------------------------------------

        st.subheader(
            "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
        )

        ket_qua = []

        # Điều kiện
        danh_sach_dieu_kien = [
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
                "Tính khả thi của phương án",
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

        for ten, gia_tri in danh_sach_dieu_kien:

            if gia_tri == "Có":

                ket_qua.append(
                    [
                        ten,
                        "Đạt",
                        "Được đánh giá là Có"
                    ]
                )

            elif gia_tri == "Không":

                ket_qua.append(
                    [
                        ten,
                        "Không đạt",
                        "Được đánh giá là Không"
                    ]
                )

            else:

                ket_qua.append(
                    [
                        ten,
                        "Chưa đánh giá",
                        "Chưa có đủ thông tin"
                    ]
                )

        # LNST
        ket_qua.append(
            [
                "Lợi nhuận sau thuế",
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

        # LTV / TSĐB
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

        st.warning(
            """
            ⚠️ LƯU Ý QUAN TRỌNG

            Kết quả thẩm định trên chỉ là kết quả hỗ trợ sơ bộ.

            ROA, ROE, LNST, tỷ lệ nợ, DSCR và LTV không phải là các
            điều kiện pháp lý duy nhất để quyết định cho vay.

            Quyết định cấp tín dụng thực tế cần xem xét tổng thể:
            hồ sơ pháp lý, mục đích vay, phương án sử dụng vốn,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm nếu có,
            khả năng quản trị và chính sách tín dụng của tổ chức
            tín dụng.
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

        <br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
