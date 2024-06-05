import streamlit as st
from PIL import Image


def convert_grey(imgName):
    img = Image.open(imgName)
    gry_img = img.convert("L")
    st.image(gry_img)


uploaded_img = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    normal_img = st.camera_input("Camera")

if normal_img:
    convert_grey(normal_img)
elif uploaded_img:
    convert_grey(uploaded_img)
