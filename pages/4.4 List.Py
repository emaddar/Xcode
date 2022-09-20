# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# List & Forms

#### Example 1 : 

""")
#from PIL import Image
#image = Image.open('Simple4.png')
#st.image(image, width=700)

if st.button('Show code'):
    code = """
        struct Weather: Identifiable{
            var id = UUID()
            var name: String
            var icon: String
        }

        var weathers = [
            Weather(name: "sun", icon: "sun.max.fill"),
            Weather(name: "cloud", icon: "smoke.fill"),
            Weather(name: "storm", icon: "cloud.bolt.fill")
        ]


        struct ExoWeather: View {
            var body: some View {
                    List(weathers) { weather in
                            ExtractedView(weather: weather)
                    }
            }
        }

        struct ExoWeather_Previews: PreviewProvider {
            static var previews: some View {
                ExoWeather()
            }
        }

        struct ExtractedView: View {
            var weather: Weather
            var body: some View {
                HStack{
                    Image(systemName: weather.icon)
                    /*@START_MENU_TOKEN@*/Text(weather.name)/*@END_MENU_TOKEN@*/
                }
            }
        }
        """
    st.code(code, language='swift')

st.markdown("""
---


""")



