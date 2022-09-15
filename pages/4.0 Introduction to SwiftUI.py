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

""")

st.code(code, language='swift')

from PIL import Image
image = Image.open('SecondApp.png')

st.image(image, width=300)


st.markdown("""
---
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














st.markdown("""
---
#### Example : Personel Card 😎

""")
from PIL import Image
image = Image.open('Three.png')

st.image(image, width=300)



code = """
struct correctionSantanaCard: View {
    var body: some View {
        VStack(alignment: .leading){
            HStack{
                Image(systemName: "person.crop.circle")
                    .font(.system(size: 130))
                    .foregroundColor(.orange)
                VStack (alignment: .leading){
                    Text("Danilo santana")
                        .font(.title)
                        .fontWeight(.semibold)
                    Text("Brazil")
                        .foregroundColor(.gray)
                    Text("Racing driver")
                        .bold()
                        .font(.callout)
                        .padding(.top, 40)

                }
            }
            RoundedRectangle(cornerRadius: 15)
                .foregroundColor(.gray)
                .padding(.horizontal)
        }
    }
}
"""

st.code(code, language='swift')




code = """

@State private var colorScreen = Color.white
    var body: some View {
        ZStack{
            colorScreen
                .ignoresSafeArea()

            HStack{
                Button(action: {
                    colorScreen = Color.red
                },
                       label:{
                    HStack{
                        Image(systemName: "paintbrush.pointed.fill")
                        Text("Red")
                    }
                    .padding()
                    .background(Color.red)
                    .foregroundColor(.white)
                    .cornerRadius(15)
                })

                Button(action: {
                    colorScreen = Color.green
                },
                       label:{
                    HStack{
                        Image(systemName: "paintbrush.pointed.fill")
                        Text("Green")
                    }
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(15)
                })
                Button(action: {
                    colorScreen = .blue

                },
                       label:{
                    HStack{
                        Image(systemName: "paintbrush.pointed.fill")
                        Text("Blue")
                    }
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(15)
                })
            }
        }

    }
"""
