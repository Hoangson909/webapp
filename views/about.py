import streamlit as st
import functions as fc
from streamlit_extras.badges import badge

me = fc.open_image("./assets/me.png")

def create_social_media_links():
    social_media_links = (
        "<div class='social-media-container' style='text-align: center;'>"
        "<a href='#'><img src='https://img.icons8.com/?size=32&id=AZOZNnY73haj&format=png' alt='GitHub'></a>"
        "<a href='#'><img src='https://img.icons8.com/?size=32&id=qNUNvR9aEWql&format=png' alt='LinkedIn'></a>"
                "<a href='#'><img src='https://img.icons8.com/?size=32&id=VJz2Ob51dvZJ&format=png' alt='Instagram'></a>"
        "<a href='#'><img src='https://img.icons8.com/?size=32&id=bUGbDbW2XLqs&format=png' alt='Twitter'></a>"
        "<a href='#'><img src='https://img.icons8.com/?size=32&id=Xy10Jcu1L2Su&format=png' alt='Instagram'></a>"
        "</div>"
    )
    st.markdown(social_media_links, unsafe_allow_html=True)

def createPage():
    col1, col2 = st.columns(2)

    with col1:
        with st.columns(3)[1]:
            st.image(me)
            create_social_media_links()
    with col2:
        st.header('Xin chào')
        st.markdown("Tôi là sơn")
        st.markdown("Cám ơn bạn đã đọc")
        
    return True