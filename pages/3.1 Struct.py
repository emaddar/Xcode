# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":blue_heart:",
)


st.markdown("""
# Random

### `Int.random( in:)` Generate random integers number within a specific range $$[a, b]$$
##### Example :
""")

code = """
var aleaInt:Int = Int.random( in: 1...10) // this will generate integer number between 1 and 10
print(aleaInt) // 8
"""

st.code(code, language='swift')



st.markdown("""
### `Double.random( in:)` Generate random double number within a specific range $$[a, b]$$
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
### Example _Cat_ :smiley_cat: :pouting_cat:
""")

code = """
import Foundation

struct Cat {
    var name : String
    var race : String
    var age : Int
    var isVaccinated: Bool
    
    init(name: String, race :String = "Unknown", age : Int, isVaccinated: Bool = false){
        self.name = name
        self.race = race
        self.age = age
        self.isVaccinated = isVaccinated
    }
}
// Cat1
var cat1: Cat = Cat(name : "minou", race : "siamois", age : 2, isVaccinated: true)
print(cat1.age)  // 2
print(cat1.name) // minou

// Cat2
var cat2: Cat = Cat(name : "Felix", race : "europeen", age : 3)
print(cat1.race)  // siamois
print(cat1.name) // minou
print(cat2) // Cat(name: "Felix", race: "europeen", age: 3, isVaccinatedA: false)

// Tabel of cats
var cats = [cat1, cat2]
for i in cats {
    print(i.name)
}  // minou
   //Felix

for cat in cats {
    print(cat.isVaccinated)
} // true
  // false
"""

st.code(code, language='swift')
