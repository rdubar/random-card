import streamlit as st
import random
import os
from utils import load_data


requirements = load_data('requirements.txt')
st.write(requirements)

from gpt_cards import get_gpt_card

# streamlit run cards_app.py

st.set_page_config(page_title="Random Card", page_icon=":game_die:")

st.write(os.getcwd())

rules = load_data('rules.md')

def load_fortunes(filename='delivery.txt'):
    return load_data(filename, split=True)

# Initialize the fortunes list in the session state if it doesn't exist
if 'fortunes' not in st.session_state:
    st.session_state.fortunes = load_fortunes()
        
# Title of the app
st.title('The Delivery Game')

# Sidebar with the rules of the game
with st.sidebar:
    # Sidebar download button for the PDF
    with open("Game_Board.pdf", "rb") as file:
        st.download_button(
                label="Download Game Board",
                data=file,
                file_name="Game_Board.pdf",
                mime="application/octet-stream"
            )        
    st.write(rules)

    # Adding a clickable email address
    st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)

# Throw a dice
if st.button('Throw the dice'):
    dice = random.randint(1, 6)
    st.write(f"You threw a {dice}!")

# Show a card button
if st.button('Show me my card'):
    if not st.session_state.fortunes:
        # Reload fortunes if all have been shown
        st.session_state.fortunes = load_fortunes()
        st.write("All fortunes have been shown. Starting over.")
    else:
        # Select a random fortune and remove it from the list to avoid duplicates
        fortune = random.choice(st.session_state.fortunes)
        st.session_state.fortunes.remove(fortune)
        # Display the selected fortune
        st.write(fortune)

if st.button('Generate unique GPT Card'):
    st.write(get_gpt_card())
