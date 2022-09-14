# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("<h1 style='text-align: center; color: black;'>Lesson 2.3</h1>", unsafe_allow_html=True)

st.markdown("""
# The for-in Loop

Use the `for-in loop` to iterate over a sequence, 
such as ranges of numbers, items in an array, or characters in a string.
The following example prints the first few entries in the five-times-table:
""")
code = """
for index in 1...5 {
    print("\(index) times 5 is \(index * 5) ")
}
//1 times 5 is 5 
//2 times 5 is 10 
//3 times 5 is 15 
//4 times 5 is 20 
//5 times 5 is 25
"""

st.code(code, language='swift')

st.markdown("""
The index variable is set at the first value in the range (1). 
The statements within the for loop are then executed in sequence, through the final item in the range (5).
""")



st.markdown("""
# The while Loop

A `while` loop performs a set of statements until a condition becomes false.
 These kinds of loops are best used when the number of iterations is not known before the first iteration begins.
while evaluates its condition at the start of each pass through the loop.
The while loop is demonstrated in the example below:
""")
code = """
while a < b {
    print(a)
    a += 1
}
"""

st.code(code, language='swift')

st.markdown("""
The code will execute until the a+=1 statement renders `a < b` as `false`.
""")





st.markdown("""
# Repeat-While

The `repeat-while` loop is the alternate while loop. 
It first makes a single pass through the loop block, 
then considers the loop's condition, and repeats the loop until the condition shows as false.
""")





code = """
repeat {
    x -= 1
} while  x > 0
"""

st.code(code, language='swift')


st.markdown("""
Swift's repeat-while loop is similar to a do-while loop in other languages.
""")







st.markdown("""
# Break

Use the **break** statement to immediately end the execution of an entire control flow statement. 
Also, the break statement is used within a switch statement or a loop statement to terminate 
its execution sooner than would otherwise be the case.


##### Break in a Loop Statement

When a break statement is used within a loop statement, the loop's execution immediately stops. 
Control transfers to the first line of code following the loop's closing brace (}). The current iteration's remaining code is skipped, and no further iterations of the loop are initiated.
For example, you can have a loop that breaks out when the value of **a** becomes less than that of **b**:


""")

code = """
var b = 7
var a = 10
while a > 0 {
     if (a<b) {
         break
    } 
    print(a) 
    a -= 1
}
//10
//9
//8
//7
"""

st.code(code, language='swift')

st.markdown("""
##### Break in a Switch Statement

A **break** causes a switch statement to end its execution immediately, 
and transfers control to the first line of code that follows the switch statement's closing brace (}).
""")

code = """
var a = 5 
var letter = "X"

switch a {
    case 1:
     letter = "A" 
    case 2 : 
     letter = "B" 
    default : 
     break 
}
"""

st.code(code, language='swift')

st.markdown("""
This example breaks out of the switch statement as soon as the default case is matched.

**_Always use a break statement to ignore a switch case._**
""")














