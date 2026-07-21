```python
import streamlit as st
import pandas as pd


# =========================================================
# 1. CẤU HÌNH ỨNG DỤNG
# =========================================================

st.set_page_config(
    page_title="Hệ thống thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. SESSION STATE
# =========================================================

# -------------------------
# Hồ sơ doanh nghiệp
# -------------------------

if "ten_dn" not in st.session_state:
    st.session_state.ten_dn = ""

if "ma_so" not in st.session_state:
    st.session_state.ma_so = ""

if "nganh_nghe" not in st.session_state:
    st.session_state.nganh_nghe = "Sản xuất"

if "thoi_gian_hd" not in st.session_state:
    st.session_state.thoi_gian_hd = 3


# -------------------------
# Điều kiện vay vốn
# -------------------------

if "nang_luc_phap_ly" not in st.session_state:
    st.session_state.nang_luc_phap_ly = "Chưa đánh giá"

if "muc_dich" not in st.session_state:
    st.session_state.muc_dich = "Chưa đánh giá"

if "co_phuong_an" not in st.session_state:
    st.session_state.co_phuong_an = "Chưa đánh giá"

if "phuong_an_kha_thi" not in st.session_state:
    st.session_state.phuong_an_kha_thi = "Chưa đánh giá"

if "kha_nang_tra_no" not in st.session_state:
    st.session_state.kha_nang_tra_no = "Chưa đánh giá"

if "dung_muc_dich" not in st.session_state:
    st.session_state.dung_muc_dich = "Chưa đánh giá"

if "tra_no_dung_han" not in st.session_state:
    st.session_state.tra_no_dung_han = "Chưa đánh giá"


# -------------------------
# Tài chính
# -------------------------

if "doanh_thu" not in st.session_state:
    st.session_state.doanh_thu = 0.0

if "lnst" not in st.session_state:
    st.session_state.lnst = 0.0

if "tong_tai_san" not in st.session_state:
    st.session_state.tong_tai_san = 0.0

if "von_chu_so_huu" not in st.session_state:
    st.session_state.von_chu_so_huu = 0.0

if "no_phai_tra" not in st.session_state:
    st.session_state.no_phai_tra = 0.0

if "dong_tien" not in st.session_state:
    st.session_state.dong_tien = 0.0

if "roa" not in st.session_state:
    st.session_state.roa = None

if "roe" not in st.session_state:
    st.session_state.roe = None

if "ty_le_no" not in st.session_state:
    st.session_state.ty_le_no = None


# -------------------------
# Khoản vay
# -------------------------

if "so_tien_vay" not in st.session_state:
    st.session_state.so_tien_vay = 0.0

if "thoi_gian_vay" not in st.session_state:
    st.session_state.thoi_gian_vay = 12

if "lai_suat" not in st.session_state:
    st.session_state.lai_suat = 0.0

if "nghia_vu_no_cu" not in st.session_state:
    st.session_state.nghia_vu_no_cu = 0.0

if "tong_nghia_vu" not in st.session_state:
    st.session_state.tong_nghia_vu = None


# -------------------------
# Tài sản bảo đảm
# -------------------------

if "co_tsdb" not in st.session_state:
    st.session_state.co_tsdb = "Chưa đánh giá"

if "gia_tri_tsdb" not in st.session_state:
    st.session_state.gia_tri_tsdb = 0.0

if "ltv" not in st.session_state:
    st.session_state.ltv = None


# =========================================================
# 3. CSS - GIAO DIỆN HIỆN ĐẠI
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       NỀN ỨNG DỤNG
    ===================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f5f8fc 0%,
            #eef4fb 50%,
            #f8fafc 100%
        );
    }


    /* =====================================================
       SIDEBAR
    ===================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #071a33 0%,
                #0b2d52 45%,
                #123f68 100%
            );
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

   
```
