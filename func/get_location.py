from geopy.geocoders import Nominatim

def get_lat_long(rua, cidade):
    address = f'{rua}, {cidade}'
    geolocator = Nominatim(user_agent="geo_app")
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None
