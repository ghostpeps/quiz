import streamlit as st

if profile is None:
    st.title("Sign Up")
    with st.form("sign-up", enter_to_submit=False):
        username = st.text_input(label="Username:", value=None, max_chars=50, placeholder="Username")
        password = st.text_input(label="Password:", value=None, max_chars=50, type="password", placeholder="Password")
        if username and password is not None:
            submit = st.form_submit_button(label="Submit", icon=":material/check:", disabled=False)
        elif username and password is None:
            submit = st.form_submit_button(label="Submit", icon=":material/check:", disabled=True)
    if submit:
        st.switch_page("quizes.py")
elif profile is not None:
    st.write("Profile Picture:")
