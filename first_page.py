import pdf_text
import image_text_recognition
import streamlit as st
PAGES = {
    "Image text": image_text_recognition,
    "pdf text": pdf_text,
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()