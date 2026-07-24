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

    # KẾT QUẢ TÀI CHÍNH
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

    # TSĐB
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
# 3. CSS GIAO DIỆN
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

    /* TIÊU ĐỀ */
    h1 {
        color: #082b4c !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0b416d !important;
        font-weight: 750 !important;
    }

    h3 {
        color: #125d8e !important;
        font-weight: 700 !important;
    }

    /* METRIC */
    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #d7e5f2;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(8,43,76,0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3d66 !important;
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
            #07518a,
            #1185c4
        );
        box-shadow: 0 5px 15px rgba(7,81,138,0.2);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* CARD */
    .hero-card {
        background: linear-gradient(
            135deg,
            #062b4d,
            #0b5c8d,
            #1292c5
        );
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 12px 30px rgba(6,43,77,0.2);
    }

    .hero-card h1 {
        color: white !important;
        font-size: 30px;
        margin-bottom: 10px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        margin: 0;
    }

    .section-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #dce8f3;
        box-shadow: 0 5px 18px rgba(8,43,76,0.06);
        margin-bottom: 20px;
    }

    .status-good {
        background: #e8f8ef;
        border-left: 6px solid #1c9b58;
        padding: 18px;
        border-radius: 12px;
        color: #17663b;
        font-weight: 700;
        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 6px solid #e0a000;
        padding: 18px;
        border-radius: 12px;
        color: #765800;
        font-weight: 700;
        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 6px solid #d43d3d;
        padding: 18px;
        border-radius: 12px;
        color: #852323;
        font-weight: 700;
        font-size: 18px;
    }

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
    except Exception:
        st.markdown(
            "<div style='text-align:center;font-size:60px;'>🏦</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:20px;
            font-weight:800;
            line-height:1.4;
            margin-top:10px;
        ">
            THẨM ĐỊNH<br>
            CHO VAY DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "<div style='font-size:16px;font-weight:800;'>📋 DANH MỤC THẨM ĐỊNH</div>",
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
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

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
        Hệ thống hỗ trợ cán bộ hoặc người sử dụng thực hiện
        thẩm định sơ bộ hồ sơ vay vốn của doanh nghiệp.
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
            if st.session_state.nang_luc_phap_ly != "Chưa đánh giá"
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
            "📊 Kết quả",
            "Sẵn sàng"
            if (
                st.session_state.da_luu_ho_so
                and st.session_state.da_phan_tich_tc
                and st.session_state.da_phan_tich_vay
            )
            else "Chưa đủ dữ liệu"
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

            Tổng hợp dữ liệu và đưa ra
            kết luận thẩm định sơ bộ.
            """
        )

    st.warning(
        """
        ⚠️ Lưu ý: Kết quả của hệ thống chỉ mang tính chất
        hỗ trợ thẩm định sơ bộ và không thay thế quyết định
        tín dụng chính thức của ngân hàng.
        """
    )


# =========================================================
# 6. HỒ SƠ & ĐIỀU KIỆN VAY
# GOM CẢ TSĐB VÀO ĐÂY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện vay":

    st.title("🏢 HỒ SƠ & ĐIỀU KIỆN VAY")

    # -----------------------------------------------------
    # A. THÔNG TIN DOANH NGHIỆP
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
        placeholder="Nhập nội dung phương án kinh doanh, nhu cầu vay và cách sử dụng vốn..."
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

    # -----------------------------------------------------
    # B. ĐIỀU KIỆN VAY VỐN
    # -----------------------------------------------------

    st.subheader("3️⃣ Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Đây là phần kiểm tra sơ bộ các điều kiện vay vốn.
        Việc đánh giá thực tế phải căn cứ hồ sơ pháp lý,
        mục đích vay, phương án sử dụng vốn, khả năng trả nợ
        và quy định nội bộ của tổ chức tín dụng.
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

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

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

            st.error(
                "🔴 Có ít nhất một điều kiện đang được đánh giá là Không."
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
    # C. TÀI SẢN BẢO ĐẢM
    # -----------------------------------------------------

    st.subheader("4️⃣ Tài sản bảo đảm")

    st.info(
        """
        Tài sản bảo đảm là một nội dung hỗ trợ trong thẩm định.
        Ngân hàng cần xem xét loại tài sản, quyền sở hữu,
        giá trị định giá, khả năng thanh khoản và tỷ lệ cho vay
        trên giá trị tài sản theo chính sách nội bộ.
        """
    )

    st.session_state.co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        options,
        index=options.index(
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
                "❌ Vui lòng nhập số tiền vay ở phần Tài chính & Khả năng trả nợ trước."
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
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm theo dữ liệu nhập."
                )


# =========================================================
# 7. TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "💰 Tài chính & Khả năng trả nợ":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ")

    st.caption(
        "Đơn vị nhập liệu tài chính và khoản vay: triệu đồng"
    )

    # -----------------------------------------------------
    # A. PHÂN TÍCH TÀI CHÍNH
    # -----------------------------------------------------

    st.subheader("1️⃣ Phân tích tài chính doanh nghiệp")

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

        st.subheader("📈 KẾT QUẢ TÀI CHÍNH")

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

    # -----------------------------------------------------
    # B. THÔNG TIN KHOẢN VAY
    # -----------------------------------------------------

    st.subheader("2️⃣ Thông tin khoản vay")

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

    # -----------------------------------------------------
    # C. DSCR
    # -----------------------------------------------------

    st.subheader("3️⃣ Khả năng trả nợ")

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng nhập và tính khoản vay trước."
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

                st.divider()

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


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

    st.info(
        """
        Kết quả được tổng hợp từ thông tin hồ sơ, điều kiện vay,
        tình hình tài chính, khả năng trả nợ và tài sản bảo đảm.
        Đây là kết quả hỗ trợ thẩm định sơ bộ.
        """
    )

    # -----------------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # -----------------------------------------------------

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
            "⚠️ Chưa đủ dữ liệu để đưa ra kết luận thẩm định."
        )

        st.write(
            "Vui lòng hoàn thành các nội dung sau:"
        )

        for item in missing:
            st.write(
                f"🔸 {item}"
            )

        st.stop()

    # -----------------------------------------------------
    # KIỂM TRA ĐIỀU KIỆN
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # THÔNG TIN DOANH NGHIỆP
    # -----------------------------------------------------

    st.subheader("🏢 THÔNG TIN DOANH NGHIỆP")

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

    # -----------------------------------------------------
    # CÁC CHỈ TIÊU CHÍNH
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # KẾT LUẬN
    # -----------------------------------------------------

    st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")

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
            Hồ sơ đang có ít nhất một điều kiện vay vốn được đánh giá
            là Không. Cần xác định rõ nguyên nhân, bổ sung hồ sơ hoặc
            điều chỉnh phương án trước khi xem xét tiếp.
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
            đồng thời dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ theo
            chỉ tiêu DSCR.

            Hồ sơ có thể được chuyển sang bước thẩm định chi tiết,
            bao gồm kiểm tra hồ sơ pháp lý, CIC, lịch sử tín dụng,
            báo cáo tài chính, phương án kinh doanh, dòng tiền,
            tài sản bảo đảm và các quy định nội bộ của ngân hàng.
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

    # -----------------------------------------------------
    # BẢNG TỔNG HỢP
    # -----------------------------------------------------

    st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

    ket_qua = []

    # Điều kiện pháp lý
    ket_qua.append([
        "Năng lực pháp lý",
        "Đạt" if st.session_state.nang_luc_phap_ly == "Có"
        else "Cần xem xét",
        st.session_state.nang_luc_phap_ly
    ])

    # Mục đích vay
    ket_qua.append([
        "Mục đích vay vốn",
        "Đạt" if st.session_state.muc_dich_hop_phap == "Có"
        else "Cần xem xét",
        st.session_state.muc_dich_hop_phap
    ])

    # Phương án sử dụng vốn
    ket_qua.append([
        "Phương án sử dụng vốn",
        "Đạt" if st.session_state.phuong_an_su_dung_von == "Có"
        else "Cần xem xét",
        st.session_state.phuong_an_su_dung_von
    ])

    # Tính khả thi
    ket_qua.append([
        "Tính khả thi phương án",
        "Đạt" if st.session_state.phuong_an_kha_thi == "Có"
        else "Cần xem xét",
        st.session_state.phuong_an_kha_thi
    ])

    # Khả năng trả nợ
    ket_qua.append([
        "Khả năng tài chính trả nợ",
        "Đạt" if st.session_state.kha_nang_tra_no == "Có"
        else "Cần xem xét",
        st.session_state.kha_nang_tra_no
    ])

    # LNST
    ket_qua.append([
        "Lợi nhuận sau thuế",
        "Tích cực" if st.session_state.lnst > 0
        else "Cần xem xét",
        f"{st.session_state.lnst:,.2f} triệu đồng"
    ])

    # ROA
    ket_qua.append([
        "ROA",
        "Tích cực" if st.session_state.roa > 0
        else "Cần xem xét",
        f"{st.session_state.roa:.2f}%"
    ])

    # ROE
    ket_qua.append([
        "ROE",
        "Tích cực" if st.session_state.roe > 0
        else "Cần xem xét",
        f"{st.session_state.roe:.2f}%"
    ])

    # Tỷ lệ nợ
    ket_qua.append([
        "Tỷ lệ nợ",
        "Tham khảo",
        f"{st.session_state.ty_le_no:.2f}%"
    ])

    # DSCR
    if st.session_state.dscr is not None:

        ket_qua.append([
            "DSCR",
            "Tích cực"
            if st.session_state.dscr >= 1
            else "Cần xem xét",
            f"{st.session_state.dscr:.2f} lần"
        ])

    # LTV
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
