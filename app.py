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
    # Hồ sơ doanh nghiệp
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 0,
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

    # Chỉ tiêu tài chính
    "roa": None,
    "roe": None,
    "ty_le_no": None,

    # Khoản vay
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    # Nghĩa vụ trả nợ
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
    "da_kiem_tra_dieu_kien": False
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

    .stApp {
        background-color: #f4f7fb;
    }

    section[data-testid="stSidebar"] {
        background-color: #08264a;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    h1 {
        color: #08264a !important;
        font-weight: 800 !important;
    }

    h2 {
        color: #0d3b66 !important;
    }

    h3 {
        color: #155a8a !important;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #d9e4f0;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    }

    .hero {
        background-color: #0d5287;
        padding: 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white !important;
        font-size: 32px;
    }

    .hero p {
        color: white;
        font-size: 16px;
    }

    .good-box {
        background-color: #e9f8ef;
        border-left: 5px solid #1e9e58;
        padding: 18px;
        border-radius: 10px;
        color: #176b3c;
        font-weight: bold;
    }

    .warning-box {
        background-color: #fff7df;
        border-left: 5px solid #e4a400;
        padding: 18px;
        border-radius: 10px;
        color: #805f00;
        font-weight: bold;
    }

    .bad-box {
        background-color: #fff0f0;
        border-left: 5px solid #d64545;
        padding: 18px;
        border-radius: 10px;
        color: #8c2525;
        font-weight: bold;
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

    # -----------------------------------------------------
    # LOGO
    # -----------------------------------------------------

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
                font-size:60px;
                padding:15px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # TÊN HỆ THỐNG
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:10px 5px 20px 5px;
        ">

            <div style="
                font-size:21px;
                font-weight:800;
                line-height:1.5;
                color:white;
            ">
                🏦 THẨM ĐỊNH CHO VAY
                <br>
                DOANH NGHIỆP
            </div>

            <div style="
                font-size:14px;
                font-weight:600;
                color:#b9d7ef;
                margin-top:8px;
            ">
                HỆ THỐNG HỖ TRỢ CHO VAY
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            font-size:17px;
            font-weight:800;
            margin-bottom:12px;
        ">
            📌 DANH MỤC THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )


    menu = st.radio(
        "Chọn nội dung",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ & điều kiện",
            "💰 Phân tích tài chính",
            "💳 Khoản vay & bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )


# =========================================================
# 5. TRANG TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.markdown(
        """
        <div class="hero">
            <h1>🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP</h1>
            <p>
                Phân tích hồ sơ • Điều kiện vay vốn •
                Tài chính • Khả năng trả nợ •
                Tài sản bảo đảm
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("👋 Chào mừng bạn đến với hệ thống")

    st.write(
        """
        Ứng dụng hỗ trợ thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp
        thông qua việc tổng hợp thông tin pháp lý, mục đích vay,
        tình hình tài chính, khả năng trả nợ và tài sản bảo đảm.
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
            **BƯỚC 1 - HỒ SƠ**

            Nhập thông tin doanh nghiệp
            và kiểm tra điều kiện vay vốn.
            """
        )

    with c2:
        st.info(
            """
            **BƯỚC 2 - TÀI CHÍNH**

            Phân tích LNST,
            ROA, ROE và tỷ lệ nợ.
            """
        )

    with c3:
        st.info(
            """
            **BƯỚC 3 - KHOẢN VAY**

            Tính nghĩa vụ trả nợ,
            DSCR và LTV.
            """
        )

    with c4:
        st.info(
            """
            **BƯỚC 4 - KẾT QUẢ**

            Tổng hợp dữ liệu
            và kết luận sơ bộ.
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

    st.title("🏢 HỒ SƠ DOANH NGHIỆP")

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
            ].index(st.session_state.nganh_nghe)
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
            ].index(st.session_state.muc_dich_vay)
        )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        placeholder="Nhập phương án kinh doanh và cách sử dụng vốn vay..."
    )

    if st.button("💾 LƯU HỒ SƠ"):

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

            st.success("✅ Đã lưu hồ sơ doanh nghiệp.")


    st.divider()

    st.subheader("2️⃣ KIỂM TRA ĐIỀU KIỆN VAY VỐN")

    st.info(
        """
        Các tiêu chí dưới đây được sử dụng để kiểm tra sơ bộ.
        Việc đáp ứng các tiêu chí này không đồng nghĩa chắc chắn
        được cấp tín dụng.
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
                "🔴 KHÔNG ĐẠT: Có ít nhất một điều kiện đang được đánh giá là Không."
            )

            st.session_state.da_kiem_tra_dieu_kien = True

        elif "Chưa đánh giá" in dieu_kien:

            st.warning(
                "🟡 CHƯA ĐỦ DỮ LIỆU: Vẫn còn điều kiện chưa được đánh giá."
            )

            st.session_state.da_kiem_tra_dieu_kien = False

        else:

            st.success(
                "🟢 ĐẠT ĐIỀU KIỆN SƠ BỘ: Tất cả điều kiện hiện được đánh giá là Có."
            )

            st.session_state.da_kiem_tra_dieu_kien = True


# =========================================================
# 7. PHÂN TÍCH TÀI CHÍNH & KHOẢN VAY
# =========================================================

elif menu == "📊 Phân tích tài chính & Khoản vay":

    st.title("📊 PHÂN TÍCH TÀI CHÍNH & KHOẢN VAY")

    # =====================================================
    # TÀI CHÍNH
    # =====================================================

    st.subheader("💰 A. PHÂN TÍCH TÀI CHÍNH")

    st.caption(
        "Đơn vị nhập liệu: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "Doanh thu",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )

        st.session_state.lnst = st.number_input(
            "Lợi nhuận sau thuế (LNST)",
            value=st.session_state.lnst
        )

        st.session_state.tong_tai_san = st.number_input(
            "Tổng tài sản",
            min_value=0.0,
            value=st.session_state.tong_tai_san
        )

    with c2:

        st.session_state.von_chu_so_huu = st.number_input(
            "Vốn chủ sở hữu",
            min_value=0.0,
            value=st.session_state.von_chu_so_huu
        )

        st.session_state.no_phai_tra = st.number_input(
            "Nợ phải trả",
            min_value=0.0,
            value=st.session_state.no_phai_tra
        )

        st.session_state.dong_tien = st.number_input(
            "Dòng tiền từ hoạt động kinh doanh/tháng",
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
                "✅ Đã phân tích tài chính."
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


    # =====================================================
    # KHOẢN VAY
    # =====================================================

    st.divider()

    st.subheader("💳 B. THÔNG TIN KHOẢN VAY")

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "Số tiền vay",
            min_value=0.0,
            value=st.session_state.so_tien_vay
        )

        st.session_state.thoi_gian_vay = st.number_input(
            "Thời hạn vay (tháng)",
            min_value=1,
            value=st.session_state.thoi_gian_vay
        )

    with c2:

        st.session_state.lai_suat = st.number_input(
            "Lãi suất (%/năm)",
            min_value=0.0,
            value=st.session_state.lai_suat
        )

        st.session_state.nghia_vu_no_cu = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
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


    # =====================================================
    # DSCR
    # =====================================================

    st.divider()

    st.subheader("📈 C. KHẢ NĂNG TRẢ NỢ - DSCR")

    if st.session_state.tong_nghia_vu is None:

        st.warning(
            "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
        )

    else:

        st.write(
            f"""
            **Dòng tiền kinh doanh:** 
            {st.session_state.dong_tien:,.2f} triệu đồng/tháng
            """
        )

        st.write(
            f"""
            **Tổng nghĩa vụ trả nợ:** 
            {st.session_state.tong_nghia_vu:,.2f} triệu đồng/tháng
            """
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
                        "🟢 Dòng tiền hiện tại đủ để đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR."
                    )

                else:

                    st.warning(
                        "🟡 Dòng tiền hiện tại chưa đủ đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR."
                    )


    # =====================================================
    # TSĐB
    # =====================================================

    st.divider()

    st.subheader("🏠 D. TÀI SẢN BẢO ĐẢM - LTV")

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

    if st.button("🏠 PHÂN TÍCH TSĐB"):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có TSĐB hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "Khoản vay được đánh giá là không có tài sản bảo đảm."
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

            st.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

            if st.session_state.ltv <= 70:

                st.success(
                    "🟢 LTV ở mức thấp theo ngưỡng tham khảo của mô hình."
                )

            elif st.session_state.ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng, tính pháp lý và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                )


# =========================================================
# 8. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📋 Kết quả thẩm định":

    st.title("📋 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả được tổng hợp từ dữ liệu bạn đã nhập.
        Đây là công cụ hỗ trợ thẩm định sơ bộ, không thay thế
        quyết định tín dụng chính thức.
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
        missing.append("Phân tích DSCR")

    if not st.session_state.da_phan_tich_tsdb:
        missing.append("Tài sản bảo đảm")


    if len(missing) > 0:

        st.warning(
            "⚠️ CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN."
        )

        st.write(
            "Vui lòng hoàn thiện các nội dung sau:"
        )

        for item in missing:
            st.write(
                f"• {item}"
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

        co_khong = "Không" in dieu_kien

        co_chua_danh_gia = (
            "Chưa đánh giá" in dieu_kien
        )


        # =================================================
        # THÔNG TIN DOANH NGHIỆP
        # =================================================

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


        # =================================================
        # CHỈ TIÊU TÀI CHÍNH
        # =================================================

        st.divider()

        st.subheader("💰 CHỈ TIÊU TÀI CHÍNH")

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


        # =================================================
        # KHOẢN VAY
        # =================================================

        st.divider()

        st.subheader("💳 THÔNG TIN KHOẢN VAY")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Số tiền vay",
            f"{st.session_state.so_tien_vay:,.2f}"
        )

        c2.metric(
            "DSCR",
            f"{st.session_state.dscr:.2f} lần"
        )

        if st.session_state.ltv is not None:

            c3.metric(
                "LTV",
                f"{st.session_state.ltv:.2f}%"
            )

        else:

            c3.metric(
                "LTV",
                "Không áp dụng"
            )


        # =================================================
        # KẾT LUẬN
        # =================================================

        st.divider()

        st.subheader("📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ")


        # -------------------------------------------------
        # TRƯỜNG HỢP 1: CÓ ĐIỀU KIỆN KHÔNG ĐẠT
        # -------------------------------------------------

        if co_khong:

            st.markdown(
                """
                <div class="bad-box">
                    🔴 CHƯA ĐẠT ĐIỀU KIỆN VAY VỐN SƠ BỘ
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Có ít nhất một điều kiện vay vốn đang được đánh giá
                là "Không". Hồ sơ chưa đủ cơ sở để xem xét theo kết quả
                thẩm định sơ bộ hiện tại.
                """
            )


        # -------------------------------------------------
        # TRƯỜNG HỢP 2: CHƯA ĐÁNH GIÁ ĐỦ
        # -------------------------------------------------

        elif co_chua_danh_gia:

            st.markdown(
                """
                <div class="warning-box">
                    🟡 CHƯA ĐỦ DỮ LIỆU ĐỂ KẾT LUẬN
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Một hoặc nhiều điều kiện vay vốn chưa được đánh giá.
                Vui lòng hoàn thiện thông tin trước khi đưa ra kết luận.
                """
            )


        # -------------------------------------------------
        # TRƯỜNG HỢP 3: ĐỦ ĐIỀU KIỆN VÀ TÀI CHÍNH TÍCH CỰC
        # -------------------------------------------------

        elif (
            st.session_state.lnst > 0
            and st.session_state.roa > 0
            and st.session_state.roe > 0
            and st.session_state.dscr >= 1
        ):

            st.markdown(
                """
                <div class="good-box">
                    🟢 ĐỦ ĐIỀU KIỆN SƠ BỘ ĐỂ XEM XÉT CHO VAY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Các điều kiện vay vốn sơ bộ đang được đánh giá là đạt.
                Doanh nghiệp có LNST dương, ROA dương, ROE dương và DSCR
                từ 1 lần trở lên theo dữ liệu đã nhập.

                Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
                chi tiết theo quy trình và chính sách của tổ chức tín dụng.
                """
            )


        # -------------------------------------------------
        # TRƯỜNG HỢP 4: CẦN THẨM ĐỊNH BỔ SUNG
        # -------------------------------------------------

        else:

            st.markdown(
                """
                <div class="warning-box">
                    🟡 CẦN THẨM ĐỊNH BỔ SUNG
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(
                """
                Hồ sơ chưa đáp ứng đầy đủ các chỉ tiêu hỗ trợ tích cực
                trong mô hình thẩm định sơ bộ.

                Cần xem xét thêm tình hình tài chính, dòng tiền,
                khả năng trả nợ, phương án kinh doanh, lịch sử tín dụng,
                tài sản bảo đảm và các yếu tố liên quan.
                """
            )


        # =================================================
        # BẢNG TỔNG HỢP
        # =================================================

        st.divider()

        st.subheader("📊 BẢNG TỔNG HỢP THẨM ĐỊNH")

        ket_qua = []


        # Điều kiện 1
        ket_qua.append(
            [
                "Năng lực pháp lý",
                st.session_state.nang_luc_phap_ly,
                "Điều kiện cơ bản"
            ]
        )


        # Điều kiện 2
        ket_qua.append(
            [
                "Mục đích vay vốn",
                st.session_state.muc_dich_hop_phap,
                "Mục đích sử dụng vốn"
            ]
        )


        # Điều kiện 3
        ket_qua.append(
            [
                "Phương án sử dụng vốn",
                st.session_state.co_phuong_an,
                "Có phương án sử dụng vốn"
            ]
        )


        # Điều kiện 4
        ket_qua.append(
            [
                "Tính khả thi",
                st.session_state.phuong_an_kha_thi,
                "Đánh giá phương án"
            ]
        )


        # Điều kiện 5
        ket_qua.append(
            [
                "Khả năng trả nợ",
                st.session_state.kha_nang_tra_no,
                "Khả năng tài chính"
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


        # =================================================
        # LƯU Ý
        # =================================================

        st.warning(
            """
            ⚠️ LƯU Ý:

            ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu
            hỗ trợ phân tích tín dụng. Không sử dụng riêng lẻ
            các chỉ tiêu này để kết luận doanh nghiệp chắc chắn
            được cấp tín dụng.

            Quyết định cho vay thực tế còn phụ thuộc vào hồ sơ
            pháp lý, mục đích sử dụng vốn, phương án kinh doanh,
            năng lực tài chính, dòng tiền, lịch sử tín dụng,
            khả năng trả nợ, tài sản bảo đảm và chính sách tín dụng
            của từng tổ chức tín dụng.
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
        <br><br>
        ⚠️ Kết quả chỉ mang tính chất tham khảo.
    </div>
    """,
    unsafe_allow_html=True
)
