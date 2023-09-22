import streamlit as st
from get_cities import get_cities





def estatistic():

    
    opcoes = ["Cidade", "Estado"]


    st.markdown("<h3 style='text-align: center; color: white;'>Veja como sua região esta indo: </h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])



    with col2:
        escolha = None
        escolha = st.radio("", opcoes)

        cidades = ["Escolha a Cidade"]
        getc = get_cities()
        cidades += [c for c in getc]

        if escolha == "Cidade":
            citychoosed = st.selectbox('', cidades)

        if escolha == "Estado":
            stateChoosed = st.selectbox('', [

                "Escolha a Região","AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
                "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
                "SP", "SE", "TO"
                ])
        
        

estatistic()