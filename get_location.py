from geopy.geocoders import Nominatim
import streamlit as st
import requests
import geocoder
import folium
from flask import Flask, request, jsonify
import googlemaps
from googlemaps.exceptions import TransportError

@st.cache_data
def get_lat_long(rua, cidade):
    address = ""
    if rua:
        address += rua + ', '
    address += cidade
    geolocator = Nominatim(user_agent="geo_app")
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None

@st.cache_data
def get_user_location():
    location = None
    
    try:
        # Use a API de geolocalização do navegador para obter a localização
        response = requests.get("https://ipinfo.io")
        data = response.json()
        
        location = [
            float(data.get("loc", "").split(",")[0]),
            float(data.get("loc", "").split(",")[1])
        ]
    except Exception as e:
        st.warning("Não foi possível obter a localização do usuário.")
        st.warning(str(e))
    
    return location


def get_location_phone():
    location = geocoder.ip('me')
    return location
print(get_location_phone())

def get_location_details(lat, lng):
    geolocator = Nominatim(user_agent="geoapp")
    location = geolocator.reverse((lat, lng), exactly_one=True)
    return location

def get_map(lat = -15.7801, lng = -47.9292):
    m = folium.Map(location=[lat, lng], zoom_start=14)
    folium.Marker([lat, lng]).add_to(m)
    return m


def get_locale_js():
    
    gmaps = googlemaps.Client(key="AIzaSyDds1kIsXkgcg43pme6jvtceszBGpWAKRM")

    try:
        # Use a função de geolocalização para obter a sua localização atual
        current_location = gmaps.geolocate()

        # Extraia a latitude e a longitude da resposta
        latitude = current_location['location']['lat']
        longitude = current_location['location']['lng']

        data = []
        data.append(latitude)
        data.append(longitude)
        return data
    
    except TransportError as e:
        print(f"Erro ao obter a localização: {e}")
        return None

        




