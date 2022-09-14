# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.3</h1>", unsafe_allow_html=True)

st.markdown("""
# Struct

...
""")
code = """
import Foundation

struct Cat {
    var name : String
    var race : String
    var age : Int
}
// Cat1
var cat1: Cat = Cat(name : "minou", race : "siamois", age : 2)
print(cat1.age)  // 2
print(cat1.name) // minou

// Cat2
var cat2: Cat = Cat(name : "Felix", race : "europeen", age : 3)
print(cat1.race)  // siamois
print(cat1.name) // minou
print(cat2) // Cat(name: "Felix", race: "europeen", age: 3)

// Tabel of cats
var cats = [cat1, cat2]
for i in cats {
    print(i.name)
}  // minou
   //Felix
"""

st.code(code, language='swift')
