import matplotlib.pyplot as plt
import streamlit as st

def grafico_radio_per_state(feedNeg, feedPos):

    progressos = [len(feedNeg), len(feedPos)]
    nomes = ["Positivos", "Negativos"]

    # Criar o gráfico
    fig, ax = plt.subplots()
    ax.pie(progressos, labels=nomes, autopct="%.1f%%", colors=['green','red'])

    # Exibir o gráfico
    st.pyplot(fig)

sb2 = [1, 2]
sb = [1, 2, 4, 5, 8, 6 , 8 , 9]
grafico_radio_per_state(sb, sb2)
