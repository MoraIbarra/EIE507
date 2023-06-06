import psycopg2

class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
            self.connection = psycopg2.connect(dbname=self.dbname,user=self.user,password=self.password, host=self.h>
            self.cursor = self.connection.cursor()

    def disconnect(self):
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query):
            self.cursor.execute(query)
            self.connection.commit()

    def execute_select_query(self, query):
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows

if __name__ == "__main__":
    dbname = "Tablas"
    user = "postgres"
    password = "matigol"
    host = "169.254.116.33"
    port = "5433"

    db_manager = DatabaseManager(dbname, user, password, host, port)
    db_manager.connect()

    query = """ SELECT store.store_id, staff.first_name, staff.last_name, address.address
                FROM staff
                INNER JOIN store ON staff.staff_id = store.manager_staff_id
                INNER JOIN address ON store.address_id = address.address_id"""
    rows = db_manager.execute_select_query(query)
    for row in rows:
        print(row)

    query = """ SELECT film.film_id, film.title, category.name, language.name, film.length
                FROM film_category
                INNER JOIN category ON film_category.category_id = category.category_id
                INNER JOIN film ON film_category.film_id = film.film_id
                INNER JOIN language ON language.language_id = film.language_id"""
    rows = db_manager.execute_select_query(query)
    for row in rows:
        print(row)

    query = """ SELECT address.address, city.city, country.country
                FROM city
                INNER JOIN address ON address.city_id = city.city_id
                INNER JOIN country ON country.country_id = city.country_id"""
    rows = db_manager.execute_select_query(query)
    for row in rows:
        print(row)
                                               
db_manager.disconnect()


