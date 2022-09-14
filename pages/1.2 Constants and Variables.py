
# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Constants and Variables
Constants and variables are used to associate a name (yourName or welcomeMessage) with a value (the number 42 or the string "Hi!").

A **constant** has a set value that cannot be changed; the value of a **variable** can be changed.

The keyword var is used to declare a variable.
The following example declares a variable, "a", and assigns its value as "42".
""")
code = """
var a = 42
"""

st.code(code, language='swift')



st.markdown("""
It is possible to change variable values over time:
""")
code = """
a = 88
// now "a" has a value  of 88 
"""

st.code(code, language='swift')












st.markdown("""
### Constants
Declare a constant using the `let` keyword.

This example declares a constant named "one" and assigns it a value of 1:
""")
code = """
let one = 1
"""

st.code(code, language='swift')



st.markdown("""
Declare multiple constants on a single line and separate them with commas:
""")
code = """
let x = 0.0, y=0.0, z=0.0
"""

st.code(code, language='swift')








st.markdown("""
### Constant and Variable Names
Constant and variable names can contain almost any character, including Unicode characters:

let $\pi = 3.14159$

However, constant and variable names must have no blank spaces, mathematical symbols, arrows, private-use (or invalid) Unicode code points, or line and box-drawing characters. Numbers can appear anywhere within a name, except for at the beginning.
""")
