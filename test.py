import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="오늘의 기분 명언", page_icon="✨", layout="centered")

# 타이틀
st.markdown("""
<h1 style='text-align: center; color: #333333;'>
오늘의 기분에 따른 명언
</h1>
<p style='text-align: center; font-size: 18px; color: #555555;'>
당신의 기분에 맞는 진지하고 차분한 메시지를 전해드립니다.
</p>
""", unsafe_allow_html=True)

# 기분별 명언 (모든 문자열 한 줄)
mood_quotes = {
    "😊 행복해요": [
        "Count your age by friends, not years. Count your life by smiles, not tears. – John Lennon",
        "행복은 준비된 자에게 온다 – Pascal",
        "Happiness is not something ready made. It comes from your own actions. – Dalai Lama"
    ],
    "😢 슬퍼요": [
        "Tears come from the heart and not from the brain. – Leonardo da Vinci",
        "Out of difficulties grow miracles. – Jean de La Bruyère",
        "슬픔이 깊을수록 영혼은 더 강해진다"
    ],
    "😡 화가 나요": [
        "Anger is one letter short of danger. – Eleanor Roosevelt",
        "Holding on to anger is like grasping a hot coal with intent to throw it; you get burned. – Buddha",
        "자신을 지배하지 못하면, 다른 것도 지배할 수 없다. – 공자"
    ],
    "😐 평범해요": [
        "The way to get started is to quit talking and begin doing. – Walt Disney",
        "평범 속에 비범이 숨어 있다",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt"
    ],
    "🤩 설레요": [
        "Shoot for the moon. Even if you miss, you'll land among the stars. – Norman Vincent Peale",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "설레는 마음은 우주의 신호다"
    ]
}

# 기분 선택
selected_mood = st.selectbox("오늘의 기분을 선택하세요:", list(mood_quotes.keys()))

# 명언 랜덤 선택
quote = random.choice(mood_quotes[selected_mood])

# 카드 스타일 출력 (진지한 배경)
st.markdown(f"""
<div style="
    background-color: #f5f5f5; 
    padding: 25px; 
    border-radius: 12px; 
    box-shadow: 1px 1px 8px #cccccc; 
    text-align: center;">
    <h2 style='color: #444444;'>{selected_mood}</h2>
    <p style='font-size:20px; color:#222222;'>{quote}</p>
</div>
""", unsafe_allow_html=True)

st.balloons()

st.markdown("---")
st.caption("🌟 Made with ❤️ using Streamlit 🌟")
