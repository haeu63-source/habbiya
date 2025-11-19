import streamlit as st

st.set_page_config(page_title="한비야", layout="centered")

st.title("한비야 안녕")

if st.button("이거눌러"):
    st.markdown(
        "<h1 style='font-size:150px; text-align:center;'>🖕</h1>",
        unsafe_allow_html=True
    )
