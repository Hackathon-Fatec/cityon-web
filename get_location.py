from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim
import folium
import exifread


def latlong_for_address(lat, long, cont):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((lat, long), exactly_one=True)
    
    if location is not None:
        address = location.raw.get('address', {})
        
        # Primeiro, tente obter o nome da cidade
        city = address.get('city', 'Cidade não encontrada')
        country = address.get('country', 'Cidade não encontrada')
        road = address.get('road', 'Cidade não encontrada')

        
        
        if country == "Brasil":
            return city, country, road        
        if cont == 0:
            lat = -lat
            long = -long
        elif cont == 1:
            lat = -lat
        else:
            long = -long
        
        cont += 1
        return latlong_for_address(lat, long, cont)
    else:
        return "Não foi possível encontrar o endereço."
    
    
def extrair_lat_long(foto):
    if foto is not None:
        # Lê os metadados EXIF da foto
        tags = exifread.process_file(foto)

        # Verifica se as informações de GPS estão presentes
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = tags['GPS GPSLatitude'].values
            longitude = tags['GPS GPSLongitude'].values
            latitude_ref = tags['GPS GPSLatitudeRef'].values
            longitude_ref = tags['GPS GPSLongitudeRef'].values

            # Converte as coordenadas de graus, minutos e segundos para graus decimais
            latitude_decimal = float(latitude[0].num) / float(latitude[0].den) + \
                               float(latitude[1].num) / float(latitude[1].den) / 60 + \
                               float(latitude[2].num) / float(latitude[2].den) / 3600
            longitude_decimal = float(longitude[0].num) / float(longitude[0].den) + \
                                float(longitude[1].num) / float(longitude[1].den) / 60 + \
                                float(longitude[2].num) / float(longitude[2].den) / 3600

            # Ajusta as coordenadas com base na referência (N/S, E/W)
            if latitude_ref == 'S':
                latitude_decimal = -latitude_decimal
            if longitude_ref == 'W':
                longitude_decimal = -longitude_decimal

            return latitude_decimal, longitude_decimal

    return None, None

def get_map(lat = -15.7801, lng = -47.9292):
    m = folium.Map(location=[lat, lng], zoom_start=14)
    folium.Marker([lat, lng]).add_to(m) 
    return m


    

