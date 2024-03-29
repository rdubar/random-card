import streamlit as st
from tools.settings import RULES, download_game_board_buttons

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title('Rules of the Game')

download_game_board_buttons()

st.write(RULES)

"""*Your comments and suggestions are always welcome!*"""

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)