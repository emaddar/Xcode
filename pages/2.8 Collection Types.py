# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("""
# Collection Types

Containers that can store multiple values Like a “group of variables“
Structures for ordered and unordered groups of values
- Set is an unordered collection of unique values
- Array is an ordered collection of values accessible by index
- Dictionary is an unordered collection of key-value associations



## Set
""")

code = """
import Foundation
// Declaring an unordered collection of unique elements
var cakeIngredients: Set = ["Eggs", "Butter", "Flour", "Milk"]
// Showing the content
print(cakeIngredients)    // "Milk", "Butter", "Flour", "Eggs"
// Inserting a new element
cakeIngredients.insert("Milk")
// Showing the content
print(cakeIngredients)    // "Milk", "Butter", "Flour", "Eggs"
"""

st.code(code, language='swift')











st.markdown("""
## Array
#### Ways to declare an array
""")

code = """
var tracks = ["Interlagos", "Velocitta", "Auto Club Speedway"]
"""

st.code(code, language='swift')


code = """
var tracks: [String] = ["Interlagos", "Velocitta", "Auto Club Speedway”]
"""

st.code(code, language='swift')


code = """
var tracks: Array<String> = ["Interlagos", "Velocitta", "Auto Club Speedway”]
"""

st.code(code, language='swift')


st.markdown("""
Example
""")
code = """

// Declaring an ordered collection
var visitedContries = ["Brazil", "USA", "Sweden", "Colombia"]
// Accessing an element using its index
print(visitedContries[0])         //"Brazil"
// Appending an element to the collection ... It will be the last element
visitedContries.append("Italy")
// Inserting an element at a specific index
visitedContries.insert("Indonesia", at: 5)
// Getting the number of elements
visitedContries.count             //6
// Remove 4'em element
visitedContries.remove(at: 3)
// Remove last element
visitedContries.removeLast()
// Replace Second element by "Sryia"
visitedContries[1] = "Syria"
print(visitedContries)   // ["Brazil", "Syria", "Sweden", "Italy"]
"""

st.code(code, language='swift')









st.markdown("""
## Dictionary
#### Ways to declare an array
""")

code = """
var airports = ["CGH":"São Paulo", "CWB":"Curitiba"]
"""

st.code(code, language='swift')




code = """
var airports: [String:String] = ["CGH":"São Paulo", "CWB":"Curitiba"]
"""

st.code(code, language='swift')



code = """
var airports: Dictionary<String,String> = ["CGH":"São Paulo", "CWB":"Curitiba"]
"""

st.code(code, language='swift')






st.markdown("""
Example
""")
code = """
// Declaring an unordered collection
var countryCode = ["BR":55, "US":1, "IT":39, "IN":62]
// Accessing an element using its key
countryCode["IT"]            // 39
// Adding an element to the collection
countryCode["UK"] = 44
// Printing the collection
print(countryCode)          // ["IT": 39, "BR": 55, "US": 1, "UK": 44, "IN": 62]
"""

st.code(code, language='swift')
