import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Ayush Trivedi photo.jpg", width=200)

with col2:
    st.title("Ayush Trivedi")
    content = """
    Hi, I am Ayush! Strong design and integration abilities as well as intuitive problem solving
abilities. JAVA, PYTHON, and SQL expert. enthusiastic about
starting and implementing new projects. understanding of how to
transform business needs into technical solutions.
"""
    st.info(content)

st.write("Below you can see some of the app I have build in Python... Feel free to contact me!")

col3, col4 = st.columns(2)

dataframe = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in dataframe[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in dataframe[10:20].iterrows():
        st.header(row["title"])