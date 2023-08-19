import streamlit as st

def exibir_feedback(foto, local, descricao, sentiment):
    st.markdown(
        f"""
        <style>
        .feedback-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            border: 1px solid #e6e6e6;
            border-radius: 5px;
            padding: 16px;
            margin-bottom: 20px;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
        }}
        .feedback-image {{
            flex: 1;
            margin-right: 16px;
            max-width: 300px;
        }}
        .feedback-info {{
            flex: 2;
            max-width: calc(100% - 316px);  /* Adjust margin and padding accordingly */
        }}
        .feedback-header {{
            font-size: 1.5em;
            margin: 0;
        }}
        .feedback-description {{
            margin: 8px 0;
            white-space: pre-wrap;
        }}
        .feedback-sentiment {{
            font-weight: bold;
            margin: 0;
        }}
        </style>
        <div class="feedback-container">
            <div class="feedback-image">
                {foto}
            </div>
            <div class="feedback-info">
                <h2 class="feedback-header">{local}</h2>
                <p class="feedback-description">{descricao}</p>
                <p class="feedback-sentiment" style="color: {'green' if sentiment == 'Positive' else 'red'};">{"Positivo" if sentiment == "Positive" else "Negativo"}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )




