import streamlit as st
import random

st.set_page_config(page_title="🌈 오늘의 기분 명언", page_icon="✨", layout="centered")

st.markdown("""
<h1 style='text-align: center; color: #FF69B4;'>
🌈 오늘의 기분에 따른 명언 ✨
</h1>
<p style='text-align: center; font-size: 18px;'>
기분에 맞는 강렬한 명언과 메시지로 당신을 응원합니다 💪🔥
</p>
""", unsafe_allow_html=True)

mood_quotes = {
    "😊 행복해요": [
        "Count your age by friends, not years. Count your life by smiles, not tears. – John Lennon 😃",
        "행복은 준비된 자에게 온다 🌸 – Pascal",
        "Happiness is not something ready made. It comes from your own actions. – Dalai Lama ☀️"
    ],
    "😢 슬퍼요": [
        "Tears come from the heart and not from the brain. – Leonardo da Vinci 💧",
        "Out of difficulties grow miracles. – Jean de La Bruyère 🌱",
        "슬픔이 깊을수록 영혼은 더 강해진다 🌑✨"
    ],
    "😡 화가 나요": [
        "Anger is one letter short of danger. – Eleanor Roosevelt 🔥",
        "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned. – Buddha 🔥🪨",
        "자신을 지배하지 못하면, 다른 것도 지배할 수 없다. ⚔️ – 공자"
    ],
    "😐 평범해요": [
        "The way to get started is to quit talking and begin doing. – Walt Disney 🎬",
        "평범 속에 비범이 숨어 있다 🌱",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt 🌍"
    ],
    "🤩 설레요": [
        "Shoot for the moon. Even if you miss, you'll land among the stars. – Norman Vincent Peale 🌌🚀",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt 🌟",
        "설레는 마음은 우주의 신호다 ✨"
    ]
}

selected_mood = st.selectbox("✨ 오늘의 기분을 선택하세요:", list(mood_quotes.keys()))

if selected_mood:
    st.markdown(f"<h2 style='color: #FFD700;'>🔍 오늘의 기분: {selected_mood}</h2>", unsafe_allow_html=True)
    quote = random.choice(mood_quotes[selected_mood])
    st.markdown(f"<p style='font-size:22px; text-align:center;'>💡 {quote}</p>", unsafe_allow_html=True)
    st.balloons()

st.markdown("---")
st.caption("🌟 Made with ❤️ using Streamlit 🌟")

