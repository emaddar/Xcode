# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Enumeration

An enumeration defines a common type for a group of related values and enables you to work with those values in a type-safe way within your code.
#### Example _Country_ :earth_africa:
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
Or
""")
code = """
enum Country: String {
    case france = "France"
    case syrie = "Syrie"
    case brunei = "Brunei"
    case philipines = "Philipines"
}
let universityCountry = Country.france.rawValue
print(universityCountry) // France
"""

st.code(code, language='swift')




st.markdown("""
#### Example _Move_ :arrow_up: :arrow_down: :arrow_right: :arrow_left:
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
#### Example _Race_ with **Struct** :smiley_cat: :smile_cat:  :heart_eyes_cat: :pouting_cat: :cat:
""")
code = """
import Foundation

enum Race {
    case siamois, europeen, persan, angora, ather
}

struct Cat {
    var name : String
    var race : Race
    var age : Int
    var isVaccinated: Bool

    init(name: String, race :Race = .ather, age : Int, isVaccinated: Bool = false){
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













st.markdown("""
#### Exercice :spades: :hearts: :clubs: :diamonds:

""")
from PIL import Image
image = Image.open('exercice.png')

st.image(image)

st.markdown("""
##### Solution : Emad & Lorenzo :man:
""")
code = """
enum Value: CaseIterable {
    case one
    case two
    case three
    case four
    case five
    case six
    case seven
    case eight
    case nine
    case ten
    case valet
    case queen
    case king
}



enum Color: CaseIterable {
    case spade
    case heart
    case tile
    case clover
}


struct Cartes {
    var value : Value
    var color : Color
}


for i in 1...3 {
    var new:Cartes = Cartes(value : .allCases.randomElement()!, color : .allCases.randomElement()!)
    print("Carte \(i) : value = \(new.value) and color = \(new.color)")
}
"""

st.code(code, language='swift')








st.markdown("""
##### Solution : Julie :woman:
""")
code = """
enum Value: String {
    case un = "As"
    case deux = "Deux"
    case trois = "Trois"
    case quatre = "Quatre"
    case cinq = "Cinq"
}

enum CardColor: String {
    case trefle = "Trèfle"
    case pique = "Pique"
    case coeur = "Coeur"
    case carreau = "Carreau"
}

struct Card {
    var couleurDeCarte: CardColor
    var valeurDeCarte: Value
}

var cartes = [
    Card(couleurDeCarte: .coeur, valeurDeCarte: .quatre),
    Card(couleurDeCarte: .carreau, valeurDeCarte: .cinq),
    Card(couleurDeCarte: .pique, valeurDeCarte: .quatre),
    Card(couleurDeCarte: .trefle, valeurDeCarte: .cinq),
    Card(couleurDeCarte: .coeur, valeurDeCarte: .un),
    Card(couleurDeCarte: .carreau, valeurDeCarte: .deux)
]

for _ in 1...3 {
//    print(cartes.randomElement()!)
    print("La carte est le \(cartes.randomElement()!.valeurDeCarte) de \(cartes.randomElement()!.couleurDeCarte)")

}
"""

st.code(code, language='swift')







st.markdown("""
##### Solution : Julie ... Emad modification: for_in  :woman: :man:
""")
code = """
for i in 1...3 {
    var CARD = cartes[Int.random(in: 0...cartes.count)]
    print("La carte \(i) est le \(CARD.valeurDeCarte) de \(CARD.couleurDeCarte)")
}
"""

st.code(code, language='swift')
