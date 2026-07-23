# =========================================================
# 12. KẾT QUẢ THẨM ĐỊNH
# =========================================================

elif menu == "📊 Kết quả thẩm định":

    st.title("📊 KẾT QUẢ THẨM ĐỊNH TÍN DỤNG DOANH NGHIỆP")

    st.info(
        """
        Kết quả được tổng hợp từ thông tin hồ sơ, điều kiện vay vốn,
        tình hình tài chính, khả năng trả nợ và tài sản bảo đảm.
        
        Đây là kết quả hỗ trợ thẩm định sơ bộ, không thay thế quyết định
        tín dụng chính thức của ngân hàng.
        """
    )

    # =====================================================
    # 1. KIỂM TRA DỮ LIỆU ĐẦU VÀO
    # =====================================================

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
            "⚠️ Chưa đủ dữ liệu để thực hiện tổng hợp kết quả thẩm định."
        )

        st.write("Các nội dung còn thiếu:")

        for item in missing:
            st.write(f"• {item}")

        st.stop()

    # =====================================================
    # 2. KIỂM TRA ĐIỀU KIỆN VAY VỐN
    # =====================================================

    dieu_kien = [
        st.session_state.nang_luc_phap_ly,
        st.session_state.muc_dich,
        st.session_state.co_phuong_an,
        st.session_state.phuong_an_kha_thi,
        st.session_state.kha_nang_tra_no,
        st.session_state.dung_muc_dich,
        st.session_state.tra_no_dung_han
    ]

    so_dieu_kien_dat = dieu_kien.count("Có")
    so_dieu_kien_khong = dieu_kien.count("Không")
    so_dieu_kien_chua_danh_gia = dieu_kien.count("Chưa đánh giá")

    # =====================================================
    # 3. ĐÁNH GIÁ TÀI CHÍNH
    # =====================================================

    lnst = st.session_state.lnst
    roa = st.session_state.roa
    roe = st.session_state.roe
    ty_le_no = st.session_state.ty_le_no

    # Đánh giá LNST
    if lnst > 0:
        danh_gia_lnst = "Tích cực"
    elif lnst == 0:
        danh_gia_lnst = "Cần xem xét"
    else:
        danh_gia_lnst = "Rủi ro"

    # Đánh giá ROA
    if roa is not None and roa > 0:
        danh_gia_roa = "Tích cực"
    else:
        danh_gia_roa = "Cần xem xét"

    # Đánh giá ROE
    if roe is not None and roe > 0:
        danh_gia_roe = "Tích cực"
    else:
        danh_gia_roe = "Cần xem xét"

    # Đánh giá tỷ lệ nợ
    if ty_le_no is not None:

        if ty_le_no <= 50:
            danh_gia_no = "Tương đối an toàn"

        elif ty_le_no <= 70:
            danh_gia_no = "Cần theo dõi"

        else:
            danh_gia_no = "Rủi ro cao"

    else:
        danh_gia_no = "Chưa đánh giá"

    # =====================================================
    # 4. ĐÁNH GIÁ KHẢ NĂNG TRẢ NỢ
    # =====================================================

    dscr = st.session_state.dscr

    if dscr is None:

        danh_gia_dscr = "Chưa tính"

    elif dscr >= 1.5:

        danh_gia_dscr = "Tốt"

    elif dscr >= 1.0:

        danh_gia_dscr = "Đạt mức tham khảo"

    else:

        danh_gia_dscr = "Rủi ro"

    # =====================================================
    # 5. ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM
    # =====================================================

    ltv = st.session_state.ltv
    co_tsdb = st.session_state.co_tsdb

    if co_tsdb == "Không":

        danh_gia_tsdb = "Không có tài sản bảo đảm"

    elif ltv is None:

        danh_gia_tsdb = "Chưa đánh giá"

    elif ltv <= 70:

        danh_gia_tsdb = "Mức bảo đảm tương đối tốt"

    elif ltv <= 100:

        danh_gia_tsdb = "Cần xem xét thêm"

    else:

        danh_gia_tsdb = "Giá trị TSĐB thấp so với khoản vay"

    # =====================================================
    # 6. THÔNG TIN KHÁCH HÀNG
    # =====================================================

    st.subheader("🏢 1. THÔNG TIN KHÁCH HÀNG")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Tên doanh nghiệp",
        st.session_state.ten_dn
    )

    c2.metric(
        "Mã số doanh nghiệp",
        st.session_state.ma_so
    )

    c3.metric(
        "Ngành nghề",
        st.session_state.nganh_nghe
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Thời gian hoạt động",
        f"{st.session_state.thoi_gian_hd} năm"
    )

    c2.metric(
        "Số tiền vay",
        f"{st.session_state.so_tien_vay:,.2f} triệu đồng"
    )

    c3.metric(
        "Thời hạn vay",
        f"{st.session_state.thoi_gian_vay} tháng"
    )

    st.divider()

    # =====================================================
    # 7. ĐIỀU KIỆN VAY VỐN
    # =====================================================

    st.subheader("⚖️ 2. ĐÁNH GIÁ ĐIỀU KIỆN VAY VỐN")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Điều kiện đạt",
        f"{so_dieu_kien_dat}/7"
    )

    c2.metric(
        "Điều kiện không đạt",
        f"{so_dieu_kien_khong}/7"
    )

    c3.metric(
        "Chưa đánh giá",
        f"{so_dieu_kien_chua_danh_gia}/7"
    )

    if so_dieu_kien_khong > 0:

        st.error(
            "🔴 Có điều kiện vay vốn đang được đánh giá là KHÔNG ĐẠT. "
            "Cần xem xét trước khi đề xuất cấp tín dụng."
        )

    elif so_dieu_kien_chua_danh_gia > 0:

        st.warning(
            "🟡 Chưa đủ thông tin để kết luận toàn bộ điều kiện vay vốn."
        )

    else:

        st.success(
            "🟢 Các điều kiện vay vốn đang được đánh giá là ĐẠT."
        )

    st.divider()

    # =====================================================
    # 8. PHÂN TÍCH TÀI CHÍNH
    # =====================================================

    st.subheader("💰 3. ĐÁNH GIÁ TÌNH HÌNH TÀI CHÍNH")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "LNST",
        f"{lnst:,.2f} triệu đồng"
    )

    c2.metric(
        "ROA",
        f"{roa:.2f}%"
    )

    c3.metric(
        "ROE",
        f"{roe:.2f}%"
    )

    c4.metric(
        "Tỷ lệ nợ",
        f"{ty_le_no:.2f}%"
    )

    tai_chinh_tot = (
        lnst > 0
        and roa > 0
        and roe > 0
        and ty_le_no <= 70
    )

    if tai_chinh_tot:

        st.success(
            "🟢 Tình hình tài chính có tín hiệu tương đối tích cực "
            "theo các chỉ tiêu đã nhập."
        )

    else:

        st.warning(
            "🟡 Tình hình tài chính còn một hoặc nhiều yếu tố cần "
            "được phân tích và thẩm định bổ sung."
        )

    st.divider()

    # =====================================================
    # 9. KHẢ NĂNG TRẢ NỢ
    # =====================================================

    st.subheader("📈 4. ĐÁNH GIÁ KHẢ NĂNG TRẢ NỢ")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Dòng tiền kinh doanh",
        f"{st.session_state.dong_tien:,.2f}"
    )

    c2.metric(
        "Nghĩa vụ trả nợ/tháng",
        f"{st.session_state.tong_nghia_vu:,.2f}"
    )

    c3.metric(
        "DSCR",
        (
            f"{dscr:.2f} lần"
            if dscr is not None
            else "Chưa tính"
        )
    )

    if dscr is None:

        st.warning(
            "🟡 Chưa có đủ dữ liệu để đánh giá DSCR."
        )

    elif dscr >= 1.5:

        st.success(
            "🟢 Khả năng trả nợ tương đối tốt theo chỉ tiêu DSCR."
        )

    elif dscr >= 1.0:

        st.warning(
            "🟡 DSCR đạt mức tham khảo nhưng cần xem xét thêm "
            "độ ổn định của dòng tiền."
        )

    else:

        st.error(
            "🔴 Dòng tiền hiện tại chưa đủ để đáp ứng nghĩa vụ trả nợ "
            "theo dữ liệu nhập."
        )

    st.divider()

    # =====================================================
    # 10. TÀI SẢN BẢO ĐẢM
    # =====================================================

    st.subheader("🏠 5. ĐÁNH GIÁ TÀI SẢN BẢO ĐẢM")

    if co_tsdb == "Có":

        c1, c2 = st.columns(2)

        c1.metric(
            "Giá trị TSĐB",
            f"{st.session_state.gia_tri_tsdb:,.2f} triệu đồng"
        )

        c2.metric(
            "LTV",
            f"{ltv:.2f}%"
            if ltv is not None
            else "Chưa tính"
        )

        if ltv <= 70:

            st.success(
                "🟢 Tỷ lệ LTV ở mức tương đối thấp. "
                "Tuy nhiên cần tiếp tục xem xét hồ sơ pháp lý, "
                "giá trị định giá và khả năng thanh khoản của tài sản."
            )

        elif ltv <= 100:

            st.warning(
                "🟡 Tỷ lệ LTV tương đối cao. Cần xem xét kỹ "
                "giá trị định giá, tính pháp lý và khả năng thanh khoản."
            )

        else:

            st.error(
                "🔴 Khoản vay lớn hơn giá trị TSĐB theo dữ liệu nhập."
            )

    else:

        st.info(
            "ℹ️ Khoản vay hiện được xác định là không có tài sản bảo đảm."
        )

    st.divider()

    # =====================================================
    # 11. KẾT LUẬN THẨM ĐỊNH
    # =====================================================

    st.subheader("📌 6. KẾT LUẬN THẨM ĐỊNH TÍN DỤNG SƠ BỘ")

    # -----------------------------------------------------
    # TRƯỜNG HỢP 1: CÓ ĐIỀU KIỆN KHÔNG ĐẠT
    # -----------------------------------------------------

    if so_dieu_kien_khong > 0:

        ket_luan = "CHƯA ĐỀ XUẤT CHO VAY"

        st.error(
            f"""
            🔴 {ket_luan}

            Hồ sơ hiện có ít nhất một điều kiện vay vốn cơ bản
            được đánh giá là không đạt. Do đó chưa có cơ sở để
            đề xuất cấp tín dụng ở thời điểm hiện tại.

            Đề nghị rà soát nguyên nhân không đạt và hoàn thiện
            hồ sơ trước khi xem xét lại.
            """
        )

    # -----------------------------------------------------
    # TRƯỜNG HỢP 2: CHƯA ĐỦ DỮ LIỆU
    # -----------------------------------------------------

    elif so_dieu_kien_chua_danh_gia > 0:

        ket_luan = "CẦN BỔ SUNG HỒ SƠ / THẨM ĐỊNH THÊM"

        st.warning(
            f"""
            🟡 {ket_luan}

            Hồ sơ chưa được đánh giá đầy đủ các điều kiện vay vốn.
            Chưa đủ cơ sở để đưa ra kết luận tín dụng sơ bộ.

            Cần bổ sung thông tin và thực hiện thẩm định đầy đủ
            trước khi xem xét quyết định cấp tín dụng.
            """
        )

    # -----------------------------------------------------
    # TRƯỜNG HỢP 3: KHẢ NĂNG TRẢ NỢ KHÔNG ĐẠT
    # -----------------------------------------------------

    elif dscr is not None and dscr < 1:

        ket_luan = "CHƯA ĐỀ XUẤT CHO VAY"

        st.error(
            f"""
            🔴 {ket_luan}

            Dòng tiền hiện tại theo dữ liệu nhập chưa đủ để đáp ứng
            nghĩa vụ trả nợ dự kiến. Đây là yếu tố rủi ro quan trọng
            cần được xem xét trước khi cấp tín dụng.

            Có thể xem xét lại quy mô khoản vay, thời hạn vay,
            nguồn trả nợ hoặc phương án kinh doanh.
            """
        )

    # -----------------------------------------------------
    # TRƯỜNG HỢP 4: HỒ SƠ TƯƠNG ĐỐI TỐT
    # -----------------------------------------------------

    elif (
        lnst > 0
        and roa > 0
        and roe > 0
        and dscr is not None
        and dscr >= 1
    ):

        ket_luan = "CÓ THỂ XEM XÉT CHO VAY"

        st.success(
            f"""
            🟢 {ket_luan}

            Hồ sơ đáp ứng các điều kiện vay vốn đang được đánh giá.
            Doanh nghiệp có kết quả kinh doanh dương và các chỉ tiêu
            tài chính có tín hiệu tích cực. Khả năng trả nợ theo DSCR
            đạt mức từ 1 lần trở lên.

            Hồ sơ có thể được chuyển sang bước thẩm định tín dụng
            chi tiết và phê duyệt theo quy trình, hạn mức và chính sách
            tín dụng của ngân hàng.
            """
        )

    # -----------------------------------------------------
    # TRƯỜNG HỢP 5: CẦN THẨM ĐỊNH BỔ SUNG
    # -----------------------------------------------------

    else:

        ket_luan = "CẦN THẨM ĐỊNH BỔ SUNG"

        st.warning(
            f"""
            🟡 {ket_luan}

            Hồ sơ chưa có đủ các yếu tố tích cực để đề xuất cho vay
            ngay ở bước thẩm định sơ bộ.

            Cần phân tích thêm tình hình tài chính, dòng tiền,
            khả năng trả nợ, phương án sử dụng vốn, lịch sử tín dụng,
            tài sản bảo đảm và các yếu tố rủi ro liên quan.
            """
        )

    st.divider()

    # =====================================================
    # 12. BẢNG TỔNG HỢP THẨM ĐỊNH
    # =====================================================

    st.subheader("📋 7. BẢNG TỔNG HỢP KẾT QUẢ THẨM ĐỊNH")

    ket_qua = [

        [
            "Điều kiện vay vốn",
            f"{so_dieu_kien_dat}/7 đạt",
            "Đạt" if so_dieu_kien_khong == 0
            and so_dieu_kien_chua_danh_gia == 0
            else "Cần xem xét"
        ],

        [
            "LNST",
            f"{lnst:,.2f} triệu đồng",
            danh_gia_lnst
        ],

        [
            "ROA",
            f"{roa:.2f}%",
            danh_gia_roa
        ],

        [
            "ROE",
            f"{roe:.2f}%",
            danh_gia_roe
        ],

        [
            "Tỷ lệ nợ",
            f"{ty_le_no:.2f}%",
            danh_gia_no
        ],

        [
            "DSCR",
            f"{dscr:.2f} lần"
            if dscr is not None
            else "Chưa tính",
            danh_gia_dscr
        ],

        [
            "Tài sản bảo đảm",
            (
                f"LTV {ltv:.2f}%"
                if ltv is not None
                else "Không có TSĐB"
            ),
            danh_gia_tsdb
        ],

        [
            "KẾT LUẬN",
            ket_luan,
            "Kết quả thẩm định sơ bộ"
        ]
    ]

    df_ket_qua = pd.DataFrame(
        ket_qua,
        columns=[
            "Nội dung thẩm định",
            "Kết quả",
            "Đánh giá"
        ]
    )

    st.dataframe(
        df_ket_qua,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # 13. ĐỀ XUẤT TÍN DỤNG
    # =====================================================

    st.subheader("📝 8. ĐỀ XUẤT TÍN DỤNG SƠ BỘ")

    if ket_luan == "CÓ THỂ XEM XÉT CHO VAY":

        st.info(
            f"""
            **Đề xuất:** Có thể chuyển hồ sơ sang bước thẩm định
            tín dụng chi tiết.

            **Khoản vay đề nghị:** 
            {st.session_state.so_tien_vay:,.2f} triệu đồng

            **Thời hạn:** 
            {st.session_state.thoi_gian_vay} tháng

            **Lãi suất nhập:** 
            {st.session_state.lai_suat:.2f}%/năm

            **Điều kiện:** 
            Tiếp tục kiểm tra hồ sơ pháp lý, CIC/lịch sử tín dụng,
            phương án kinh doanh, nguồn trả nợ, tài sản bảo đảm,
            khả năng thanh khoản và các điều kiện tín dụng khác
            trước khi phê duyệt.
            """
        )

    elif ket_luan == "CHƯA ĐỀ XUẤT CHO VAY":

        st.error(
            """
            **Đề xuất:** Chưa đề xuất cấp tín dụng tại thời điểm
            thẩm định sơ bộ.

            Doanh nghiệp cần khắc phục các yếu tố rủi ro hoặc
            bổ sung thông tin trước khi xem xét lại.
            """
        )

    else:

        st.warning(
            """
            **Đề xuất:** Chưa đủ cơ sở để đề xuất cấp tín dụng.

            Cần bổ sung hồ sơ và thực hiện thẩm định chi tiết
            trước khi đưa ra quyết định tín dụng.
            """
        )

    # =====================================================
    # 14. LƯU Ý
    # =====================================================

    st.warning(
        """
        ⚠️ LƯU Ý QUAN TRỌNG

        Kết quả trên chỉ là kết quả hỗ trợ thẩm định sơ bộ.

        Quyết định cấp tín dụng thực tế cần căn cứ vào:
        • Hồ sơ pháp lý và tư cách pháp nhân của doanh nghiệp.
        • Mục đích vay và tính hợp pháp của mục đích sử dụng vốn.
        • Phương án sản xuất kinh doanh và hiệu quả phương án.
        • Báo cáo tài chính và chất lượng tài sản.
        • Dòng tiền và nguồn trả nợ thực tế.
        • Lịch sử tín dụng và thông tin tín dụng.
        • Nghĩa vụ nợ hiện tại.
        • Tài sản bảo đảm và hồ sơ pháp lý của tài sản.
        • Kết quả thẩm định thực tế của ngân hàng.
        • Chính sách tín dụng và thẩm quyền phê duyệt của tổ chức tín dụng.

        ROA, ROE, LNST, DSCR và LTV chỉ là các chỉ tiêu hỗ trợ
        phân tích, không phải là căn cứ duy nhất để quyết định
        doanh nghiệp được vay hoặc không được vay.
        """
    )
