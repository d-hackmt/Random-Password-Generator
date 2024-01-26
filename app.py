import streamlit as st
from PIL import Image
import random
import string
import pyperclip
import requests
from io import BytesIO


# Set page title and favicon
st.set_page_config(page_title="Password Generator", page_icon="🔒")

# Define app header
def app_header():
    st.markdown(
        """
        <div style='background-color:#F5F5F5;padding:10px;border-radius:5px'>
        <h1 style='text-align:center;color:#2e7d32;font-family:Helvetica'>Password Generator 🔒</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Define function to generate password
def generate_password(length, use_digits=True, use_punctuation=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password

# Define function to display password generator
def password_generator():
    st.subheader("Password Generator")
    app_list = {
        "Facebook": "https://www.facebook.com/",
        "Twitter": "https://twitter.com/",
        "LinkedIn": "https://www.linkedin.com/",
        "Instagram": "https://www.instagram.com/",
        "GitHub": "https://github.com/",
        "Gmail": "https://mail.google.com/",
        "Cub Bank": "https://www.cubbank.com/"
    }
    app_name = st.selectbox("Select the app", list(app_list.keys()))
    app_url = app_list[app_name]
    
    try:
        response = requests.get(app_url + "favicon.ico")
        img = Image.open(BytesIO(response.content))
        st.image(img, width=50)
    except:
        st.warning("Could not retrieve app logo")

    password_length = st.slider("Select password length", 6, 50, 12, 1)

    use_digits = st.checkbox("Use digits (0-9)")
    use_punctuation = st.checkbox("Use punctuation")

    if st.button("Generate Password"):
        password = generate_password(password_length, use_digits, use_punctuation)
        st.success("Generated Password: " + password)
        pyperclip.copy(password)
        st.success("Password copied to clipboard")

# Define app
def app():
    app_header()
    password_generator()

if __name__ == "__main__":
    app()
