import smbus
import time

class Med:
    def __init__(self, address):
        self.address = address
        self.bus = smbus.SMBus(1)
        self.power_mgmt_1 = 0x6b
        self.temp_reg = 0x41
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0)

    def read_temp(self):
        temp_raw = self.read_word_2c(self.temp_reg)
        temp_celsius = temp_raw / 340.0 + 36.53
        return temp_celsius

    def read_word_2c(self, reg):
        high = self.bus.read_byte_data(self.address, reg)
        low = self.bus.read_byte_data(self.address, reg+1)
        value = (high << 8) + low
        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

if __name__ == "__main__":
    mtx = []
    TERM = Med(0x68)
    while True:
        temp = TERM.read_temp()
        print("La temperatura es: {:.2f} °C".format(temp))
        time.sleep(1)
        Ntem = float(temp)
        mtx.append(Ntem)
        if len(mtx) == 10
          prom = sum(mtx)/len(mtx)
          prom = round(prom, 4)
          print("El promedio es: ", prom, "°C")
          mtx.clear()          
