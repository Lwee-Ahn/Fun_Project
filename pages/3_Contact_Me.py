import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(
    page_title= "Contact Me",
    page_icon = '🍥',
    layout="centered"
)

def load_littieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/astronaut2026@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages/style/style.css")

st.write("")
st.write("")
st.write("")
st.subheader("You can also contact me via these social media")

facebook,instagram,twitter,youtube=st.columns(4)

with facebook:
    lottie_fb = load_littieurl("https://assets2.lottiefiles.com/packages/lf20_xwabp3dh.json")
    st_lottie(lottie_fb,key="facebook",width=70)
    st.markdown("[Facebook](https://www.facebook.com/meemee.meemee.1044)")
with instagram:
    lottie_ig = load_littieurl("https://assets4.lottiefiles.com/packages/lf20_86afyky0.json")
    st_lottie(lottie_ig,key="instagram",width=70)
    st.markdown("[Instagram](https://www.instagram.com/zura_janai_lwee_da/)")
with twitter:
    lottie_tt= load_littieurl("https://assets9.lottiefiles.com/packages/lf20_5mhyg2hz.json")
    st_lottie(lottie_tt,key="twitter",width=70)
    st.markdown("[Twitter](https://www.facebook.com/meemee.meemee.1044)")
with youtube:
    lottie_yt= load_littieurl("https://assets6.lottiefiles.com/packages/lf20_ej2lfhv2.json")
    st_lottie(lottie_yt,key="youtube",width=70)
    st.markdown("[Youtube](https://www.facebook.com/meemee.meemee.1044)")
