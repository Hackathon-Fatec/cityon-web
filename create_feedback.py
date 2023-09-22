import streamlit as st
import os
from get_cities import get_cities
import psycopg2
from db import insert_itens
import datetime
from predict import predict
from get_location import extrair_lat_long, latlong_for_address






from streamlit_folium import folium_static



def create_feedback():
    st.title("Cadastre Feedback de um Local")

    foto = st.file_uploader("Faça o upload de uma foto", type=["jpg", "jpeg", "png"])
    
    
    
    
    cidade = ""
    pais = ""
    rua = ""
    if foto is not None:
        with open(foto.name, "wb") as f:
            f.write(foto.read())
        st.image(foto.name, width=100)
    if foto is not None:
        lat, long = extrair_lat_long(foto) 

        print(lat, long)      

        
        cidade, pais, rua = latlong_for_address(lat, long, 0)
        nome = st.text_input("Nome do local", "", placeholder="Praça da Sé")
        opinion = st.text_area("Descreva sobre esse local", "", placeholder="Este local é...")
        
    

    today_data = datetime.date.today()
    strDate = str(today_data.year) + "-" + str(today_data.month) + "-" + str(today_data.day)


    
  

    col1, col2, col3 = st.columns(3)
    
    with col1:
        if foto is not None:
            submit = st.button("Enviar Feedback")
        else:
            submit = st.button("Enviar Feedback", disabled=True)
    
   

    
    """  
    if locate:
        latitude_to_map = lat
        longitude_to_map = long
        if latitude_to_map and longitude_to_map:
            st.session_state.latitude = latitude_to_map
            st.session_state.longitude = longitude_to_map
            folium_static(get_map(latitude_to_map, longitude_to_map))
            st.session_state.show_warning = False
        else:
            st.warning('Não foi possivel obter a localização!', icon="⚠️")
    """
    if submit:
        if foto:
            caminho = os.path.abspath(foto.name)
            with open(caminho, 'rb') as img_file:
                imagem_data = img_file.read()

            hash_img = psycopg2.Binary(imagem_data)
            
            
            if hash_img and (cidade or rua )and opinion and today_data and lat and long:
                sentiment = predict(opinion)
                res = insert_itens(nome, hash_img, cidade, rua, opinion, sentiment.title(), str(today_data), lat, long)

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

create_feedback()