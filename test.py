import streamlit as st

# 페이지 세팅
st.set_page_config(page_title="Emoji Floating Quotes", page_icon="✨", layout="centered")

# 제목
st.markdown("<h2 style='text-align:center;'>✨ Inspiring Emoji Quote ✨</h2>", unsafe_allow_html=True)

# 명언
quote = "🌟 The best way to get started is to quit talking and begin doing. 🌟"
st.markdown(f"<p style='font-size:22px; text-align:center; font-weight:bold;'>{quote}</p>", unsafe_allow_html=True)

# 이모지 애니메이션 (CSS 활용)
emoji_animation = """
<style>
@keyframes floatUp {
  0%   { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(-150px); opacity: 0; }
}
.emoji {
  position: absolute;
  bottom: 10px;
  left: 50%;
  font-size: 30px;
  animation: floatUp 3s linear infinite;
}
</style>

<div class="emoji">✨</div>
<div class="emoji" style="left:45%; animation-delay: 0.5s;">💫</div>
<div class="emoji" style="left:55%; animation-delay: 1s;">🌸</div>
<div class="emoji" style="left:52%; animation-delay: 1.5s;">🌟</div>
"""

st.markdown(emoji_animation, unsafe_allow_html=True)
