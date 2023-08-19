import streamlit as st

def home():
    col1, col2 = st.columns([17, 83])

    header = (
        f'<p><span><img src="https://avatars.githubusercontent.com/u/141507743?s=200&v=4" style="border-radius:30px; width:6vw" ></span></p>'
    )

    text = (
         f'<p style="line-height: 2rem;" ><span><h6>Bem vindo ao</h6></span></p>'
         f'<p  style="line-height:2px;  font-size: 4vw; font-weight:bold ">CITY<span style="color:#3b71d3;">ON</span><p>'
    )

    with col1:
        st.markdown(header, unsafe_allow_html=True)
    with col2:
        st.markdown(text, unsafe_allow_html=True)
        
