# Get Humidiity & Temperature from DHT11
# Prints Temperature & Humidity rapidly after intervals of 1 sec
# Needs Adafruit DHT11 Library. Get it Here - https://github.com/adafruit/Adafruit_Python_DHT
# Samiran Das - github.com/samiran-das

import sys
import Adafruit_DHT
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    time.sleep(1)
    
    # End of Code
