import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image 

st.set_page_config(
    page_title= "Softunroll",
    page_icon = '🍥',
    layout="centered"
)

def load_littieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("Softunroll")
col1,col2=st.columns([2,1])
with col1:
    st.markdown("**Softunroll** is an American subscription video on-demand over-the-top streaming service owned by **Lwee** through a joint venture between **Zone Pictures** and **Zone Music Entertainment Japan's Aniplex**. The company focuses on the distribution, production and licensing of *Japanese anime* and *dorama*.Softunroll offers over 1,000 anime shows, more than 200 East Asian dramas to users, and around 80 manga titles as Softunroll Manga, although not all programming is available worldwide due to *licensing restrictions*. Softunroll also releases titles on home video either directly or by having select anime titles released through its distribution partners (**Sentai Filmworks**, **Viz** Media, **Discotek** Media, and its corporate sibling, **Aniplex** of America in North America; Anime Limited in the United Kingdom).")
with col2:
    lottie_hello = load_littieurl("https://assets2.lottiefiles.com/packages/lf20_ueIPoNUkNO.json")
    st_lottie(lottie_hello,key="Hello")
    # st.write("If you already have an account")
    # st.markdown("[Click to Log in](Login)")
    # st.write("If you don't have an account")
    # st.markdown("[Click to Sign up](Signup)")

st.subheader("Enjoy!!")

choose_options = st.selectbox("What do you want to do? Read Manga or Watch Anime?",
        ['Watch Anime','Read Manga'])

if choose_options == "Watch Anime":
    radio_options = st.radio("Choose your favourite Genre",['Shonen','Horror','Comedy'], horizontal = True )
    if radio_options=='Horror':
        st.warning(":warning: Content Warning!!! :warning:\n The following videos contain scenes that may be uncomfortable for some viewers.Children as well as youth audiences, please exercise cautions beforoe watching.")
        first,second = st.columns(2)
        with first:
            st.video("https://youtu.be/v_SInAQqN-Y")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=v_SInAQqN-Y&list=PLwLSw1_eDZl28nYqV_gPaNLe-PL2JEnCR)")

            st.video("https://youtu.be/msuo-BMNzkA")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=msuo-BMNzkA&list=PLgGyVwzdovwajsidBmkMe0sfpFRMaOl2d)")
        with second:
            st.video("https://youtu.be/HS9BLbk7vzc")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=HS9BLbk7vzc&list=PLgGyVwzdovwZBCs7SsXl1JLEMdpY_tNj3)")

            st.video("https://youtu.be/Q_peJ3FbtsM")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=Q_peJ3FbtsM&list=PLwLSw1_eDZl17reRE_OPjNhFb-IgV1aYY)")

    if radio_options=='Shonen':
        first,second =st.columns(2)
        with first:
            st.video("https://youtu.be/sLMep-eefDQ")
            st.markdown("[Click Here to watch full season>>>](https://www.crunchyroll.com/series/GYQ4MW246/naruto-shippuden)")

            st.video("https://youtu.be/0JJptAoOxQA")
            st.markdown("[Click Here to watch full season>>>](https://www.crunchyroll.com/series/GYQWNXPZY/fire-force)")

        with second:
            st.video("https://youtu.be/QOF75HhM7fc")
            st.markdown("[Click Here to watch full season>>>](https://www.crunchyroll.com/series/GYQ4MW246/naruto-shippuden)")

            st.video("https://youtu.be/nida6gx05kk")
            st.markdown("[Click Here to watch full season>>>](https://www.crunchyroll.com/series/GYP8DP1MY/jojos-bizarre-adventure)")

    if radio_options=='Comedy':
        first,second =st.columns(2)
        with first:
            st.video("https://youtu.be/phjbaDTEikE")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=phjbaDTEikE&list=PLmQJyfHFUpd43qzSifv9CNC5nT_ourFN6)")

        with second:
            st.video("https://youtu.be/VvK6UZWNU2Q")
            st.markdown("[Click Here to watch full season>>>](https://www.youtube.com/watch?v=VvK6UZWNU2Q&list=PLwLSw1_eDZl2XdtLhB9NG2Ch050jWFm9G)")

            # st.image("https://upload.wikimedia.org/wikipedia/it/c/cb/Chainsaw_Man_Volume_1.jpg")
if choose_options == "Read Manga":
    radio_options = st.radio("Choose your favourite Genre",['Shonen','Romance','Comedy'], horizontal = True )
    if radio_options=='Shonen':
        col1,col2 = st.columns(2)
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/it/c/cb/Chainsaw_Man_Volume_1.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100037)")
            st.image("https://m.media-amazon.com/images/M/MV5BNGY4MTg3NzgtMmFkZi00NTg5LWExMmEtMWI3YzI1ODdmMWQ1XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100037)")
            st.image("https://m.media-amazon.com/images/M/MV5BN2FlYjYxMTMtZGQzYy00OWU2LTkyYWMtNWJhODhmZmM0N2FhXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100034)")

    if radio_options=='Romance':
        col1,col2 = st.columns(2)
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/en/0/04/Tonari_no_Kaibutsu-kun_manga_vol_1.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100034)")
            st.image("https://m.media-amazon.com/images/M/MV5BYWQ5OGRiNDItMGZkOC00YzMzLTgxNzAtOThmMjZlYmJjOWZlL2ltYWdlXkEyXkFqcGdeQXVyMzgxODM4NjM@._V1_.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100034)")
            st.image("https://m.media-amazon.com/images/M/MV5BYzBkOGIyMTMtZjViZC00NGY1LWFhMzItZGI2MmEwODIyYjVjXkEyXkFqcGdeQXVyNjc3MjQzNTI@._V1_FMjpg_UX1000_.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100034)")

    if radio_options=='Comedy':
        col1,col2 = st.columns(2)
        with col1:
            st.image("https://m.media-amazon.com/images/M/MV5BZmNiZTk5MDQtMjIwMi00ZDU4LTgxOWMtODYwOGU5N2E5YzY0XkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg")
            st.markdown("[Click Here to Read>>>](https://www.youtube.com/watch?v=phjbaDTEikE&list=PLmQJyfHFUpd43qzSifv9CNC5nT_ourFN6)")
            st.image("https://m.media-amazon.com/images/M/MV5BMTNjNGRhZWYtN2U0Yi00ZjU4LWI0MTUtZTc4ZDI0ZTk0YzI2XkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_FMjpg_UX1000_.jpg")
            st.markdown("[Click Here to Read>>>](https://mangaplus.shueisha.co.jp/titles/100037)")

# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
with st.sidebar:
    stars = st.select_slider(
        'Rate Us',
        options=['🌟', '🌟🌟', '🌟🌟🌟', '🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'])
    st.write(f'Thanks for giving us {stars}')
