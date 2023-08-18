import streamlit as st

def main(name, description, foto):
    st.title("feedbacks")

    feedb = [
        {"nome": "muro 2", "descricao": "é ruim dms", "foto": "feed2.jpg"},
        {"nome": "asfalto", "descricao": "ta muito lindo", "foto": "feed1.jpg"},
        {"nome": "calçada", "descricao": "isso ta gostosin", "foto": "feed3.jpg"}
    ]

    for feedback in feedb:
        exibir_feedback(feedback)

def exibir_feedback(feedback):
    st.markdown("<div style='border: 1px solid #ccc; padding: 16px; margin-bottom: 10px; border-radius: 5px; display: flex;'>"
                f"<img src='https://www.ocasaldafoto.com/wp-content/uploads/2019/11/fotografia-celular-melhores-fotos-angulo-3.jpg.webp' alt='{prato['nome']}' width='150' style='margin-right: 16px;'>"
                "<div>"
                f"<h2 style='font-size: 1.2em;'>{feedback['nome']}</h2>"
                f"<p>{feedback['descricao']}</p>"
                "</div>"
                "</div>", unsafe_allow_html=True)
