import streamlit as st
from list_feedback import list_feedback
from create_feedback import create_feedback
from home import home
from maps import mapPlot


def main():
    
    menu = st.sidebar.selectbox(
        "Escolha a pagina",
        ("Home", "Listagem de Feedbacks", "Criação de Feedback", "Plotagem no Mapa")
    )

    if menu == "Listagem de Feedbacks":
        list_feedback()
    elif menu == "Criação de Feedback":
        create_feedback()
    elif menu == "Plotagem no Mapa":
        mapPlot()
    else:
        home()
        
main()