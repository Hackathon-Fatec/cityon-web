import streamlit as st
from db import get_itens
from get_cities import get_cities
from PIL import Image
import io

cities = get_cities()

def list_feedback():
    st.title("Busque Feedbacks de sua cidade")
    
    city = st.selectbox('Escolha a cidade', cities)

    if st.button("Buscar"):
        for i in get_itens(city):
            imagem = Image.open(io.BytesIO(i[2]))
            st.image(imagem, width=100)


list_feedback()