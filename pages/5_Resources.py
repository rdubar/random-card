import streamlit as st
from tools.settings import PROMPT, CARDS, OPEN_AI_API_KEY, WORDCLOUD_PATH, show_gitub_repo_link
from tools.mongo_logger import get_all_records

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

# create anchor at top of page
st.markdown("<a id='top'></a>", unsafe_allow_html=True)
st.title('Resources')

# get all records, to test if we want to show this content
records = get_all_records()

# Create a table of contents
st.markdown("[Source Code](#source-code)")
st.markdown("[Default Game Cards](#default-game-cards)")
if OPEN_AI_API_KEY:
    st.markdown("[AI Prompt](#ai-prompt)")
if records:
    st.markdown("[AI Generated Cards](#ai-generated-cards)")
st.markdown("[Wordcloud](#wordcloud)")

# Create the content
st.header("Source Code")
show_gitub_repo_link()

st.header("Default Game Cards")
st.text_area("Default Game Cards:", value=CARDS, height=400, max_chars=1500, key='cards')

if OPEN_AI_API_KEY:
    st.header("AI Prompt")
    st.text_area("AI Prompt (combined with rules and default cards):", value=PROMPT, height=400, max_chars=1500, key='prompt')

if records:
    st.header("AI Generated Cards:")
    text = ""
    count = 0
    for record in records:
        entry = record['generated_text']
        if "example log entry" in entry:
            continue
        count += 1
        time = record['timestamp'].strftime("%Y-%m-%d %H:%M")
        model = record['model'] if 'model' in record else 'gpt-3.5-turbo'
        text += f"{time}  {model:20}\n{entry}\n\n"
    st.text_area(f"There have been {count:,} AI Generated Cards", text, height=400)


st.header("Wordcloud")

"""
This is a wordcloud of all of the text in the game:
"""

st.image(WORDCLOUD_PATH)


# link to top of page
st.markdown("<a href='#top'>Back to top</a>", unsafe_allow_html=True)