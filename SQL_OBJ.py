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

    query = "UPDATE country SET country = 'Atlantida' WHERE country_id = '104'"
    db_manager.execute_query(query)
    query ="INSERT INTO country (country_id, country, last_update) VALUES (110, 'Mordor', current_timestamp)"
    ##query = "DELETE FROM country WHERE country_id = '110'"
    db_manager.execute_query(query)
    query = "SELECT * FROM country ORDER BY country_id ASC"
    rows = db_manager.execute_select_query(query)
    for row in rows:
        print(row)
    db_manager.disconnect()
