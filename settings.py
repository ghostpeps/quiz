import streamlit as st

def login_screen():
    st.title("Please Login.")
    st.button("Log in with Google", on_click=st.login, icon=":material/login:")
if not st.experimental_user.is_logged_in:
    login_screen()
else:
    st.title("Settings")
    st.write(f"Username: {st.experimental_user}")
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
