# -*- coding: utf-8 -*-
"""
@author: Muhammad Ali
@github: @alihussainia
"""

import streamlit as st
import requests
import random
import warnings
<<<<<<< HEAD
import json 


=======
>>>>>>> bfb3f62e2b11c2d267d26c7e3addf3b85277ea00
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title="loveLetter", page_icon="love_letter", layout='centered', initial_sidebar_state='auto', menu_items=None)

st.title("AI based Love Letter Generator Application")
st.write("A web app that writes love letters using AI")

<<<<<<< HEAD
To = st.text_input("To")
From = st.text_input("From")
input_txt = st.text_input("Enter a starting text")
submit_button = st.button('Write!')

length= int(st.sidebar.number_input(label = "length", value = 64, max_value = 2048, help = """What is response length?

Response length is the length of the generated text, in tokens, you’d like based on your prompt. A token is roughly 4 characters including alphanumerics and special characters.

Note that the max response length for GPT-J is 2048 tokens."""))

if submit_button:
  if To=="": To="Love"
  if From=="": From="Anonymous"
  if input_txt=="":
    st.error("Enter some starting text!")
    submit_button=False

if submit_button:
  headers = {
  "Authorization": st.secrets["AUTHORIZATION_TOKEN"],
  "Content-Type": "application/json"
} 

  body = {
    "text": f"{input_txt}",
    "top_p": 1,
    "top_k": 40,
    "temperature": 0.8,
    "repetition_penalty":  1,
    "length": length
  }

  response = requests.post(
  "https://shared-api.forefront.link/organization/QPP6ce99Y37v/gpt-j-6b-vanilla/completions/lsWkUsFftG2j",
  json=body,
  headers=headers
)
  data = response.json()
  
  st.markdown(f"""Dear {To},
  
  {input_txt} {data['result'][0]['completion']}
  
  From,
  
  {From}""") 
=======
response = None

To = st.text_input("Enter whom you are writing this letter to!", value="")
From = st.text_input("Enter who is writing this letter!", value="")

submit_button = st.button('Write!')

if submit_button: 
  if To==None: To="Love"
  if From==None: From="Anonymous"

  response = requests.post("http://35.224.65.114:8000/generate").json()
  final_resp = f"""Dear {To},
  
 {response}
 
 From
 
 {From}"""
  st.markdown(final_resp) 
>>>>>>> bfb3f62e2b11c2d267d26c7e3addf3b85277ea00

st.text("App developed with ❤️ by @alihussainia")

st.text(f"Connect with me via Email at malirashid1994@gmail.com")
