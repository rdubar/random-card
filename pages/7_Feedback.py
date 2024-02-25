import streamlit as st
from tools.mongo_logger import log_text

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Feedback")

"""
I'd love to hear your thoughts on the game. Please fill out the form below.

You can leave your name, location and email address if you like!
"""

with st.form(key="feedback_form"):
    feedback = st.text_area("What do you think of the game?")
    submit = st.form_submit_button("Submit")

if submit:
    log_text(feedback, tag="feedback")
    st.write("Thank you for your feedback!")
