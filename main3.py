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
    sensortemp = DHT('11', 5)
    lejos=True
    medio=True
    cerca=True
    while True:
        distance = int(sensor.get_distance())
        humi, temp = sensortemp.read()
        if distance >= 150 and lejos:
            print('fuera')
            print('{} cm'.format(distance))
            lejos=False
            if not medio:
                medio=True
            if not cerca:
                cerca=True

    		time.sleep(1)
            #temp
            payload = 'temp_test,temp=actual'+' value='+str(temp)
            r= requests.post(url,params=params,data=payload)

            #humi
            payloadhumi = 'humi_test,humi=actual' + ' value='+ str(humi)
            ri= requests.post(url,params=params,data=payloadhumi)

            #dist
            payloaddist = 'meas_test,distance=bad' + ' value=' + str(distance)
            rd= requests.post(url,params=params,data=payloaddist)
    
        if distance >=50 and distance <150 and medio:
            print('optimo')
            print('{} cm'.format(distance))
            medio=False
            if not lejos:
                lejos=True
            if not cerca:
                cerca=True
            
            #temp
            payload = 'temp_test,temp=actual'+' value='+str(temp)
            r= requests.post(url,params=params,data=payload)
            
            #humi
            payloadhumi = 'humi_test,humi=actual' + ' value='+ str(humi)
            ri= requests.post(url,params=params,data=payloadhumi)

            #dist
            payloaddist = 'meas_test,distance=optimum' + ' value=' + str(distance)
            rd= requests.post(url,params=params,data=payloaddist)
    
        if distance < 50 and cerca:
            print('muy cerca')
            print('{} cm'.format(distance))
            cerca=False
            if not medio:
                medio=True
            if not lejos:
                lejos=True
            
            #temp
            #payload = 'temp_test,temp=actual'+'value='+str(temp)
            #r= requests.post(url,params=params,data=payload)
 
            #humi
            #payloadhumi = 'humi_test,humi=actual' + 'value='+ str(humi)
            #ri= requests.post(url,params=params,data=payloadhumi)


            #dist
            payloaddist = 'meas_test,distance=out'+'value=' + str(distance)
            rd= requests.post(url,params=params,data=payloaddist)
    
    time.sleep(1)
def main():
    myfunction()

if __name__ == '__main__':
 main()
