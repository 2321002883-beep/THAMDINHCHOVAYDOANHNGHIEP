import streamlit as st
import pandas as pd
from datetime import datetime

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
# 2. CẤU HÌNH MYSQL
# =========================================================
# Nếu CHƯA dùng MySQL:
# MYSQL_ENABLED = False
#
# Nếu dùng MySQL/Aiven:
# MYSQL_ENABLED = True
# Sau đó thay thông tin bên dưới bằng thông tin MySQL của bạn.

MYSQL_ENABLED = False

MYSQL_CONFIG = {
    "host": "YOUR_MYSQL_HOST",
    "port": 3306,
    "user": "YOUR_MYSQL_USER",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "YOUR_MYSQL_DATABASE"
}


# =========================================================
# 3. KHỞI TẠO SESSION STATE
# =========================================================

default_values = {

    # ĐIỀU HƯỚNG
    "buoc_hien_tai": 1,

    # HỒ SƠ DOANH NGHIỆP
    "ten_dn": "",
    "ma_so": "",
    "nganh_nghe": "Sản xuất",
    "thoi_gian_hd": 1,

    # MỤC ĐÍCH VAY
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

    "da_kiem_tra_dieu_kien": False,

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

    "da_phan_tich_tc": False,

    # KHOẢN VAY
    "so_tien_vay": 0.0,
    "thoi_gian_vay": 12,
    "lai_suat": 0.0,
    "nghia_vu_no_cu": 0.0,

    "tien_goc_thang": None,
    "tien_lai_thang": None,
    "tong_nghia_vu": None,

    "da_phan_tich_vay": False,

    # DSCR
    "dscr": None,
    "da_phan_tich_dscr": False,

    # TSĐB
    "co_tsdb": "Chưa đánh giá",
    "gia_tri_tsdb": 0.0,
    "ltv": None,

    "da_phan_tich_tsdb": False,

    # TRẠNG THÁI
    "da_luu_ho_so": False,

    # MYSQL
    "mysql_error": ""
}


for key, value in default_values.items():

    if key not in st.session_state:

        st.session_state[key] = value


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
            #f4f8fc 0%,
            #eef6fc 50%,
            #f8fbff 100%
        );
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #061a33 0%,
            #0a3158 55%,
            #0d4d78 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    /* =========================
       TIÊU ĐỀ
    ========================= */

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


    /* =========================
       HERO
    ========================= */

    .hero-card {
        background:
        linear-gradient(
            135deg,
            #062b4d,
            #0b5c8d,
            #1292c5
        );

        padding: 32px;

        border-radius: 22px;

        color: white;

        margin-bottom: 25px;

        box-shadow:
        0 12px 35px
        rgba(6,43,77,0.20);
    }

    .hero-card h1 {
        color: white !important;
        font-size: 30px;
        margin-bottom: 8px;
    }

    .hero-card p {
        color: rgba(255,255,255,0.92);
        font-size: 16px;
        margin: 0;
    }


    /* =========================
       CARD
    ========================= */

    .card {
        background: white;

        padding: 24px;

        border-radius: 18px;

        border:
        1px solid #dce8f3;

        box-shadow:
        0 6px 20px
        rgba(8,43,76,0.07);

        margin-bottom: 20px;
    }


    /* =========================
       STEP
    ========================= */

    .step-card {
        background: white;

        padding: 15px;

        border-radius: 15px;

        text-align: center;

        border:
        1px solid #dce8f3;

        box-shadow:
        0 4px 12px
        rgba(8,43,76,0.05);

        font-weight: 700;

        min-height: 80px;
    }

    .step-active {
        background:
        linear-gradient(
            135deg,
            #07518a,
            #1185c4
        );

        color: white;

        border: none;
    }

    .step-done {
        background: #e8f8ef;

        color: #17663b;
    }


    /* =========================
       METRIC
    ========================= */

    div[data-testid="stMetric"] {
        background: white;

        border:
        1px solid #d7e5f2;

        padding: 18px;

        border-radius: 16px;

        box-shadow:
        0 6px 20px
        rgba(8,43,76,0.07);
    }

    div[data-testid="stMetricLabel"] {
        color: #55708d !important;

        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #0b3d66 !important;

        font-weight: 800;
    }


    /* =========================
       BUTTON
    ========================= */

    .stButton > button {
        width: 100%;

        border-radius: 12px;

        border: none;

        padding:
        0.7rem 1rem;

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
        rgba(7,81,138,0.2);
    }

    .stButton > button:hover {
        transform:
        translateY(-2px);

        box-shadow:
        0 8px 20px
        rgba(7,81,138,0.3);
    }


    /* =========================
       STATUS
    ========================= */

    .status-good {
        background: #e8f8ef;

        border-left:
        6px solid #1c9b58;

        padding: 18px;

        border-radius: 12px;

        color: #17663b;

        font-weight: 700;

        font-size: 18px;
    }

    .status-warning {
        background: #fff7df;

        border-left:
        6px solid #e0a000;

        padding: 18px;

        border-radius: 12px;

        color: #765800;

        font-weight: 700;

        font-size: 18px;
    }

    .status-bad {
        background: #fff0f0;

        border-left:
        6px solid #d43d3d;

        padding: 18px;

        border-radius: 12px;

        color: #852323;

        font-weight: 700;

        font-size: 18px;
    }


    /* =========================
       FOOTER
    ========================= */

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
# 5. HÀM RESET
# =========================================================

def reset_application():

    for key, value in default_values.items():

        st.session_state[key] = value


# =========================================================
# 6. HÀM KẾT NỐI MYSQL
# =========================================================

def get_mysql_connection():

    if not MYSQL_ENABLED:

        return None

    try:

        import mysql.connector

        conn = mysql.connector.connect(
            host=MYSQL_CONFIG["host"],
            port=MYSQL_CONFIG["port"],
            user=MYSQL_CONFIG["user"],
            password=MYSQL_CONFIG["password"],
            database=MYSQL_CONFIG["database"]
        )

        return conn

    except Exception as e:

        st.session_state.mysql_error = str(e)

        return None


# =========================================================
# 7. HÀM LƯU HỒ SƠ VÀO MYSQL
# =========================================================

def save_to_mysql():

    conn = get_mysql_connection()

    if conn is None:

        return False

    try:

        cursor = conn.cursor()

        sql = """
        INSERT INTO ho_so_tham_dinh
        (
            ten_dn,
            ma_so,
            nganh_nghe,
            thoi_gian_hd,
            muc_dich_vay,
            phuong_an,
            doanh_thu,
            lnst,
            tong_tai_san,
            von_chu_so_huu,
            no_phai_tra,
            dong_tien,
            so_tien_vay,
            thoi_gian_vay,
            lai_suat,
            gia_tri_tsdb
        )
        VALUES
        (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        """

        values = (
            st.session_state.ten_dn,
            st.session_state.ma_so,
            st.session_state.nganh_nghe,
            st.session_state.thoi_gian_hd,
            st.session_state.muc_dich_vay,
            st.session_state.phuong_an,
            st.session_state.doanh_thu,
            st.session_state.lnst,
            st.session_state.tong_tai_san,
            st.session_state.von_chu_so_huu,
            st.session_state.no_phai_tra,
            st.session_state.dong_tien,
            st.session_state.so_tien_vay,
            st.session_state.thoi_gian_vay,
            st.session_state.lai_suat,
            st.session_state.gia_tri_tsdb
        )

        cursor.execute(
            sql,
            values
        )

        conn.commit()

        cursor.close()

        conn.close()

        return True

    except Exception as e:

        st.session_state.mysql_error = str(e)

        return False


# =========================================================
# 8. SIDEBAR
# =========================================================

with st.sidebar:

    try:

        st.image(
            "logo.jpg",
            use_container_width=True
        )

    except Exception:

        st.markdown(
            """
            <div style="
            text-align:center;
            font-size:60px;
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
        font-size:18px;
        font-weight:800;
        line-height:1.4;
        ">
        HỆ THỐNG<br>
        THẨM ĐỊNH DOANH NGHIỆP
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown(
        "### 📋 TIẾN ĐỘ THẨM ĐỊNH"
    )


    buoc = st.session_state.buoc_hien_tai


    progress_value = (
        (buoc - 1)
        / 3
    )


    st.progress(
        progress_value
    )


    st.write(
        f"Đang thực hiện: **Bước {buoc}/4**"
    )


    st.divider()


    st.markdown(
        "### 🏢 THÔNG TIN HỒ SƠ"
    )


    if st.session_state.ten_dn:

        st.write(
            f"**Doanh nghiệp:** "
            f"{st.session_state.ten_dn}"
        )

    else:

        st.write(
            "Chưa nhập doanh nghiệp"
        )


    if st.session_state.ma_so:

        st.write(
            f"**Mã số:** "
            f"{st.session_state.ma_so}"
        )


    st.divider()


    if MYSQL_ENABLED:

        st.success(
            "🟢 MySQL đang bật"
        )

    else:

        st.info(
            "🔵 Đang lưu Session State"
        )


    st.divider()


    if st.button(
        "🔄 LÀM MỚI HỒ SƠ"
    ):

        reset_application()

        st.rerun()


# =========================================================
# 9. HEADER
# =========================================================

st.markdown(
    """
    <div class="hero-card">

        <h1>
        🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
        CHO VAY DOANH NGHIỆP
        </h1>

        <p>
        Quy trình phân tích và thẩm định sơ bộ hồ sơ tín dụng doanh nghiệp
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 10. THANH TIẾN TRÌNH 4 BƯỚC
# =========================================================

buoc = st.session_state.buoc_hien_tai


c1, c2, c3, c4 = st.columns(4)


step_list = [

    ("1", "🏢", "Hồ sơ doanh nghiệp"),

    ("2", "⚖️", "Điều kiện vay"),

    ("3", "💰", "Phân tích tín dụng"),

    ("4", "📊", "Kết quả thẩm định")

]


columns = [
    c1,
    c2,
    c3,
    c4
]


for i in range(4):

    with columns[i]:

        if buoc == i + 1:

            st.markdown(
                f"""
                <div class="step-card step-active">

                {step_list[i][1]}
                <br>

                <b>BƯỚC {step_list[i][0]}</b>

                <br>

                {step_list[i][2]}

                </div>
                """,
                unsafe_allow_html=True
            )

        elif buoc > i + 1:

            st.markdown(
                f"""
                <div class="step-card step-done">

                ✓
                <br>

                <b>HOÀN THÀNH</b>

                <br>

                {step_list[i][2]}

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="step-card">

                {step_list[i][1]}
                <br>

                <b>BƯỚC {step_list[i][0]}</b>

                <br>

                {step_list[i][2]}

                </div>
                """,
                unsafe_allow_html=True
            )


st.progress(
    (buoc - 1) / 3
)


# =========================================================
# 11. BƯỚC 1 - HỒ SƠ DOANH NGHIỆP
# =========================================================

if buoc == 1:

    st.title(
        "🏢 BƯỚC 1: HỒ SƠ DOANH NGHIỆP"
    )

    st.caption(
        "Nhập thông tin cơ bản về doanh nghiệp và nhu cầu vay vốn."
    )


    with st.container(border=True):

        st.subheader(
            "🏢 Thông tin doanh nghiệp"
        )


        c1, c2 = st.columns(2)


        with c1:

            ten_dn = st.text_input(
                "🏷️ Tên doanh nghiệp *",
                value=st.session_state.ten_dn
            )


            ma_so = st.text_input(
                "🆔 Mã số doanh nghiệp *",
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

                "🏭 Ngành nghề kinh doanh",

                danh_sach_nganh,

                index=danh_sach_nganh.index(
                    st.session_state.nganh_nghe
                )

            )


            thoi_gian_hd = st.number_input(

                "📅 Thời gian hoạt động (năm)",

                min_value=0,

                value=st.session_state.thoi_gian_hd

            )


    with st.container(border=True):

        st.subheader(
            "💳 Nhu cầu vay vốn"
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

            "📝 Phương án sử dụng vốn *",

            value=st.session_state.phuong_an,

            height=160,

            placeholder=
            "Mô tả phương án kinh doanh, "
            "nhu cầu vay vốn, cách sử dụng vốn "
            "và nguồn trả nợ dự kiến..."

        )


    st.divider()


    if st.button(
        "💾 LƯU HỒ SƠ & TIẾP TỤC →",
        type="primary"
    ):

        if not ten_dn.strip():

            st.error(
                "❌ Vui lòng nhập tên doanh nghiệp."
            )

        elif not ma_so.strip():

            st.error(
                "❌ Vui lòng nhập mã số doanh nghiệp."
            )

        elif not phuong_an.strip():

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


            if MYSQL_ENABLED:

                if save_to_mysql():

                    st.success(
                        "✅ Đã lưu hồ sơ vào MySQL."
                    )

                else:

                    st.warning(
                        "⚠️ Hồ sơ đã lưu trong Session State "
                        "nhưng chưa lưu được vào MySQL."
                    )

            else:

                st.success(
                    "✅ Đã lưu hồ sơ trong Session State."
                )


            st.session_state.buoc_hien_tai = 2

            st.rerun()


# =========================================================
# 12. BƯỚC 2 - ĐIỀU KIỆN VAY
# =========================================================

elif buoc == 2:

    st.title(
        "⚖️ BƯỚC 2: ĐIỀU KIỆN VAY VỐN"
    )

    st.caption(
        "Đánh giá sơ bộ các điều kiện liên quan đến hồ sơ vay vốn."
    )


    st.info(
        """
        ℹ️ Đây là bước đánh giá hỗ trợ. Kết quả của ứng dụng
        không thay thế việc thẩm định tín dụng chính thức của ngân hàng.
        """
    )


    options = [

        "Chưa đánh giá",

        "Có",

        "Không"

    ]


    with st.container(border=True):

        st.subheader(
            "📋 Đánh giá điều kiện vay vốn"
        )


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


    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "← QUAY LẠI HỒ SƠ"
        ):

            st.session_state.buoc_hien_tai = 1

            st.rerun()


    with c2:

        if st.button(
            "🔍 KIỂM TRA & TIẾP TỤC →",
            type="primary"
        ):

            dieu_kien = [

                st.session_state.nang_luc_phap_ly,

                st.session_state.muc_dich_hop_phap,

                st.session_state.phuong_an_su_dung_von,

                st.session_state.phuong_an_kha_thi,

                st.session_state.kha_nang_tra_no,

                st.session_state.su_dung_von_dung_muc_dich,

                st.session_state.tra_no_dung_han

            ]


            if "Chưa đánh giá" in dieu_kien:

                st.warning(
                    "⚠️ Vui lòng đánh giá đầy đủ 7 điều kiện trước khi tiếp tục."
                )

            else:

                st.session_state.da_kiem_tra_dieu_kien = True


                if "Không" in dieu_kien:

                    st.warning(
                        "🟡 Có ít nhất một điều kiện được đánh giá là Không. "
                        "Hồ sơ vẫn được chuyển sang bước phân tích để xem xét tổng thể."
                    )

                else:

                    st.success(
                        "🟢 Các điều kiện sơ bộ hiện đang được đánh giá là Có."
                    )


                st.session_state.buoc_hien_tai = 3

                st.rerun()


# =========================================================
# 13. BƯỚC 3 - PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif buoc == 3:

    st.title(
        "💰 BƯỚC 3: PHÂN TÍCH TÀI CHÍNH & KHẢ NĂNG TRẢ NỢ"
    )

    st.caption(
        "Đơn vị nhập liệu: triệu đồng. Dòng tiền và nghĩa vụ trả nợ tính theo tháng."
    )


    # =====================================================
    # 3.1 TÀI CHÍNH
    # =====================================================

    with st.container(border=True):

        st.subheader(
            "📈 1. Phân tích tài chính doanh nghiệp"
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


        if st.button(
            "📊 TÍNH CHỈ TIÊU TÀI CHÍNH"
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

                    /

                    st.session_state.tong_tai_san

                    * 100

                )


                st.session_state.roe = (

                    st.session_state.lnst

                    /

                    st.session_state.von_chu_so_huu

                    * 100

                )


                st.session_state.ty_le_no = (

                    st.session_state.no_phai_tra

                    /

                    st.session_state.tong_tai_san

                    * 100

                )


                st.session_state.da_phan_tich_tc = True


                st.success(
                    "✅ Đã tính các chỉ tiêu tài chính."
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


    # =====================================================
    # 3.2 KHOẢN VAY
    # =====================================================

    with st.container(border=True):

        st.subheader(
            "💳 2. Thông tin khoản vay"
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

                    /

                    st.session_state.thoi_gian_vay

                )


                tien_lai = (

                    st.session_state.so_tien_vay

                    *

                    st.session_state.lai_suat

                    /

                    100

                    /

                    12

                )


                tong_nghia_vu = (

                    st.session_state.nghia_vu_no_cu

                    +

                    tien_goc

                    +

                    tien_lai

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
    # 3.3 DSCR
    # =====================================================

    with st.container(border=True):

        st.subheader(
            "📈 3. Phân tích khả năng trả nợ - DSCR"
        )


        if st.session_state.tong_nghia_vu is None:

            st.warning(
                "⚠️ Vui lòng tính nghĩa vụ trả nợ trước."
            )

        else:

            c1, c2 = st.columns(2)


            c1.metric(
                "Dòng tiền kinh doanh/tháng",
                f"{st.session_state.dong_tien:,.2f}"
            )


            c2.metric(
                "Nghĩa vụ trả nợ/tháng",
                f"{st.session_state.tong_nghia_vu:,.2f}"
            )


            if st.button(
                "📈 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
            ):

                if st.session_state.dong_tien <= 0:

                    st.error(
                        "❌ Dòng tiền kinh doanh phải lớn hơn 0 để tính DSCR."
                    )

                else:

                    st.session_state.dscr = (

                        st.session_state.dong_tien

                        /

                        st.session_state.tong_nghia_vu

                    )


                    st.session_state.da_phan_tich_dscr = True


                    if st.session_state.dscr >= 1:

                        st.success(
                            f"🟢 DSCR = "
                            f"{st.session_state.dscr:.2f} lần. "
                            "Dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ theo mô hình."
                        )

                    else:

                        st.warning(
                            f"🟡 DSCR = "
                            f"{st.session_state.dscr:.2f} lần. "
                            "Dòng tiền hiện tại thấp hơn nghĩa vụ trả nợ."
                        )


    # =====================================================
    # 3.4 TSĐB
    # =====================================================

    with st.container(border=True):

        st.subheader(
            "🏠 4. Tài sản bảo đảm"
        )


        st.info(
            """
            TSĐB là yếu tố hỗ trợ trong thẩm định tín dụng.
            Việc đánh giá thực tế cần xem xét quyền sở hữu,
            tính pháp lý, giá trị định giá, khả năng thanh khoản
            và chính sách tín dụng của từng ngân hàng.
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

            "🏠 Giá trị tài sản bảo đảm",

            min_value=0.0,

            value=st.session_state.gia_tri_tsdb

        )


        if st.button(
            "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
        ):

            if st.session_state.co_tsdb == "Chưa đánh giá":

                st.warning(
                    "⚠️ Vui lòng xác định có hoặc không có TSĐB."
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
                    "❌ Vui lòng nhập số tiền vay trước."
                )

            else:

                st.session_state.ltv = (

                    st.session_state.so_tien_vay

                    /

                    st.session_state.gia_tri_tsdb

                    *

                    100

                )


                st.session_state.da_phan_tich_tsdb = True


                if st.session_state.ltv <= 70:

                    st.success(
                        f"🟢 LTV = "
                        f"{st.session_state.ltv:.2f}%. "
                        "Tỷ lệ vay trên giá trị TSĐB ở mức tương đối thấp."
                    )

                elif st.session_state.ltv <= 100:

                    st.warning(
                        f"🟡 LTV = "
                        f"{st.session_state.ltv:.2f}%. "
                        "Cần xem xét thêm chất lượng và khả năng thanh khoản TSĐB."
                    )

                else:

                    st.error(
                        f"🔴 LTV = "
                        f"{st.session_state.ltv:.2f}%. "
                        "Số tiền vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
                    )


    # =====================================================
    # NÚT ĐIỀU HƯỚNG
    # =====================================================

    st.divider()


    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "← QUAY LẠI ĐIỀU KIỆN"
        ):

            st.session_state.buoc_hien_tai = 2

            st.rerun()


    with c2:

        if st.button(
            "📊 XEM KẾT QUẢ THẨM ĐỊNH →",
            type="primary"
        ):

            missing = []


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
                    "Phân tích khả năng trả nợ DSCR"
                )


            if not st.session_state.da_phan_tich_tsdb:

                missing.append(
                    "Phân tích tài sản bảo đảm"
                )


            if len(missing) > 0:

                st.error(
                    "❌ Chưa thể xem kết quả. "
                    "Vui lòng hoàn thành: "
                    + ", ".join(missing)
                )

            else:

                st.session_state.buoc_hien_tai = 4

                st.rerun()


# =========================================================
# 14. BƯỚC 4 - KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif buoc == 4:

    st.title(
        "📊 BƯỚC 4: KẾT QUẢ THẨM ĐỊNH"
    )

    st.caption(
        "Kết quả được tổng hợp từ hồ sơ, điều kiện vay, tài chính, khả năng trả nợ và TSĐB."
    )


    # =====================================================
    # THÔNG TIN DOANH NGHIỆP
    # =====================================================

    with st.container(border=True):

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


    # =====================================================
    # CHỈ TIÊU CHÍNH
    # =====================================================

    st.subheader(
        "📈 CÁC CHỈ TIÊU CHÍNH"
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
    # TÍNH ĐIỂM HỖ TRỢ
    # =====================================================

    st.subheader(
        "🎯 ĐIỂM ĐÁNH GIÁ HỖ TRỢ"
    )


    diem = 0

    diem_toi_da = 100

    chi_tiet_diem = []


    # ĐIỀU KIỆN VAY
    dieu_kien = [

        st.session_state.nang_luc_phap_ly,

        st.session_state.muc_dich_hop_phap,

        st.session_state.phuong_an_su_dung_von,

        st.session_state.phuong_an_kha_thi,

        st.session_state.kha_nang_tra_no,

        st.session_state.su_dung_von_dung_muc_dich,

        st.session_state.tra_no_dung_han

    ]


    so_dieu_kien_dat = dieu_kien.count(
        "Có"
    )


    diem_dieu_kien = (

        so_dieu_kien_dat

        /

        7

        *

        30

    )


    diem += diem_dieu_kien


    chi_tiet_diem.append(

        [

            "Điều kiện vay vốn",

            f"{so_dieu_kien_dat}/7",

            f"{diem_dieu_kien:.1f}/30"

        ]

    )


    # LNST
    if st.session_state.lnst > 0:

        diem += 15

        chi_tiet_diem.append(

            [

                "LNST",

                "Tích cực",

                "15/15"

            ]

        )

    else:

        chi_tiet_diem.append(

            [

                "LNST",

                "Không dương",

                "0/15"

            ]

        )


    # ROA
    if st.session_state.roa > 0:

        diem += 10

        chi_tiet_diem.append(

            [

                "ROA",

                "Dương",

                "10/10"

            ]

        )

    else:

        chi_tiet_diem.append(

            [

                "ROA",

                "Không dương",

                "0/10"

            ]

        )


    # ROE
    if st.session_state.roe > 0:

        diem += 10

        chi_tiet_diem.append(

            [

                "ROE",

                "Dương",

                "10/10"

            ]

        )

    else:

        chi_tiet_diem.append(

            [

                "ROE",

                "Không dương",

                "0/10"

            ]

        )


    # DSCR
    if st.session_state.dscr >= 1:

        diem += 20

        chi_tiet_diem.append(

            [

                "DSCR",

                f"{st.session_state.dscr:.2f} lần",

                "20/20"

            ]

        )

    else:

        chi_tiet_diem.append(

            [

                "DSCR",

                f"{st.session_state.dscr:.2f} lần",

                "0/20"

            ]

        )


    # TSĐB
    if st.session_state.ltv is not None:

        if st.session_state.ltv <= 70:

            diem += 15

            chi_tiet_diem.append(

                [

                    "LTV",

                    f"{st.session_state.ltv:.2f}%",

                    "15/15"

                ]

            )

        else:

            chi_tiet_diem.append(

                [

                    "LTV",

                    f"{st.session_state.ltv:.2f}%",

                    "0/15"

                ]

            )

    else:

        chi_tiet_diem.append(

            [

                "TSĐB",

                "Không có TSĐB",

                "Tham khảo"

            ]

        )


    # HIỂN THỊ ĐIỂM

    c1, c2, c3 = st.columns(3)


    c1.metric(
        "ĐIỂM HỖ TRỢ",
        f"{diem:.1f}/100"
    )


    if diem >= 80:

        xep_loai = "Tốt"

    elif diem >= 65:

        xep_loai = "Khá"

    elif diem >= 50:

        xep_loai = "Trung bình"

    else:

        xep_loai = "Thấp"


    c2.metric(
        "MỨC ĐÁNH GIÁ",
        xep_loai
    )


    c3.metric(
        "ĐIỀU KIỆN ĐẠT",
        f"{so_dieu_kien_dat}/7"
    )


    st.progress(
        min(
            diem / 100,
            1.0
        )
    )


    st.divider()


    # =====================================================
    # KẾT LUẬN
    # =====================================================

    st.subheader(
        "📌 KẾT LUẬN THẨM ĐỊNH SƠ BỘ"
    )


    co_dieu_kien_khong = (

        "Không"

        in

        dieu_kien

    )


    co_chua_danh_gia = (

        "Chưa đánh giá"

        in

        dieu_kien

    )


    if co_chua_danh_gia:

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
            Cần hoàn thiện thông tin trước khi đưa ra kết luận thẩm định sơ bộ.
            """

        )


    elif co_dieu_kien_khong:

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
            Hồ sơ đang có ít nhất một điều kiện vay vốn được đánh giá là Không.
            Cần xác định nguyên nhân, bổ sung hồ sơ hoặc điều chỉnh phương án
            trước khi xem xét tiếp.

            Kết quả điểm số chỉ mang tính chất hỗ trợ và không làm thay đổi
            kết luận về điều kiện vay vốn.
            """

        )


    elif (

        st.session_state.lnst > 0

        and

        st.session_state.roa > 0

        and

        st.session_state.roe > 0

        and

        st.session_state.dscr >= 1

        and

        diem >= 65

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
            doanh nghiệp có lợi nhuận sau thuế dương, ROA và ROE dương,
            đồng thời dòng tiền hiện tại đáp ứng nghĩa vụ trả nợ theo chỉ tiêu DSCR.

            Hồ sơ có thể được chuyển sang bước thẩm định chi tiết,
            bao gồm kiểm tra pháp lý, CIC, lịch sử tín dụng,
            báo cáo tài chính, phương án kinh doanh, dòng tiền,
            tài sản bảo đảm và chính sách tín dụng nội bộ của ngân hàng.
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
            Hồ sơ chưa có đủ các tín hiệu tích cực theo mô hình hỗ trợ hiện tại.
            Cần thẩm định bổ sung tình hình tài chính, dòng tiền,
            khả năng trả nợ, phương án kinh doanh, lịch sử tín dụng
            và tài sản bảo đảm.
            """

        )


    st.divider()


    # =====================================================
    # BẢNG CHI TIẾT ĐIỂM
    # =====================================================

    st.subheader(
        "📋 CHI TIẾT ĐIỂM ĐÁNH GIÁ"
    )


    df_diem = pd.DataFrame(

        chi_tiet_diem,

        columns=[

            "Tiêu chí",

            "Đánh giá",

            "Điểm"

        ]

    )


    st.dataframe(

        df_diem,

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    # =====================================================
    # BẢNG TỔNG HỢP
    # =====================================================

    st.subheader(
        "📊 BẢNG TỔNG HỢP THẨM ĐỊNH"
    )


    ket_qua = []


    ket_qua.append(

        [

            "Năng lực pháp lý",

            "Đạt"
            if st.session_state.nang_luc_phap_ly == "Có"
            else "Cần xem xét",

            st.session_state.nang_luc_phap_ly

        ]

    )


    ket_qua.append(

        [

            "Mục đích vay vốn",

            "Đạt"
            if st.session_state.muc_dich_hop_phap == "Có"
            else "Cần xem xét",

            st.session_state.muc_dich_hop_phap

        ]

    )


    ket_qua.append(

        [

            "Phương án sử dụng vốn",

            "Đạt"
            if st.session_state.phuong_an_su_dung_von == "Có"
            else "Cần xem xét",

            st.session_state.phuong_an_su_dung_von

        ]

    )


    ket_qua.append(

        [

            "Tính khả thi phương án",

            "Đạt"
            if st.session_state.phuong_an_kha_thi == "Có"
            else "Cần xem xét",

            st.session_state.phuong_an_kha_thi

        ]

    )


    ket_qua.append(

        [

            "Khả năng tài chính trả nợ",

            "Đạt"
            if st.session_state.kha_nang_tra_no == "Có"
            else "Cần xem xét",

            st.session_state.kha_nang_tra_no

        ]

    )


    ket_qua.append(

        [

            "Lợi nhuận sau thuế",

            "Tích cực"
            if st.session_state.lnst > 0
            else "Cần xem xét",

            f"{st.session_state.lnst:,.2f} triệu đồng"

        ]

    )


    ket_qua.append(

        [

            "ROA",

            "Tích cực"
            if st.session_state.roa > 0
            else "Cần xem xét",

            f"{st.session_state.roa:.2f}%"

        ]

    )


    ket_qua.append(

        [

            "ROE",

            "Tích cực"
            if st.session_state.roe > 0
            else "Cần xem xét",

            f"{st.session_state.roe:.2f}%"

        ]

    )


    ket_qua.append(

        [

            "Tỷ lệ nợ",

            "Tham khảo",

            f"{st.session_state.ty_le_no:.2f}%"

        ]

    )


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

                "Không có TSĐB",

                "Không áp dụng LTV"

            ]

        )


    df_ket_qua = pd.DataFrame(

        ket_qua,

        columns=[

            "Tiêu chí",

            "Kết quả",

            "Chi tiết"

        ]

    )


    st.dataframe(

        df_ket_qua,

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    # =====================================================
    # NÚT ĐIỀU HƯỚNG CUỐI
    # =====================================================

    c1, c2, c3 = st.columns(3)


    with c1:

        if st.button(
            "← QUAY LẠI PHÂN TÍCH"
        ):

            st.session_state.buoc_hien_tai = 3

            st.rerun()


    with c2:

        if st.button(
            "💾 LƯU KẾT QUẢ MYSQL"
        ):

            if not MYSQL_ENABLED:

                st.info(
                    "ℹ️ MySQL đang tắt. "
                    "Hiện dữ liệu đang được lưu trong Session State."
                )

            else:

                if save_to_mysql():

                    st.success(
                        "✅ Đã lưu kết quả vào MySQL."
                    )

                else:

                    st.error(
                        "❌ Không thể lưu kết quả vào MySQL."
                    )


    with c3:

        if st.button(
            "🔄 TẠO HỒ SƠ MỚI"
        ):

            reset_application()

            st.rerun()


    st.divider()


    st.warning(

        """
        ⚠️ LƯU Ý QUAN TRỌNG

        Điểm đánh giá trong ứng dụng chỉ là điểm hỗ trợ phân tích,
        không phải hệ thống chấm điểm tín dụng chính thức.

        ROA, ROE, LNST, DSCR, LTV và tỷ lệ nợ không phải là căn cứ
        duy nhất để quyết định cho vay.

        Quyết định tín dụng thực tế cần xem xét tổng thể:
        hồ sơ pháp lý doanh nghiệp, mục đích vay vốn,
        phương án kinh doanh, báo cáo tài chính, dòng tiền,
        lịch sử tín dụng, CIC, nghĩa vụ nợ,
        khả năng trả nợ, tài sản bảo đảm
        và chính sách tín dụng của ngân hàng.

        Kết quả của ứng dụng chỉ có giá trị hỗ trợ thẩm định sơ bộ.
        """

    )


# =========================================================
# 15. FOOTER
# =========================================================

st.divider()


st.markdown(

    """
    <div class="footer">

    🏦 Công cụ hỗ trợ phân tích và thẩm định sơ bộ
    hồ sơ tín dụng doanh nghiệp

    <br><br>

    Session State • MySQL • Phân tích tài chính • DSCR • LTV

    </div>
    """,

    unsafe_allow_html=True

)
