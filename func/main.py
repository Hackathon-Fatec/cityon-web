import streamlit as st
from list_feedback import list_feedback
from create_feedback import create_feedback
from home import home

def main():
    st.set_page_config(page_title="CityOn", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
    menu = st.sidebar.selectbox(
        "Escolha a pagina",
        ("Home", "Listagem de Feedbacks", "Criação de Feedback")
    )


    if menu == "Listagem de Feedbacks":
        list_feedback()
    elif menu == "Criação de Feedback":
        create_feedback()
    else:
        home()
        
main()