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

    if st.button("Buscar"):
        filtred_cities = []
        if sentiment_choosed == "Todos":
            filtred_cities = get_itens(city_choosed)
        else:
            filtred_cities = get_filtred_cities(city_choosed, "Positive" if sentiment_choosed == "Positivo" else "Negative")

        if len(filtred_cities) > 0:
            for i in filtred_cities:
                bytes_io = io.BytesIO(i[2])
                imagem = Image.open(bytes_io)
                image_base64 = base64.b64encode(bytes_io.getvalue()).decode()

                html_code = f'<img src="data:image/jpeg;base64,{image_base64}" alt="Imagem" width="150" style="margin-right: 16px;" />'
                exibir_feedback(html_code, i[1], i[5], i[6])
        else:
            st.warning('Nenhum dado encontrado!', icon="⚠️")