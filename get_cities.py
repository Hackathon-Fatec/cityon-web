import requests

def get_cities():
    url = "http://servicodados.ibge.gov.br/api/v1/localidades/distritos"

    response = requests.request("GET", url)
    response = response.json()

    cities = [city["nome"] for city in response]

    return cities