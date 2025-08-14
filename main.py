import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

st.title("💼 MBTI 기반 직업 추천")
st.write("MBTI를 선택하면 어울리는 직업을 추천해드립니다.")

# MBTI → 추천 직업 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "변호사", "품질관리 전문가"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "INFJ": ["상담사", "작가", "심리학자"],
    "INTJ": ["데이터 분석가", "전략 기획자", "엔지니어"],
    "ISTP": ["기계공", "경찰관", "응급구조사"],
    "ISFP": ["디자이너", "물리치료사", "예술가"],
    "INFP": ["작가", "아동 상담가", "심리학자"],
    "INTP": ["연구원", "프로그래머", "교수"],
    "ESTP": ["영업 전문가", "스포츠 코치", "응급구조사"],
    "ESFP": ["배우", "이벤트 기획자", "유튜버"],
    "ENFP": ["광고 기획자", "강사", "작가"],
    "ENTP": ["기업가", "변호사", "마케팅 전문가"],
    "ESTJ": ["경영자", "군인", "프로젝트 매니저"],
    "ESFJ": ["간호사", "초등교사", "HR 전문가"],
    "ENFJ": ["리더십 코치", "교육자", "홍보 전문가"],
    "ENTJ": ["CEO", "전략가", "정치가"]
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"✅ {job}")

# 추가 정보
st.markdown("---")
st.caption("본 서비스는 참고용이며, 실제 직업 선택은 다양한 요소를 고려해야 합니다.")

