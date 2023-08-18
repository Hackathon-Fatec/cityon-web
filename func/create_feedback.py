import streamlit as st
from PIL import Image
import os
from get_cities import get_cities
import psycopg2
from db import insert_itens
from transformers import pipeline
from googletrans import Translator
import datetime

pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")

st.title("Cadastre Feedback de um Local")

fileupload = st.file_uploader("Foto do local", type=['png', 'jpg'])


if fileupload is not None:
    with open(fileupload.name, "wb") as f:
        f.write(fileupload.read())
    st.image(fileupload.name, width=100)



city, name, data = st.columns(3)
with city:
    cidade = st.selectbox("Cidade do Local", get_cities())

with name:
    nome = st.text_input("Nome do local", "", placeholder="Praça da Sé")

with data:
    today_data = st.date_input("Data que a foto foi tirada", datetime.date(2023, 8, 18))

street = st.text_input("Rua", "", placeholder="Rua, Bairro")

opinion = st.text_area("Descreva sobre esse local", "", placeholder="Este local é...")
cont = len(opinion)

st.write("Quantidade de caracteries: ", cont)



submit = st.button("Enviar Feedback")

#apaga foto do arquivo após ser enviada
if(submit):
    if fileupload:
        caminho = os.path.abspath(fileupload.name)
        with open(caminho, 'rb') as img_file:
            imagem_data = img_file.read()

        hash_img = psycopg2.Binary(imagem_data)
        
        if hash_img and city and street and opinion and today_data:
            translator = Translator()
            translated_opinion = translator.translate(opinion, dest="en")
            sentiment = pipe(translated_opinion.text)[0]['label']
            res = insert_itens(nome, hash_img, cidade, street, opinion, sentiment.title(), str(today_data))

            if res:
                st.success('Feedback enviado com sucesso!', icon="✅")
                st.balloons()
            else:
                st.error('Não foi possivel enviar o feedback!', icon="🚨")
        else:
            st.error('Há campos vazios!', icon="🚨")
        os.remove(caminho)
    else:
        st.warning('Adicione uma imagem!', icon="⚠️")

