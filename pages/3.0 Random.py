# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)






st.markdown("""
# Random :game_die:

### `Int.random( in:)` 
### Generate random _integers_ number within a specific range
##### Example :
""")

code = """
var aleaInt:Int = Int.random( in: 1...10) // this will generate integer number between 1 and 10
print(aleaInt) // 8
"""

st.code(code, language='swift')



st.markdown("""
___


### `Double.random( in:)` 
### Generate random _double_ number within a specific range
##### Example :
""")

code = """
for item in 1...4{
    print(Double.random( in: 0...1)) // this will generate double number between 0 and 1
}
/* 
0.966226978409593
0.6771410253613475
0.4939236087280944
0.9151552047956388
*/
"""

st.code(code, language='swift')




st.markdown("""

___

### `.randomElement()` 
### Pick a random element from an array
##### Example :
""")

code = """
let array = ["Frodo", "Samwise", "Merry", "Pippin"]
print(array.randomElement()!) // Using ! knowing I have array.count > 0
// Merry
"""

st.code(code, language='swift')


st.markdown("""
or if you don't like to use `!`
""")


code = """
let array = ["Frodo", "Samwise", "Merry", "Pippin"]
if let sCode = array.randomElement(){
    print(sCode)
}
// Samwise
"""

st.code(code, language='swift')
