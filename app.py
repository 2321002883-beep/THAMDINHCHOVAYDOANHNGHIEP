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

    # -------------------------
    # HỒ SƠ DOANH NGHIỆP
    # -------------------------
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # -------------------------
    # ĐIỀU KIỆN VAY VỐN
    # -------------------------
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "co_phuong_an": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # -------------------------
    # TÀI CHÍNH
    # Đơn vị: triệu đồng
    # -------------------------
    "doanh_thu": 0.0,
    "lnst": 0.0,
    "tong_tai_san": 0.0,
    "von_chu_so_huu": 0.0,
    "no_phai_tra": 0.0,
    "dong_tien": 0.0,

    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # -------------------------
    # KHOẢN VAY
    # -------------------------
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,

    # -------------------------
    # KHẢ NĂNG TRẢ NỢ
    # -------------------------
    "dscr": None,

    # -------------------------
    # TÀI SẢN BẢO ĐẢM
    # -------------------------
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # -------------------------
    # TRẠNG THÁI
    # -------------------------
    "da_luu_ho_so": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_dscr": False,
    "da_phan_tich_tsdb": False,
}


for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# 3. HÀM XÓA DỮ LIỆU
# =========================================================

def reset_data():

    for key, value in default_values.items():
        st.session_state[key] = value

    st.success("✅ Đã xóa dữ liệu và sẵn sàng nhập hồ sơ mới.")


# =========================================================
# 4. CSS - GIAO DIỆN
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       NỀN ỨNG DỤNG
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
        box-shadow: 0 8px 24px rgba(13,59,102,0.08);
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
        box-shadow: 0 5px 15px rgba(11,79,138,0.22);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(11,79,138,0.3);
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
        box-shadow: 0 15px 35px rgba(8,38,74,0.22);
        margin-bottom: 25px;
    }

    .hero-card h1 {
        color: white !important;
        font-size: 32px;
        margin-bottom: 8px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.9);
        font-size: 16px;
        margin-bottom: 0;
    }


    /* =========================
       CARD
    ========================= */

    .section-card {
        background: rgba(255,255,255,0.95);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #dce7f2;
        box-shadow: 0 6px 20px rgba(13,59,102,0.06);
        margin-bottom: 18px;
    }


    /* =========================
       TRẠNG THÁI
    ========================= */

    .status-good {
        background: #e9f8ef;
        border-left: 5px solid #1e9e58;
        padding: 18px;
        border-radius: 12px;
        color: #176b3c;
        font-weight: 700;
        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;
        border-left: 5px solid #e4a400;
        padding: 18px;
        border-radius: 12px;
        color: #805f00;
        font-weight: 700;
        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 5px solid #d64545;
        padding: 18px;
        border-radius: 12px;
        color: #8c2525;
        font-weight: 700;
        font-size: 18px;
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
# 5. SIDEBAR - MENU RÚT GỌN
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:10px 5px 20px 5px;">

            <div style="font-size:42px;">
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

    menu = st.radio(
        "📌 DANH MỤC",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & Điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & Tài sản",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption(
        "Phiên bản hỗ trợ thẩm định sơ bộ"
    )

    st.divider()

    if st.button("🗑️ XÓA DỮ LIỆU"):

        reset_data()


# =========================================================
# 6. TỔNG QUAN
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
            "🏠 Tài sản",
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
            và kiểm tra điều kiện vay vốn.
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

            Tổng hợp dữ liệu và
            đưa ra kết luận sơ bộ.
            """
        )

    st.divider()

    st.warning(
        """
        ⚠️ Lưu ý: Ứng dụng chỉ mang tính chất hỗ trợ
        thẩm định sơ bộ. Kết quả không thay thế quyết định
        tín dụng chính thức của tổ chức tín dụng.
        """
    )


# =========================================================
# 7. HỒ SƠ & ĐIỀU KIỆN VAY
# =========================================================

elif menu == "🏢 Hồ sơ & Điều kiện":

    st.title("🏢 HỒ SƠ DOANH NGHIỆP & ĐIỀU KIỆN VAY")

    # =====================================================
    # HỒ SƠ
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
            value=st.session_state.thoi_gian_hd
        )

        muc_dich_vay = st.selectbox(
            "Mục đích sử dụng vốn",
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
            ].index(
                st.session_state.muc_dich_vay
            )
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

    # =====================================================
    # ĐIỀU KIỆN VAY
    # =====================================================

    st.subheader("⚖️ 2. Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Các tiêu chí dưới đây dùng để kiểm tra sơ bộ.
        Kết quả thực tế còn phụ thuộc hồ sơ pháp lý,
        quy định pháp luật và chính sách tín dụng của
        từng tổ chức tín dụng.
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
            "2. Mục đích vay vốn có hợp pháp?",
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
            "4. Phương án sử dụng vốn có khả thi?",
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

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN VAY"):

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
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.title("💰 PHÂN TÍCH TÀI CHÍNH")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        doanh_thu = st.number_input(
            "💵 Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )

        lnst = st.number_input(
            "📈 Lợi nhuận sau thuế (LNST)",
            value=st.session_state.lnst
        )

        tong_tai_san = st.number_input(
            "🏢 Tổng tài sản",
            min_value=0.0,
            value=st.session_state.tong_tai_san
        )

    with c2:

        von_chu_so_huu = st.number_input(
            "💼 Vốn chủ sở hữu",
            min_value=0.0,
            value=st.session_state.von_chu_so_huu
        )

        no_phai_tra = st.number_input(
            "📌 Nợ phải trả",
            min_value=0.0,
            value=st.session_state.no_phai_tra
        )

        dong_tien = st.number_input(
            "💧 Dòng tiền từ hoạt động kinh doanh/tháng",
            value=st.session_state.dong_tien
        )

    if st.button("📊 PHÂN TÍCH TÀI CHÍNH"):

        st.session_state.doanh_thu = doanh_thu
        st.session_state.lnst = lnst
        st.session_state.tong_tai_san = tong_tai_san
        st.session_state.von_chu_so_huu = von_chu_so_huu
        st.session_state.no_phai_tra = no_phai_tra
        st.session_state.dong_tien = dong_tien

        if tong_tai_san <= 0:

            st.error(
                "❌ Tổng tài sản phải lớn hơn 0."
            )

        elif von_chu_so_huu <= 0:

            st.error(
                "❌ Vốn chủ sở hữu phải lớn hơn 0."
            )

        elif no_phai_tra > tong_tai_san:

            st.error(
                "❌ Nợ phải trả không được lớn hơn tổng tài sản."
            )

        else:

            st.session_state.roa = (
                lnst / tong_tai_san * 100
            )

            st.session_state.roe = (
                lnst / von_chu_so_huu * 100
            )

            st.session_state.ty_le_no = (
                no_phai_tra / tong_tai_san * 100
            )

            st.session_state.da_phan_tich_tc = True

            st.success(
                "✅ Phân tích tài chính thành công."
            )

    if st.session_state.roa is not None:

        st.divider()

        st.subheader("📈 KẾT QUẢ PHÂN TÍCH")

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
            💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu hỗ trợ phân tích
            tài chính. Không nên sử dụng riêng lẻ các chỉ tiêu này
            để kết luận doanh nghiệp được vay vốn.
            """
        )


# =========================================================
# 9. KHOẢN VAY & TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "💳 Khoản vay & Tài sản":

    st.title("💳 KHOẢN VAY & TÀI SẢN BẢO ĐẢM")

    # =====================================================
    # KHOẢN VAY
    # =====================================================

    st.subheader("💳 1. Thông tin khoản vay")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        so_tien_vay = st.number_input(
            "💰 Số tiền vay",
            min_value=0.0,
            value=st.session_state.so_tien_vay
        )

        thoi_gian_vay = st.number_input(
            "📅 Thời hạn vay (tháng)",
            min_value=1,
            value=st.session_state.thoi_gian_vay
        )

    with c2:

        lai_suat = st.number_input(
            "📈 Lãi suất (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )

        nghia_vu_no_cu = st.number_input(
            "💳 Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0,
            value=st.session_state.nghia_vu_no_cu
        )

    if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

        st.session_state.so_tien_vay = so_tien_vay
        st.session_state.thoi_gian_vay = thoi_gian_vay
        st.session_state.lai_suat = lai_suat
        st.session_state.nghia_vu_no_cu = nghia_vu_no_cu

        if so_tien_vay <= 0:

            st.error(
                "❌ Số tiền vay phải lớn hơn 0."
            )

        else:

            tien_goc = (
                so_tien_vay / thoi_gian_vay
            )

            tien_lai = (
                so_tien_vay
                * lai_suat
                / 100
                / 12
            )

            tong_nghia_vu = (
                nghia_vu_no_cu
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
    # KHẢ NĂNG TRẢ NỢ
    # =====================================================

    st.subheader("📈 2. Khả năng trả nợ")

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
                        "🟢 Dòng tiền hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."
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

    co_tsdb = st.selectbox(
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

    st.session_state.co_tsdb = co_tsdb

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm (triệu đồng)",
        min_value=0.0,
        value=st.session_state.gia_tri_tsdb
    )

    st.session_state.gia_tri_tsdb = gia_tri_tsdb

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có TSĐB hay không."
            )

        elif co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được đánh giá là không có tài sản bảo đảm."
            )

        elif gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif so_tien_vay <= 0:

            st.error(
                "❌ Vui lòng nhập số tiền vay trước."
            )

        else:

            st.session_state.ltv = (
                so_tien_vay
                / gia_tri_tsdb
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
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 10. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả dưới đây được tổng hợp từ dữ liệu đã nhập.
        Đây là công cụ hỗ trợ thẩm định sơ bộ và không thay thế
        quyết định tín dụng chính thức của tổ chức tín dụng.
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

    # =====================================================
    # CHƯA ĐỦ DỮ LIỆU
    # =====================================================

    if len(missing) > 0:

        st.warning(
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN"
        )

        st.write(
            "Vui lòng hoàn thiện các nội dung sau:"
        )

        for item in missing:

            st.write(
                f"• {item}"
            )

        st.stop()


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

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
    # CHỈ TIÊU TÀI CHÍNH
    # =====================================================

    st.subheader("📊 CÁC CHỈ TIÊU CHÍNH")

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
    # KIỂM TRA ĐIỀU KIỆN VAY
    # =====================================================

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


    # =====================================================
    # ĐÁNH GIÁ TÀI CHÍNH
    # =====================================================

    tai_chinh_tich_cuc = (

        st.session_state.lnst > 0

        and st.session_state.roa > 0

        and st.session_state.roe > 0

    )


    # =====================================================
    # ĐÁNH GIÁ DSCR
    # =====================================================

    dscr_dat = (

        st.session_state.dscr is not None

        and st.session_state.dscr >= 1

    )


    # =====================================================
    # ĐÁNH GIÁ LTV
    # =====================================================

    if st.session_state.ltv is None:

        ltv_dat = True

    else:

        ltv_dat = (
            st.session_state.ltv <= 70
        )


    # =====================================================
    # KẾT LUẬN
    # =====================================================

    st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")


    # -----------------------------------------------------
    # TRƯỜNG HỢP 1
    # CÓ ĐIỀU KIỆN KHÔNG ĐẠT
    # -----------------------------------------------------

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
            Hồ sơ có ít nhất một điều kiện vay vốn đang được
            đánh giá là Không. Do đó, hồ sơ chưa đáp ứng điều kiện
            sơ bộ để tiếp tục xem xét theo mô hình hỗ trợ.
            """
        )


    # -----------------------------------------------------
    # TRƯỜNG HỢP 2
    # CHƯA ĐÁNH GIÁ ĐỦ
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # TRƯỜNG HỢP 3
    # ĐẠT CÁC TIÊU CHÍ HỖ TRỢ
    # -----------------------------------------------------

    elif (

        tai_chinh_tich_cuc

        and dscr_dat

        and ltv_dat

    ):

        st.markdown(
            """
            <div class="status-good">
                🟢 ĐẠT CÁC TIÊU CHÍ HỖ TRỢ THẨM ĐỊNH SƠ BỘ
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Hồ sơ đang đáp ứng các điều kiện vay vốn được đánh giá
            là Có. Các chỉ tiêu tài chính, khả năng trả nợ và tài sản
            bảo đảm cũng đang cho tín hiệu tích cực theo dữ liệu nhập.

            Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
            chi tiết theo quy trình và chính sách của tổ chức tín dụng.
            """
        )


    # -----------------------------------------------------
    # TRƯỜNG HỢP 4
    # CẦN THẨM ĐỊNH BỔ SUNG
    # -----------------------------------------------------

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
            Hồ sơ chưa đáp ứng đầy đủ các tiêu chí hỗ trợ của mô hình.
            Cần xem xét bổ sung về tình hình tài chính, dòng tiền,
            khả năng trả nợ, phương án kinh doanh, lịch sử tín dụng,
            tài sản bảo đảm và các yếu tố liên quan.
            """
        )


    st.divider()


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

    ket_qua = []


    # -------------------------
    # ĐIỀU KIỆN VAY
    # -------------------------

    dieu_kien_list = [

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


    for ten, ket_qua_danh_gia in dieu_kien_list:

        if ket_qua_danh_gia == "Có":

            ket_qua.append(
                [
                    ten,
                    "Đạt",
                    "Đang được đánh giá là Có"
                ]
            )

        elif ket_qua_danh_gia == "Không":

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
                    "Chưa có dữ liệu"
                ]
            )


    # -------------------------
    # LNST
    # -------------------------

    if st.session_state.lnst > 0:

        ket_qua.append(
            [
                "LNST",
                "Tích cực",
                f"{st.session_state.lnst:,.2f} triệu đồng"
            ]
        )

    else:

        ket_qua.append(
            [
                "LNST",
                "Cần xem xét",
                "LNST không dương"
            ]
        )


    # -------------------------
    # ROA
    # -------------------------

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


    # -------------------------
    # ROE
    # -------------------------

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


    # -------------------------
    # TỶ LỆ NỢ
    # -------------------------

    if st.session_state.ty_le_no <= 70:

        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Tham khảo",
                f"{st.session_state.ty_le_no:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "Tỷ lệ nợ",
                "Cần xem xét",
                f"{st.session_state.ty_le_no:.2f}%"
            ]
        )


    # -------------------------
    # DSCR
    # -------------------------

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


    # -------------------------
    # LTV
    # -------------------------

    if st.session_state.ltv is None:

        ket_qua.append(
            [
                "Tài sản bảo đảm",
                "Không áp dụng",
                "Khoản vay không có TSĐB"
            ]
        )

    elif st.session_state.ltv <= 70:

        ket_qua.append(
            [
                "LTV",
                "Tích cực",
                f"{st.session_state.ltv:.2f}%"
            ]
        )

    else:

        ket_qua.append(
            [
                "LTV",
                "Cần xem xét",
                f"{st.session_state.ltv:.2f}%"
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


    # =====================================================
    # LƯU Ý
    # =====================================================

    st.warning(
        """
        ⚠️ LƯU Ý QUAN TRỌNG

        Kết quả "Đạt các tiêu chí hỗ trợ thẩm định sơ bộ" không có
        nghĩa là doanh nghiệp chắc chắn được ngân hàng phê duyệt khoản vay.

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ chỉ là các chỉ tiêu
        hỗ trợ phân tích. Quyết định cho vay thực tế còn phụ thuộc vào:

        • Hồ sơ pháp lý của doanh nghiệp.
        • Mục đích sử dụng vốn.
        • Phương án kinh doanh.
        • Năng lực tài chính.
        • Dòng tiền và khả năng trả nợ.
        • Lịch sử tín dụng.
        • Tài sản bảo đảm.
        • Kết quả thẩm định thực tế.
        • Chính sách tín dụng của từng tổ chức tín dụng.
        """
    )


# =========================================================
# 11. FOOTER
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

        ⚠️ Kết quả chỉ mang tính chất tham khảo
        và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
