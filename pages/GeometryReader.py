# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# GeometryReader

A container view that defines its content as a function of its own size and coordinate space.

#### Example : flags 

""")
from PIL import Image
image = Image.open('flags.png')
st.image(image, width=500)

if st.button('Show code'):
    code = """

struct geometryReaderExemple: View {
    var body: some View {
       
        VStack {
//            Spacer(minLength: 300)
            Spacer(minLength: 20)
            ExtractedView(color1: .black, color2: .yellow, color3: .red, height: 0.7, width: 0.34)
            ExtractedView(color1: .blue, color2: .white, color3: .red, height: 1, width: 0.34)
            ExtractedView(color1: .green, color2: .red, color3: .red, height: 0.7, width: 0.34)
            
        }
        

    }
}

struct geometryReaderExemple_Previews: PreviewProvider {
    static var previews: some View {
        geometryReaderExemple()
    }
}

struct ExtractedView: View {
    var color1: Color
    var color2: Color
    var color3: Color
    var height: Double
    var width: Double
    var body: some View {
        HStack {
            
            GeometryReader{ geometry in
                
                HStack(spacing: 0) {
                    Rectangle().fill(color1)
                        .frame(
                            width: geometry.size.width * width,
                            height: geometry.size.height * height
                        )
                    Rectangle().fill(color2)
                        .frame(
                            width: geometry.size.width * width,
                            height: geometry.size.height * height
                        )
                    Rectangle().fill(color3)
                        .frame(
                            width: geometry.size.width * width,
                            height: geometry.size.height * height
                            
                        )
                }
                .ignoresSafeArea()
            }
        }
    }
}
        """
    st.code(code, language='swift')

st.markdown("""
---

 
""")



