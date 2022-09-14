# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Conditional Statements

A conditional statement executes certain code under certain conditions. 
For example, you can run a particular code when an error occurs, 
or display a message when a value exceeds a certain baseline. 
To set conditions, use **if** or **switch statements**.

### The if Statement

The most basic **if statement** contains a single if condition, 
and executes a set of statements only if that condition is true:
""")
code = """
var temp = 25 
if temp <= 30 {
    print("It's cold.")
}
"""

st.code(code, language='swift')

st.markdown("""
You can specify additional conditions by chaining together multiple if statements.
""")


code = """
if cardValue == 11 {
    print("Jack")
} else if cardValue == 12 {
    print("Queen")
} else {
    print("not found")
}
"""

st.code(code, language='swift')



































st.markdown("""
### The switch Statement

Use the **switch statement** as an alternative to the if statement for multiple potential states.
 The switch statement compares a value with several possible matching patterns, 
 executing a block of code using the first matching pattern.

Each case begins with the keyword case
""")
code = """
// program to find the day of the week 

let dayOfWeek = 4

switch dayOfWeek {
  case 1:
    print("Sunday")
	    
  case 2:
    print("Monday")
	    
  case 3:
    print("Tuesday")
	    
  case 4:
    print("Wednesday")
	    
  case 5:
    print("Thursday")
	    
  case 6:
    print("Friday")
	    
  case 7:
    print("Saturday")
	    
  default:
    print("Invalid day")
}  // Output : Wednesday
"""

st.code(code, language='swift')

st.markdown("""
A single case can contain multiple values. It can also contain ranges, using the range operators.
""")


code = """
let ageGroup = 33

switch ageGroup {
  case 0...16:
    print("Child")

  case 17...30:
    print("Young Adults")

  case 31...45:
    print("Middle-aged Adults")

  default:
    print("Old-aged Adults")
} // Output : Middle-aged Adults
"""

st.code(code, language='swift')



st.markdown("""
Every switch statement must be exhaustive, i.e. take every possible value into consideration. 
In cases in which it is not appropriate to provide a switch case for every possible value, 
you can define a **default** catch-all case to cover any values that are not explicitly addressed. 
Indicate the catch-all case by using the keyword **default**. This always appears last.


### The ternary operator
The ternary operator is a condition plus true or false blocks all in one, split up by a question mark and a colon, all of which which makes it rather hard to read. Here’s an example:
""")

code = """
let firstCard = 11
let secondCard = 10
print(firstCard == secondCard ? "Cards are the same" : "Cards are different")
"""




st.code(code, language='swift')

















