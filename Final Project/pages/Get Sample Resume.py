import streamlit as st
import os
import openai
import json
from PIL import Image

def _open_ai_(context):
    
    openai.api_key = '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'

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=context,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response['choices'][0]['text']
    


file = 'png_logo.png'
c1, c2 = st.columns([2, 5])
image = Image.open(file)
image = image.resize((130,130))
c1.image(image)

c2.markdown("<h1 style='text-align: left; color: #36CC9B; font: 60px Georgia, sans-serif;'>Sample Resume</h1>", unsafe_allow_html=True)
c2.markdown('-AI Based Auto Resume Generator')
'---'
col1, col2 = st.columns(2)
name = col1.text_input("Name")
job_title = col2.text_input("Job Title")


prompt = 'name:'+name+'\n'+'job_title:'+job_title+'\n'+'write a resume on above data'
'---'
if st.button('Create Resume'):
    response = _open_ai_(prompt)
    st.write(response)
