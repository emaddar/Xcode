# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Comparison Operators
Swift supports all of the standard comparison operators in C:
- Equal to (a == b)
- Not equal to (a != b)
- Greater than (a > b)
- Less than (a < b)
- Greater than or equal to (a >= b)
- Less than or equal to (a <= b)

Each of the comparison operators returns a **Bool** value indicating whether or not the statement is true:
""")
code = """
1 ==1 // ture, because 1 is equal to 1
2 != 2 // ture, because 2 is not equal to 1
2 > 1 // ture, because 2 is greater than 1
1 > 2 //  ture, because 1 is less than 2
1 >= 1 //   ture, because 1 is greater than or euqal 1
2 <=1 // false, because 2 is not less than or euqal 1
"""

st.code(code, language='swift')

st.markdown("""
Swift also provides two identity operators, `===` and `!==`, which test whether two object references both refer to the same object instance.
""")





























st.markdown("""
# Range Operators
Swift offers two range operators, which are shortcuts for expressing a range of values.

The **closed rangeoperator (a...b)** defines **a** range running from **a** to **b**,
 and includes the values **a** and **b**. The value of **a** must not be greater than that of **b**.
""")

code = """
1...3 // 1,2,3
"""

st.code(code, language='swift')

st.markdown("""
The **half-open rangeoperator (a..<b)** defines a range that runs from **a** to **b**, but does not include **b**.
 It is said to be half-open because it contains its first value, but not its final value. 
As with the closed range operator, the value of **a** must not be greater than that of **b**
""")


code = """
1..<3 // 1,2
"""

st.code(code, language='swift')

























st.markdown("""
# Logical Operators
Logical operators modify or combine the Boolean logic values **true** and **false**.
 Swift supports the three standard logical operators found in C-based languages:

- Logical **NOT** operator (`!a`): Inverts a Boolean value so that true becomes false and false becomes true.

- Logical **AND** operator (`a && b`): Creates logical expressions in which both values must be true for the overall expression to be true.

- Logical **OR** operator (`a || b`): An infixed operator made from two adjacent pipe characters. It creates logical expressions
 in which only one of the two values has to be true for the overall expression to be true.
""")
