import streamlit as st

def login_screen():
    st.title("Please Login.")
    st.button("Log in with Google", on_click=st.login, icon=":material/login:")
    button_with_image = """
        <style>
        .image-button {
            background-color: transparent;
            border: 2px solid #037bfc;
            cursor: pointer;
            border-radius: 12px;
        }
        .image-button:hover {
            background-color: rgba(92, 126, 228, 0.25);
            border: 2px solid #037bfc;
        }
        .image-button img {
            width: auto;
            height: auto;
        }
        </style>
        <button class="image-button">
            <img src="google.png" alt="    Login with Google">
        </button>
    """
    st.markdown(button_with_image, unsafe_allow_html=True)
user = st.experimental_user
if not user.is_logged_in:
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
        pic = picture.name
        image = st.image(image=pic, width=218)
        logo = st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
    elif picture is None:
        pic = "profile-pic.png"
    st.write(f"Username: {user}")
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
    logo = st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
