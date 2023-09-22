import psycopg2
from get_cities import get_cities_in_bd
import requests

def get_itens(city):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = f"SELECT * FROM posts WHERE cidade='{city}';"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return results

    except psycopg2.Error as e:
        return False

def get_all_itens():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = f"SELECT * FROM posts;"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return results

    except psycopg2.Error as e:
        return False
    
def get_filtred_cities(city, sentiment):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = f"SELECT * FROM posts WHERE cidade='{city}' AND sentiment='{sentiment}';"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return results

    except psycopg2.Error as e:
        return False

def insert_itens(name, picture, city, street, opinion, sentiment, date, latitude, longitude):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = "INSERT INTO posts(nome, foto, cidade, endereco, opiniao, sentiment, data, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (name, picture, city, street, opinion, sentiment, date, latitude, longitude)

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()
        
        return True

    except psycopg2.Error as e:
        return False


def get_itens_by_UF(uf):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos"

    response = requests.get(url)
    response = response.json()
    citiesUF = [city["nome"] for city in response]
    cityBd = get_cities_in_bd()
    vetGood = []
    vetBad=[]
    
    for ct in cityBd:
        if ct in citiesUF:
            
            try:
                connection = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="(CityOn)1234.",
                host="db.vaedsocphtwkarwvmmtl.supabase.co"
            )

                cursor = connection.cursor()
                query = f"SELECT * FROM posts WHERE cidade='{ct}';"
                cursor.execute(query)

                results = cursor.fetchall()
                cursor.close()
                connection.close()
                g = 0
                m = 0
                
                

                for res in results:
                    if res[6] == "Negative": m+=1
                    else: g+=1

            except psycopg2.Error as e:
                return False
    return g, m

'''
def get_cities_by_UF():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = f"SELECT * FROM posts WHERE cidade='{city}' AND sentiment='{sentiment}';"
        
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return results
    
    except psycopg2.Error as e:
        return False
'''


g, m = get_itens_by_UF("PR")
print(g, " ", m)
    






        

