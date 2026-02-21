import streamlit as st
from PyPDF2 import PdfReader

st.title("Insurance Policy Decoder")

uploaded_file = st.file_uploader("Upload your insurance policy (PDF)", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")
    st.write(text[:2000])  # show first 2000 characters