# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Functions

Functions are self-contained chunks of code that perform a specific task. You give a function a name that identifies what it does, and this name is used to “call” the function to perform its task when needed.
""")

code = """
let someString = "Some string literal value"// Declaring a function to reuse the code block
func greetingUser () {
    let userName = "Danilo"
    let today = "Jul 9 1984"
    let message = "Hello \(userName), today is \(today)"
    print (message)
}

// Calling the function
greetingUser() //  Hello Danilo, today is Jul 9 1984
"""

st.code(code, language='swift')

st.markdown("""
#### Declaring a function that receives parameters
""")
code = ("""
func greetingUser (name: String, date: String) {
    let userName =
    let today =
    let message = "Hello \(userName), today is \(today)"
    print (message)
}
// Calling the function
greetingUser(name: "Danilo", date:"Jul 9 84") // Hello Danilo, today is Jul 9 84
greetingUser(name: "Gilles", date:"Mar 3 48") //  Hello Gilles, today is Mar 3 48
""")

st.code(code, language='swift')

st.markdown("""
#### Declaring a function that returns a value
""")

code = """
func greetingUser (name: String, date: String) -> String {
    let userName = name
    let today = date
    let message = "Hello \(userName), today is \(today)"
    return message
}
// Calling the function
let finalMessage = greetingUser(name: "Mark", date:"Apr 2 2084")
print ( finalMessage ) // Hello Mark, today is Apr 2 2084
"""

st.code(code, language='swift')