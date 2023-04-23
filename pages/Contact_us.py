import streamlit as st
from send_email import send_mail
st.header("Contact Me via Gmail")

with st.form(key='email'):
    user_email = st.text_input("Enter your Email")
    raw_user_msg = st.text_area("Your Message")
    user_msg = f"""\
    Subject: New Message from {user_email}
    
    From: {user_email}
    {raw_user_msg}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_mail(user_msg)
        st.info("Your email was send successfully")