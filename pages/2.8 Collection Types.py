# Contents of ~/my_app/streamlit_app.py
from cProfile import label
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
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
#### Example _countries_
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
#### Example _cats_
""")
code = """
// Déclaration d'un array de strings
var cats: [String] = ["minou", "leChat", "monsieur", "garfield", "felix", "pspspspspsps"]

// Afficher l'array
print(cats)

// Afficher chaque élément de l'array
for cat in cats {
    print(cat)
}

// Afficher chaque élément de l'array et leur position dans l'array
for (index, cat) in cats.enumerated() {
    print("\(cat) est le \(index + 1) élement de mon tableau")
}

// Connaitre le nombre d'éléments dans l'array
cats.count

// Afficher le 4ème élément de l'array (Index 3)
print(cats[3])


// Savoir si mon array contient l'élément "félix"
if cats.contains("felix") {
    print("Felix est dans le tableau")
}

// Insérer gamixQuinze dans l'array en 3ème position (index 2)
cats.insert("gamixQuinze", at: 2)

// Supprimer le dernier élément de l'array
print(cats.removeLast())

// Supprimer le 4ème élément de l'array (index 3)
cats.remove(at: 3)

// Remplacer le 3ème élément par gamixTreize
cats[2] = "gamixTreize"
print(cats)

// Déclaration d'une fonction avec 2 paramètres (1 de type String et 1 de type Int) qui doit me retourner un élément de type String
func catIdentity(name: String, age: Int) -> String {
    let name = name
    let age = age

    return "Le chat s'appelle \(name) et a \(age) ans"
}

// Appels de la fonction pour qu'elle s'éxecute avec des arguments personalisés
catIdentity(name: "Jean", age: 10)

catIdentity(name: "paul", age: 1)
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
