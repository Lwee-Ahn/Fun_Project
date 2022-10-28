import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title= "Login",
    page_icon = '🍥',
    layout="centered"
)
def load_littieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")


if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
    st.balloons()
    lottie_hello = load_littieurl("https://assets6.lottiefiles.com/packages/lf20_pkrfkdjy.json")
    st_lottie(lottie_hello,height=400,key="Hello")
    st.markdown("[Return to Main Page](Home/#enjoy)")
    
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed. Try Again")
    
else:
    pass