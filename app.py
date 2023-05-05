from PIL import Image                         #import別人寫好的工具箱，裡面有很多工具=functions
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")  #set arguments

def load_lottieurl(url):      #這是一個function，def funtion名(可input的值)
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    
    
#---LOAD ASSETS--- 把檔案叫進來
lottie_baking = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_XldOcZ.json")
img_bday_cake = Image.open("images/bday_cake.jpg")


#----HEADER SECTION----
with st.container():
    st.subheader("Hi, I'm Connie :wave:")
    st.title("A Taiwanese girl")                
    
    st.write("[about me >](https://www.google.com/)")
                  
#---WHAT I DO---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
            st.header("What I like")
            st.write("##")
            st.write(
                """
                - baking
                - cooking
                - traveling
                
                if this sounds interesting to you, please go check out my channel
                """
            )
            st.write("[YouTube Channel >](https://www.google.com/)")
    with right_column:
        st_lottie(lottie_baking, height=300)
            
#--- Projects---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_bday_cake)
    with text_column:
        st.subheader("bake a b-day cake for your family!")
        st.write(
            """
            Learn how to bake a b-day cake right here
            """
        )
        st.markdown("[Watch Video](https://www.google.com/)")
          
    
                   