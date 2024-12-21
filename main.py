import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Oleksii Timonov")
    content = """
    Hi, My name is Oleksii Timonov and I am just start teaching python and I will add some more 
information later on
"""
    st.info(content)