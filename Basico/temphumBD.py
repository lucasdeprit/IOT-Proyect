import time
from seeed_dht import DHT
import requests
from timeit import default_timer as timer
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO

url = 'https://corlysis.com:8086/write'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "ecbef8c057c4ebac95399b37189bcf5e"}
def main():
	# Grove - Temperature&Humidity Sensor connected to port D5
	sensor = DHT('11', 5)
	while True:
    		humi, temp = sensor.read()
    		print('temperature {}C, humidity {}%'.format(temp, humi))
    		time.sleep(1)
    		payload = 'meas_humtemp,humtemp=perfect' + ' value=' + str(temp) + ' value2=' + str(hum)
            r = requests.post(url, params=params, data=payload)
 
if __name__ == '__main__':
	main()

