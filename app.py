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
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 3,
    "muc_dich_vay": "",
    "phuong_an": "",

    # Điều kiện vay vốn
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich": "Chưa đánh giá",
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
    "da_phan_tich_dscr": False,
    "da_phan_tich_tsdb": False,
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

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f5f8fc 0%,
                #eef4fb 50%,
                #f8fafc 100%
            );
    }

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

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.95);
        border: 1px solid #d9e4f0;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(13,59,102,0.08);
    }

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
    }

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

    .status-good {
        background: #e9f8ef;
        border-left: 5px solid #1e9e58;
        padding: 15px;
        border-radius: 12px;
        color: #176b3c;
        font-weight: 700;
    }

    .status-warning {
        background: #fff7df;
        border-left: 5px solid #e4a400;
        padding: 15px;
        border-radius: 12px;
        color: #805f00;
        font-weight: 700;
    }

    .status-bad {
        background: #fff0f0;
        border-left: 5px solid #d64545;
        padding: 15px;
        border-radius: 12px;
        color: #8c2525;
        font-weight: 700;
    }

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
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">
            <div style="font-size:42px;">🏦</div>

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
        "📌 DANH MỤC CHỨC NĂNG",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "📈 Khả năng trả nợ",
            "🏠 Tài sản bảo đảm",
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

    st.subheader("📊 TỔNG QUAN HỒ SƠ")

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
            "💰 Phân tích tài chính",
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
            "🏠 Tài sản bảo đảm",
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

            Nhập thông tin doanh nghiệp,
            ngành nghề và mục đích vay.
            """
        )

    with c2:
        st.info(
            """
            **02 | TÀI CHÍNH**

            Phân tích doanh thu,
            LNST, ROA, ROE và tỷ lệ nợ.
            """
        )

    with c3:
        st.info(
            """
            **03 | TRẢ NỢ**

            Phân tích dòng tiền,
            nghĩa vụ trả nợ và DSCR.
            """
        )

    with c4:
        st.info(
            """
            **04 | KẾT QUẢ**

            Tổng hợp điều kiện,
            chỉ tiêu và kết luận sơ bộ.
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
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.title("🏢 HỒ SƠ DOANH NGHIỆP")

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

        ds_nganh = [
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
            ds_nganh,
            index=ds_nganh.index(
                st.session_state.nganh_nghe
            )
        )

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

    st.subheader("💳 Mục đích vay vốn")

    ds_muc_dich = [
        "Bổ sung vốn lưu động",
        "Mua nguyên vật liệu",
        "Đầu tư máy móc thiết bị",
        "Mở rộng sản xuất",
        "Mua tài sản cố định",
        "Khác"
    ]

    muc_dich_vay = st.selectbox(
        "Mục đích sử dụng vốn",
        ds_muc_dich,
        index=(
            ds_muc_dich.index(
                st.session_state.muc_dich_vay
            )
            if st.session_state.muc_dich_vay in ds_muc_dich
            else 0
        )
    )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder=(
            "Nhập mô tả chi tiết phương án kinh doanh "
            "và nhu cầu sử dụng vốn..."
        )
    )

    if st.button("💾 LƯU HỒ SƠ DOANH NGHIỆP"):

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
                "✅ Đã lưu thông tin hồ sơ doanh nghiệp."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.title("⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN")

    st.info(
        """
        Phần này kiểm tra sơ bộ các điều kiện vay vốn
        theo quy định pháp luật và thông tin hồ sơ.

        Các chỉ tiêu ROA, ROE, DSCR, LTV được sử dụng
        ở phần phân tích tín dụng để hỗ trợ đánh giá,
        không phải là điều kiện pháp lý bắt buộc riêng biệt.
        """
    )

    st.subheader("1️⃣ Điều kiện cơ bản")

    c1, c2 = st.columns(2)

    options = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "Doanh nghiệp có năng lực pháp luật dân sự, năng lực hành vi phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich = st.selectbox(
            "Mục đích vay vốn có hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich
            )
        )

        st.session_state.co_phuong_an = st.selectbox(
            "Có phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.co_phuong_an
            )
        )

    with c2:

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "Phương án sử dụng vốn có hiệu quả và khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )

        st.session_state.kha_nang_tra_no = st.selectbox(
            "Khách hàng có khả năng tài chính để trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )

    st.subheader("2️⃣ Cam kết của khách hàng")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.dung_muc_dich = st.selectbox(
            "Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.dung_muc_dich
            )
        )

    with c2:

        st.session_state.tra_no_dung_han = st.selectbox(
            "Cam kết hoàn trả nợ gốc và lãi đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )

    st.divider()

    if st.button("🔍 KIỂM TRA ĐIỀU KIỆN"):

        dieu_kien = [
            st.session_state.nang_luc_phap_ly,
            st.session_state.muc_dich,
            st.session_state.co_phuong_an,
            st.session_state.phuong_an_kha_thi,
            st.session_state.kha_nang_tra_no,
            st.session_state.dung_muc_dich,
            st.session_state.tra_no_dung_han
        ]

        so_dat = dieu_kien.count("Có")
        so_khong = dieu_kien.count("Không")
        so_chua_danh_gia = dieu_kien.count(
            "Chưa đánh giá"
        )

        st.metric(
            "Số điều kiện được đánh giá đạt",
            f"{so_dat}/7"
        )

        if so_khong > 0:

            st.error(
                "🔴 KHÔNG ĐẠT ĐIỀU KIỆN SƠ BỘ: "
                "Có ít nhất một điều kiện đang được đánh giá là Không."
            )

        elif so_chua_danh_gia > 0:

            st.warning(
                "🟡 CHƯA ĐỦ DỮ LIỆU: "
                "Vẫn còn điều kiện chưa được đánh giá."
            )

        else:

            st.success(
                "🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ: "
                "Tất cả điều kiện đang được đánh giá là Có."
            )

    st.warning(
        """
        ⚠️ Lưu ý: Việc đánh giá điều kiện vay vốn trên ứng dụng
        chỉ là bước hỗ trợ. Tổ chức tín dụng vẫn phải kiểm tra
        hồ sơ, chứng từ và các điều kiện thực tế theo quy định
        pháp luật và quy định nội bộ.
        """
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

        elif (
            st.session_state.no_phai_tra
            > st.session_state.tong_tai_san
        ):

            st.warning(
                "⚠️ Nợ phải trả đang lớn hơn tổng tài sản. "
                "Vui lòng kiểm tra lại số liệu."
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
            "📈 KẾT QUẢ PHÂN TÍCH"
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
            chart.set_index(
                "Chỉ tiêu"
            )
        )

        if st.session_state.lnst > 0:

            st.success(
                "🟢 Doanh nghiệp đang có lợi nhuận sau thuế dương."
            )

        else:

            st.warning(
                "🟡 Doanh nghiệp đang có LNST không dương."
            )

        st.info(
            """
            💡 ROA, ROE và tỷ lệ nợ là các chỉ tiêu hỗ trợ
            phân tích tài chính. Không sử dụng riêng lẻ các
            chỉ tiêu này để kết luận doanh nghiệp được vay.
            """
        )


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.title("💳 THÔNG TIN KHOẢN VAY")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
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
                "✅ Đã tính toán nghĩa vụ trả nợ."
            )

    if (
        st.session_state.tong_nghia_vu
        is not None
    ):

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

        st.info(
            """
            💡 Đây là cách tính nghĩa vụ trả nợ sơ bộ theo phương pháp
            chia đều tiền gốc và tính lãi tháng đầu trên toàn bộ dư nợ.
            Khoản vay thực tế có thể áp dụng phương pháp tính khác
            tùy theo hợp đồng tín dụng.
            """
        )


# =========================================================
# 10. KHẢ NĂNG TRẢ NỢ
# =========================================================

elif menu == "📈 Khả năng trả nợ":

    st.title(
        "📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
    )

    st.info(
        """
        DSCR là chỉ tiêu hỗ trợ đánh giá khả năng dòng tiền
        đáp ứng nghĩa vụ trả nợ. Ngưỡng DSCR sử dụng trong
        thẩm định thực tế phụ thuộc vào chính sách của từng
        tổ chức tín dụng và đặc điểm ngành nghề.
        """
    )

    if (
        st.session_state.tong_nghia_vu
        is None
    ):

        st.warning(
            "⚠️ Vui lòng nhập và tính khoản vay trước."
        )

    else:

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien:,.2f} triệu đồng"
            )

        with c2:

            st.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f} triệu đồng"
            )

        if st.button(
            "📈 PHÂN TÍCH DSCR"
        ):

            if (
                st.session_state.tong_nghia_vu
                <= 0
            ):

                st.error(
                    "❌ Không thể tính DSCR."
                )

            else:

                st.session_state.dscr = (
                    st.session_state.dong_tien
                    / st.session_state.tong_nghia_vu
                )

                st.session_state.da_phan_tich_dscr = True

                st.divider()

                st.metric(
                    "DSCR",
                    f"{st.session_state.dscr:.2f} lần"
                )

                if (
                    st.session_state.dscr
                    >= 1
                ):

                    st.success(
                        "🟢 Dòng tiền hiện tại đủ hoặc lớn hơn "
                        "nghĩa vụ trả nợ theo chỉ tiêu DSCR."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ. "
                        "Cần thẩm định bổ sung."
                    )


# =========================================================
# 11. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.title(
        "🏠 TÀI SẢN BẢO ĐẢM"
    )

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm của khoản vay.
        Việc chấp nhận tài sản bảo đảm phụ thuộc vào loại tài sản,
        giá trị định giá, tính pháp lý, khả năng thanh khoản và
        chính sách tín dụng của tổ chức tín dụng.
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

    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
    ):

        if (
            st.session_state.co_tsdb
            == "Không"
        ):

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được xác định là không có tài sản bảo đảm."
            )

        elif (
            st.session_state.co_tsdb
            == "Chưa đánh giá"
        ):

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có tài sản bảo đảm hay không."
            )

        elif (
            st.session_state.gia_tri_tsdb
            <= 0
        ):

            st.error(
                "❌ Giá trị tài sản bảo đảm phải lớn hơn 0."
            )

        elif (
            st.session_state.so_tien_vay
            <= 0
        ):

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

            if (
                st.session_state.ltv
                <= 70
            ):

                st.success(
                    "🟢 LTV ở mức tương đối thấp theo mô hình hỗ trợ."
                )

            elif (
                st.session_state.ltv
                <= 100
            ):

                st.warning(
                    "🟡 LTV ở mức cần xem xét thêm chất lượng "
                    "và khả năng thanh khoản của tài sản."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị tài sản bảo đảm "
                    "theo dữ liệu nhập."
                )


# =========================================================
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title(
        "📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ"
    )

    st.info(
        """
        Kết quả được tổng hợp từ dữ liệu người dùng nhập.
        Đây là công cụ hỗ trợ phân tích sơ bộ, không thay thế
        quy trình thẩm định và quyết định tín dụng chính thức.
        """
    )

    # -----------------------------------------------------
    # KIỂM TRA DỮ LIỆU
    # -----------------------------------------------------

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
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ TỔNG HỢP KẾT QUẢ."
        )

        st.write(
            "Các phần còn thiếu:"
        )

        for item in missing:

            st.write(
                f"• {item}"
            )

        st.stop()

    # -----------------------------------------------------
    # KIỂM TRA ĐIỀU KIỆN VAY
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # THÔNG TIN KHÁCH HÀNG
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # CHỈ TIÊU TÀI CHÍNH
    # -----------------------------------------------------

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
        "Khoản vay",
        f"{st.session_state.so_tien_vay:,.2f}"
    )

    st.divider()

    # -----------------------------------------------------
    # ĐÁNH GIÁ CHỈ TIÊU HỖ TRỢ
    # -----------------------------------------------------

    tai_chinh_xau = False
    tra_no_xau = False

    # Đánh giá tài chính
    if (
        st.session_state.lnst <= 0
        or st.session_state.roa <= 0
        or st.session_state.roe <= 0
    ):
        tai_chinh_xau = True

    # Đánh giá khả năng trả nợ
    if (
        st.session_state.dscr is not None
        and st.session_state.dscr < 1
    ):
        tra_no_xau = True

    # -----------------------------------------------------
    # KẾT LUẬN
    # -----------------------------------------------------

    st.subheader(
        "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
    )

    if co_dieu_kien_khong:

        st.markdown(
            """
            <div class="status-bad">
                🔴 KHÔNG ĐẠT ĐIỀU KIỆN VAY VỐN SƠ BỘ
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Có ít nhất một điều kiện vay vốn cơ bản đang được
            đánh giá là Không. Hồ sơ chưa phù hợp để kết luận
            đạt điều kiện sơ bộ và cần được xem xét, bổ sung
            hoặc điều chỉnh.
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
            Cần hoàn thiện thông tin trước khi đưa ra kết luận
            thẩm định sơ bộ.
            """
        )

    elif tai_chinh_xau or tra_no_xau:

        st.markdown(
            """
            <div class="status-warning">
                🟡 CẦN THẨM ĐỊNH BỔ SUNG
            </div>
            """,
            unsafe_allow_html=True
        )

        if tai_chinh_xau:

            st.write(
                """
                ⚠️ Các chỉ tiêu tài chính đang có dấu hiệu cần
                xem xét thêm: LNST, ROA hoặc ROE không dương.
                """
            )

        if tra_no_xau:

            st.write(
                """
                ⚠️ DSCR nhỏ hơn 1, cho thấy dòng tiền hiện tại
                chưa đủ để đáp ứng nghĩa vụ trả nợ theo mô hình
                tính toán sơ bộ.
                """
            )

        st.write(
            """
            Hồ sơ chưa nên được kết luận đủ điều kiện chỉ dựa
            trên dữ liệu hiện tại. Cần thẩm định bổ sung về
            dòng tiền, phương án kinh doanh, lịch sử tín dụng,
            tài chính và các yếu tố liên quan.
            """
        )

    else:

        st.markdown(
            """
            <div class="status-good">
                🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CHO VAY
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Các điều kiện vay vốn cơ bản đang được đánh giá là đạt.
            Các chỉ tiêu tài chính và khả năng trả nợ hiện có tín hiệu
            tích cực theo dữ liệu đã nhập.

            Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
            chi tiết theo quy trình, hồ sơ chứng từ và chính sách
            của tổ chức tín dụng.
            """
        )

    st.divider()

    # -----------------------------------------------------
    # BẢNG TỔNG HỢP
    # -----------------------------------------------------

    st.subheader(
        "📋 BẢNG TỔNG HỢP THẨM ĐỊNH"
    )

    ket_qua = []

    # Điều kiện 1
    ket_qua.append(
        [
            "Năng lực pháp lý",
            (
                "Đạt"
                if st.session_state.nang_luc_phap_ly == "Có"
                else "Cần xem xét"
            ),
            st.session_state.nang_luc_phap_ly
        ]
    )

    # Điều kiện 2
    ket_qua.append(
        [
            "Mục đích vay vốn",
            (
                "Đạt"
                if st.session_state.muc_dich == "Có"
                else "Cần xem xét"
            ),
            st.session_state.muc_dich
        ]
    )

    # Điều kiện 3
    ket_qua.append(
        [
            "Phương án sử dụng vốn",
            (
                "Đạt"
                if st.session_state.co_phuong_an == "Có"
                else "Cần xem xét"
            ),
            st.session_state.co_phuong_an
        ]
    )

    # Điều kiện 4
    ket_qua.append(
        [
            "Tính khả thi phương án",
            (
                "Đạt"
                if st.session_state.phuong_an_kha_thi == "Có"
                else "Cần xem xét"
            ),
            st.session_state.phuong_an_kha_thi
        ]
    )

    # Điều kiện 5
    ket_qua.append(
        [
            "Khả năng tài chính trả nợ",
            (
                "Đạt"
                if st.session_state.kha_nang_tra_no == "Có"
                else "Cần xem xét"
            ),
            st.session_state.kha_nang_tra_no
        ]
    )

    # Điều kiện 6
    ket_qua.append(
        [
            "Cam kết sử dụng vốn đúng mục đích",
            (
                "Đạt"
                if st.session_state.dung_muc_dich == "Có"
                else "Cần xem xét"
            ),
            st.session_state.dung_muc_dich
        ]
    )

    # Điều kiện 7
    ket_qua.append(
        [
            "Cam kết trả nợ đúng hạn",
            (
                "Đạt"
                if st.session_state.tra_no_dung_han == "Có"
                else "Cần xem xét"
            ),
            st.session_state.tra_no_dung_han
        ]
    )

    # LNST
    ket_qua.append(
        [
            "Lợi nhuận sau thuế",
            (
                "Tích cực"
                if st.session_state.lnst > 0
                else "Cần xem xét"
            ),
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ]
    )

    # ROA
    ket_qua.append(
        [
            "ROA",
            (
                "Tích cực"
                if st.session_state.roa > 0
                else "Cần xem xét"
            ),
            f"{st.session_state.roa:.2f}%"
        ]
    )

    # ROE
    ket_qua.append(
        [
            "ROE",
            (
                "Tích cực"
                if st.session_state.roe > 0
                else "Cần xem xét"
            ),
            f"{st.session_state.roe:.2f}%"
        ]
    )

    # Tỷ lệ nợ
    ket_qua.append(
        [
            "Tỷ lệ nợ",
            (
                "Tham khảo"
                if st.session_state.ty_le_no <= 70
                else "Cần xem xét"
            ),
            f"{st.session_state.ty_le_no:.2f}%"
        ]
    )

    # DSCR
    if st.session_state.dscr is not None:

        ket_qua.append(
            [
                "DSCR",
                (
                    "Tích cực"
                    if st.session_state.dscr >= 1
                    else "Cần xem xét"
                ),
                f"{st.session_state.dscr:.2f} lần"
            ]
        )

    # LTV
    if st.session_state.ltv is not None:

        ket_qua.append(
            [
                "LTV",
                (
                    "Tham khảo"
                    if st.session_state.ltv <= 70
                    else "Cần xem xét"
                ),
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
        ⚠️ LƯU Ý QUAN TRỌNG

        Các chỉ tiêu ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ
        chỉ là các chỉ tiêu hỗ trợ phân tích tín dụng.

        Không nên sử dụng riêng lẻ các chỉ tiêu này để kết luận
        doanh nghiệp chắc chắn được vay vốn.

        Quyết định cho vay thực tế còn phụ thuộc vào hồ sơ pháp lý,
        mục đích sử dụng vốn, phương án kinh doanh, năng lực tài chính,
        dòng tiền, lịch sử tín dụng, khả năng trả nợ, tài sản bảo đảm
        và chính sách tín dụng của từng tổ chức tín dụng.
        """
    )


# =========================================================
# 13. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

        🏦 <b>
        HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP
        </b>

        <br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

        <br><br>

        ⚠️ Kết quả chỉ mang tính chất tham khảo
        và hỗ trợ ra quyết định.

    </div>
    """,
    unsafe_allow_html=True
)
