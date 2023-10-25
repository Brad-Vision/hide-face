# https://www.youtube.com/watch?v=VqgUkExPvLY
# pip install streamlit 

import streamlit as st
import requests # pip install requests
from streamlit_lottie import st_lottie

# https://webfx.com/tools/emoji-cheat-sheet
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# pip install streamlit-lottie
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi, I am Brad :wave:")
# st.title("A developer from Australia")
# st.write("blah~")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On blah~
            """
        )
        st.write("[YouTube Channel >](https://youtube.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        st.subheader("image")
        
    with text_column:
        st.subheader("Integrate Lottie")
        st.write(
            """
            Learn how..
            """
        )
        st.markdown("[Watch video...](https://youtu.be/TXSOitGoINE)")
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"