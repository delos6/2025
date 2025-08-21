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

# 기분별 명언
mood_quotes = {
    "😊 해피해피함": [
        ("Count your age by friends, not years. – John Lennon", "나이를 세지 말고 친구를 세라 – 존 레논"),
        ("Happiness is not something ready made. – Dalai Lama", "행복은 이미 준비된 것이 아니다 – 달라이 라마")
    ],
    "😢 슬퍼요": [
        ("Tears come from the heart. – Leonardo da Vinci", "눈물은 마음에서 나온다 – 레오나르도 다빈치"),
        ("Out of difficulties grow miracles. – Jean de La Bruyère", "어려움 속에서 기적이 자란다 – 장 드 라 브뤼에르")
    ],
    "😡 화가 나요": [
        ("Anger is one letter short of danger. – Eleanor Roosevelt", "분노는 ‘위험’에서 한 글자 부족하다 – 엘리너 루즈벨트")
    ],
    "😐 평범해요": [
        ("The way to get started is to quit talking. – Walt Disney", "시작하는 방법은 말하는 걸 멈추고 행동하는 것이다 – 월트 디즈니")
    ]
}

# 기분별 이모지
mood_emojis = {
    "😊 해피해피함": ["😊", "😃", "🥳"],
    "😢 슬퍼요": ["😢", "😭", "😔"],
    "😡 화가 나요": ["😡", "😠", "🤬"],
    "😐 평범해요": ["😐", "😶", "😑"]
}

# 기분 선택
selected_mood = st.selectbox("오늘의 기분을 선택하세요:", list(mood_quotes.keys()))

# 랜덤 명언 선택
quote_en, quote_kr = random.choice(mood_quotes[selected_mood])

# 명언 카드
st.markdown(f"""
<div style="
    background-color: #f5f5f5; 
    padding: 25px; 
    border-radius: 12px; 
    box-shadow: 1px 1px 8px #cccccc; 
    text-align: center;">
    <h2 style='color: #444444;'>{selected_mood}</h2>
    <p style='font-size:20px; color:#222222;'>{quote_en}</p>
    <p style='font-siz
