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

if st.button('Show code                    '):
    code = """
struct gradient: View {
    @State var gradientChoix : Int = 0
    var body: some View {
        
        VStack{
            
            switch gradientChoix{
            case 1 :
                ExtGradient1()
            case 2 :
                ExtGradient2()
            case 3 :
                ExtGradient3()
            case 4 :
                ExtGradient4()
            case 5 :
                ExtGradient5()
            case 6 :
                ExtGradient6()
            default :
                Color.white.ignoresSafeArea()
            
        }
        VStack{
            ButtonQuestion(text: "1° Gradient", changeNumber: 1, gradientChoix: $gradientChoix)
            ButtonQuestion(text: "2° Gradient", changeNumber: 2, gradientChoix: $gradientChoix)
            ButtonQuestion(text: "3° Gradient", changeNumber: 3, gradientChoix: $gradientChoix)
            ButtonQuestion(text: "4° Gradient", changeNumber: 4, gradientChoix: $gradientChoix)
            ButtonQuestion(text: "5° Gradient", changeNumber: 5, gradientChoix: $gradientChoix)
            ButtonQuestion(text: "6° Gradient", changeNumber: 6, gradientChoix: $gradientChoix)
        }
 
       
        
}
}
    

struct gradient_Previews: PreviewProvider {
    static var previews: some View {
        gradient()
    }
}

struct ExtGradient1 :View{
    var body: some View{
    HStack{
        Text("Hello World")
            .padding()
            .foregroundColor(.white)
            .font(.largeTitle)
            .background(
                LinearGradient(gradient: Gradient(colors: [.white, .black]), startPoint: .top, endPoint: .bottom)
            )
    }
    }
}

struct ExtGradient2 : View{
    var body : some View {
        Text("Hello World")
            .padding()
            .foregroundColor(.white)
            .font(.largeTitle)
            .background(
                LinearGradient(gradient: Gradient(colors: [.white, .red, .black]), startPoint: .top, endPoint: .bottom)
            )
    }
}

struct ExtGradient3 : View{
    var body : some View {
        Text("Hello World")
            .padding()
            .foregroundColor(.white)
            .font(.largeTitle)
            .background(
                LinearGradient(gradient: Gradient(colors: [.white, .red, .black]), startPoint: .leading, endPoint: .trailing)
            )
    }
}

struct ExtGradient4 : View{
    var body : some View {
        Circle()
            .fill(
                RadialGradient(gradient: Gradient(colors: [.red, .yellow, .green, .blue, .purple]), center: .center, startRadius: 50, endRadius: 100)
            )
            .frame(width: 200, height: 200)
    }
}
struct ExtGradient5 : View{
    var body : some View {
        Circle()
            .fill(
                AngularGradient(gradient: Gradient(colors: [.red, .yellow, .green, .blue, .purple, .red]), center: .center)
            )
            .frame(width: 200, height: 200)
    }
}
struct ExtGradient6 : View{
    var body : some View {

        Circle()
            .strokeBorder(
                AngularGradient(gradient: Gradient(colors: [.red, .yellow, .green, .blue, .purple, .red]), center: .center, startAngle: .zero, endAngle: .degrees(360)),
                lineWidth: 50
            )
            .frame(width: 200, height: 200)

    }
}


struct ButtonQuestion :View{
    var text : String
    var changeNumber :Int
    @Binding var gradientChoix : Int
    var body : some View {
    Button(action : {
        gradientChoix = changeNumber
    },label : {

        ZStack{
            Rectangle()
                .frame(width: 90, height: 30 )
                .foregroundColor(.red).cornerRadius(10.0)
            HStack{
                Image(systemName: "eyedropper").foregroundColor(.white)

                Text(text).foregroundColor(.white)
        }

    }
    })
}
}
}
        """
    st.code(code, language='swift')

st.markdown("""
---

 
""")



