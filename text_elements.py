import streamlit as st
import os

# Title of the App
st.title("This is the App Title")

# Header of section
st.header("This is a Header")

# Sub-header of section
st.subheader("This is a Sub-header")

# Markdown Text
st.markdown("This is a ***Markdown*** Text!")

# Caption for the images and charts
st.caption("This is caption")

# Displaying code snippets
code_snippet = """
def greet(name):
    print(f'Hello {name}!')
"""
st.code(code_snippet, language="python")

# Dividing the sections
st.divider()

# Rendering an image
image_path = os.path.join(os.getcwd(), "static", "BG.png")
st.image(image_path)
