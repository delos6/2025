import streamlit as st
import random

# =======================
# 페이지 설정
# =======================
st.set_page_config(
    page_title="오늘의 기분 명언",
    page_icon="✨",
    layout="centered"
)

# =======================
# 타이틀과 설명
# =======================
st.markdown("""
<h1 style='text-align: center; color: #fff;'>
오늘의 기분에 따른 명언
</h1>
<p style='text-align: center; font-size: 18px; color: #eee;'>
당신의 기분에 맞는 메시지와 이모지로 하루를 특별하게 💫
</p>
""", unsafe_allow_html=True)

# =======================
# 기분별 명언 데이터
# =======================
mood_quotes = {
    "😊 해피함": [
        ("Count your age by friends, not years. – John Lennon", "나이를 세지 말고 친구를 세라 – 존 레논"),
        ("Happiness is not something ready made. – Dalai Lama", "행복은 이미 준비된 것이 아니다 – 달라이 라마"),
        ("행복은 준비된 자에게 온다 – Pascal", None)
    ],
    "😢 슬픔": [
        ("Tears come from the heart and not from the brain. – Leonardo da Vinci", "눈물은 마음에서 나온다 – 다빈치"),
        ("Out of difficulties grow miracles. – Jean de La Bruyère", "어려움 속에서 기적이 자란다 – 장 드 라 브뤼에르"),
        ("슬픔이 깊을수록 영혼은 더 강해진다", None)
    ],
    "😡 화남": [
        ("Anger is one letter short of danger. – Eleanor Roosevelt", "분노는 ‘위험’에서 한 글자 부족하다 – 루즈벨트"),
        ("Holding on to anger is like grasping a hot coal; you get burned. – Buddha", "분노를 붙잡는 것은 뜨거운 숯을 쥐는 것과 같아 – 부처"),
        ("자신을 지배하지 못하면, 다른 것도 지배할 수 없다. – 공자", None)
    ],
    "😐 구냥저냥": [
        ("The way to get started is to quit talking and begin doing. – Walt Disney", "시작하려면 말하는 걸 멈추고 행동하라 – 디즈니"),
        ("Do what you can, with what you have, where you are. – Theodore Roosevelt", "지금 있는 곳에서 가진 것으로 할 수 있는 것을 하라 – 루즈벨트"),
        ("평범 속에 비범이 숨어 있다", None)
    ],
    "🤩 설레임": [
        ("Shoot for the moon. Even if you miss, you'll land among the stars. – Norman Vincent Peale", "달을 향해 쏘라 – 노먼 빈센트 필"),
        ("The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt", "미래는 꿈을 믿는 사람들의 것이다 – 루즈벨트"),
        ("설레는 마음은 우주의 신호다", None)
    ],
    "🤔 싱숭생숭": [
        ("Sometimes you feel unsettled, and that's okay. – Unknown", "가끔 마음이 싱숭생숭해도 괜찮다 – 작자 미상"),
        ("Change is the only constant in life. – Heraclitus", "변화만이 인생의 유일한 상수이다 – 헤라클리토스"),
        ("혼란 속에서도 자신을 잃지 마세요", None)
    ]
}

# =======================
# 기분별 배경색과 이모지
# =======================
mood_styles = {
    "😊 해피함": {"bg": "#FFECB3", "emojis": ["😊","😃","🥳"]},
    "😢 슬픔": {"bg": "#90CAF9", "emojis": ["😢","😭","😔"]},
    "😡 화남": {"bg": "#EF9A9A", "emojis": ["😡","😠","🤬"]},
    "😐 구냥저냥": {"bg": "#B0BEC5", "emojis": ["😐","😶","😑"]},
    "🤩 설레임": {"bg": "#F48FB1", "emojis": ["🤩","✨","💫"]},
    "🤔 싱숭생숭": {"bg": "#CE93D8", "emojis": ["🤔","😕","🤯"]}
}

# =======================
# 기분 선택
# =======================
selected_mood = st.selectbox("오늘의 기분을 선택하세요:", list(mood_styles.keys()))
quote_en, quote_kr = random.choice(mood_quotes.get(selected_mood, [("","")]))
bg_color = mood_styles[selected_mood]["bg"]
emoji_list = mood_styles[selected_mood]["emojis"]

# =======================
# 명언 카드 출력
# =======================
st.markdown(f"""
<div style="
    background-color: {bg_color};
    padding: 30px;
    border-radius: 15px;
    box-shadow: 2px 2px 12px #aaaaaa;
    text-align: center;
    animation: fadeIn 1.5s;">
    <h2 style='color: #333;'>{selected_mood}</h2>
    <p style='font-size:22px; color:#222;'>{quote_en}</p>
    {'<p style="font-size:18px; color:#555; margin-top:10px;">'+quote_kr+'</p>' if quote_kr else ''}
</div>
<style>
@keyframes fadeIn {{
    from {{opacity:0; transform: translateY(-20px);}}
    to {{opacity:1; transform: translateY(0);}}
}}
</style>
""", unsafe_allow_html=True)

# =======================
# 기분별 이모지 애니메이션
# =======================
emoji_animation = "<style>@keyframes floatUp {{0% {{ transform: translateY(0); opacity:1; }} 100% {{ transform: translateY(-200px); opacity:0; }} }}"
for i, e in enumerate(emoji_list):
    emoji_animation += f".emoji{i} {{ position: fixed; bottom: 10px; left:{30+i*20}%; font-size:50px; animation: floatUp 4s ease-in-out infinite; animation-delay:{i*0.5}s; }}"
emoji_animation += "</style>"
emoji_animation += "".join([f"<div class='emoji{i}'>{e}</div>" for i, e in enumerate(emoji_list)])
st.markdown(emoji_animation, unsafe_allow_html=True)

# =======================
# 구분선과 캡션
# =======================
st.markdown("---")
st.caption("🌟 Made with ❤️ using Streamlit 🌟")
