# Contents of ~/my_app/streamlit_app.py
from cProfile import label
from ctypes import sizeof
import streamlit as st

st.set_page_config(
    page_icon=":apple:",
)


st.markdown("""
# Boutons & Bindings

#### Example 1: Counter :arrows_counterclockwise:

""")
from PIL import Image
image = Image.open('Simple1.png')
st.image(image, width=300)

if st.button('Show code'):
    code = """
    @State var counter: Int = 0
        var body: some View {
            VStack{
                        Text("Count : \(self.counter)")
                        .padding()
            
                        Button(
                            action: {self.counter += 1},
                            label: {
                                HStack {
                                    Image(systemName: "plus")
                                    Text("Increment")
                                       }
                                   }
                              )
                            .padding(10.0)
                            .overlay(
                                RoundedRectangle(cornerRadius: 5)
                                .stroke(lineWidth: 2.0)
                                 )
                Spacer()
            }
        }
    }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")





st.markdown("""


#### Example 2: Print random double number in $[0,10]$ :game_die:

""")
from PIL import Image
image = Image.open('Simple2.png')
st.image(image, width=300)

if st.button('Show code '):
    code = """
    @State var random: Double = 0
        var body: some View {
            VStack{
                        Text("Random : \(self.random)")
                        .padding()
            
                        Button(
                            action: {self.random = Double.random(in: 0...10)},
                            label: {
                                HStack {
                                    Image(systemName: "play.circle")
                                    Text("Create")
                                       }
                                   }
                              )
                            .padding(10.0)
                            .overlay(
                                RoundedRectangle(cornerRadius: 5)
                                .stroke(lineWidth: 2.0)
                                 )
                Spacer()
            }
        }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")








st.markdown("""


#### Example 3 : Increment percentage values with slider :100:

""")
from PIL import Image
image = Image.open('Simple3.png')
st.image(image, width=300)

if st.button('Show code  '):
    code = """
        @State private var pourcentage: Double = 0.5
    var body: some View {
        VStack {
              Text("\(Int(pourcentage*100)) %")
                .bold()
                .padding()
                
              
              Button("Incrémenter") {
                            pourcentage += 0.01
                          }
              .padding()
              .foregroundColor(.red)
              .overlay(
                    RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 2.0)
                    .fill(Color.red)
                      )
            
            Slider(value: $pourcentage, in: 0...1)
            
            Spacer()
        }
    }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")








st.markdown("""


#### Exercice : Change background color :heart: :green_heart: :blue_heart:

""")
from PIL import Image
image = Image.open('Simple4.png')
st.image(image, width=300)

if st.button('Show Lorenzo\'s code '):
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
    st.code(code, language='swift')

st.markdown("""
---
""")






st.markdown("""


#### Idea (Emad) : Change background randomely :game_die: :game_die: :game_die: :game_die: :game_die:

""")
from PIL import Image
image = Image.open('Simple5.png')
st.image(image, width=300)

if st.button('Show code     '):
    code = """
    var myList: [Color] = [.red, .green, .blue, .orange, .black, .gray, .accentColor, .brown, .cyan, .indigo, .mint, .pink, .purple, .primary, .yellow, .secondary, .teal]
    
    @State var myColor :Color = Color.white
        var body: some View {
                ZStack{
                    myColor
                    .ignoresSafeArea()
                    
                    HStack(){
                        Button(action: {
                            myColor = myList.randomElement()!
                        },
                               label:{
                            HStack{
                                Image(systemName: "paintbrush.pointed.fill")
                                Text("Alea")
                            }
                            .padding()
                            .background(Color.black)
                            .foregroundColor(.white)
                            .cornerRadius(15)
                        })
                }
            }
        }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")











st.markdown("""


#### Idea (Emad) : My first calculator :heavy_plus_sign: :heavy_minus_sign: :heavy_multiplication_x: :heavy_division_sign:

""")
from PIL import Image
image = Image.open('calc.png')
st.image(image, width=300)

if st.button('Show code      '):
    code = """
    @State private var num1:Double = 0
    @State private var num2:Double = 0
    @State private var plus: Double = 0

        var body: some View {
            VStack {
                HStack{
                TextField("Enter Num_1", value: $num1, format: .number)
                    .textFieldStyle(.roundedBorder)
                    .font(.system(size: 20, weight: .heavy, design: .default))
                    .padding()


                TextField("Enter Num_2", value: $num2, format: .number)
                    .textFieldStyle(.roundedBorder)
                    .font(.system(size: 20, weight: .heavy, design: .default))
                    .padding()

                }
                .padding()




                HStack{
                                    Button(action: {
                                        plus = num1 + num2
                                    },
                                           label:{
                                            Image(systemName: "plus")
                                        .background(Color.blue)
                                        .foregroundColor(.white)
                                    }).padding()
                                    .frame(width: 80, height: 60)
                                    .background(Color.blue)
                                    .cornerRadius(15)


                                Button(action: {
                                    plus = num1 - num2
                                },
                                       label:{
                                        Image(systemName: "minus")
                                    .foregroundColor(.white)
                                })
                                    .padding()
                                    .frame(width: 80, height: 60)
                                    .background(Color.blue)
                                    .cornerRadius(15)


                                Button(action: {
                                    plus = num1 * num2
                                },
                                       label:{
                                        Image(systemName: "multiply")
                                    .foregroundColor(.white)
                                })
                                .padding()
                                .frame(width: 80, height: 60)
                                .background(Color.blue)
                                .cornerRadius(15)


                                Button(action: {
                                    plus = num1 / num2
                                },
                                       label:{
                                        Image(systemName: "divide")
                                    .foregroundColor(.white)
                                })
                                .padding()
                                .frame(width: 80, height: 60)
                                .background(Color.blue)
                                .cornerRadius(15)

                }.padding()


                Image(systemName: "equal")
                    .padding()
                

                Text("\(plus)")
                    .padding()
                    .font(.system(size: 20, weight: .heavy, design: .default))
                    .multilineTextAlignment(.center)
                    .overlay(
                                                    RoundedRectangle(cornerRadius: 5)
                                                    .stroke(lineWidth: 2.0)
                                                     )
                }

        }
    """
    st.code(code, language='swift')

st.markdown("""
---
""")
