import smbus

address = 0x68
power_mgmt_1 = 0x6b
temp_reg = 0x41
bus = smbus.SMBus(1)
bus.write_byte_data(address, power_mgmt_1, 0)


def read_word_2c(bus, address, reg):
    high = bus.read_byte_data(address, reg)
    low = bus.read_byte_data(address, reg+1)
    value = (high << 8) + low
    if (value >= 0x8000):
      return -((65535 - value) +1)
    else:
      return value
   
while True:
  
  temp_raw = read_word_2c(bus, address, temp_reg)
  temp_celsius = temp_raw / 340.0 +36.53
  
  print("La temeratura es: {:.2f} °C".forma(temp_celsius))
 
