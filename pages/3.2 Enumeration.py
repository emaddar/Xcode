# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("""
# Enumeration

An enumeration defines a common type for a group of related values and enables you to work with those values in a type-safe way within your code.
#### Example _Country_
""")
code = """
enum Country {
    case France
    case Syrie
    case Brunei
    case Philipines
}
let universityCountry = Country.France
print(universityCountry) // France
"""

st.code(code, language='swift')



st.markdown("""
# Enumeration

An enumeration defines a common type for a group of related values and enables you to work with those values in a type-safe way within your code.
#### Example _Move_
""")
code = """
enum Move {
    case up, down, right, left
}
let CharacterNextMove : Move = .right
// Or : let CharacterNextMove =Move.right
switch CharacterNextMove {
case Move.up:
    print("Hero will jump")
case Move.down:
    print("Hero will crouch")
case Move.right:
    print("Hero will walk")
case Move.left:
    print("Hero will block")
} // Hero will walk
"""

st.code(code, language='swift')