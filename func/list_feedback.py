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

    # Outside the columns
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
                    st.markdown("# Foto")
                    st.image(imagem, use_column_width=True)
                with col2:
                    st.markdown("# Informações")
                    st.write(f"Nome: {local[1]}")
                    st.write(f"Cidade: {local[3]}")
                    st.write(f"Endereço: {local[4]}")
                    st.write(f"Descrição: {local[5]}")
                    st.write(f"Data: {local[7]}")
                    if local[6] == "Positive":
                        st.write(f"Sentimento: {local[6]} 😀")
                    else:
                        st.write(f"Sentimento: {local[6]} 😔")

        else:
            st.warning('Nenhum dado encontrado!', icon="⚠️")

list_feedback()