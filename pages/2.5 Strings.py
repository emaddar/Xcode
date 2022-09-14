# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Strings

A **string** is an ordered collection of characters, such as "Hello, World". Swift strings are represented by the String type, which in turn represents a collection of Character type values.

Predefined String values can be included within code as string literals, or fixed sequences of textual characters within double quotation marks (""). Use a string literal as an initial value for a constant or variable.
""")

code = """
let someString = "Some string literal value"
"""

st.code(code, language='swift')

st.markdown("""
Because it is initialized with a string literal value, Swift infers a type of String for the someString constant.
""")



st.markdown("""
Multiline string literals are enclosed in three double quotation marks (\"\"\"):
""")

code = """
let banner = \"\"\"
          __,
         (           o  /) _/_
          `.  , , , ,  //  /
        (___)(_(_/_(_ //_ (__
                     /)
                    (/
        \"\"\"
print(banner)
"""
st.code(code, language='swift')



st.markdown("""
## Empty Strings

An empty String value can be created as the starting point for a longer string. 
To do this, either assign an empty string literal to a variable or initialize a
 new String instance using initializer syntax:
""")

code = """
var emptyString = "" //empty string literal
var anotherEmptyString = string() // initializer syntax
"""

st.code(code, language='swift')

st.markdown("""
_Both strings are empty and equivalent to each other._

Determine whether a String value is empty by checking its Boolean `isEmpty` property:
""")

code = """
if emptyString.isEmpty {
    print("String is empty")
}
"""
st.code(code, language='swift')

