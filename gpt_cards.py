import streamlit as st
from openai import OpenAI
import os
from utils import load_data

api_key = st.secrets["openai"]["openai_api_key"] if "openai" in st.secrets else os.environ.get('OPENAI_API_KEY', '')
engine = "gpt-3.5-turbo"
client = OpenAI(api_key=api_key)

prompt = load_data('prompt.txt')
rules = load_data('rules.md')
cards = load_data('delivery.txt')

full_prompt = prompt + rules + cards

def query_chatgpt(prompt, engine=engine, history=[]):
    messages = history + [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(model=engine, messages=messages)
    return response

def get_gpt_card():
    try:
        return query_chatgpt(full_prompt).choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_gpt_card())