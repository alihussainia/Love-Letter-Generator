# -*- coding: utf-8 -*-
"""
@author: Muhammad Ali
@github: @alihussainia
"""

import streamlit as st
import requests
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title="loveLetter", page_icon="love_letter", layout='centered', initial_sidebar_state='auto', menu_items=None)

st.title("AI based Love Letter Generator Application")
st.write("A web app that writes love letters using AI")

response = None

To = st.text_input(label, value="")
From = st.text_input(label, value="")

submit_button = st.button('Write!')

if submit_button: 
  if To==None: To="Love"
  if From==None: From="Anonymous"

  response = requests.post("http://35.224.65.114:8000/generate")

  st.markdown(f"""Dear +{To}+,+\n+{response}+\n+From+\n+{From}""") 

st.text("App developed with ❤️ by @alihussainia")

st.text(f"Connect with me via Email at malirashid1994@gmail.com")
