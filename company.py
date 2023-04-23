import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.header("The Best Company")

information = """
You can justify a higher price point for your products and services, 
if you go into details about your
 production values or ethically-sourced materials.
For instance, Starbucks’ coffee may not necessarily be better than Dunkin’ Donuts’ coffee,
 but because Starbucks goes into details about its high-quality ingredients, 
 it immediately creates the sense that you’ll be paying a little more for a "better" product.
 """
st.write(information)

st.header("Our Team")

df = pandas.read_csv("comp_data.csv", sep=',')

col1, col2, col3 = st.columns(3)
with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Comp_img/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Comp_img/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("Comp_img/" + row["image"])
