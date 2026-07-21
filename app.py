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
# 2. LOGO
# =========================================================

LOGO_PATH = Path(__file__).parent / "logo.png"


# =========================================================
# 3. CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

section[data-testid="stSidebar"] * {
    color: white;
}

.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
}

.sub-title {
    font-size: 16px;
    color: #64748b;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 3px 10px rgba(15,23,42,.05);
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 4. SIDEBAR
# =========================================================

with st.sidebar:

    if LOGO_PATH.exists():
        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

    st.divider()

    st.markdown(
        "### 🏦 HỆ THỐNG THẨM ĐỊNH"
    )

    st.caption(
        "Hỗ trợ thẩm định cho vay doanh nghiệp"
    )

    st.divider()

    menu = st.radio(
        "Chọn chức năng",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption("Phiên bản 1.0")
    st.caption("© 2026")


# =========================================================
# 5. HEADER
# =========================================================

col_logo, col_header = st.columns([1, 5])

with col_logo:

    if LOGO_PATH.exists():
        st.image(
            str(LOGO_PATH),
            width=130
        )
    else:
        st.write("🏦")


with col_header:

    st.markdown(
        '<div class="main-title">'
        '🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH'
        '<br>'
        'CHO VAY DOANH NGHIỆP'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Điều kiện vay vốn • Phân tích tài chính • '
        'Khả năng trả nợ • Tài sản bảo đảm'
        '</div>',
        unsafe_allow_html=True
    )


st.divider()


# =========================================================
# 6. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.info("""
    👋 **Chào mừng bạn đến với Hệ thống hỗ trợ thẩm định
    cho vay doanh nghiệp**

    Hệ thống hỗ trợ kiểm tra điều kiện vay vốn,
    phân tích tình hình tài chính, đánh giá khả năng trả nợ
    và phân tích tài sản bảo đảm.
    """)

    st.subheader("📌 Các nhóm đánh giá")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("⚖️", "Điều kiện vay")
    c2.metric("💰", "Tài chính")
    c3.metric("💳", "Khả năng trả nợ")
    c4.metric("🏠", "TSĐB")

    st.divider()

    st.subheader("📋 Quy trình")

    st.write("""
    **Bước 1:** Kiểm tra thông tin pháp lý doanh nghiệp.

    **Bước 2:** Kiểm tra mục đích vay và phương án sử dụng vốn.

    **Bước 3:** Phân tích khả năng tài chính và trả nợ.

    **Bước 4:** Đánh giá tài sản bảo đảm nếu có.

    **Bước 5:** Tổng hợp kết quả thẩm định.

    **Bước 6:** Đưa ra kết luận hỗ trợ.
    """)

    st.warning("""
    ⚠️ Kết quả của ứng dụng chỉ mang tính chất hỗ trợ thẩm định.
    Quyết định cho vay thực tế thuộc thẩm quyền của tổ chức tín dụng
    và phải tuân thủ quy định pháp luật, chính sách tín dụng nội bộ
    và kết quả thẩm định hồ sơ thực tế.
    """)


# =========================================================
# 7. HỒ SƠ DOANH NGHIỆP
# =========================================================

if menu == "🏢 Hồ sơ doanh nghiệp":

    st.header("🏢 Hồ sơ doanh nghiệp")

    st.subheader("Thông tin pháp lý")

    c1, c2 = st.columns(2)

    with c1:

        ten_dn = st.text_input(
            "Tên doanh nghiệp"
        )

        ma_so = st.text_input(
            "Mã số doanh nghiệp"
        )

    with c2:

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
            ]
        )

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=3
        )

    st.subheader("Thông tin khoản vay")

    muc_dich_vay = st.selectbox(
        "Mục đích vay",
        [
            "Bổ sung vốn lưu động",
            "Mua nguyên vật liệu",
            "Đầu tư máy móc thiết bị",
            "Mở rộng sản xuất",
            "Mua tài sản cố định",
            "Khác"
        ]
    )

    muc_dich_hop_phap = st.selectbox(
        "Mục đích vay có phù hợp quy định pháp luật?",
        [
            "Có",
            "Không"
        ]
    )

    phuong_an = st.text_area(
        "Mô tả phương án sử dụng vốn",
        height=150
    )

    phuong_an_kha_thi = st.selectbox(
        "Phương án sử dụng vốn có khả thi?",
        [
            "Có",
            "Không",
            "Chưa đánh giá"
        ]
    )

    st.success(
        "Thông tin doanh nghiệp đã được nhập."
    )


# =========================================================
# 8. ĐIỀU KIỆN VAY VỐN
# =========================================================

if menu == "⚖️ Điều kiện vay vốn":

    st.header(
        "⚖️ Kiểm tra điều kiện vay vốn"
    )

    st.info("""
    **Căn cứ mô hình:** Điều kiện vay vốn được xây dựng
    theo các điều kiện cốt lõi tại Điều 7 Thông tư 39/2016/TT-NHNN
    đã được sửa đổi, bổ sung bởi Thông tư 12/2024/TT-NHNN.

    Các chỉ tiêu ROA, ROE, tỷ lệ nợ, DSCR và LTV là chỉ tiêu
    hỗ trợ phân tích tín dụng, không phải điều kiện pháp lý
    bắt buộc chung cho mọi doanh nghiệp.
    """)

    st.subheader(
        "1️⃣ Kiểm tra điều kiện pháp lý và mục đích vay"
    )

    nang_luc_phap_ly = st.selectbox(
        "Doanh nghiệp có năng lực pháp luật dân sự?",
        [
            "Có",
            "Không"
        ]
    )

    muc_dich = st.selectbox(
        "Mục đích sử dụng vốn có hợp pháp?",
        [
            "Có",
            "Không"
        ]
    )

    co_phuong_an = st.selectbox(
        "Có phương án sử dụng vốn?",
        [
            "Có",
            "Không"
        ]
    )

    phuong_an_kha_thi = st.selectbox(
        "Phương án sử dụng vốn có khả thi?",
        [
            "Có",
            "Không",
            "Chưa đánh giá"
        ]
    )

    kha_nang_tra_no = st.selectbox(
        "Có khả năng tài chính để trả nợ?",
        [
            "Có",
            "Không",
            "Chưa đánh giá"
        ]
    )

    st.subheader(
        "2️⃣ Cam kết của khách hàng"
    )

    dung_muc_dich = st.selectbox(
        "Cam kết sử dụng vốn đúng mục đích?",
        [
            "Có",
            "Không"
        ]
    )

    tra_no_dung_han = st.selectbox(
        "Có khả năng và cam kết hoàn trả nợ đúng hạn?",
        [
            "Có",
            "Không"
        ]
    )

    st.divider()

    if st.button(
        "⚖️ KIỂM TRA ĐIỀU KIỆN VAY VỐN"
    ):

        dieu_kien = [
            nang_luc_phap_ly == "Có",
            muc_dich == "Có",
            co_phuong_an == "Có",
            phuong_an_kha_thi == "Có",
            kha_nang_tra_no == "Có",
            dung_muc_dich == "Có",
            tra_no_dung_han == "Có"
        ]

        so_dieu_kien_dat = sum(dieu_kien)

        st.subheader(
            "📊 Kết quả kiểm tra"
        )

        st.metric(
            "Số điều kiện đạt",
            f"{so_dieu_kien_dat}/7"
        )

        if all(dieu_kien):

            st.success("""
            🟢 **ĐẠT ĐIỀU KIỆN SƠ BỘ**

            Doanh nghiệp đáp ứng các điều kiện được nhập
            trong mô hình kiểm tra sơ bộ.

            Hồ sơ có thể chuyển sang bước thẩm định tín dụng
            chi tiết.
            """)

        else:

            st.error("""
            🔴 **CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ**

            Có ít nhất một điều kiện chưa đáp ứng.
            Cần kiểm tra và bổ sung hồ sơ trước khi xem xét
            cấp tín dụng.
            """)


# =========================================================
# 9. PHÂN TÍCH TÀI CHÍNH
# =========================================================

if menu == "💰 Phân tích tài chính":

    st.header(
        "💰 Phân tích tài chính"
    )

    st.caption(
        "Đơn vị: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        doanh_thu = st.number_input(
            "Doanh thu",
            min_value=0.0
        )

        lnst = st.number_input(
            "Lợi nhuận sau thuế (LNST)"
        )

        tong_tai_san = st.number_input(
            "Tổng tài sản",
            min_value=0.0
        )

    with c2:

        von_chu_so_huu = st.number_input(
            "Vốn chủ sở hữu",
            min_value=0.0
        )

        no_phai_tra = st.number_input(
            "Nợ phải trả",
            min_value=0.0
        )

        dong_tien = st.number_input(
            "Dòng tiền từ hoạt động kinh doanh"
        )

    if st.button(
        "📊 PHÂN TÍCH TÀI CHÍNH"
    ):

        if tong_tai_san <= 0:

            st.error(
                "Tổng tài sản phải lớn hơn 0."
            )

        elif von_chu_so_huu <= 0:

            st.error(
                "Vốn chủ sở hữu phải lớn hơn 0."
            )

        else:

            roa = (
                lnst
                / tong_tai_san
                * 100
            )

            roe = (
                lnst
                / von_chu_so_huu
                * 100
            )

            ty_le_no = (
                no_phai_tra
                / tong_tai_san
                * 100
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "ROA",
                f"{roa:.2f}%"
            )

            c2.metric(
                "ROE",
                f"{roe:.2f}%"
            )

            c3.metric(
                "Tỷ lệ nợ",
                f"{ty_le_no:.2f}%"
            )

            chart = pd.DataFrame(
                {
                    "Chỉ tiêu": [
                        "ROA",
                        "ROE",
                        "Tỷ lệ nợ"
                    ],

                    "Giá trị": [
                        roa,
                        roe,
                        ty_le_no
                    ]
                }
            )

            st.bar_chart(
                chart.set_index(
                    "Chỉ tiêu"
                )
            )


# =========================================================
# 10. KHOẢN VAY VÀ KHẢ NĂNG TRẢ NỢ
# =========================================================

if menu == "💳 Thông tin khoản vay":

    st.header(
        "💳 Thông tin khoản vay"
    )

    st.caption(
        "Đơn vị: triệu đồng"
    )

    c1, c2 = st.columns(2)

    with c1:

        so_tien_vay = st.number_input(
            "Số tiền vay",
            min_value=0.0
        )

        thoi_gian_vay = st.number_input(
            "Thời hạn vay (tháng)",
            min_value=1,
            value=12
        )

    with c2:

        lai_suat = st.number_input(
            "Lãi suất cho vay (%/năm)",
            min_value=0.0
        )

        nghia_vu_no_cu = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0
        )

    if st.button(
        "💳 PHÂN TÍCH KHẢ NĂNG TRẢ NỢ"
    ):

        tien_goc = (
            so_tien_vay
            / thoi_gian_vay
        )

        tien_lai = (
            so_tien_vay
            * lai_suat
            / 100
            / 12
        )

        no_moi = (
            tien_goc
            + tien_lai
        )

        tong_nghia_vu = (
            nghia_vu_no_cu
            + no_moi
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Gốc/tháng",
            f"{tien_goc:,.2f}"
        )

        c2.metric(
            "Lãi tháng đầu",
            f"{tien_lai:,.2f}"
        )

        c3.metric(
            "Tổng nghĩa vụ/tháng",
            f"{tong_nghia_vu:,.2f}"
        )

        st.info("""
        ℹ️ Nghĩa vụ trả nợ chỉ là một yếu tố để đánh giá
        khả năng tài chính. Khi thẩm định thực tế cần phân tích
        dòng tiền, doanh thu, chi phí, lịch sử tín dụng và
        các nghĩa vụ nợ khác của doanh nghiệp.
        """)


# =========================================================
# 11. TÀI SẢN BẢO ĐẢM
# =========================================================

if menu == "🏠 Tài sản bảo đảm":

    st.header(
        "🏠 Tài sản bảo đảm"
    )

    st.info("""
    Tài sản bảo đảm là một yếu tố hỗ trợ quản trị rủi ro tín dụng.
    Không nên sử dụng LTV như một điều kiện pháp lý chung áp dụng
    cho mọi khoản vay doanh nghiệp.
    """)

    co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        [
            "Có",
            "Không"
        ]
    )

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0
    )

    so_tien_vay_tsdb = st.number_input(
        "Số tiền vay",
        min_value=0.0
    )

    if st.button(
        "🏠 PHÂN TÍCH TÀI SẢN BẢO ĐẢM"
    ):

        if co_tsdb == "Không":

            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )

        elif gia_tri_tsdb <= 0:

            st.error(
                "Giá trị TSĐB phải lớn hơn 0."
            )

        else:

            ltv = (
                so_tien_vay_tsdb
                / gia_tri_tsdb
                * 100
            )

            st.metric(
                "LTV",
                f"{ltv:.2f}%"
            )

            if ltv <= 70:

                st.success(
                    "🟢 Tỷ lệ khoản vay/giá trị TSĐB "
                    "ở mức tương đối thấp theo mô hình minh họa."
                )

            elif ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng "
                    "thanh khoản của tài sản bảo đảm."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

if menu == "📊 Kết quả thẩm định":

    st.header(
        "📊 KẾT QUẢ THẨM ĐỊNH"
    )

    st.subheader(
        "🎯 Mô hình đánh giá"
    )

    st.write("""
    Hệ thống có thể tổng hợp các nhóm tiêu chí:

    **Nhóm 1 – Điều kiện vay vốn theo quy định:**

    - Tư cách pháp lý của doanh nghiệp.
    - Mục đích vay hợp pháp.
    - Phương án sử dụng vốn khả thi.
    - Khả năng tài chính để trả nợ.
    - Cam kết sử dụng vốn đúng mục đích.
    - Cam kết hoàn trả nợ đầy đủ, đúng hạn.

    **Nhóm 2 – Phân tích tín dụng hỗ trợ:**

    - LNST.
    - ROA.
    - ROE.
    - Tỷ lệ nợ.
    - Dòng tiền.
    - Khả năng trả nợ.
    - LTV.
    - Giá trị tài sản bảo đảm.
    """)

    st.warning("""
    ⚠️ Lưu ý: ROA, ROE, tỷ lệ nợ và LTV không phải là
    các điều kiện pháp lý bắt buộc chung để doanh nghiệp
    được vay vốn. Đây là các chỉ tiêu hỗ trợ phân tích
    và có thể được ngân hàng sử dụng theo chính sách tín dụng
    và mô hình quản trị rủi ro của mình.
    """)

    st.info("""
    💡 **Kết luận:** Việc đáp ứng điều kiện pháp lý chỉ là
    bước đầu. Quyết định cho vay còn phụ thuộc vào kết quả
    thẩm định tín dụng, khả năng trả nợ, mục đích sử dụng vốn,
    hồ sơ tài chính, lịch sử tín dụng, tài sản bảo đảm (nếu có)
    và chính sách của tổ chức tín dụng.
    """)


# =========================================================
# 13. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH CHO VAY DOANH NGHIỆP

    <br>

    Điều kiện vay vốn • Phân tích tài chính •
    Khả năng trả nợ • Tài sản bảo đảm

    <br><br>

    © 2026

    </div>
    """,
    unsafe_allow_html=True
)
