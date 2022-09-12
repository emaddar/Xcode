# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("""
# Working with Strings


### Concatenation
String values can be added together (or concatenated) with the **addition operator (+)** to create a new String value:
""")

code = """
let string1 = "Hello" 
let string2 = " World" 
var welcome = string1 + string2 
// welcome now equals "Hello World"
"""

st.code(code, language='swift')

st.markdown("""
The addition assignment operator (+=) appends a String value to an existing String variable.
""")


code = """
var msg = "Hi" 
msg += " David" 
// msg is now "Hello David"
"""
st.code(code, language='swift')



















st.markdown("""
### String Interpolation
String interpolation includes the values of a mix of constants, variables, literals, and expressions inside a string literal to form a new String value. Prefix each item with a backslash, place the item in parentheses, and insert it into the string literal.
""")

code = """
let mult = 4 
let message = "\(mult) times 1.5 is \(Double(mult) * 1.5)" 
//message is "4 times 1.5 is 6.0"
"""

st.code(code, language='swift')

st.markdown("""
In the above example, the multiplier value is inserted into the string literal as \(mult). When the string interpolation is evaluated prior to creating the actual string, this placeholder is replaced with the actual value of mult.

Later in the string, the value of mult appears within a larger expression within the string literal: \(Double(mult) * 1.5). The expression calculates the value of Double(mult) * 1.5 and then inserts the result (6) into the string.
""")






st.markdown("""
### Counting Characters

To retrieve a **count** of the Character values in a string, use the `count` property of the string:literal to form a new String value. Prefix each item with a backslash, place the item in parentheses, and insert it into the string literal.
""")

code = """
let someString = "I am learning swift 4" 
print("somString has \(someString.count) charachters")
// somString has 21 charachters
"""

st.code(code, language='swift')



st.markdown("""
## Changing Case
### uppercased
Returns an uppercase version of the string
""")
code = """
let phrase = "cat and dog"
let upper = phrase.uppercased()
print(upper) // CAT AND DOG
"""
st.code(code, language='swift')


st.markdown("""
### lowercased
Returns a lowercase version of the string
""")
code = """
let lower = phrase.lowercase()
print(lower) // cat and dog
"""
st.code(code, language='swift')



st.markdown("""
### Capitalized
This method changes word-starting characters in a string. It uppercases letters after spaces and other punctuation chars.
""")
code = """
let phrase = "antarctica, asia, africa"
let upperFirst = phrase.capitalized
print(upperFirst) // Antarctica, Asia, Africa
"""
st.code(code, language='swift')


st.markdown("""
### Finding Substrings
#### hasPrefix()
The `hasPrefix()` method returns: 
- **true** if the string begins with the given string. 
- **false** if the string doesn't begin with the given string.
""")
code = """
// Create strings 
let str1 = "Edpresso is the best"
let str2 = "Best place to be"
let str3 = "Learn all you need"

// Check if the following prefixes exist
print(str1.hasPrefix("Edpresso"))  // true
print(str2.hasPrefix("great"))  // false
print(str3.hasPrefix("Learn")) // true
"""
st.code(code, language='swift')







st.markdown("""
#### hasSuffix()
The `hasSuffix()` method returns:
- **true** if the string ends with the given string
- **false** if the string doesn't end with the given string
""")
code = """
// Create strings 
var str = "Swift Programming"

print(str.hasSuffix("ing")) // true
print(str.hasSuffix("g")) // true
print(str.hasSuffix("Programming")) // true

print(str.hasSuffix("programming")) // false
print(str.hasSuffix("min")) // false
"""
st.code(code, language='swift')


st.markdown("""
#### contains()
Returns a Boolean value indicating whether a sequence or string contains the given element.
""")
code = """
var str = "swift@apple.com"

print(str.contains("@apple")) // true
"""
st.code(code, language='swift')

