import serial
import time
import psycopg2

class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        self.connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def execute_query(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()

    def execute_select_query(self, query, params=None):
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        return rows

if __name__ == "__main__":
    dbname = "postgres"
    user = "postgres"
    password = "matigol"
    host = "169.254.116.33"
    port = "5433"

    db_manager = DatabaseManager(dbname, user, password, host, port)
    db_manager.connect()

ser = serial.Serial('/dev/ttyACM0', 9600)  # USB
time_anterior = time.time()
temp = [None] * 10

def read_temperature():
    while True:
        if ser.in_waiting > 0:
            temperature = ser.readline().decode().strip()
            return temperature

while True:
    con = 1
    for i in range(9):
        temperature = read_temperature()
        temp[con] = temperature
        con += 1

    time.sleep(1)
    time_actual = time.time()
    if time_actual - time_anterior >= 30:
        con = 1
        i = 0
        while i < 9:
            db_manager.connect()
            print(temp[con])
            temp_value = temp[con]
            sens = con
            query = "INSERT INTO public.measurement (sensor_id, temperature) VALUES (%s, %s)"
            params = (sens, temp_value)
            db_manager.execute_query(query, params)
            db_manager.disconnect()
            con += 1
            i += 1
            time.sleep(1)

        temperature_values = [float(t) for t in temp[1:]]
        average_temperature = sum(temperature_values) / len(temperature_values)
        max_temperature = max(temperature_values)
        min_temperature = min(temperature_values)

        temperature_values_1 = [float(t) for t in temp[1:4]]
        average_temperature_1 = sum(temperature_values_1) / len(temperature_values_1)
        max_temperature_1 = max(temperature_values_1)
        min_temperature_1 = min(temperature_values_1)

        temperature_values_2 = [float(t) for t in temp[4:7]]
        average_temperature_2 = sum(temperature_values_2) / len(temperature_values_2)
        max_temperature_2 = max(temperature_values_2)
        min_temperature_2 = min(temperature_values_2)

        temperature_values_3 = [float(t) for t in temp[7:10]]
        average_temperature_3 = sum(temperature_values_3) / len(temperature_values_3)
        max_temperature_3 = max(temperature_values_3)
        min_temperature_3 = min(temperature_values_3)

        db_manager.connect()

        house_query = "UPDATE public.house_data SET house_avg_temp = %s, house_max_temp = %s, house_min_temp = %s"
        house_params = (average_temperature, max_temperature, min_temperature)
        db_manager.execute_query(house_query, house_params)

        query_1 = "UPDATE public.room_data SET room_avg_temp = %s, room_max_temp = %s, room_min_temp = %s WHERE room_data_id = 1"
        params_1 = (average_temperature_1, max_temperature_1, min_temperature_1)
        db_manager.execute_query(query_1, params_1)

        query_2 = "UPDATE public.room_data SET room_avg_temp = %s, room_max_temp = %s, room_min_temp = %s WHERE room_data_id = 2"
        params_2 = (average_temperature_2, max_temperature_2, min_temperature_2)
        db_manager.execute_query(query_2, params_2)

        query_3 = "UPDATE public.room_data SET room_avg_temp = %s, room_max_temp = %s, room_min_temp = %s WHERE room_data_id = 3"
        params_3 = (average_temperature_3, max_temperature_3, min_temperature_3)
        db_manager.execute_query(query_3, params_3)

        db_manager.disconnect()

        time_anterior = time.time()
