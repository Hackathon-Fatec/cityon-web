import psycopg2

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

def insert_itens(name, picture, city, street, opinion):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="(CityOn)1234.",
            host="db.vaedsocphtwkarwvmmtl.supabase.co"
        )

        cursor = connection.cursor()
        query = "INSERT INTO posts(nome, foto, cidade, endereco, opiniao) VALUES (%s, %s, %s, %s, %s);"
        data = (name, picture, city, street, opinion)

        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()
        
        return True

    except psycopg2.Error as e:
        return False