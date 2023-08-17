import streamlit as st

# Cria um campo de texto
text_area = st.text_area("Meu campo de texto")

# Cria um contador de caracteres
character_count = len(text_area)

# Define a cor do contador com base na contagem de caracteres
if character_count > 15:
    color_style = "color: red;"
else:
    color_style = "color: black;"

# Exibe o contador de caracteres com a cor de estilo apropriada
st.write(f"<span >Número de caracteres: {character_count}</span>", unsafe_allow_html=True)
st.write(f"<span style='{color_style}'>Número de caracteres: {character_count}</span>", unsafe_allow_html=True)