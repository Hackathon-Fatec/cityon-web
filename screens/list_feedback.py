import streamlit as st
import requests

def get_cities():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"

    response = requests.request("GET", url)
    response = response.json()

    cities = [city["nome"] for city in response]

    return cities

cities = get_cities()

def list_feedback():
    st.title("Busque Feedbacks de sua cidade")
    
    city = st.selectbox('Escolha a cidade', cities)


list_feedback()

#https://chat.openai.com/share/fd4635d8-37af-44fe-9de2-78cd9be1a647