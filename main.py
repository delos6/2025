import streamlit as st

# 페이지 설정
st.set_page_config(page_title="💎 MBTI 명품 브랜드 추천", page_icon="👜", layout="centered")

# 타이틀
st.markdown("""
<h1 style='text-align: center; color: gold;'>
💎 MBTI 기반 명품 브랜드 추천 🛍
</h1>
<p style='text-align: center; font-size: 18px; color: #444;'>
당신의 성격 유형에 어울리는 명품 브랜드를 찾아드립니다. <br> 
✨ 오늘은 어떤 럭셔리 무드를 입어볼까요?
</p>
""", unsafe_allow_html=True)

# MBTI → 명품 브랜드 매핑
mbti_brands = {
    "ISTJ": ["👜 Louis Vuitton", "⌚ Rolex", "👔 Burberry"],
    "ISFJ": ["🩰 Chanel", "💍 Tiffany & Co.", "👗 Dior"],
