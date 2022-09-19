# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# 

#### Example 1 : Change background color :heart: :green_heart: :blue_heart:

""")
from PIL import Image
image = Image.open('Simple4.png')
st.image(image, width=700)

if st.button('Show code'):
    code = """
    struct SwiftUIView: View {
        @State var backColor: Color = Color.white
        var body: some View {
            ZStack {
            backColor
                    .ignoresSafeArea()
                HStack {
                    
                    ExtButton(text: "Red", fond: .red, backColor: $backColor)
                    ExtButton(text: "Green", fond: .green, backColor: $backColor)
                    ExtButton(text: "Blue", fond: .blue, backColor: $backColor)
                    ExtButton(text: "Yellow", fond: .yellow, backColor: $backColor)
                }
            }
            
            
            
        }
    }

    struct ExtButton : View{
        var text: String
        var fond: Color
        @Binding var backColor: Color
        var body: some View{
            Button {
                backColor = fond
            } label: {
                HStack {
                    Image(systemName: "pencil")
                    Text(text)
                }
                .padding()
                .background(fond)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
        }
    }
        """
    st.code(code, language='swift')

st.markdown("""
---
""")






























st.markdown("""
# 

#### Example 2 : click to print icon

""")
from PIL import Image
image = Image.open('Simple10.png')
st.image(image, width=700)

if st.button('Show code'):
    code = """

struct ContentView: View {
    @State var ImageString: String = ""
            var body: some View {
                VStack {
                    Image(systemName: ImageString)
                        .foregroundColor(.black)
                        .font(.system(size: 155))
                    HStack {
                        ExtButton(fond: .red, myImageB: "hifispeaker.2", ImageString: $ImageString)
                        ExtButton(fond: .blue, myImageB: "speaker.wave.3.fill", ImageString: $ImageString)
                        ExtButton(fond: .red, myImageB: "speaker.zzz.fill", ImageString: $ImageString)
                        ExtButton(fond: .blue, myImageB: "speaker.slash", ImageString: $ImageString)
                    }
                }

            }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


struct ExtButton : View{
    var fond: Color
    var myImageB: String
    @Binding var ImageString: String

    var body: some View{
        Button {
             ImageString = myImageB
        } label: {
            HStack {
                Image(systemName: myImageB)
            }
            .padding()
            .foregroundColor(.white)
            .background(fond)
            .cornerRadius(10)
        }
    }
}

        """
    st.code(code, language='swift')

st.markdown("""
---
""")



