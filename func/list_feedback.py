import streamlit as st
from db import get_itens, get_filtred_cities
from get_cities import get_cities
from PIL import Image
import io

cities = get_cities()

def list_feedback():
    st.title("Busque Feedbacks de sua cidade")
    
    city, sentiment = st.columns(2)
    with city:
        city_choosed = st.selectbox('Escolha a cidade', cities)
    with sentiment:
        sentiment_choosed = st.selectbox('Escolha o sentimento do comentario', ["Positivo", "Negativo", "Todos"])

    st.write("Content outside the cards.")

    if st.button("Buscar"):
        filtred_cities = []
        if sentiment_choosed == "Todos":
            filtred_cities = get_itens(city_choosed)
        else:
            filtred_cities = get_filtred_cities(city_choosed, "Positive" if sentiment_choosed == "Positivo" else "Negative")

        if len(filtred_cities) > 0:
            for local in filtred_cities:
                bytes_io = io.BytesIO(local[2])
                imagem = Image.open(bytes_io)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### Foto")
                    st.image(imagem, use_column_width=True)
                with col2:
                    st.markdown("### Descrição")
                    if local[6] == "Positive":
                        stment = f"Sentimento: {local[6]} 😀"
                    else: 
                        stment = f"{local[6]} 😔"
                    texto_description = (
                          f'<p style = "color: #808080"><span style="color: white;">Nome: </span> {local[1]}</p>'
                          f'<p style = "color: #808080" ><span style="color: white;">Cidade: </span> {local[3]}</p>'
                          f'<p style = "color: #808080" ><span style="color: white;">Endereço: </span> {local[4]}</p>'
                          f'<p style = "color: #808080" ><span style="color: white;">Descrição: </span> {local[5]}</p>'
                          f'<p style = "color: #808080" ><span style="color: white;">Date: </span> {local[7]}</p>'
                          f'<p style = "color: #808080" ><span style="color: white;">Sentimento: </span> {stment}</p>'
                    )
                    st.markdown(texto_description, unsafe_allow_html=True)

                space = '<p style = "color: #4a28ea" > ______________________________________________________________________________________</p>'
                st.markdown(space, unsafe_allow_html=True)
                    

                    #st.markdown("# Informações")
                    #st.write(f"Nome: {local[1]}")
                    #st.write(f"Cidade: {local[3]}")
                    #st.write(f"Endereço: {local[4]}")
                    #st.write(f"Descrição: {local[5]}")
                    #st.write(f"Data: {local[7]}")
                   

        else:
            st.warning('Nenhum dado encontrado!', icon="⚠️")