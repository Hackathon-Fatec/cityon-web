import streamlit as st
import os
from get_cities import get_cities
import psycopg2
from db import insert_itens
import datetime
from predict import predict
from get_location import obter_localizacao_da_foto, latlong_for_address

from streamlit_folium import folium_static



def create_feedback():
    st.title("Cadastre Feedback de um Local")

    fileupload = st.file_uploader("Foto do local", type=['png', 'jpg'])

    

    if fileupload is not None:
        with open(fileupload.name, "wb") as f:
            f.write(fileupload.read())
        st.image(fileupload.name, width=100)

    cities = get_cities()
   
    cidade = st.selectbox("Cidade do Local", cities)
    nome = st.text_input("Nome do local", "", placeholder="Praça da Sé")

    today_data = st.date_input("Data que a foto foi tirada", datetime.date(2023, 8, 18))

    rua = st.text_input("Rua", "", placeholder="Rua")
    opinion = st.text_area("Descreva sobre esse local", "", placeholder="Este local é...")
    cont = len(opinion)

    col1, col2, col3 = st.columns(3)
    with col1:
        locate = st.button("Obter Localização")        
    
    with col2:
        submit = st.button("Enviar Feedback")
    
    with col3:    
        st.write("Quantidade de caracteres: ", cont)

    
    if locate:
        latitude_to_map, longitude_to_map = get_lat_long(rua, cidade)
        if latitude_to_map and longitude_to_map:
            st.session_state.latitude = latitude_to_map
            st.session_state.longitude = longitude_to_map
            folium_static(get_map(latitude_to_map, longitude_to_map))
            st.session_state.show_warning = False
        else:
            st.warning('Não foi possivel obter a localização!', icon="⚠️")

    if submit:
        if fileupload:
            caminho = os.path.abspath(fileupload.name)
            with open(caminho, 'rb') as img_file:
                imagem_data = img_file.read()

            hash_img = psycopg2.Binary(imagem_data)
            latitude, longitude = get_lat_long(rua or '', cidade)
            
            if hash_img and (cidade or rua )and opinion and today_data and latitude and longitude:
                sentiment = predict(opinion)
                res = insert_itens(nome, hash_img, cidade, rua, opinion, sentiment.title(), str(today_data), latitude, longitude)

                if res:
                    st.success('Feedback enviado com sucesso!', icon="✅")
                    st.balloons()
                else:
                    st.error('Não foi possível enviar o feedback!', icon="🚨")
            else:
                st.error('Não foi possível enviar o feedback! Preencha todos os campos.', icon="🚨")
            os.remove(caminho)
        else:
            st.warning('Adicione uma imagem!', icon="⚠️")