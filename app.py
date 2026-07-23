import streamlit as st
import pandas as pd

# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Hệ thống thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. SESSION STATE
# =========================================================

default_values = {
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # Điều kiện vay
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "cam_ket_dung_muc_dich": "Chưa đánh giá",
    "cam_ket_tra_no": "Chưa đánh giá",

    # Lịch sử tín dụng
    "lich_su_tin_dung": "Chưa đánh giá",
    "no_xau": "Chưa đánh giá",

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

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # Trạng thái
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_tsdb": False,
    "da_phan_tich_dscr": False,
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

    /* NỀN CHUNG */
    .stApp {
        background: linear-gradient(
            135deg,
            #f4f8fc 0%,
            #edf5fb 50%,
            #f8fbff 100%
        );
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #061a33 0%,
            #0a3157 45%,
            #0d4d78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* TIÊU ĐỀ */
    h1 {
        color: #082b4c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b4775 !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #126394 !important;
        font-weight: 700 !important;
    }

    /* CARD */
    .hero-card {
        background: linear-gradient(
            135deg,
            #06264a,
            #0b5689,
            #1594c5
        );
        padding: 35px;
        border-radius: 24px;
        color: white;
        box-shadow: 0 15px 35px rgba(6,38,74,0.22);
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
        background: rgba(255,255,255,0.95);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #d8e6f2;
        box-shadow: 0 7px 22px rgba(13,59,102,0.07);
        margin-bottom: 20px;
    }

    /* METRIC */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.96);
        border: 1px solid #d8e5f0;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 7px 22px rgba(13,59,102,0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #55718d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3d67 !important;
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
            #07528b,
            #1594c5
        );
        box-shadow: 0 5px 15px rgba(7,82,139,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* STATUS */
    .status-good {
        background: #e8f8ef;
        border-left: 6px solid #1d9b58;
        padding: 18px;
        border-radius: 12px;
        color: #176c3e;
        font-weight: 700;
        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 6px solid #e3a000;
        padding: 18px;
        border-radius: 12px;
        color: #7b5b00;
        font-weight: 700;
        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 6px solid #d74343;
        padding: 18px;
        border-radius: 12px;
        color: #8b2525;
        font-weight: 700;
        font-size: 18px;
    }

    .sidebar-title {
        text-align: center;
        font-size: 18px;
        font-weight: 800;
        line-height: 1.4;
        margin-top: 10px;
    }

    .sidebar-subtitle {
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        opacity: 0.85;
        margin-top: 5px;
    }

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

    # LOGO NẰM TRÊN CHỮ THẨM ĐỊNH
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

    st.markdown(
        """
        <div class="sidebar-title">
            🏦 THẨM ĐỊNH CHO VAY<br>
            DOANH NGHIỆP

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.radio(
        "📌 DANH MỤC THẨM ĐỊNH",
        [
            "🏠 Trang chủ",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & trả nợ",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )


# =========================================================
# 5. TRANG CHỦ
# =========================================================

if menu == "🏠 Trang chủ":

    st.markdown(
        """
        <div class="hero-card">
            <h1>🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</h1>
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
        Hệ thống hỗ trợ thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp
        dựa trên thông tin pháp lý, tài chính, khoản vay,
        khả năng trả nợ và tài sản bảo đảm.
        """
    )

    st.divider()

    st.subheader("📊 TIẾN ĐỘ THẨM ĐỊNH")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🏢 Hồ sơ",
            "Đã nhập" if st.session_state.da_luu_ho_so else "Chưa nhập"
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
            "📊 Kết quả",
            "Sẵn sàng"
            if (
                st.session_state.da_phan_tich_tc
                and st.session_state.da_phan_tich_vay
            )
            else "Chưa đủ dữ liệu"
        )

    st.divider()

    st.subheader("🚀 QUY TRÌNH THẨM ĐỊNH")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            """
            **01 | HỒ SƠ & ĐIỀU KIỆN**

            Kiểm tra thông tin doanh nghiệp,
            mục đích vay, phương án sử dụng vốn,
            năng lực pháp lý và lịch sử tín dụng.
            """
        )

    with c2:
        st.success(
            """
            **02 | TÀI CHÍNH & TRẢ NỢ**

            Phân tích LNST, ROA, ROE,
            tỷ lệ nợ, DSCR và nghĩa vụ trả nợ.
            """
        )

    with c3:
        st.warning(
            """
            **03 | KẾT QUẢ**

            Tổng hợp các yếu tố tín dụng,
            đưa ra kết luận sơ bộ và kiến nghị
            thẩm định tiếp theo.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ. Quyết định cấp tín dụng thực tế
        phải căn cứ hồ sơ, quy định pháp luật, quy trình nội bộ
        và chính sách tín dụng của từng tổ chức tín dụng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN
# =========================================================

elif menu == "🏢 Hồ sơ & điều kiện":

    st.title("🏢 HỒ SƠ VÀ ĐIỀU KIỆN VAY VỐN")

    tab1, tab2, tab3 = st.tabs(
        [
            "📋 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay",
            "📜 Lịch sử tín dụng"
        ]
    )

    # -----------------------------------------------------
    # TAB 1
    # -----------------------------------------------------

    with tab1:

        st.subheader("📋 Thông tin doanh nghiệp")

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

        st.subheader("💳 Mục đích và phương án vay")

        danh_sach_muc_dich = [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]

        muc_dich_vay = st.selectbox(
            "Mục đích sử dụng vốn",
            danh_sach_muc_dich,
            index=danh_sach_muc_dich.index(
                st.session_state.muc_dich_vay
            )
        )

        phuong_an = st.text_area(
            "Mô tả phương án sử dụng vốn",
            value=st.session_state.phuong_an,
            placeholder=(
                "Nhập nội dung phương án kinh doanh, "
                "nguồn vốn, doanh thu dự kiến, "
                "hiệu quả sử dụng vốn..."
            )
        )

        if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

            if ten_dn.strip() == "":
                st.error("❌ Vui lòng nhập tên doanh nghiệp.")

            elif ma_so.strip() == "":
                st.error("❌ Vui lòng nhập mã số doanh nghiệp.")

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

    # -----------------------------------------------------
    # TAB 2
    # -----------------------------------------------------

    with tab2:

        st.subheader("⚖️ Kiểm tra điều kiện vay vốn")

        st.info(
            """
            Phần này dùng để kiểm tra sơ bộ các điều kiện
            cần xem xét khi thẩm định khoản vay doanh nghiệp.
            Không phải tất cả tiêu chí đều là điều kiện pháp lý
            độc lập; việc cấp tín dụng còn phụ thuộc quy định
            pháp luật và chính sách của tổ chức tín dụng.
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
                "1. Doanh nghiệp có năng lực pháp lý phù hợp?",
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
                "5. Có khả năng tài chính để trả nợ?",
                options,
                index=options.index(
                    st.session_state.kha_nang_tra_no
                )
            )

            st.session_state.cam_ket_dung_muc_dich = st.selectbox(
                "6. Cam kết sử dụng vốn đúng mục đích?",
                options,
                index=options.index(
                    st.session_state.cam_ket_dung_muc_dich
                )
            )

            st.session_state.cam_ket_tra_no = st.selectbox(
                "7. Cam kết trả nợ đúng hạn?",
                options,
                index=options.index(
                    st.session_state.cam_ket_tra_no
                )
            )

        if st.button("🔍 KIỂM TRA ĐIỀU KIỆN"):

            dieu_kien = [
                st.session_state.nang_luc_phap_ly,
                st.session_state.muc_dich_hop_phap,
                st.session_state.co_phuong_an,
                st.session_state.phuong_an_kha_thi,
                st.session_state.kha_nang_tra_no,
                st.session_state.cam_ket_dung_muc_dich,
                st.session_state.cam_ket_tra_no
            ]

            if "Không" in dieu_kien:
                st.error(
                    "🔴 Có điều kiện đang được đánh giá là Không."
                )

            elif "Chưa đánh giá" in dieu_kien:
                st.warning(
                    "🟡 Chưa thể hoàn tất đánh giá vì còn "
                    "điều kiện chưa được đánh giá."
                )

            else:
                st.success(
                    "🟢 Các điều kiện sơ bộ đang được đánh giá là Có."
                )

    # -----------------------------------------------------
    # TAB 3
    # -----------------------------------------------------

    with tab3:

        st.subheader("📜 Lịch sử tín dụng")

        options_lich_su = [
            "Chưa đánh giá",
            "Tốt",
            "Bình thường",
            "Có dấu hiệu cần xem xét"
        ]

        st.session_state.lich_su_tin_dung = st.selectbox(
            "Đánh giá lịch sử tín dụng",
            options_lich_su,
            index=options_lich_su.index(
                st.session_state.lich_su_tin_dung
            )
        )

        options_no_xau = [
            "Chưa đánh giá",
            "Không có nợ xấu",
            "Có nợ xấu / khoản nợ cần xử lý"
        ]

        st.session_state.no_xau = st.selectbox(
            "Tình trạng nợ xấu",
            options_no_xau,
            index=options_no_xau.index(
                st.session_state.no_xau
            )
        )

        st.info(
            """
            💡 Khi thẩm định thực tế, cần kiểm tra thông tin
            tín dụng của doanh nghiệp và người có liên quan
            theo quy trình của tổ chức tín dụng.
            """
        )


# =========================================================
# 7. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÌNH HÌNH TÀI CHÍNH")

    st.caption("Đơn vị nhập liệu: triệu đồng")

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
            "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
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
            💡 Các chỉ tiêu ROA, ROE và tỷ lệ nợ chỉ mang tính
            chất hỗ trợ phân tích. Cần so sánh với ngành nghề,
            quy mô doanh nghiệp, xu hướng nhiều kỳ và chính sách
            tín dụng của tổ chức tín dụng.
            """
        )


# =========================================================
# 8. KHOẢN VAY & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💳 Khoản vay & trả nợ":

    st.title("💳 KHOẢN VAY VÀ KHẢ NĂNG TRẢ NỢ")

    st.caption("Đơn vị nhập liệu: triệu đồng")

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

        st.subheader("📈 PHÂN TÍCH DSCR")

        if st.button("📊 TÍNH DSCR"):

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

        if st.session_state.dscr is not None:

            st.metric(
                "DSCR",
                f"{st.session_state.dscr:.2f} lần"
            )

            if st.session_state.dscr >= 1.2:

                st.success(
                    "🟢 Khả năng trả nợ tương đối tốt theo chỉ tiêu DSCR."
                )

            elif st.session_state.dscr >= 1:

                st.warning(
                    "🟡 Khả năng trả nợ ở mức cần theo dõi."
                )

            else:

                st.error(
                    "🔴 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                )


# =========================================================
# 9. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title("🏠 TÀI SẢN BẢO ĐẢM")

    st.info(
        """
        Tài sản bảo đảm là một yếu tố hỗ trợ quản trị rủi ro tín dụng.
        Việc cấp tín dụng không nên chỉ dựa vào giá trị tài sản bảo đảm
        mà cần đánh giá khả năng trả nợ và nguồn trả nợ của doanh nghiệp.
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
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
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
                "Khoản vay được ghi nhận là không có TSĐB."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị TSĐB phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Vui lòng nhập số tiền vay."
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
                    "🟢 Tỷ lệ khoản vay trên giá trị TSĐB ở mức tương đối thấp."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm tỷ lệ khấu trừ, chất lượng và khả năng thanh khoản TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 10. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả được tổng hợp từ thông tin hồ sơ, điều kiện vay,
        tình hình tài chính, khả năng trả nợ, lịch sử tín dụng
        và tài sản bảo đảm. Đây là kết quả hỗ trợ thẩm định sơ bộ,
        không phải quyết định cấp tín dụng chính thức.
        """
    )

    # =====================================================
    # KIỂM TRA DỮ LIỆU BẮT BUỘC
    # =====================================================

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
            "⚠️ Chưa đủ dữ liệu để thực hiện kết luận thẩm định."
        )

        st.write("Các nội dung còn thiếu:")

        for item in missing:
            st.write(
                f"• {item}"
            )

        st.stop()

    # =====================================================
    # 1. THÔNG TIN KHÁCH HÀNG
    # =====================================================

    st.subheader("🏢 1. THÔNG TIN KHÁCH HÀNG")

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
    # 2. THÔNG TIN KHOẢN VAY
    # =====================================================

    st.subheader("💳 2. THÔNG TIN KHOẢN VAY")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Số tiền vay",
        f"{st.session_state.so_tien_vay:,.2f} triệu"
    )

    c2.metric(
        "Thời hạn",
        f"{st.session_state.thoi_gian_vay} tháng"
    )

    c3.metric(
        "Lãi suất",
        f"{st.session_state.lai_suat:.2f}%/năm"
    )

    c4.metric(
        "Mục đích",
        st.session_state.muc_dich_vay
    )

    st.divider()

    # =====================================================
    # 3. CHỈ TIÊU TÀI CHÍNH
    # =====================================================

    st.subheader("💰 3. CHỈ TIÊU TÀI CHÍNH")

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
        "Lịch sử tín dụng",
        st.session_state.lich_su_tin_dung
    )

    st.divider()

    # =====================================================
    # 4. TỔNG HỢP ĐIỀU KIỆN
    # =====================================================

    dieu_kien = [
        st.session_state.nang_luc_phap_ly,
        st.session_state.muc_dich_hop_phap,
        st.session_state.co_phuong_an,
        st.session_state.phuong_an_kha_thi,
        st.session_state.kha_nang_tra_no,
        st.session_state.cam_ket_dung_muc_dich,
        st.session_state.cam_ket_tra_no
    ]

    co_dieu_kien_khong = "Không" in dieu_kien
    co_chua_danh_gia = "Chưa đánh giá" in dieu_kien

    # =====================================================
    # 5. XÁC ĐỊNH RỦI RO
    # =====================================================

    ly_do_rui_ro = []
    diem_tich_cuc = 0
    diem_rui_ro = 0

    # Điều kiện vay
    if co_dieu_kien_khong:

        diem_rui_ro += 5

        ly_do_rui_ro.append(
            "Có ít nhất một điều kiện vay vốn cơ bản được đánh giá là Không."
        )

    elif co_chua_danh_gia:

        diem_rui_ro += 2

        ly_do_rui_ro.append(
            "Một số điều kiện vay vốn chưa được đánh giá đầy đủ."
        )

    else:

        diem_tich_cuc += 2

    # LNST
    if st.session_state.lnst > 0:

        diem_tich_cuc += 2

    else:

        diem_rui_ro += 2

        ly_do_rui_ro.append(
            "Lợi nhuận sau thuế không dương."
        )

    # ROA
    if st.session_state.roa > 0:

        diem_tich_cuc += 1

    else:

        diem_rui_ro += 1

        ly_do_rui_ro.append(
            "ROA không dương, hiệu quả sử dụng tài sản cần xem xét."
        )

    # ROE
    if st.session_state.roe > 0:

        diem_tich_cuc += 1

    else:

        diem_rui_ro += 1

        ly_do_rui_ro.append(
            "ROE không dương, hiệu quả sử dụng vốn chủ sở hữu cần xem xét."
        )

    # Tỷ lệ nợ
    if st.session_state.ty_le_no <= 70:

        diem_tich_cuc += 1

    elif st.session_state.ty_le_no > 100:

        diem_rui_ro += 2

        ly_do_rui_ro.append(
            "Tổng nợ phải trả lớn hơn tổng tài sản theo dữ liệu nhập."
        )

    else:

        diem_rui_ro += 1

        ly_do_rui_ro.append(
            "Tỷ lệ nợ ở mức cao, cần đánh giá thêm cơ cấu nợ."
        )

    # DSCR
    if st.session_state.dscr is not None:

        if st.session_state.dscr >= 1.2:

            diem_tich_cuc += 3

        elif st.session_state.dscr >= 1:

            diem_tich_cuc += 1

            ly_do_rui_ro.append(
                "DSCR chỉ ở mức vừa đủ, cần theo dõi khả năng trả nợ."
            )

        else:

            diem_rui_ro += 3

            ly_do_rui_ro.append(
                "DSCR dưới 1, dòng tiền chưa đủ để đáp ứng nghĩa vụ trả nợ."
            )

    # Lịch sử tín dụng
    if st.session_state.no_xau == "Có nợ xấu / khoản nợ cần xử lý":

        diem_rui_ro += 5

        ly_do_rui_ro.append(
            "Có thông tin về nợ xấu hoặc khoản nợ cần xử lý."
        )

    elif st.session_state.no_xau == "Chưa đánh giá":

        diem_rui_ro += 2

        ly_do_rui_ro.append(
            "Chưa hoàn tất đánh giá tình trạng nợ xấu."
        )

    else:

        diem_tich_cuc += 2

    # TSĐB
    if st.session_state.ltv is not None:

        if st.session_state.ltv <= 70:

            diem_tich_cuc += 2

        elif st.session_state.ltv <= 100:

            diem_rui_ro += 1

            ly_do_rui_ro.append(
                "Tỷ lệ LTV tương đối cao, cần xem xét giá trị định giá và khả năng thanh khoản TSĐB."
            )

        else:

            diem_rui_ro += 2

            ly_do_rui_ro.append(
                "Giá trị khoản vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
            )

    else:

        ly_do_rui_ro.append(
            "Khoản vay không có tài sản bảo đảm; cần đánh giá kỹ nguồn trả nợ và các biện pháp bảo đảm khác."
        )

    # =====================================================
    # 6. KẾT LUẬN THẨM ĐỊNH
    # =====================================================

    st.subheader("📌 4. KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

    # Kết luận 1: Không đề xuất
    if co_dieu_kien_khong:

        ket_luan = "🔴 CHƯA ĐỀ XUẤT CẤP TÍN DỤNG Ở GIAI ĐOẠN SƠ BỘ"

        st.markdown(
            f"""
            <div class="status-bad">
                {ket_luan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Hồ sơ đang có điều kiện vay vốn cơ bản được đánh giá
            là Không. Cần làm rõ và khắc phục vấn đề trước khi
            tiếp tục xem xét cấp tín dụng.
            """
        )

    # Kết luận 2: Chưa đủ dữ liệu
    elif co_chua_danh_gia:

        ket_luan = "🟡 CHƯA ĐỦ CƠ SỞ ĐỂ KẾT LUẬN"

        st.markdown(
            f"""
            <div class="status-warning">
                {ket_luan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Hồ sơ chưa hoàn thiện đầy đủ thông tin cần thiết.
            Cần bổ sung đánh giá pháp lý, tín dụng, phương án kinh doanh
            hoặc các nội dung liên quan trước khi đưa ra kết luận.
            """
        )

    # Kết luận 3: Rủi ro cao
    elif diem_rui_ro >= 5:

        ket_luan = "🔴 KHÔNG ĐỀ XUẤT CẤP TÍN DỤNG Ở MỨC SƠ BỘ"

        st.markdown(
            f"""
            <div class="status-bad">
                {ket_luan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Dữ liệu hiện tại cho thấy hồ sơ có một số yếu tố rủi ro
            đáng kể liên quan đến khả năng trả nợ, tình hình tài chính
            hoặc lịch sử tín dụng. Cần thẩm định chuyên sâu trước
            khi xem xét cấp tín dụng.
            """
        )

    # Kết luận 4: Tích cực
    elif (
        diem_tich_cuc >= 8
        and diem_rui_ro <= 2
        and st.session_state.lnst > 0
        and st.session_state.dscr is not None
        and st.session_state.dscr >= 1
    ):

        ket_luan = "🟢 ĐỀ XUẤT XEM XÉT CẤP TÍN DỤNG"

        st.markdown(
            f"""
            <div class="status-good">
                {ket_luan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Hồ sơ có các yếu tố tích cực về điều kiện vay,
            tình hình tài chính và khả năng trả nợ theo dữ liệu nhập.
            Có thể chuyển sang bước thẩm định tín dụng chi tiết,
            phê duyệt theo thẩm quyền và chính sách của tổ chức tín dụng.
            """
        )

    # Kết luận 5
    else:

        ket_luan = "🟡 CẦN THẨM ĐỊNH BỔ SUNG TRƯỚC KHI QUYẾT ĐỊNH"

        st.markdown(
            f"""
            <div class="status-warning">
                {ket_luan}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Hồ sơ chưa có đủ cơ sở để đề xuất cấp tín dụng ngay.
            Cần phân tích sâu hơn về phương án kinh doanh, dòng tiền,
            cơ cấu nợ, lịch sử tín dụng, tài sản bảo đảm và các yếu tố
            rủi ro khác trước khi quyết định.
            """
        )

    st.divider()

    # =====================================================
    # 7. LÝ DO VÀ KIẾN NGHỊ
    # =====================================================

    st.subheader("🔎 5. CÁC YẾU TỐ CẦN LƯU Ý")

    if len(ly_do_rui_ro) == 0:

        st.success(
            "✅ Chưa ghi nhận yếu tố rủi ro nổi bật từ các dữ liệu đã nhập."
        )

    else:

        for ly_do in ly_do_rui_ro:

            st.warning(
                f"⚠️ {ly_do}"
            )

    st.divider()

    # =====================================================
    # 8. BẢNG TỔNG HỢP
    # =====================================================

    st.subheader("📋 6. BẢNG TỔNG HỢP THẨM ĐỊNH")

    ket_qua = []

    # Hồ sơ
    ket_qua.append(
        [
            "Hồ sơ doanh nghiệp",
            "Đạt" if st.session_state.da_luu_ho_so else "Chưa đạt",
            st.session_state.ten_dn
        ]
    )

    # Pháp lý
    ket_qua.append(
        [
            "Năng lực pháp lý",
            st.session_state.nang_luc_phap_ly,
            "Cần kiểm tra hồ sơ pháp lý thực tế"
        ]
    )

    # Mục đích
    ket_qua.append(
        [
            "Mục đích vay",
            st.session_state.muc_dich_hop_phap,
            st.session_state.muc_dich_vay
        ]
    )

    # Phương án
    ket_qua.append(
        [
            "Phương án sử dụng vốn",
            st.session_state.co_phuong_an,
            "Có phương án" if st.session_state.phuong_an else "Chưa có mô tả"
        ]
    )

    # Tính khả thi
    ket_qua.append(
        [
            "Tính khả thi phương án",
            st.session_state.phuong_an_kha_thi,
            "Cần thẩm định phương án kinh doanh"
        ]
    )

    # Khả năng trả nợ
    ket_qua.append(
        [
            "Khả năng trả nợ",
            st.session_state.kha_nang_tra_no,
            (
                f"DSCR: {st.session_state.dscr:.2f} lần"
                if st.session_state.dscr is not None
                else "Chưa tính DSCR"
            )
        ]
    )

    # LNST
    ket_qua.append(
        [
            "Lợi nhuận sau thuế",
            "Tích cực" if st.session_state.lnst > 0 else "Cần xem xét",
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ]
    )

    # ROA
    ket_qua.append(
        [
            "ROA",
            "Tích cực" if st.session_state.roa > 0 else "Cần xem xét",
            f"{st.session_state.roa:.2f}%"
        ]
    )

    # ROE
    ket_qua.append(
        [
            "ROE",
            "Tích cực" if st.session_state.roe > 0 else "Cần xem xét",
            f"{st.session_state.roe:.2f}%"
        ]
    )

    # Tỷ lệ nợ
    ket_qua.append(
        [
            "Tỷ lệ nợ",
            (
                "Tương đối an toàn"
                if st.session_state.ty_le_no <= 70
                else "Cần xem xét"
            ),
            f"{st.session_state.ty_le_no:.2f}%"
        ]
    )

    # DSCR
    ket_qua.append(
        [
            "DSCR",
            (
                "Tích cực"
                if st.session_state.dscr is not None
                and st.session_state.dscr >= 1.2
                else "Cần xem xét"
            ),
            (
                f"{st.session_state.dscr:.2f} lần"
                if st.session_state.dscr is not None
                else "Chưa tính"
            )
        ]
    )

    # Lịch sử tín dụng
    ket_qua.append(
        [
            "Lịch sử tín dụng",
            st.session_state.lich_su_tin_dung,
            st.session_state.no_xau
        ]
    )

    # TSĐB
    ket_qua.append(
        [
            "Tài sản bảo đảm",
            st.session_state.co_tsdb,
            (
                f"LTV: {st.session_state.ltv:.2f}%"
                if st.session_state.ltv is not None
                else "Không áp dụng"
            )
        ]
    )

    df = pd.DataFrame(
        ket_qua,
        columns=[
            "Nội dung thẩm định",
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

    # =====================================================
    # 9. KIẾN NGHỊ
    # =====================================================

    st.subheader("📝 7. KIẾN NGHỊ THẨM ĐỊNH")

    if ket_luan.startswith("🟢"):

        st.success(
            """
            Có thể xem xét chuyển hồ sơ sang bước thẩm định chi tiết.
            Cần tiếp tục kiểm tra hồ sơ pháp lý, báo cáo tài chính,
            phương án kinh doanh, lịch sử tín dụng, dòng tiền thực tế,
            mục đích sử dụng vốn và hồ sơ tài sản bảo đảm trước khi
            phê duyệt khoản vay.
            """
        )

    elif ket_luan.startswith("🟡"):

        st.warning(
            """
            Cần bổ sung và làm rõ các thông tin còn thiếu.
            Đặc biệt cần kiểm tra khả năng trả nợ thực tế,
            dòng tiền, lịch sử tín dụng, phương án kinh doanh
            và các yếu tố rủi ro trước khi đưa ra quyết định.
            """
        )

    else:

        st.error(
            """
            Chưa nên đề xuất cấp tín dụng ở giai đoạn sơ bộ.
            Cần xác định rõ nguyên nhân rủi ro và chỉ xem xét lại
            sau khi doanh nghiệp khắc phục hoặc bổ sung đầy đủ
            hồ sơ và thông tin cần thiết.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ LƯU Ý NGHIỆP VỤ

        Kết quả trên chỉ là công cụ hỗ trợ thẩm định sơ bộ.
        ROA, ROE, LNST, tỷ lệ nợ, DSCR và LTV không phải là
        những chỉ tiêu có thể sử dụng độc lập để quyết định
        doanh nghiệp chắc chắn được vay vốn.

        Quyết định cấp tín dụng thực tế cần căn cứ vào:
        hồ sơ pháp lý; mục đích vay vốn; phương án sử dụng vốn;
        năng lực tài chính; dòng tiền và nguồn trả nợ;
        lịch sử tín dụng; tài sản bảo đảm; khả năng quản trị;
        tình hình ngành nghề; tình hình thị trường; quy định
        pháp luật và chính sách tín dụng của tổ chức tín dụng.
        """
    )


# =========================================================
# 11. FOOTER
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
