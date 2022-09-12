# https://blog.streamlit.io/introducing-multipage-apps/

# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()



st.markdown("<h1 style='text-align: center; color: black;'>Welcome to Swift!</h1>", unsafe_allow_html=True)
st.image("https://cdn.arstechnica.net/wp-content/uploads/2015/06/swift-federighi.jpg")

st.markdown("""
Swift (introduced at Apple's 2014 Worldwide Developers Conference) is an open source combines the best of `C` and `Objective-C`.

It's ideal for creating new apps and works seamlessly with `Objective-C`, so it's compatible with apps previously created in that language.

Swift is a **save** language :
- Explicit object "type"
- Type inference
- Optionals
- Error hanling


#### Playfround
- Open **Xcode**
- Choose **iOS**, select the **Blank template** and click Next
- Choose a name
- Click create
""")