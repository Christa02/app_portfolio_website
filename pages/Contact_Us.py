import streamlit as st
from send_mail import send_mail

st.header("Contact Us")

with st.form(key="contact_us_form"):
    email_address = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    submit_button = st.form_submit_button("Submit")

    message = f"""\
Subject: New mail from {email_address}

From: {email_address}
{raw_message}
"""
    if submit_button:
        send_mail(message)
        st.info("Your email was sent successfully.")

