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

submit_button = st.button('Write!')

To = st.text_input("To")
From = st.text_input("From")
input_txt = st.text_input("Enter any letter salutation here...")

if submit_button:
  if To==None: To="Love"
  if From==None: From="Anonymous"
  if input_txt==None: "Dear love"

  headers = {
  "Authorization": st.secrets["AUTHORIZATION_TOKEN"],
  "Content-Type":  st.secrets["CONTENT_TYPE"],
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

  st.markdown(f"""Dear +{To}+,+\n+{response}+\n+From+\n+{From}""") 

st.text("App developed with ❤️ by @alihussainia")

st.text(f"Connect with me via Email at malirashid1994@gmail.com")
