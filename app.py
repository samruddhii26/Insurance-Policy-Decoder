import streamlit as st
from PyPDF2 import PdfReader

# --- Dummy credentials ---
USERNAME = "admin"
PASSWORD = "1234"

# --- Initialize session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# --- Login Function ---
def login():
    st.title("Insurance Policy Decoder - Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")


# --- Main App ---
if not st.session_state.logged_in:
    login()
else:
    st.title("Insurance Policy Decoder")

    uploaded_file = st.file_uploader(
        "Upload your insurance policy (PDF)",
        type="pdf"
    )

    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        st.subheader("Extracted Text Preview")
        st.write(text[:2000])

        st.download_button(
            label="Download Extracted Text",
            data=text,
            file_name="policy_summary.txt",
            mime="text/plain"
        )
