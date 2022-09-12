# Run SQL queries in EXCEL

# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)



st.markdown("""
# "Hello, World!"
Printing text is easy:
""")
code = """
print("Hello, world!")
"""

st.code(code, language='swift')




st.markdown("""
To print the value of a variable inside a text, place it in parentheses, and insert a backslash just prior to the opening parenthesis:
""")
code = """
var myVariable = 42
print("The value is \(myVariable)")
"""

st.code(code, language='swift')





st.markdown("""
You do not need the backslash for printing only the variable value:
""")
code = """
var myVariable = 42
print(myVariable)
"""

st.code(code, language='swift')







st.markdown("""
### Comments
The Swift compiler ignores **comments**, which are used to include non-executable text in your code that may be used as a reminder or note-to-self.
A single-line comment opens with two forward-slashes (`//`):
""")
code = """
// this is a comment
"""

st.code(code, language='swift')




st.markdown("""
A multiline comment begins with a single forward-slash, followed by an asterisk (/*). It concludes with an asterisk, then a forward-slash (*/):
""")
code = """
/* this is also a comment, 
but written over multiple lines */
"""

st.code(code, language='swift')

