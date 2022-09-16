# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Structures de contrôle en SwiftUI

#### Example 1: Slider Température

""")
from PIL import Image
image = Image.open('CSC1.png')
st.image(image, width=500)

if st.button('Show code'):
    code = """
        @State private var pourcentage: Double = 0
    var colorScreen : Color {
        switch pourcentage {
        case ...0 :
            return .blue
        case  1...25 :
            return .gray
        case 26... :
            return .red
        default :
            return .black
        }
    }
        
        var statee : String {
            switch pourcentage {
            case ...0 :
                return "TRES FROID"
            case  1...25 :
                return "FRAIS"
            case 26... :
                return "TROP CHAUD"
            default :
                return "ERROR"
            }
        
    }
    
        var body: some View {
            ZStack{
                Spacer()
                colorScreen
                .ignoresSafeArea()
                
          
            VStack {
                  Text("\(Int(pourcentage))")
                    .bold()
                    .font(.system(size: 20, weight: .heavy, design: .default))
                    .padding()
                
                Text("Il fait \(statee)")
                    .font(.system(size: 20, weight: .heavy, design: .default))
                    .padding()


                Slider(value: $pourcentage, in: -20...50, step: 1)

                Spacer()
            }
        }
        }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")



