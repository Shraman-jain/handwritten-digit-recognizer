import streamlit as st
import pdfplumber
def app():
    st.write("""
          # Pdf text Recognition
          """
          )

    file = st.file_uploader("Please upload a file", type=[".pdf"])
    
    if file is None:
      st.write("""
      #### Please upload an image file""")
    else:
        with pdfplumber.open(file) as pdf:
            first_page = pdf.pages[0]
            data=first_page.extract_text()
        
        pdf_text=data.split('\n')
        st.write("**Text on the pdf is**")
        
        for i in pdf_text:
            st.write(i)