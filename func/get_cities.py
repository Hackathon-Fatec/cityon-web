import requests

def get_cities():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"

    response = requests.request("GET", url)
    response = response.json()

    cities = [city["nome"] for city in response]

    return cities