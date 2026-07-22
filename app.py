# =========================================================
# TRANG TỔNG QUAN - GIAO DIỆN CHÍNH
# =========================================================

if menu == "🏠 Tổng quan":

    # =====================================================
    # HERO - TIÊU ĐỀ CHÍNH
    # =====================================================

    st.markdown(
        """
        <div class="hero-container">

            <div class="hero-icon">
                🏦
            </div>

            <div class="hero-content">

                <h1>
                    HỆ THỐNG HỖ TRỢ THẨM ĐỊNH
                    <br>
                    CHO VAY DOANH NGHIỆP
                </h1>

                <div class="welcome-text">
                    Phân tích hồ sơ • Kiểm tra điều kiện vay •
                    Đánh giá tài chính • Khả năng trả nợ •
                    Tài sản bảo đảm • Tổng hợp kết quả
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # LỜI CHÀO
    # =====================================================

    st.markdown(
        """
        <div class="welcome-card">

            <div class="welcome-card-icon">
                👋
            </div>

            <div>
                <h2>Chào mừng bạn đến với hệ thống</h2>

                <p>
                    Ứng dụng hỗ trợ cán bộ tín dụng thực hiện
                    <b>thẩm định sơ bộ hồ sơ vay vốn doanh nghiệp</b>
                    thông qua việc kiểm tra thông tin doanh nghiệp,
                    điều kiện vay vốn, tình hình tài chính,
                    khả năng trả nợ và tài sản bảo đảm.
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # TIÊU ĐỀ TRẠNG THÁI HỒ SƠ
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            📊 TRẠNG THÁI HỒ SƠ
        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # 4 CARD TRẠNG THÁI
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    # -----------------------------------------------------
    # HỒ SƠ DOANH NGHIỆP
    # -----------------------------------------------------

    with c1:

        if st.session_state.da_luu_ho_so:

            st.markdown(
                """
                <div class="dashboard-card card-green">

                    <div class="card-icon">
                        🏢
                    </div>

                    <div class="card-title">
                        Hồ sơ doanh nghiệp
                    </div>

                    <div class="card-status">
                        ✓ ĐÃ NHẬP
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="dashboard-card card-gray">

                    <div class="card-icon">
                        🏢
                    </div>

                    <div class="card-title">
                        Hồ sơ doanh nghiệp
                    </div>

                    <div class="card-status">
                        ○ CHƯA NHẬP
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # PHÂN TÍCH TÀI CHÍNH
    # -----------------------------------------------------

    with c2:

        if st.session_state.da_phan_tich_tc:

            st.markdown(
                """
                <div class="dashboard-card card-blue">

                    <div class="card-icon">
                        💰
                    </div>

                    <div class="card-title">
                        Phân tích tài chính
                    </div>

                    <div class="card-status">
                        ✓ ĐÃ PHÂN TÍCH
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="dashboard-card card-gray">

                    <div class="card-icon">
                        💰
                    </div>

                    <div class="card-title">
                        Phân tích tài chính
                    </div>

                    <div class="card-status">
                        ○ CHƯA PHÂN TÍCH
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # KHOẢN VAY
    # -----------------------------------------------------

    with c3:

        if st.session_state.da_phan_tich_vay:

            st.markdown(
                """
                <div class="dashboard-card card-orange">

                    <div class="card-icon">
                        💳
                    </div>

                    <div class="card-title">
                        Thông tin khoản vay
                    </div>

                    <div class="card-status">
                        ✓ ĐÃ TÍNH TOÁN
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="dashboard-card card-gray">

                    <div class="card-icon">
                        💳
                    </div>

                    <div class="card-title">
                        Thông tin khoản vay
                    </div>

                    <div class="card-status">
                        ○ CHƯA TÍNH
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # TÀI SẢN BẢO ĐẢM
    # -----------------------------------------------------

    with c4:

        if st.session_state.da_phan_tich_tsdb:

            st.markdown(
                """
                <div class="dashboard-card card-purple">

                    <div class="card-icon">
                        🏠
                    </div>

                    <div class="card-title">
                        Tài sản bảo đảm
                    </div>

                    <div class="card-status">
                        ✓ ĐÃ PHÂN TÍCH
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="dashboard-card card-gray">

                    <div class="card-icon">
                        🏠
                    </div>

                    <div class="card-title">
                        Tài sản bảo đảm
                    </div>

                    <div class="card-status">
                        ○ CHƯA PHÂN TÍCH
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")
    st.write("")

    # =====================================================
    # QUY TRÌNH THẨM ĐỊNH
    # =====================================================

    st.markdown(
        """
        <div class="section-title">
            🚀 QUY TRÌNH THẨM ĐỊNH
        </div>
        """,
        unsafe_allow_html=True
    )

    p1, p2, p3 = st.columns(3)

    with p1:

        st.markdown(
            """
            <div class="process-card process-blue">

                <div class="process-number">
                    01
                </div>

                <div class="process-icon">
                    🏢
                </div>

                <h3>
                    HỒ SƠ DOANH NGHIỆP
                </h3>

                <p>
                    Nhập thông tin doanh nghiệp,
                    ngành nghề hoạt động,
                    mục đích vay và phương án
                    sử dụng vốn.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with p2:

        st.markdown(
            """
            <div class="process-card process-green">

                <div class="process-number">
                    02
                </div>

                <div class="process-icon">
                    📊
                </div>

                <h3>
                    PHÂN TÍCH VÀ ĐÁNH GIÁ
                </h3>

                <p>
                    Kiểm tra điều kiện vay vốn,
                    phân tích ROA, ROE,
                    tỷ lệ nợ và DSCR.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with p3:

        st.markdown(
            """
            <div class="process-card process-orange">

                <div class="process-number">
                    03
                </div>

                <div class="process-icon">
                    📋
                </div>

                <h3>
                    KẾT QUẢ THẨM ĐỊNH
                </h3>

                <p>
                    Tổng hợp các chỉ tiêu,
                    đánh giá rủi ro và đưa ra
                    kết luận thẩm định sơ bộ.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    # =====================================================
    # HƯỚNG DẪN SỬ DỤNG
    # =====================================================

    st.markdown(
        """
        <div class="guide-box">

            <div class="guide-icon">
                💡
            </div>

            <div>

                <h3>
                    HƯỚNG DẪN SỬ DỤNG
                </h3>

                <p>
                    Để thực hiện thẩm định, bạn nên thực hiện
                    theo trình tự:
                </p>

                <p>
                    <b>①</b> Nhập hồ sơ doanh nghiệp
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>②</b> Kiểm tra điều kiện vay vốn
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>③</b> Phân tích tài chính
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>④</b> Nhập khoản vay
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>⑤</b> Phân tích khả năng trả nợ
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>⑥</b> Đánh giá tài sản bảo đảm
                    &nbsp;&nbsp;→&nbsp;&nbsp;

                    <b>⑦</b> Xem kết quả thẩm định
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # CẢNH BÁO
    # =====================================================

    st.warning(
        """
        ⚠️ **Lưu ý:** Hệ thống chỉ hỗ trợ thẩm định sơ bộ dựa trên
        dữ liệu được nhập vào. Kết quả không thay thế quy trình
        thẩm định, phê duyệt và quyết định tín dụng chính thức
        của tổ chức tín dụng.
        """
    )
