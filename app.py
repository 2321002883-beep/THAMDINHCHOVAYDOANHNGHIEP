import streamlit as st
import pandas as pd
from pathlib import Path


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
    # BƯỚC 1 - HỒ SƠ
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,
    "muc_dich_vay": "Bổ sung vốn lưu động",
    "phuong_an": "",

    # BƯỚC 2 - ĐIỀU KIỆN
    "nang_luc_phap_ly": "Chưa đánh giá",
    "muc_dich_hop_phap": "Chưa đánh giá",
    "phuong_an_su_dung_von": "Chưa đánh giá",
    "phuong_an_kha_thi": "Chưa đánh giá",
    "kha_nang_tra_no": "Chưa đánh giá",
    "su_dung_von_dung_muc_dich": "Chưa đánh giá",
    "tra_no_dung_han": "Chưa đánh giá",

    # BƯỚC 3 - TÀI CHÍNH
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

    # TÀI SẢN BẢO ĐẢM
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    # TRẠNG THÁI
    "da_luu_ho_so": False,
    "da_kiem_tra_dieu_kien": False,
    "da_phan_tich_tc": False,
    "da_phan_tich_vay": False,
    "da_phan_tich_dscr": False,
    "da_phan_tich_tsdb": False,

    # TRANG HIỆN TẠI
    "buoc_hien_tai": 1
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

    /* ================================
       NỀN CHÍNH
    ================================= */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f4f8fc 0%,
                #edf5fb 50%,
                #f8fbff 100%
            );
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
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


    /* ================================
       INPUT
    ================================= */

    div[data-baseweb="input"],
    div[data-baseweb="select"],
    textarea {
        border-radius: 10px !important;
    }


    /* ================================
       BUTTON
    ================================= */

    .stButton > button {
        width: 100%;
        min-height: 46px;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 700;
        color: white;
        background:
            linear-gradient(
                135deg,
                #07518a,
                #1185c4
            );
        box-shadow:
            0 5px 15px
            rgba(7,81,138,0.20);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 8px 20px
            rgba(7,81,138,0.30);
    }


    /* ================================
       HERO
    ================================= */

    .hero-box {
        background:
            linear-gradient(
                135deg,
                #062b4d,
                #0b5c8d,
                #1292c5
            );
        padding: 35px;
        border-radius: 24px;
        color: white;
        margin-bottom: 25px;
        box-shadow:
            0 12px 30px
            rgba(6,43,77,0.20);
    }

    .hero-box h1 {
        color: white !important;
        font-size: 30px;
        line-height: 1.3;
        margin-bottom: 12px;
    }

    .hero-box p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        line-height: 1.6;
    }


    /* ================================
       CARD
    ================================= */

    .card {
        background: white;
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #dce8f3;
        box-shadow:
            0 5px 18px
            rgba(8,43,76,0.06);
        margin-bottom: 20px;
    }


    /* ================================
       STEP BAR
    ================================= */

    .step-active {
        background:
            linear-gradient(
                135deg,
                #07518a,
                #1292c5
            );
        color: white;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-weight: 800;
    }

    .step-done {
        background: #e8f8ef;
        color: #17663b;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
    }

    .step-wait {
        background: #eef3f7;
        color: #71869b;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
    }


    /* ================================
       STATUS
    ================================= */

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


    /* ================================
       FOOTER
    ================================= */

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
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    logo_path = Path("logo.jpg")

    if logo_path.exists():

        st.image(
            str(logo_path),
            use_container_width=True
        )

    else:

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
            font-size:19px;
            font-weight:800;
            line-height:1.5;
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
        """
        <div style="
            font-size:15px;
            font-weight:800;
            margin-bottom:10px;
        ">
            📋 TIẾN ĐỘ HỒ SƠ
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.da_luu_ho_so:
        st.success("✅ Bước 1: Hồ sơ")
    else:
        st.info("1️⃣ Bước 1: Hồ sơ")

    if st.session_state.da_kiem_tra_dieu_kien:
        st.success("✅ Bước 2: Điều kiện")
    else:
        st.info("2️⃣ Bước 2: Điều kiện")

    if st.session_state.da_phan_tich_tc:
        st.success("✅ Bước 3: Tài chính")
    else:
        st.info("3️⃣ Bước 3: Tài chính")

    if st.session_state.da_phan_tich_vay:
        st.success("✅ Bước 4: Khoản vay")
    else:
        st.info("4️⃣ Bước 4: Khoản vay")

    if st.session_state.da_phan_tich_dscr:
        st.success("✅ Bước 5: Trả nợ")
    else:
        st.info("5️⃣ Bước 5: Trả nợ")

    if st.session_state.da_phan_tich_tsdb:
        st.success("✅ Bước 6: TSĐB")
    else:
        st.info("6️⃣ Bước 6: TSĐB")

    st.divider()

    if st.button("🏠 Về trang tổng quan"):

        st.session_state.buoc_hien_tai = 1

        st.rerun()

    st.caption(
        "💡 Bạn có thể sử dụng nút Tiếp tục để chuyển bước."
    )


# =========================================================
# 5. TIÊU ĐỀ CHÍNH + ẢNH BÊN PHẢI
# =========================================================

col_left, col_right = st.columns(
    [3, 1],
    gap="large"
)


with col_left:

    st.markdown(
        """
        <div class="hero-box">

            <div style="
                font-size:14px;
                font-weight:700;
                letter-spacing:1px;
                color:#bfe7ff;
                margin-bottom:10px;
            ">
                🏦 CREDIT APPRAISAL SYSTEM
            </div>

            <h1>
                HỆ THỐNG HỖ TRỢ
                THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Hỗ trợ thu thập thông tin doanh nghiệp,
                phân tích tài chính, đánh giá khả năng trả nợ
                và tổng hợp kết quả thẩm định sơ bộ.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col_right:

    logo_path = Path("logo.jpg")

    if logo_path.exists():

        st.image(
            str(logo_path),
            use_container_width=True
        )

    else:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:20px;
                padding:50px 20px;
                text-align:center;
                font-size:70px;
                box-shadow:0 8px 25px rgba(0,0,0,0.08);
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 6. THANH TIẾN TRÌNH
# =========================================================

st.subheader("📌 QUY TRÌNH THẨM ĐỊNH")

step1, step2, step3, step4, step5, step6 = st.columns(6)

with step1:

    if st.session_state.buoc_hien_tai == 1:
        st.markdown(
            '<div class="step-active">1<br>Hồ sơ</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_luu_ho_so:
        st.markdown(
            '<div class="step-done">✓<br>Hồ sơ</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">1<br>Hồ sơ</div>',
            unsafe_allow_html=True
        )


with step2:

    if st.session_state.buoc_hien_tai == 2:
        st.markdown(
            '<div class="step-active">2<br>Điều kiện</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_kiem_tra_dieu_kien:
        st.markdown(
            '<div class="step-done">✓<br>Điều kiện</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">2<br>Điều kiện</div>',
            unsafe_allow_html=True
        )


with step3:

    if st.session_state.buoc_hien_tai == 3:
        st.markdown(
            '<div class="step-active">3<br>Tài chính</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_phan_tich_tc:
        st.markdown(
            '<div class="step-done">✓<br>Tài chính</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">3<br>Tài chính</div>',
            unsafe_allow_html=True
        )


with step4:

    if st.session_state.buoc_hien_tai == 4:
        st.markdown(
            '<div class="step-active">4<br>Khoản vay</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_phan_tich_vay:
        st.markdown(
            '<div class="step-done">✓<br>Khoản vay</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">4<br>Khoản vay</div>',
            unsafe_allow_html=True
        )


with step5:

    if st.session_state.buoc_hien_tai == 5:
        st.markdown(
            '<div class="step-active">5<br>Trả nợ</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_phan_tich_dscr:
        st.markdown(
            '<div class="step-done">✓<br>Trả nợ</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">5<br>Trả nợ</div>',
            unsafe_allow_html=True
        )


with step6:

    if st.session_state.buoc_hien_tai == 6:
        st.markdown(
            '<div class="step-active">6<br>TSĐB</div>',
            unsafe_allow_html=True
        )
    elif st.session_state.da_phan_tich_tsdb:
        st.markdown(
            '<div class="step-done">✓<br>TSĐB</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="step-wait">6<br>TSĐB</div>',
            unsafe_allow_html=True
        )


st.divider()


# =========================================================
# 7. BƯỚC 1 - HỒ SƠ DOANH NGHIỆP
# =========================================================

if st.session_state.buoc_hien_tai == 1:

    st.title("1️⃣ Thông tin doanh nghiệp")

    st.info(
        "Bước 1/6 — Nhập thông tin cơ bản của doanh nghiệp và phương án vay vốn."
    )

    c1, c2 = st.columns(2)

    with c1:

        ten_dn = st.text_input(
            "🏷️ Tên doanh nghiệp",
            value=st.session_state.ten_dn
        )

        ma_so = st.text_input(
            "🆔 Mã số doanh nghiệp",
            value=st.session_state.ma_so
        )

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
            "🏭 Ngành nghề kinh doanh",
            danh_sach_nganh,
            index=danh_sach_nganh.index(
                st.session_state.nganh_nghe
            )
        )

    with c2:

        thoi_gian_hd = st.number_input(
            "📅 Thời gian hoạt động (năm)",
            min_value=0,
            value=st.session_state.thoi_gian_hd
        )

        muc_dich_list = [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]

        muc_dich_vay = st.selectbox(
            "🎯 Mục đích sử dụng vốn",
            muc_dich_list,
            index=muc_dich_list.index(
                st.session_state.muc_dich_vay
            )
        )

    phuong_an = st.text_area(
        "📝 Mô tả phương án sử dụng vốn",
        value=st.session_state.phuong_an,
        height=150,
        placeholder="Nhập nội dung phương án kinh doanh, nhu cầu vay và cách sử dụng vốn..."
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

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

                st.success(
                    "✅ Đã lưu hồ sơ doanh nghiệp."
                )

    with c2:

        if st.button("➡️ TIẾP TỤC ĐIỀU KIỆN VAY"):

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
                st.session_state.buoc_hien_tai = 2

                st.rerun()


# =========================================================
# 8. BƯỚC 2 - ĐIỀU KIỆN VAY
# =========================================================

elif st.session_state.buoc_hien_tai == 2:

    st.title("2️⃣ Kiểm tra điều kiện vay vốn")

    st.info(
        "Bước 2/6 — Đánh giá sơ bộ các điều kiện liên quan đến khoản vay."
    )

    options = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.nang_luc_phap_ly = st.selectbox(
            "⚖️ Năng lực pháp lý phù hợp?",
            options,
            index=options.index(
                st.session_state.nang_luc_phap_ly
            )
        )

        st.session_state.muc_dich_hop_phap = st.selectbox(
            "🎯 Mục đích vay vốn hợp pháp?",
            options,
            index=options.index(
                st.session_state.muc_dich_hop_phap
            )
        )

        st.session_state.phuong_an_su_dung_von = st.selectbox(
            "💰 Có phương án sử dụng vốn?",
            options,
            index=options.index(
                st.session_state.phuong_an_su_dung_von
            )
        )

        st.session_state.phuong_an_kha_thi = st.selectbox(
            "📈 Phương án sử dụng vốn khả thi?",
            options,
            index=options.index(
                st.session_state.phuong_an_kha_thi
            )
        )

    with c2:

        st.session_state.kha_nang_tra_no = st.selectbox(
            "💳 Có khả năng tài chính trả nợ?",
            options,
            index=options.index(
                st.session_state.kha_nang_tra_no
            )
        )

        st.session_state.su_dung_von_dung_muc_dich = st.selectbox(
            "🔐 Cam kết sử dụng vốn đúng mục đích?",
            options,
            index=options.index(
                st.session_state.su_dung_von_dung_muc_dich
            )
        )

        st.session_state.tra_no_dung_han = st.selectbox(
            "⏰ Cam kết trả nợ đúng hạn?",
            options,
            index=options.index(
                st.session_state.tra_no_dung_han
            )
        )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button("⬅️ QUAY LẠI"):

            st.session_state.buoc_hien_tai = 1

            st.rerun()

    with c2:

        if st.button("🔍 KIỂM TRA"):

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

                st.session_state.da_kiem_tra_dieu_kien = True

                st.error(
                    "🔴 Có ít nhất một điều kiện được đánh giá là Không."
                )

            elif "Chưa đánh giá" in dieu_kien:

                st.warning(
                    "🟡 Vui lòng đánh giá đầy đủ 7 điều kiện."
                )

            else:

                st.session_state.da_kiem_tra_dieu_kien = True

                st.success(
                    "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
                )

    with c3:

        if st.button("➡️ TIẾP TỤC TÀI CHÍNH"):

            st.session_state.buoc_hien_tai = 3

            st.rerun()


# =========================================================
# 9. BƯỚC 3 - TÀI CHÍNH
# =========================================================

elif st.session_state.buoc_hien_tai == 3:

    st.title("3️⃣ Phân tích tài chính doanh nghiệp")

    st.info(
        "Bước 3/6 — Nhập số liệu tài chính để tính ROA, ROE và tỷ lệ nợ."
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.doanh_thu = st.number_input(
            "💵 Doanh thu (triệu đồng)",
            min_value=0.0,
            value=st.session_state.doanh_thu
        )

        st.session_state.lnst = st.number_input(
            "📈 Lợi nhuận sau thuế - LNST",
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
            "💧 Dòng tiền từ HĐKD/tháng",
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

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅️ QUAY LẠI ĐIỀU KIỆN"):

            st.session_state.buoc_hien_tai = 2

            st.rerun()

    with c2:

        if st.button("➡️ TIẾP TỤC KHOẢN VAY"):

            if not st.session_state.da_phan_tich_tc:

                st.error(
                    "❌ Vui lòng phân tích tài chính trước."
                )

            else:

                st.session_state.buoc_hien_tai = 4

                st.rerun()


# =========================================================
# 10. BƯỚC 4 - KHOẢN VAY
# =========================================================

elif st.session_state.buoc_hien_tai == 4:

    st.title("4️⃣ Thông tin khoản vay")

    st.info(
        "Bước 4/6 — Nhập khoản vay và tính nghĩa vụ trả nợ hàng tháng."
    )

    c1, c2 = st.columns(2)

    with c1:

        st.session_state.so_tien_vay = st.number_input(
            "💰 Số tiền vay (triệu đồng)",
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

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅️ QUAY LẠI TÀI CHÍNH"):

            st.session_state.buoc_hien_tai = 3

            st.rerun()

    with c2:

        if st.button("➡️ TIẾP TỤC KHẢ NĂNG TRẢ NỢ"):

            if not st.session_state.da_phan_tich_vay:

                st.error(
                    "❌ Vui lòng tính nghĩa vụ trả nợ trước."
                )

            else:

                st.session_state.buoc_hien_tai = 5

                st.rerun()


# =========================================================
# 11. BƯỚC 5 - KHẢ NĂNG TRẢ NỢ
# =========================================================

elif st.session_state.buoc_hien_tai == 5:

    st.title("5️⃣ Phân tích khả năng trả nợ")

    st.info(
        "Bước 5/6 — Đánh giá khả năng đáp ứng nghĩa vụ trả nợ thông qua DSCR."
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "💧 Dòng tiền kinh doanh/tháng",
            f"{st.session_state.dong_tien:,.2f} triệu đồng"
        )

    with c2:

        st.metric(
            "💳 Nghĩa vụ trả nợ/tháng",
            f"{st.session_state.tong_nghia_vu:,.2f} triệu đồng"
        )

    if st.button("📈 PHÂN TÍCH DSCR"):

        if st.session_state.tong_nghia_vu is None:

            st.error(
                "❌ Vui lòng tính khoản vay trước."
            )

        elif st.session_state.tong_nghia_vu <= 0:

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

            if st.session_state.dscr >= 1:

                st.success(
                    "🟢 Dòng tiền hiện tại lớn hơn hoặc bằng nghĩa vụ trả nợ."
                )

            else:

                st.warning(
                    "🟡 Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅️ QUAY LẠI KHOẢN VAY"):

            st.session_state.buoc_hien_tai = 4

            st.rerun()

    with c2:

        if st.button("➡️ TIẾP TỤC TÀI SẢN BẢO ĐẢM"):

            if not st.session_state.da_phan_tich_dscr:

                st.error(
                    "❌ Vui lòng phân tích DSCR trước."
                )

            else:

                st.session_state.buoc_hien_tai = 6

                st.rerun()


# =========================================================
# 12. BƯỚC 6 - TÀI SẢN BẢO ĐẢM
# =========================================================

elif st.session_state.buoc_hien_tai == 6:

    st.title("6️⃣ Tài sản bảo đảm")

    st.info(
        "Bước 6/6 — Nhập thông tin tài sản bảo đảm và tính tỷ lệ LTV."
    )

    options_tsdb = [
        "Chưa đánh giá",
        "Có",
        "Không"
    ]

    st.session_state.co_tsdb = st.selectbox(
        "🏠 Khoản vay có tài sản bảo đảm?",
        options_tsdb,
        index=options_tsdb.index(
            st.session_state.co_tsdb
        )
    )

    if st.session_state.co_tsdb == "Có":

        st.session_state.gia_tri_tsdb = st.number_input(
            "🏠 Giá trị tài sản bảo đảm (triệu đồng)",
            min_value=0.0,
            value=st.session_state.gia_tri_tsdb
        )

    st.info(
        """
        Tài sản bảo đảm chỉ là một yếu tố hỗ trợ trong thẩm định.
        Cần xem xét thêm quyền sở hữu, hồ sơ pháp lý,
        giá trị định giá, khả năng thanh khoản và chính sách
        cho vay của từng ngân hàng.
        """
    )

    if st.button("🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"):

        if st.session_state.co_tsdb == "Chưa đánh giá":

            st.warning(
                "⚠️ Vui lòng xác định khoản vay có TSĐB hay không."
            )

        elif st.session_state.co_tsdb == "Không":

            st.session_state.ltv = None
            st.session_state.da_phan_tich_tsdb = True

            st.info(
                "ℹ️ Khoản vay được đánh giá là không có tài sản bảo đảm."
            )

        elif st.session_state.gia_tri_tsdb <= 0:

            st.error(
                "❌ Giá trị TSĐB phải lớn hơn 0."
            )

        elif st.session_state.so_tien_vay <= 0:

            st.error(
                "❌ Số tiền vay phải lớn hơn 0."
            )

        else:

            st.session_state.ltv = (
                st.session_state.so_tien_vay
                / st.session_state.gia_tri_tsdb
                * 100
            )

            st.session_state.da_phan_tich_tsdb = True

            st.success(
                "✅ Phân tích tài sản bảo đảm thành công."
            )

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

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button("⬅️ QUAY LẠI KHẢ NĂNG TRẢ NỢ"):

            st.session_state.buoc_hien_tai = 5

            st.rerun()

    with c2:

        if st.button("📊 XEM KẾT QUẢ THẨM ĐỊNH"):

            if not st.session_state.da_phan_tich_tsdb:

                st.error(
                    "❌ Vui lòng phân tích tài sản bảo đảm trước."
                )

            else:

                st.session_state.buoc_hien_tai = 7

                st.rerun()


# =========================================================
# 13. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif st.session_state.buoc_hien_tai == 7:

    st.title("📊 KẾT QUẢ THẨM ĐỊNH SƠ BỘ")

    st.info(
        """
        Kết quả được tổng hợp từ hồ sơ doanh nghiệp,
        điều kiện vay vốn, tình hình tài chính,
        khả năng trả nợ và tài sản bảo đảm.
        """
    )

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


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

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


    # =====================================================
    # CHỈ TIÊU TÀI CHÍNH
    # =====================================================

    st.divider()

    st.subheader("📈 CHỈ TIÊU TÀI CHÍNH")

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


    # =====================================================
    # CHỈ TIÊU KHOẢN VAY
    # =====================================================

    st.divider()

    st.subheader("💳 KHOẢN VAY & KHẢ NĂNG TRẢ NỢ")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Số tiền vay",
        f"{st.session_state.so_tien_vay:,.2f}"
    )

    c2.metric(
        "DSCR",
        (
            f"{st.session_state.dscr:.2f} lần"
            if st.session_state.dscr is not None
            else "Chưa tính"
        )
    )

    c3.metric(
        "LTV",
        (
            f"{st.session_state.ltv:.2f}%"
            if st.session_state.ltv is not None
            else "Không áp dụng"
        )
    )


    # =====================================================
    # KẾT LUẬN
    # =====================================================

    st.divider()

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
            Hồ sơ đang có ít nhất một điều kiện vay vốn
            được đánh giá là Không. Cần xác định nguyên nhân,
            bổ sung hồ sơ hoặc điều chỉnh phương án trước
            khi xem xét tiếp.
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
            Hồ sơ có các tín hiệu tích cực theo mô hình hỗ trợ:
            doanh nghiệp có lợi nhuận sau thuế dương,
            ROA và ROE dương, đồng thời dòng tiền hiện tại
            đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR.
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
            hỗ trợ hiện tại. Cần thẩm định bổ sung về tài chính,
            dòng tiền, khả năng trả nợ, phương án kinh doanh,
            lịch sử tín dụng và tài sản bảo đảm.
            """
        )


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.divider()

    st.subheader("📋 BẢNG TỔNG HỢP THẨM ĐỊNH")

    ket_qua = [

        [
            "Năng lực pháp lý",
            "Đạt"
            if st.session_state.nang_luc_phap_ly == "Có"
            else "Cần xem xét",
            st.session_state.nang_luc_phap_ly
        ],

        [
            "Mục đích vay vốn",
            "Đạt"
            if st.session_state.muc_dich_hop_phap == "Có"
            else "Cần xem xét",
            st.session_state.muc_dich_hop_phap
        ],

        [
            "Phương án sử dụng vốn",
            "Đạt"
            if st.session_state.phuong_an_su_dung_von == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_su_dung_von
        ],

        [
            "Tính khả thi phương án",
            "Đạt"
            if st.session_state.phuong_an_kha_thi == "Có"
            else "Cần xem xét",
            st.session_state.phuong_an_kha_thi
        ],

        [
            "Khả năng tài chính trả nợ",
            "Đạt"
            if st.session_state.kha_nang_tra_no == "Có"
            else "Cần xem xét",
            st.session_state.kha_nang_tra_no
        ],

        [
            "Lợi nhuận sau thuế",
            "Tích cực"
            if st.session_state.lnst > 0
            else "Cần xem xét",
            f"{st.session_state.lnst:,.2f} triệu đồng"
        ],

        [
            "ROA",
            "Tích cực"
            if st.session_state.roa > 0
            else "Cần xem xét",
            f"{st.session_state.roa:.2f}%"
        ],

        [
            "ROE",
            "Tích cực"
            if st.session_state.roe > 0
            else "Cần xem xét",
            f"{st.session_state.roe:.2f}%"
        ],

        [
            "Tỷ lệ nợ",
            "Tham khảo",
            f"{st.session_state.ty_le_no:.2f}%"
        ]

    ]


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

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ chỉ là các chỉ tiêu
        hỗ trợ phân tích tín dụng, không phải là căn cứ duy nhất
        để quyết định cho vay.

        Quyết định tín dụng thực tế cần xem xét tổng thể hồ sơ
        pháp lý doanh nghiệp, mục đích vay vốn, phương án kinh doanh,
        báo cáo tài chính, dòng tiền, lịch sử tín dụng,
        nghĩa vụ nợ, khả năng trả nợ, tài sản bảo đảm và
        chính sách tín dụng của ngân hàng.

        Kết quả của ứng dụng chỉ có giá trị hỗ trợ thẩm định sơ bộ.
        """
    )

    st.divider()

    if st.button("🔄 TẠO HỒ SƠ THẨM ĐỊNH MỚI"):

        for key, value in default_values.items():

            st.session_state[key] = value

        st.rerun()


# =========================================================
# 14. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

        <br><br>

        Công cụ hỗ trợ phân tích và thẩm định sơ bộ hồ sơ tín dụng

    </div>
    """,
    unsafe_allow_html=True
)
