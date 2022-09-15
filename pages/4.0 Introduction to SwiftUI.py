# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Introduction à SwiftUI

#### Example : My first app. 📲

""")
from PIL import Image
image = Image.open('MyfirstApp.png')

st.image(image, width=300)

code = """
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack{
            Text("My first app.")
                .font(.system(size: 36))
            Spacer()
            HStack{
                Text("Sweet")
                    .foregroundColor(Color.red)
                    .font(.system(size: 36))
                Image(systemName: "heart.fill")
                    .foregroundColor(Color.red)
                    .font(.system(size: 36))
            }
            Spacer(minLength: 50)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
"""

st.markdown("""
---
""")

st.code(code, language='swift')

from PIL import Image
image = Image.open('SecondApp.png')

st.image(image, width=300)


st.markdown("""
#### Example : My second app. 📱 📱 📱

""")



code = """
import SwiftUI

struct Test2: View {
    var body: some View {
        ZStack{
            Rectangle()
                .fill(Color.red)
            Rectangle()
                .fill(Color.green)
                .frame(width: 150, height: 120)
                .cornerRadius(15)
            Circle()
                .fill(Color.blue)
                .frame(width: 100, height: 100)
            Text("hello")

    }
}
}

struct Test2_Previews: PreviewProvider {
    static var previews: some View {
        Test2()
    }
}
"""

st.code(code, language='swift')
