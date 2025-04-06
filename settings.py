import streamlit as st

pic = None
def login_screen():
    st.title("Please Login.")
    st.button("Log in with Google", on_click=st.login, icon=":material/login:")
if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.title("Settings")
    if pic is None:
        pic = "profile-pic.png"
    st.write("Profile Picture:")
    st.image(image=pic, width=218)
    button = st.button(label="Change Profile Picture", type="tertiary")
    if button:
        picture = st.file_uploader(label="", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if picture is not None:
        pic = picture
    elif picture is None:
        pic = "profile-pic.png"
    st.write(f"Username: {st.experimental_user}")
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
