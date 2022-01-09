
import requests
from timeit import default_timer as timer
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
import RPi.GPIO as GPIO
import time
import threading

url = 'https://corlysis.com:8086/write'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "1dba55a4bca39916c0264efd2af30c63"}

def myfunction():
    sensor = GroveUltrasonicRanger(16)
    sensor2 = DHT('11', 5) 
    lejos=True
    medio=True
    cerca=True
    while True:
        distance = int(sensor.get_distance())
        humi, temp = sensortemp.read()
        if distance >= 150 and lejos:
            print('lejos')
            print('{} cm'.format(distance))
            lejos=False
            if not medio:
                medio=True
            if not cerca:
                cerca=True
            payload = 'meas_test,distance=out' + ' value=' + str(distance)
            r= requests.post(url,params=params,data=payload)

            payload2 = 'temp_test,distance=actual' + ' value=' + str(distance)
            r= requests.post(url,params=params,data=payload)
    
        if distance >=50 and distance <150 and medio:
            print('cerca')
            print('{} cm'.format(distance))
            medio=False
            if not lejos:
                lejos=True
            if not cerca:
                cerca=True
            
            payload = 'meas_test,distance=optimum' + ' value=' + str(distance)
            r= requests.post(url,params=params,data=payload)
    
        if distance < 50 and cerca:
            print('muy cerca')
            print('{} cm'.format(distance))
            cerca=False
            if not medio:
                medio=True
            if not lejos:
                lejos=True
            
            payload = 'meas_test,distance=bad' + ' value=' + str(distance)
            r= requests.post(url,params=params,data=payload)
    
    time.sleep(1)
def main():
    myfunction()

if __name__ == '__main__':
 main()
