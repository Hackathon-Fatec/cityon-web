import streamlit as st
from PIL import Image
import os
from get_cities import get_cities
import psycopg2
from db import insert_itens
from transformers import pipeline
from googletrans import Translator

pipe = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment-latest")

st.title("Cadastre Feedback")

fileupload = st.file_uploader("Escolha sua foto", type=['png', 'jpg'])


if fileupload is not None:
    with open(fileupload.name, "wb") as f:
        f.write(fileupload.read())
    st.image(fileupload.name, width=100)



city, name, col3 = st.columns(3)
with city:
    cidade = st.selectbox("Cidade do Local", get_cities())

with name:
    nome = st.text_input("Seu nome", "")

    street = st.text_input("Rua", "")

    opinion = st.text_area("Descreva sobre esse local", "")
    cont = len(opinion)

st.write("Quantidade de caracteries: ", cont)



submit = st.button("enviar")

#apaga foto do arquivo após ser enviada
if(submit):
    caminho = os.path.abspath(fileupload.name)
    with open(caminho, 'rb') as img_file:
        imagem_data = img_file.read()

    hash_img = psycopg2.Binary(imagem_data)
    
    if hash_img and city and street and opinion:
        translator = Translator()
        translated_opinion = translator.translate(opinion, dest="en")

        sentiment = pipe(translated_opinion.text)

        print(translated_opinion.text, sentiment)

        #res = insert_itens(nome, hash_img, cidade, street, opinion, sentiment)

    os.remove(caminho)

