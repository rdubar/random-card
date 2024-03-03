import random
import streamlit as st
from tools.settings import SPECIAL

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Special Delivery")

"""
*Optional Special Delivery Rules:*
* Each player received a random Special Delivery Card a the start of the game.
* Select a card at random, or use the app to select a random card for you.
* Special Delivery cards may be used as indicated. One used, they are returned to the deck.
* Players may trade one Star or one Lucky Break token for a new Special Delivery Card
* Players may trade Special Delivery cards with each other at any time, for free, or for Stars or Lucky Break tokens.
* Only one Special Delivery card can be used per turn.
"""

# set session state of last_special
if 'last_special' not in st.session_state:
    st.session_state.last_special = "No Special Delivery Card"
special_list = []

def create_special_list():
    special_list = SPECIAL.split('\n\n')  # split the string into a list
    special_list = [x for x in special_list if x]  # remove empty lines
    random.shuffle(special_list)  # shuffle the list
    return special_list

# create button to draw a random special delivery card
if st.button("Draw a Special Delivery Card"):
    if not special_list:
        special_list = create_special_list()
    st.session_state.last_special = special_list.pop()
    st.write(st.session_state.last_special)
