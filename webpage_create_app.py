# Build a Website in only 12 minutes using Python & Streamlit
# https://github.com/Sven-Bo
# !pip install streamlit
# !pip install streamlit-lottie

# app.py
# Find more emojis https://webfx.com/tools/emoji-cheat-sheet/
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
# lottieFiles https://lottiefiles.com(dharma6872 계정을 회원 가입)
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")
img_contact_form = Image.open("images/yt_contact_from.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("안녕하세요. 저는 김무경입니다. :wave:")
    st.title("한국에 사는 데이터 엔지니어 입니다.")
    st.write("빅데이터 관련 기술 및 데이터 분석, 웹 대시보드 개발하는 일을 하고 있습니다.")
    st.write("[참조](http://www.bplace.kr)")

# ---- WHAT I DO ----
with st.container():
    st.write("---") # 라인 출력

    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##") # 공백 출력
        st.write(
            """
            - 하둡 시스템 구축
            - 하둡 시스템 운영
            - 데이터웨어하우스 구축
            - 데이터 이관
            - 데이터 수집
            - 데이터 분석
            - 클라우드 등
            """
        )
        st.write("[참조](http://www.bplace.kr)")


    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("통계청 SGIS")
        st.write(
            """
            - 지도 기반 빅데이터 분석 결과 시각화
            - 빅데이터 시스템 구축
            """
        )
        st.markdown("[Watching Video...](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("통계청 SGIS")
        st.write(
            """
            - 지도 기반 빅데이터 분석 결과 시각화
            - 빅데이터 시스템 구축
            """
        )
        st.markdown("[Watching Video...](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    st.write("---")
    st.header("Got In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/77ca21456791ed2bc6ae0f6773383030" method="POST">
        <input type="hidden" name="_captcha" value=false>
        <input type="text" name="name" required>
        <input type="email" name="email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

