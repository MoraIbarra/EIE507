import serial
import time

class Conexion:
    def __init__(self, port = '/dev/ttyACM0' , baudrate = 9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        time.sleep(2)

    def read_data(self):
        data = self.ser.readline().decode().strip()
        return data

if __name__ == '__main__':
    con = Conexion()
    mtx = []
    while True:
        try:
            rn = con.read_data()
