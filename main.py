
import streamlit as st
import os
import google.generativeai as genai
st.set_page_config(
    page_title='Q&A Demo!',
    layout='centered',
    initial_sidebar_state='collapsed'
)

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Gemini Pro model and get response

model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


""" initialize our streamlit app"""

st.header('Gemini Pro LLM Application')
input = st.text_input('Input: ', key='input')
submit = st.button('Ask the Question')

# When submit is clicked

if submit:
    st.write(get_gemini_response(question=input))




