# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# 

#### Example 1: : Change background color :heart: :green_heart: :blue_heart:

""")
from PIL import Image
image = Image.open('Simple4.png')
st.image(image, width=700)

if st.button('Show code'):
    code = """

    """
    st.code(code, language='swift')

st.markdown("""
---
""")


