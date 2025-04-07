import streamlit as st
 
def login_screen():
     st.title("Please Login.")
     button_with_image = """
         <button class="gsi-material-button" style="background-color: rgba(128, 128, 128, 0.5); border: none; border-radius: 8px; padding: 10px; cursor: pointer; display: flex; align-items: center; gap: 8px;">
           <div class="gsi-material-button-icon">
             <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" xmlns:xlink="http://www.w3.org/1999/xlink" style="display: block; width: 24px; height: 24px;">
               <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"></path>
               <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"></path>
               <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"></path>
               <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"></path>
               <path fill="none" d="M0 0h48v48H0z"></path>
             </svg>
           </div>
           <span class="gsi-material-button-contents" style="font-size: 16px;">Login with Google</span>
         </button>
     """
     st.markdown(button_with_image, unsafe_allow_html=True)
grade = 0
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
    st.write(f"Username: {user.name}")
    gradenotog = st.radio(label="Select your Grade Level:", options=[r"1$^st$ - 3$^rd$", r"4$^th$ - 5$^th$", r"6$^th$ - 8$^th$", r"9$^th$ & 10$^th$", r"11$^th$ & 12$^th$"], index=None)
    if gradenotog is r"1$^st$ - 3$^rd$":
        grade = 1
    elif gradenotog is r"4$^th$ - 5$^th$":
        grade = 2
    elif gradenotog is r"6$^th$ - 8$^th$":
        grade = 3
    elif gradenotog is r"9$^th$ & 10$^th$":
        grade = 4
    elif gradenotog is r"11$^th$ & 12$^th$":
        grade = 5
    st.button("Log out", on_click=st.logout, icon=":material/logout:")
    logo = st.logo(image=pic, size="large", link="https://quizes.streamlit.app/settings", icon_image=pic)
