import streamlit as st


def home():
    col1, col2 = st.columns([17, 83])
    half1, half2 = st.columns([30, 40])


    custom_css = """
        <style>
            @media screen and (max-width: 400px) {
                .custom-title {
                    font-size: 25px !important;
                }
            }
        </style>
        <script>
            window.addEventListener("DOMContentLoaded", function() {
                var title = document.querySelector(".title");
                if (window.innerWidth <= 400) {
                    title.classList.add("custom-title");
                }
            });
        </script>
        """
    st.markdown(custom_css, unsafe_allow_html=True)


    header = (
        f'<p><span><img src="https://i.imgur.com/BO4iVgo.png" style="border-radius: 30px; max-width: 20vw; max-height: 20vh;"></span></p>'
    )

    text = (
        f'<h6 style="font-size: 2vw;">Bem vindo ao</h6>'
        f'<p class = ".custom-title" style="line-height: 2px; font-size: 50px; font-weight: bold;">CITY<span style="color: #3b71d3;">ON</span></p>'
    )


    with col1:
        st.markdown(header, unsafe_allow_html=True)
    with col2:
        st.markdown(text, unsafe_allow_html=True)

    with half2:
        half = (
            f'<img style="width:20vw" src ="https://i.imgur.com/fVeaojE.png">'
        )

        st.markdown(half, unsafe_allow_html=True)
    with half1:


        description_system = (
            f'<div style="width: 100%; height: 6vh;" ></div>'
            f'<p style="font-size: 2vh;">Envie <span style="color:#3b71d3" >feedback</span> sobre Locais sobre a cidade que você mais ama, <span style="color:#3b71d3" >A SUA</span>. Onde nós fazemos o <span style="color:#3b71d3" >papel</span> de <span style="color:#3b71d3" >centralizar</span> esses feedbacks em uma plataforma <span style="color:#3b71d3" >simples</span> e <span style="color:#3b71d3" >organizada<span></p>'        )

        st.markdown(description_system, unsafe_allow_html=True)
