import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="🌈 오늘의 기분 명언", page_icon="✨", layout="centered")

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
    "😊 행복해요": [
        "Count your age by friends, not years. Count your life by smiles, not tears. – John Lennon",
        "행복은 준비된 자에게 온다 – Pascal",
        "Happiness is not something ready made. It com
