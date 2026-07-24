# =========================================================
# TIÊU ĐỀ TRANG + ẢNH BÊN PHẢI
# =========================================================

col_left, col_right = st.columns([3, 1])

with col_left:
    st.markdown(
        """
        <div class="hero-card">
            <div style="
                font-size: 14px;
                font-weight: 700;
                letter-spacing: 1px;
                color: #bfe7ff;
                margin-bottom: 8px;
            ">
                🏦 CREDIT APPRAISAL SYSTEM
            </div>

            <h1>
                HỆ THỐNG HỖ TRỢ<br>
                THẨM ĐỊNH CHO VAY DOANH NGHIỆP
            </h1>

            <p>
                Hỗ trợ thu thập thông tin, phân tích tài chính,
                đánh giá khả năng trả nợ và tổng hợp kết quả
                thẩm định sơ bộ hồ sơ tín dụng doanh nghiệp.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_right:
    st.markdown(
        """
        <div style="
            background: white;
            border-radius: 22px;
            padding: 15px;
            height: 100%;
            min-height: 190px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 30px rgba(8,43,76,0.12);
            border: 1px solid #dce8f3;
        ">
        """,
        unsafe_allow_html=True
    )

    try:
        st.image(
            "logo.jpg",
            use_container_width=True
        )
    except:
        st.markdown(
            """
            <div style="
                text-align: center;
                font-size: 80px;
                padding: 30px;
            ">
                🏦
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
