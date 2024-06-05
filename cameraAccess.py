import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    normal_img = st.camera_input("Camera")

if normal_img:
    img = Image.open(normal_img)
    gry_img = img.convert("L")
    st.image(gry_img)