import streamlit as st
import folium
from streamlit_folium import folium_static
from db import get_all_itens
from folium import IFrame

plots = get_all_itens()
markers = [{"lat": element[9], "lon": element[8], "info": element[5], "local": element[1], "sentiment": element[6]} for element in plots]

print(plots)
def mapPlot():
    st.title("Plotagem dos feedbacks")
    
    # Create a Folium map object
    m = folium.Map(location=[-23.553720852012958, -46.657163972338864], zoom_start=12) # São Paulo
    
    for marker in markers:
        popup_html = f"<b>Local:</b> {marker['local']}<br><b>Descrição:</b> {marker['info']}<br><b>Sentimento:</b> {marker['sentiment']}"
        iframe = IFrame(html=popup_html, width=300, height=150)
        popup = folium.Popup(iframe, max_width=500)
        
        folium.Marker([marker["lat"], marker["lon"]], popup=popup).add_to(m)
    
    # Display the map
    folium_static(m)
