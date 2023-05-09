import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode().strip()
        print(f"Valor aleatorio: {line}")
