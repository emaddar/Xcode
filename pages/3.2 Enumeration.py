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










st.markdown("""
#### Example _Race_ with **Struct**
""")
code = """
import Foundation

enum Race {
    case siamois, europeen, persan, angora, autre
}

struct Cat {
    var name : String
    var race : Race
    var age : Int
    var isVaccinated: Bool

    init(name: String, race :Race = .autre, age : Int, isVaccinated: Bool = false){
        self.name = name
        self.race = race
        self.age = age
        self.isVaccinated = isVaccinated
    }
}
// Cat1
var cat1: Cat = Cat(name : "minou", race : .siamois, age : 2, isVaccinated: true)
print(cat1.age)  // 2
print(cat1.race) // siamois

// Cat2
var cat2: Cat = Cat(name : "Felix", race : .europeen, age : 3)
print(cat2.race)  // europeen
print(cat2.name) // Felix
print(cat2) // Cat(name: "Felix", race: __lldb_expr_333.Race.europeen, age: 3, isVaccinated: false)
"""

st.code(code, language='swift')

