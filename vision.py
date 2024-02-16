import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

st.set_page_config(
    page_title='Gemini Image Demo',
    layout='centered',
    initial_sidebar_state='collapsed'
)

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([input, image])
    return response.text


st.header('Gemini Pro LLM Application')
input = st.text_input('Input Prompt: ', key='input')

uploaded_file = st.file_uploader("Choose an image.. ",
                                 type=['jpg', 'jpeg', 'png'])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,
             caption="Upload Image",
             use_column_width=True)

submit = st.button("Tell me about the Image")

if submit:
    response = get_gemini_response(input, image)
    st.write(response)


