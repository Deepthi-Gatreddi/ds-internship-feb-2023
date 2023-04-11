import streamlit as st
import pickle
import numpy as np
from PIL import Image

def space():
    st.markdown("<br>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Hello",
    page_icon="😎",
)


st.write("# Welcome to the laptop prize prediciton ! 👋")

st.markdown("# :red[Deepthi Gatreddi]")
st.subheader(" :blue[flipkart]")
space()
image = Image.open('com.jpg')
st.image(image)



st.markdown(
    """
    #### Get Best Laptop Prices Online in India. Choose from Ultra-thin Laptop, Gaming Laptop from brands like HP, Dell, Lenovo, Acer, and avail great offers.
    """
)

space()

