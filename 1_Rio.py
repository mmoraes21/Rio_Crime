import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Rio Crime",
                   page_icon=":knife:")


audio_file_path = 'GarotaDeIpanema.mp3'
st.audio(audio_file_path, format='audio/mp3')


st.title("Rio de Janeiro crime stats for turists")

st.image('rio.jpg', use_column_width=True)

st.subheader("Welcome to Rio de Janeiro – a vibrant city pulsating with energy, captivating landscapes and a rich cultural tapestry.")

st.markdown("""
From the iconic Christ the Redeemer statue to the rhythmic beats of samba echoing through its streets, Rio captivates visitors with its undeniable charm. While Rio's beauty is undeniable, it's essential to address concerns about safety, particularly for our valued tourists.

Like any major urban center, Rio de Janeiro faces challenges with petty crime, including pickpocketing and opportunistic theft in certain areas frequented by visitors. 

We are here to prioritize your safety and aim to equip you with guidance to ensure a memorable and secure experience in this stunning city. Our goal is to celebrate Rio's splendor while empowering you with knowledge to navigate its streets confidently.
""")



