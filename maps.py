import streamlit as st
import folium

from streamlit_folium import folium_static
from db import get_all_itens
from folium import IFrame
from PIL import Image
import base64
import io

plots = get_all_itens()
markers = [{"lat": element[9], "lon": element[8], "info": element[5], "local": element[1], "sentiment": element[6], "foto": element[2]} for element in plots]

def mapPlot():
    st.title("Plotagem dos feedbacks")
    
    lat = -23.553720852012958
    lng = -46.657163972338864
    # Create a Folium map object
    m = folium.Map(location=[lat,lng], zoom_start=12)
    
    for marker in markers:
        
        popup_html = f"<img src='data:image/jpeg;base64,{base64.b64encode(marker['foto']).decode()}' style='max-width:100%;height:auto;'><br><b>Local:</b> {marker['local']}<br><b>Descrição:</b> {marker['info']}<br><b>Sentimento:</b> {marker['sentiment']}"
        iframe = IFrame(html=popup_html, width=300, height=150)
        popup = folium.Popup(iframe, max_width=500)
        
        marker_color = "green" if marker["sentiment"] == "Positive" else "red"
        icon = folium.Icon(color=marker_color)
        
        folium.Marker([marker["lat"], marker["lon"]], popup=popup, icon=icon).add_to(m)
    
    # Display the map
    folium_static(m)
