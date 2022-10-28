import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title= "Signup",
    page_icon = '🍥',
    layout="centered"
)
def load_littieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

emptycontainer = st.empty()

with emptycontainer.form("Signup"):
    st.markdown("### Please Fill the Requirements Below!")

    first_name = st.text_input("First Name ", placeholder='Type Here')
    last_name = st.text_input("Last Name", placeholder = 'Type Here')
    # gender = st.radio("Choose your Gender",['Male','Female','Other'],horizontal=True)
    email = st.text_input("Email", placeholder='e.g. tt@kuku.com')
    password = st.text_input("Password", type='password')
    repassword = st.text_input("Retype your Password", type='password')
    
    text = st.text_area("Terms and Agreements","Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",disabled=True)

    check = st.checkbox("I agree Terms and Regulations",)


    if password != repassword:
        st.warning("The password must be match")
    else:
        pass
    
    st.write("")
    submit = st.form_submit_button("Submit")
    if submit:
        # emptycontainer.empty()
        st.success("Account created successfully")

        lottie_hello = load_littieurl("https://assets6.lottiefiles.com/packages/lf20_pkrfkdjy.json")
        st_lottie(lottie_hello,height=400,key="Hello")
        st.markdown("[Return to Main Page](Home/#you-can-start-and-watch-here)")
