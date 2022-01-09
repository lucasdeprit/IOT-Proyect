
import requests
from timeit import default_timer as timer
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
import time
import threading

url = 'https://corlysis.com:8086/write'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "ecbef8c057c4ebac95399b37189bcf5e"}

def main():
    sensor = GroveUltrasonicRanger(16)
    lejos=True
    medio=True
    cerca=True
    while True:
        distance = int(sensor.get_distance())
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

if __name__ == '__main__':
 main()
