import streamlit as st

def login_screen():
    st.title("Please Login.")
    st.button("Log in with Google", on_click=st.login, icon=":material/login:")
if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.title("Settings")
    pic = None
    if pic is None:
        pic = "profile-pic.png"
    st.write("Profile Picture:")
    image = st.image(image=pic, width=218)
    button = st.button(label="Change Profile Picture", type="tertiary")
    picture = None
    if button:
        picture = st.file_uploader(label="", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if picture is not None:
        pic = picture
        image = st.image(image=pic, width=218)
        logo = st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
        st.write(picture.name)
    elif picture is None:
        pic = "profile-pic.png"
    st.write(f"Username: {st.experimental_user}")
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
    logo = st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
