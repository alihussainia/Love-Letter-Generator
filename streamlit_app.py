# -*- coding: utf-8 -*-
"""
@author: Muhammad Ali
@github: @alihussainia
"""

import streamlit as st
import requests
import random
import warnings
import json 


warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title="loveLetter", page_icon="love_letter", layout='centered', initial_sidebar_state='auto', menu_items=None)

st.title("AI based Love Letter Generator Application")
st.write("A web app that writes love letters using AI")

To = st.text_input("To")
From = st.text_input("From")
input_txt = st.text_input("Enter a starting sentence below")
submit_button = st.button('Write!')

if submit_button:
  if To=="": To="Love"
  if From=="": From="Anonymous"
  if input_txt=="": "Dear love"

  headers = {
  "Authorization": st.secrets["AUTHORIZATION_TOKEN"],
  "Content-Type": "application/json",
}

  body = {
    "text": f"{input_txt}",
    "top_p": 1,
    "top_k": 40,
    "temperature": 0.9,
    "repetition_penalty":  1,
    "length": 24
    }

  response = requests.post(
  "https://shared-api.forefront.link/organization/QPP6ce99Y37v/gpt-j-6b-vanilla/completions/lsWkUsFftG2j",
  json=body,
  headers=headers
).json()

  st.markdown(f"""Dear {To},\n{response}\nFrom\n{From}""") 

st.text("App developed with ❤️ by @alihussainia")

st.text(f"Connect with me via Email at malirashid1994@gmail.com")
