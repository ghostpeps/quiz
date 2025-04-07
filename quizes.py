import streamlit as st

from settings import user

from ela import days

user = user
def quizzes():
    user = global user
    co1l, co2l, co3l = st.columns([0.5, 0.3, 0.2])
    with co1l:
        st.title("Quizes")
    with co3l:
        settings = st.button(label="", type="tertiary", icon=":material/settings:")
    with co2l:
        if user.is_logged_in:
            if days == 0:
                st.markdown("streak-off.png :gray[0]")
            elif days > 0:
                st.markdown(f"streak-on.png :orange[{days}]")
        elif user.is_logged_in:
            st.write("")
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    with col1:
        ela = st.button(label="ELA", icon=":material/language_us:")
    with col2:
        math = st.button(label="Math", icon=":material/calculate:")
    with col3:
        lan = st.button(label="Languages", icon=":material/translate:")
    with col4:
        history = st.button(label="History", icon=":material/history:")
    with col5:
        science = st.button(label="Science", icon=":material/science:")
    with col6:
        music = st.button(label="Music", icon=":material/music_note:")
    with col7:
        geo = st.button(label="Geography", icon=":material/public:")
    with col8:
        st.button(label="TBD")
    with col9:
        st.button(label="N/A")
    if ela:
        st.switch_page("ela.py")
    if math:
        st.switch_page("math.py")
    if lan:
        st.switch_page("languages.py")
    if history:
        st.switch_page("history.py")
    if science:
        st.switch_page("science.py")
    if music:
        st.switch_page("music.py")
    if geo:
        st.switch_page("geography.py")
    if settings:
        st.switch_page("settings.py")
pages = [
    st.Page(page=quizes, title="Quizes", icon=":material/quiz:"),
    st.Page(page="ela.py", title="ELA", icon=":material/language_us:"),
    st.Page(page="math.py", title="Math", icon=":material/calculate:"),
    st.Page(page="languages.py", title="Languages", icon=":material/translate:"),
    st.Page(page="history.py", title="History", icon=":material/history:"),
    st.Page(page="science.py", title="Science", icon=":material/science:"),
    st.Page(page="music.py", title="Music", icon=":material/music_note:"),
    st.Page(page="geography.py", title="Geography", icon=":material/public:"),
    st.Page(page="settings.py", title="Settings", icon=":material/settings:")
]
pgs = st.navigation(pages)
pgs.run()
