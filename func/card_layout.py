import streamlit as st

def exibir_feedback(foto, local, descricao, sentiment):
    st.markdown("<div style='border: 1px solid #ccc; padding: 16px; margin-bottom: 10px; border-radius: 5px; display: flex;'>"
                f"{foto}"
                "<div>"
                f"<h2 style='font-size: 1.2em;'>{local}</h2>"
                f"<p>{descricao}</p>"
                f"<p>{sentiment}</p>"
                "</div>"
                "</div>", unsafe_allow_html=True
                )
