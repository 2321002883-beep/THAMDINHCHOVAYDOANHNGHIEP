import streamlit as st
import pandas as pd

# =========================================================
# 1. CẤU HÌNH APP
# =========================================================

st.set_page_config(
    page_title="Hệ thống hỗ trợ thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

# =========================================================
# 2. CSS GIAO DIỆN
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

.title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
}

.subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 20px;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
    height: 45px;
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🏦")

    st.markdown(
        "### HỆ THỐNG THẨM ĐỊNH"
    )

    st.caption(
        "Hỗ trợ thẩm định cho vay doanh nghiệp"
    )

    st.divider()

    menu = st.radio(
        "MENU",
        [
            "🏠 Tổng quan",
            "🏢 Hồ sơ doanh nghiệp",
            "⚖️ Điều kiện vay vốn",
            "💰 Phân tích tài chính",
            "💳 Thông tin khoản vay",
            "🏠 Tài sản bảo đảm",
            "📊 Kết quả thẩm định"
        ]
    )

    st.divider()

    st.caption("Phiên bản 1.0")
    st.caption("© 2026")


# =========================================================
# 4. HEADER
# =========================================================

st.markdown(
    '<div class="title">'
    '🏦 HỆ THỐNG HỖ TRỢ THẨM ĐỊNH '
    'CHO VAY DOANH NGHIỆP'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Điều kiện vay vốn • Phân tích tài chính • '
    'Khả năng trả nợ • Tài sản bảo đảm'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# 5. TỔNG QUAN
# =========================================================

if menu == "🏠 Tổng quan":

    st.info(
        """
        👋 **Chào mừng bạn đến với Hệ thống hỗ trợ thẩm định
        cho vay doanh nghiệp.**

        Ứng dụng hỗ trợ kiểm tra điều kiện vay vốn,
        phân tích tình hình tài chính, khả năng trả nợ
        và tài sản bảo đảm.
        """
    )

    st.subheader("📌 Các nhóm chức năng")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🏢", "Hồ sơ doanh nghiệp")

    with c2:
        st.metric("⚖️", "Điều kiện vay")

    with c3:
        st.metric("💰", "Tài chính")

    with c4:
        st.metric("📊", "Thẩm định")

    st.divider()

    st.subheader("📋 Quy trình sử dụng")

    st.write(
        """
        **Bước 1:** Nhập thông tin doanh nghiệp.

        **Bước 2:** Kiểm tra điều kiện vay vốn.

        **Bước 3:** Nhập số liệu tài chính.

        **Bước 4:** Nhập thông tin khoản vay.

        **Bước 5:** Đánh giá tài sản bảo đảm.

        **Bước 6:** Tổng hợp kết quả thẩm định.
        """
    )

    st.warning(
        """
        ⚠️ Kết quả chỉ mang tính chất hỗ trợ phân tích.
        Không thay thế quyết định tín dụng thực tế của ngân hàng.
        """
    )


# =========================================================
# 6. HỒ SƠ DOANH NGHIỆP
# =========================================================

elif menu == "🏢 Hồ sơ doanh nghiệp":

    st.header("🏢 Hồ sơ doanh nghiệp")

    st.subheader("Thông tin doanh nghiệp")

    col1, col2 = st.columns(2)

    with col1:

        ten_dn = st.text_input(
            "Tên doanh nghiệp",
            placeholder="Ví dụ: Công ty TNHH ABC"
        )

        ma_so = st.text_input(
            "Mã số doanh nghiệp",
            placeholder="Ví dụ: 0312345678"
        )

        thoi_gian_hd = st.number_input(
            "Thời gian hoạt động (năm)",
            min_value=0,
            value=3
        )

    with col2:

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

    phuong_an = st.text_area(
        "Phương án sử dụng vốn",
        placeholder="Mô tả phương án sử dụng khoản vay..."
    )

    if st.button("💾 LƯU THÔNG TIN DOANH NGHIỆP"):

        if ten_dn.strip() == "":
            st.error("Vui lòng nhập tên doanh nghiệp.")

        elif ma_so.strip() == "":
            st.error("Vui lòng nhập mã số doanh nghiệp.")

        elif phuong_an.strip() == "":
            st.error("Vui lòng nhập phương án sử dụng vốn.")

        else:
            st.success(
                "✅ Đã nhập đầy đủ thông tin hồ sơ doanh nghiệp."
            )


# =========================================================
# 7. ĐIỀU KIỆN VAY VỐN
# =========================================================

elif menu == "⚖️ Điều kiện vay vốn":

    st.header("⚖️ Kiểm tra điều kiện vay vốn")

    st.info(
        """
        Phần này kiểm tra các điều kiện vay vốn cơ bản.
        ROA, ROE, tỷ lệ nợ và LTV là chỉ tiêu phân tích hỗ trợ,
        không phải điều kiện pháp lý bắt buộc chung cho mọi doanh nghiệp.
        """
    )

    st.subheader("1. Điều kiện pháp lý và mục đích vay")

    nang_luc_phap_ly = st.selectbox(
        "Doanh nghiệp có năng lực pháp luật dân sự?",
        ["Có", "Không"]
    )

    muc_dich_hop_phap = st.selectbox(
        "Mục đích vay có hợp pháp?",
        ["Có", "Không"]
    )

    st.subheader("2. Phương án sử dụng vốn")

    co_phuong_an = st.selectbox(
        "Doanh nghiệp có phương án sử dụng vốn?",
        ["Có", "Không"]
    )

    phuong_an_kha_thi = st.selectbox(
        "Phương án sử dụng vốn có khả thi?",
        ["Có", "Không", "Chưa đánh giá"]
    )

    st.subheader("3. Khả năng trả nợ")

    kha_nang_tra_no = st.selectbox(
        "Doanh nghiệp có khả năng tài chính để trả nợ?",
        ["Có", "Không", "Chưa đánh giá"]
    )

    st.subheader("4. Cam kết của doanh nghiệp")

    dung_muc_dich = st.selectbox(
        "Cam kết sử dụng vốn đúng mục đích?",
        ["Có", "Không"]
    )

    tra_no_dung_han = st.selectbox(
        "Cam kết hoàn trả nợ gốc và lãi đúng hạn?",
        ["Có", "Không"]
    )

    st.divider()

    if st.button("⚖️ KIỂM TRA ĐIỀU KIỆN VAY"):

        dieu_kien = [
            nang_luc_phap_ly == "Có",
            muc_dich_hop_phap == "Có",
            co_phuong_an == "Có",
            phuong_an_kha_thi == "Có",
            kha_nang_tra_no == "Có",
            dung_muc_dich == "Có",
            tra_no_dung_han == "Có"
        ]

        dat = sum(dieu_kien)

        st.metric(
            "Số điều kiện đạt",
            str(dat) + "/7"
        )

        if dat == 7:

            st.success(
                """
                🟢 **ĐẠT ĐIỀU KIỆN SƠ BỘ**

                Doanh nghiệp đáp ứng các điều kiện được kiểm tra.
                Hồ sơ có thể tiếp tục chuyển sang bước thẩm định tín dụng chi tiết.
                """
            )

        else:

            st.error(
                """
                🔴 **CHƯA ĐẠT ĐIỀU KIỆN SƠ BỘ**

                Doanh nghiệp chưa đáp ứng đầy đủ các điều kiện được kiểm tra.
                Cần xem xét và bổ sung hồ sơ.
                """
            )


# =========================================================
# 8. PHÂN TÍCH TÀI CHÍNH
# =========================================================

elif menu == "💰 Phân tích tài chính":

    st.header("💰 Phân tích tài chính")

    st.caption("Đơn vị: triệu đồng")

    col1, col2 = st.columns(2)

    with col1:

        doanh_thu = st.number_input(
            "Doanh thu",
            min_value=0.0
        )

        lnst = st.number_input(
            "Lợi nhuận sau thuế (LNST)",
            min_value=0.0
        )

        tong_tai_san = st.number_input(
            "Tổng tài sản",
            min_value=0.0
        )

    with col2:

        von_chu_so_huu = st.number_input(
            "Vốn chủ sở hữu",
            min_value=0.0
        )

        no_phai_tra = st.number_input(
            "Nợ phải trả",
            min_value=0.0
        )

        dong_tien = st.number_input(
            "Dòng tiền từ hoạt động kinh doanh",
            min_value=0.0
        )

    if st.button("📊 TÍNH CHỈ TIÊU TÀI CHÍNH"):

        if tong_tai_san <= 0:

            st.error(
                "Tổng tài sản phải lớn hơn 0."
            )

        elif von_chu_so_huu <= 0:

            st.error(
                "Vốn chủ sở hữu phải lớn hơn 0."
            )

        else:

            roa = lnst / tong_tai_san * 100

            roe = lnst / von_chu_so_huu * 100

            ty_le_no = no_phai_tra / tong_tai_san * 100

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "ROA",
                    f"{roa:.2f}%"
                )

            with c2:
                st.metric(
                    "ROE",
                    f"{roe:.2f}%"
                )

            with c3:
                st.metric(
                    "Tỷ lệ nợ",
                    f"{ty_le_no:.2f}%"
                )

            data = pd.DataFrame(
                {
                    "Chỉ tiêu": [
                        "ROA",
                        "ROE",
                        "Tỷ lệ nợ"
                    ],
                    "Giá trị (%)": [
                        roa,
                        roe,
                        ty_le_no
                    ]
                }
            )

            st.bar_chart(
                data.set_index("Chỉ tiêu")
            )


# =========================================================
# 9. THÔNG TIN KHOẢN VAY
# =========================================================

elif menu == "💳 Thông tin khoản vay":

    st.header("💳 Thông tin khoản vay")

    st.caption("Đơn vị: triệu đồng")

    col1, col2 = st.columns(2)

    with col1:

        so_tien_vay = st.number_input(
            "Số tiền vay",
            min_value=0.0
        )

        thoi_gian_vay = st.number_input(
            "Thời hạn vay (tháng)",
            min_value=1,
            value=12
        )

    with col2:

        lai_suat = st.number_input(
            "Lãi suất cho vay (%/năm)",
            min_value=0.0
        )

        no_hien_tai = st.number_input(
            "Nghĩa vụ trả nợ hiện tại/tháng",
            min_value=0.0
        )

    if st.button("💳 TÍNH NGHĨA VỤ TRẢ NỢ"):

        tien_goc = so_tien_vay / thoi_gian_vay

        tien_lai = (
            so_tien_vay
            * lai_suat
            / 100
            / 12
        )

        no_moi = tien_goc + tien_lai

        tong_nghia_vu = (
            no_hien_tai
            + no_moi
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Gốc/tháng",
                f"{tien_goc:,.2f}"
            )

        with c2:
            st.metric(
                "Lãi tháng đầu",
                f"{tien_lai:,.2f}"
            )

        with c3:
            st.metric(
                "Tổng nghĩa vụ/tháng",
                f"{tong_nghia_vu:,.2f}"
            )

        st.info(
            """
            Đây là cách tính minh họa theo phương pháp
            chia đều gốc hàng tháng và tính lãi trên số tiền vay ban đầu.
            Lịch trả nợ thực tế có thể khác tùy phương thức cấp tín dụng.
            """
        )


# =========================================================
# 10. TÀI SẢN BẢO ĐẢM
# =========================================================

elif menu == "🏠 Tài sản bảo đảm":

    st.header("🏠 Tài sản bảo đảm")

    st.info(
        """
        LTV là chỉ tiêu hỗ trợ đánh giá mức độ bảo đảm của khoản vay.
        Ngưỡng LTV cụ thể phụ thuộc chính sách tín dụng và loại tài sản,
        không phải ngưỡng pháp lý chung áp dụng cho mọi doanh nghiệp.
        """
    )

    co_tsdb = st.selectbox(
        "Khoản vay có tài sản bảo đảm?",
        ["Có", "Không"]
    )

    gia_tri_tsdb = st.number_input(
        "Giá trị tài sản bảo đảm",
        min_value=0.0
    )

    so_tien_vay_tsdb = st.number_input(
        "Số tiền vay",
        min_value=0.0
    )

    if st.button("🏠 ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM"):

        if co_tsdb == "Không":

            st.info(
                "Khoản vay không có tài sản bảo đảm."
            )

        elif gia_tri_tsdb <= 0:

            st.error(
                "Giá trị tài sản bảo đảm phải lớn hơn 0."
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
                    "🟢 LTV ở mức tương đối thấp theo mô hình minh họa."
                )

            elif ltv <= 100:

                st.warning(
                    "🟡 Cần xem xét thêm chất lượng và khả năng thanh khoản của TSĐB."
                )

            else:

                st.error(
                    "🔴 Số tiền vay lớn hơn giá trị TSĐB."
                )


# =========================================================
# 11. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.header("📊 KẾT QUẢ THẨM ĐỊNH")

    st.info(
        """
        Kết quả thẩm định cần được tổng hợp từ:
        điều kiện vay vốn, tình hình tài chính,
        khả năng trả nợ, mục đích sử dụng vốn
        và tài sản bảo đảm nếu có.
        """
    )

    st.subheader("🎯 Các nhóm tiêu chí")

    st.write(
        """
        **1. Điều kiện vay vốn**

        - Năng lực pháp lý.
        - Mục đích vay hợp pháp.
        - Phương án sử dụng vốn khả thi.
        - Khả năng tài chính để trả nợ.
        - Cam kết sử dụng vốn đúng mục đích.
        - Cam kết trả nợ đúng hạn.

        **2. Phân tích tài chính**

        - LNST.
        - ROA.
        - ROE.
        - Tỷ lệ nợ.
        - Dòng tiền.

        **3. Khả năng trả nợ**

        - Nghĩa vụ trả nợ hiện tại.
        - Nghĩa vụ trả nợ khoản vay mới.

        **4. Tài sản bảo đảm**

        - Giá trị TSĐB.
        - Tỷ lệ LTV.
        """
    )

    st.warning(
        """
        ⚠️ Lưu ý: ROA, ROE, tỷ lệ nợ và LTV là các chỉ tiêu
        hỗ trợ phân tích tín dụng, không phải điều kiện pháp lý
        bắt buộc chung cho mọi doanh nghiệp.
        """
    )

    st.success(
        """
        💡 **KẾT LUẬN:**

        Việc doanh nghiệp đáp ứng các điều kiện vay vốn cơ bản
        không đồng nghĩa chắc chắn được cấp tín dụng.
        Quyết định cho vay còn phụ thuộc vào kết quả thẩm định
        thực tế, khả năng trả nợ, hồ sơ tài chính, lịch sử tín dụng,
        phương án kinh doanh và chính sách của tổ chức tín dụng.
        """
    )


# =========================================================
# 12. FOOTER
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
