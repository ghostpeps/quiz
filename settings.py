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
    st.button(label="Change Profile Picture", type="tertiary")
    st.write(f"Username: {st.experimental_user}")
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
