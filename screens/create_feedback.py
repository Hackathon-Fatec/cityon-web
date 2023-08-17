import streamlit as st
import os as os
from list_feedback import get_cities

st.title("Cadastre Feedback")

fileupload = st.file_uploader("Escolha sua foto", type=['png', 'jpg'])


if fileupload is not None:

    with open(fileupload.name, "wb") as f:
        f.write(fileupload.read())

    st.image(fileupload.name, width=100)



col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("Cidade do Local", get_cities())

with col2:
   st.text_input("CEP", "")



st.text_input("Rua", "")

txt_area = st.text_area("Descreva sobre esse local", "")
cont = len(txt_area)

st.write("Quantidade de caracteries: ", cont)



submit = st.button("enviar")

#apaga foto do arquivo após ser enviada
if(submit):
   caminho = os.path.abspath(fileupload.name)
   os.remove(caminho)

