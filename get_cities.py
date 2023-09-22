import requests
import json
import psycopg2


def get_cities():
    url = "http://servicodados.ibge.gov.br/api/v1/localidades/distritos"

    response = requests.request("GET", url)
    response = response.json()

    cities = [city["nome"] for city in response]

    return cities

def get_city_unique():
    url = "http://servicodados.ibge.gov.br/api/v1/localidades/distritos"

    response = requests.request("GET", url)
    response = response.json()

    cities = [city["nome"] for city in response]


    '''
    fb = []
    

    if response.status_code == 200:
        data = response.json()
        cities = [city["nome"] for city in data]
        
        for city in cities:
            fb.append(get_filtred_cities(city, "positive"))
            fb.append(get_filtred_cities(city, "negative"))
        return fb
    else:
        return []'''
def get_cities_in_bd():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = f"SELECT DISTINCT cidade FROM posts;"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        cities = [result[0] for result in results]
        return cities

    except psycopg2.Error as e:
        return False

    
    


