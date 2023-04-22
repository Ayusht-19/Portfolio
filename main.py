import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Ayush Trivedi photo.jpg", width=200)

with col2:
    st.title("Ayush Trivedi")
    content = """
    Strong design and integration abilities as well as intuitive problemsolving
abilities. JAVA, PYTHON, and SQL expert. enthusiastic about
starting and implementing new projects. understanding of how to
transform business needs into technical solutions.
"""
    st.info(content)
