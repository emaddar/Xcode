# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# TabView

#### Example :  

""")
from PIL import Image
image = Image.open('tabview.png')
st.image(image, width=500)

if st.button('Show code'):
    code = """
    struct ContentView: View {
    var body: some View {
        TabView{
            RGB()
            //view préalablement créée
                .tabItem {
                    Label("Color", systemImage: "eyedropper")
                }
            Icons()
                .tabItem {
                               Label("Volume", systemImage: "speaker.fill")
                           }
            SliderView()
                .tabItem {
                            Label("Slider", systemImage: "thermometer.snowflake")
                }

        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
        """
    st.code(code, language='swift')

st.markdown("""
---
""")

