import streamlit as st  # Streamlit 라이브러리 불러오기
import random  # 랜덤으로 명언 선택할 때 사용

# =======================
# 페이지 설정
# =======================
st.set_page_config(
    page_title="오늘의 기분 명언",  # 브라우저 탭 제목
    page_icon="✨",                  # 브라우저 탭 아이콘
    layout="centered"               # 앱 레이아웃을 중앙 정렬
)

# =======================
# 타이틀과 설명
# =======================
st.markdown("""
<h1 style='text-align: center; color: #333333;'>
오늘의 기분에 따른 명언
</h1>
<p style='text-align: center; font-size: 18px; color: #555555;'>
당신의 기분에 맞는 진지하고 차분한 메시지를 전해드립니다.
</p>
""", unsafe_allow_html=True)
# unsafe_allow_html=True를 통해 HTML 태그 사용 가능

# =======================
# 기분별 명언 데이터
# =======================
# 각 기분을 key로, 명언 리스트를 value로 설정
# 각 명언은 (영어, 한국어) 튜플로 구성
mood_quotes = {
    "😊 해피해피함": [
        ("Count your age by friends, not years. – John Lennon", "나이를 세지 말고 친구를 세라 – 존 레논"),
        ("Happiness is not something ready made. – Dalai Lama", "행복은 이미 준비된 것이 아니다 – 달라이 라마"),
        ("행복은 준비된 자에게 온다 – Pascal", "행복은 준비된 자에게 온다 – Pascal")
    ],
    "😢 슬퍼요": [
        ("Tears come from the heart and not from the brain. – Leonardo da Vinci", "눈물은 머리에서가 아니라 마음에서 나온다. – 레오나르도 다빈치"),
        ("Out of difficulties grow miracles. – Jean de La Bruyère", "어려움 속에서 기적이 자란다. – 장 드 라 브뤼에르"),
        ("슬픔이 깊을수록 영혼은 더 강해진다", "슬픔이 깊을수록 영혼은 더 강해진다")
    ],
    "😡 화가 나요": [
        ("Anger is one letter short of danger. – Eleanor Roosevelt", "분노는 ‘위험’에서 한 글자 부족하다 – 엘리너 루즈벨트"),
        ("Holding on to anger is like grasping a hot coal; you get burned. – Buddha", "분노를 붙잡는 것은 뜨거운 숯을 쥐는 것과 같아 결국 자신이 데인다. – 부처"),
        ("자신을 지배하지 못하면, 다른 것도 지배할 수 없다. – 공자", "자신을 지배하지 못하면, 다른 것도 지배할 수 없다. – 공자")
    ],
    "😐 평범해요": [
        ("The way to get started is to quit talking and begin doing. – Walt Disney", "시작하는 방법은 말하는 걸 멈추고 행동하는 것이다. – 월트 디즈니"),
        ("Do what you can, with what you have, where you are. – Theodore Roosevelt", "할 수 있는 것을, 가진 것으로, 지금 있는 곳에서 하라. – 시어도어 루즈벨트"),
        ("평범 속에 비범이 숨어 있다", "평범 속에 비범이 숨어 있다")
    ],
    "🤩 설레임": [
        ("Shoot for the moon. Even if you miss, you'll land among the stars. – Norman Vincent Peale", "달을 향해 쏘라. 별들 사이에 도착할 것이다. – 노먼 빈센트 필"),
        ("The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt", "미래는 자신의 꿈의 아름다움을 믿는 사람들의 것이다. – 엘리너 루즈벨트"),
        ("설레는 마음은 우주의 신호다", "설레는 마음은 우주의 신호다")
    ],
    "🤔 싱숭생숭해요": [
        ("Sometimes you feel unsettled, and that's okay. – Unknown", "가끔 마음이 싱숭생숭할 때도 있다. 그것도 괜찮다. – 작자 미상"),
        ("Change is the only constant in life. – Heraclitus", "변화만이 인생에서 유일한 상수이다. – 헤라클리토스"),
        ("혼란 속에서도 자신을 잃지 마세요", "혼란 속에서도 자신을 잃지 마세요")
    ]
}

# =======================
# 기분별 이모지 데이터
# =======================
# 선택된 기분에 맞춰서 떠오를 이모지를 설정
mood_emojis = {
    "😊 해피해피함": ["😊", "😃", "🥳"],
    "😢 슬퍼요": ["😢", "😭", "😔"],
    "😡 화가 나요": ["😡", "😠", "🤬"],
    "😐 평범해요": ["😐", "😶", "😑"],
    "🤩 설레임": ["🤩", "✨", "💫"],
    "🤔 싱숭생숭해요": ["🤔", "😕", "🤯"]
}

# =======================
# 사용자가 선택할 기분
# =======================
# selectbox의 항목을 mood_emojis 기준으로 생성 → KeyError 방지
selected_mood = st.selectbox("오늘의 기분을 선택하세요:", list(mood_emojis.keys()))

# =======================
# 랜덤 명언 선택
# =======================
# get 사용: 선택된 키가 없으면 빈 명언 반환 (안전하게 처리)
quote_en, quote_kr = random.choice(mood_quotes.get(selected_mood, [("","")]))

# =======================
# 명언 카드 출력
# =======================
# HTML + CSS를 사용하여 카드 스타일 적용
st.markdown(f"""
<div style="
    background-color: #f5f5f5; 
    padding: 25px; 
    border-radius: 12px; 
    box-shadow: 1px 1px 8px #cccccc; 
    text-align: center;">
    <h2 style='color: #444444;'>{selected_mood}</h2>
    <p style='font-size:20px; color:#222222;'>{quote_en}</p>
    <p style='font-size:18px; color:#555555; margin-top:10px;'>{quote_kr}</p>
</div>
""", unsafe_allow_html=True)

# =======================
# 기분별 이모지 애니메이션
# =======================
# @keyframes floatUp: 이모지를 위로 떠오르게 하는 CSS 애니메이션
emoji_list = mood_emojis.get(selected_mood, [])
emoji_animation = "<style>@keyframes floatUp {{ 0% {{ transform: translateY(0); opacity:1; }} 100% {{ transform: translateY(-200px); opacity:0; }} }}"

# 각 이모지를 화면에 띄우고 애니메이션 적용
for i, e in enumerate(emoji_list):
    emoji_animation += f".emoji{i} {{ position: fixed; bottom: 10px; left:{40+i*15}%; font-size:40px; animation: floatUp 4s ease-in-out infinite; animation-delay:{i*0.5}s; }}"
emoji_animation += "</style>"

# HTML div로 이모지 표시
emoji_animation += "".join([f"<div class='emoji{i}'>{e}</div>" for i, e in enumerate(emoji_list)])

# Streamlit에서 HTML 렌더링
st.markdown(emoji_animation, unsafe_allow_html=True)

# =======================
# 구분선과 캡션
# =======================
st.markdown("---")
st.caption("🌟 Made with ❤️ using Streamlit 🌟")
