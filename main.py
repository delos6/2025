import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌈 MBTI 직업 추천 💼", page_icon="💎", layout="centered")

# 제목 영역
st.markdown("""
<h1 style='text-align: center; color: #FF69B4;'>
🌟 MBTI 기반 직업 추천 💼🎯
</h1>
<p style='text-align: center; font-size: 18px;'>
당신의 성격 유형에 맞는 최고의 직업을 찾아드립니다 💖 <br>
🌈 MBTI + 직업 정보로 미래를 준비해보세요 ✨
</p>
""", unsafe_allow_html=True)

# MBTI 데이터
mbti_jobs = {
    "ISTJ": ["📊 회계사", "⚖️ 변호사", "🛠 품질관리 전문가"],
    "ISFJ": ["🩺 간호사", "📚 교사", "🤝 사회복지사"],
    "INFJ": ["🗣 상담사", "✍️ 작가", "🧠 심리학자"],
    "INTJ": ["📈 데이터 분석가", "📝 전략 기획자", "🔧 엔지니어"],
    "ISTP": ["⚙️ 기계공", "🚓 경찰관", "🚑 응급구조사"],
    "ISFP": ["🎨 디자이너", "🧘 물리치료사", "🎭 예술가"],
    "INFP": ["📖 작가", "👶 아동 상담가", "🧠 심리학자"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "🎓 교수"],
    "ESTP": ["💼 영업 전문가", "🏆 스포츠 코치", "🚑 응급구조사"],
    "ESFP": ["🎤 배우", "🎉 이벤트 기획자", "📹 유튜버"],
    "ENFP": ["📢 광고 기획자", "🎯 강사", "✍️ 작가"],
    "ENTP": ["🚀 기업가", "⚖️ 변호사", "📊 마케팅 전문가"],
    "ESTJ": ["📋 경영자", "🪖 군인", "📂 프로젝트 매니저"],
    "ESFJ": ["🩺 간호사", "📚 초등교사", "💼 HR 전문가"],
    "ENFJ": ["🏅 리더십 코치", "👩‍🏫 교육자", "📢 홍보 전문가"],
    "ENTJ": ["👑 CEO", "🧠 전략가", "🏛 정치가"]
}

# 선택 박스
selected_mbti = st.selectbox("✨ 당신의 MBTI를 선택하세요 💖", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.markdown(f"""
    <h2 style='color: #FFD700;'>🔍 {selected_mbti} 유형의 추천 직업</h2>
    """, unsafe_allow_html=True)

    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<p style='font-size: 20px;'>✅ {job}</p>", unsafe_allow_html=True)

    # 팁 메시지
    st.success("💡 팁: MBTI는 참고용! 다양한 경험을 해보며 진짜 적성을 찾아보세요 🌱")

# 구분선
st.markdown("---")

# 푸터
st.markdown("""
<p style='text-align: center; font-size: 14px;'>
🌟 Made with ❤️ using Streamlit 🌟
</p>
""", unsafe_allow_html=True)
