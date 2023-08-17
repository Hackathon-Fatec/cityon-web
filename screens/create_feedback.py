import streamlit as st
import os as os

st.title("Cadastre Feedback")

fileupload = st.file_uploader("Escolha sua foto", type=['png', 'jpg'])


if fileupload is not None:

    with open(fileupload.name, "wb") as f:
        f.write(fileupload.read())

    st.image(fileupload.name, width=100)

col1, col2, col3 = st.columns(3)

with col1:
   st.text_input("Your name", "Bard")

with col2:
   st.text_input("Your name", "Bard2")

with col3:
   st.text_input("Your name", "Bard3")

submit = st.button("enviar")



#apaga foto do arquivo após ser enviada
if(submit):
   caminho = os.path.abspath(fileupload.name)
   os.remove(caminho)

