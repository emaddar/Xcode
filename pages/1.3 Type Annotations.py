
# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("""
# Type Annotations
**Type annotations** ensure that your code is clear about the value stored within your constant or variable. Swift's basic types include:

- **Int**: Integers
- **Double** and **Float**: Floating-Point Values
- **Bool**: Boolean Values
- **String**: Textual Data.

Add a type annotation by placing a colon (:) after the constant or variable name, then add a space, and then add the type name, as follows:
""")
code = """
var WelcomeMsg : String
WelcomeMsg = "Hello"
"""

st.code(code, language='swift')



st.markdown("""
Or """)
code = """
var WelcomeMsg : String = "Hello"
"""

st.code(code, language='swift')


st.markdown("""
This example provides a type annotation for a variable called "welcomeMsg", that indicates that the variable can store **String** values.


It's possible to define multiple related variables of the same type. Include them all on a single line, separated by commas, then add a single type annotation after the final variable name:
""")
code = """
a = 88
var red, green, blue: Double
"""

st.code(code, language='swift')

































st.markdown("""
In practice, you will rarely need to add type annotations. Providing an initial value for a constant or a variable at the point at which it is defined, will almost always be sufficient for Swift to infer which type should be used:
""")
code = """
let pi = 3.14159 // Double
"""

st.code(code, language='swift')



st.markdown("""
Swift always chooses Double (as opposed to Float) when inferring the type for floating-point numbers.

Swift is a **type safe** language, meaning that it supports clarity when specifying value types for code. When part of your code expects a String, you can't pass it an Int by mistake.
""")

