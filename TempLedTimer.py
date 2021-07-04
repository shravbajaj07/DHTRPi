import Adafruit_DHT as DHT
import time
from datetime import datetime
sensor = DHT.DHT11
sensor_pin = 4

def GetTemp(count):
    exact_time = 0
    humidity, temperature = DHT.read_retry(sensor,sensor_pin)
    while temperature < 27:
        if count == 0:
            exact_time = datetime.now()
            count += 1
        humidity, temperature = DHT.read_retry(sensor,sensor_pin)
        print("LED ON")
    print(exact_time)
    end = time.time()
    print("LED OFF")
    total_time = (end - start)/60    
    if total_time > 1:
        return str(exact_time), str(total_time)

def DataLogging(data):
    file = open("log.txt", 'a')
    if data != None:
        s_data = ', '.join(data)
        file.write(s_data)
        file.write('\n')
    file.close()

while True:
    humidity, temperature = DHT.read_retry(sensor,sensor_pin)
    print("Temp = {0:0.1f}*C Humidity = {1:0.1f}%".format(temperature,humidity))
    start = time.time()
    if temperature < 27:
        values = GetTemp(0)
        DataLogging(values)
  

