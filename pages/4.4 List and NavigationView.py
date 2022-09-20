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
from PIL import Image
image = Image.open('list.png')
st.image(image, width=500)

if st.button('Show code    '):
    code = """
    import SwiftUI

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


    struct WeatherView: View {
        let name: String

        var body: some View {
            Text("Selected weather: \(name)")
                .font(.largeTitle)
        }
    }



    struct ExoWeather: View {
        var body: some View {
            NavigationView{
                List(weathers) { weather in
                    NavigationLink(destination: ExtractedView1(weather: weather),
                                    label: {ExtractedView(weather: weather)}
                    
                    )
    //                    ExtractedView(weather: weather)
                }
                .navigationTitle("Weather")
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
                Text(weather.name)
            }
        }
    }



    // nouvelle écran
    struct ExtractedView1: View {
        var weather: Weather
        var body: some View {
            VStack{
                Text("Today is : \(Date(), style: .date)   \(Date(), style: .time)")
                    .padding(50)
                Image(systemName: weather.icon)
                    .font(.system(size: 155))
                Text("Weather : \(weather.name)")
            }
        }
    }



        """
    st.code(code, language='swift')

st.markdown("""
---

 
""")



