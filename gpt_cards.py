import streamlit as st
import openai
import os
from utils import load_data
from mongo_logger import log_text

api_key = st.secrets["openai"]["openai_api_key"] if "openai" in st.secrets else os.environ.get('OPENAI_API_KEY', '')
engine = "gpt-3.5-turbo"
openai.api_key = api_key

"""
Use OpenAI's GPT-3 model to generate random cards for the game.
"""


prompt = load_data('prompt.txt')
rules = load_data('rules.md')
cards = load_data('delivery.txt')

full_prompt = prompt + rules + cards

def query_chatgpt(prompt, engine=engine, history=[]):
    messages = history + [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model=engine, messages=messages)
    return response

def get_gpt_card():
    try:
        text = query_chatgpt(full_prompt).choices[0].message.content
        log_text(text)
        return text
    except Exception as e:
        return f"Error: {e} [{len(api_key)} {len(full_prompt)}]"

if __name__ == "__main__":
    print(get_gpt_card())
