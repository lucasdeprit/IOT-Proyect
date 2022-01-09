#prerequisites: pip install requests
import requests
from timeit import default_timer as timer
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import RPi.GPIO as GPIO
import time

url = 'https://corlysis.com:8086/write'
params = {"db": "Technology_Health_Computing", "u": "token", "p": "ecbef8c057c4ebac95399b37189bcf5e"}


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

def main():
    # Grove - Ultrasonic Ranger connected to port D16
    sensor = GroveUltrasonicRanger(16)

    start = timer()
    while True:
        distance = sensor.get_distance()
        print('{} cm'.format(distance))
        if distance < 50:
            print('WARNING DEMASIADO CERCA')
            #GPIO.output(24, True)
            time.sleep(5)
            #GPIO.output(24, False)
            #end = timer()
            #print(end - start)
            #payload = 'meas_test,distance=bad' + ' value=' + str(start)
            #r = requests.post(url, params=params, data=payload)
            #start.stop()

        elif distance <= 150 and distance >= 50:
            print('DISTANCIA OPTIMA PARSERO!')
            GPIO.output(24, False)
            time.sleep(5)
            #end = timer()
            #print(end - start)
            #payload = 'meas_test,distance=bad' + ' value=' + str(end - start)
            #r = requests.post(url, params=params, data=payload)
            #start = timer()
        else:
            time.sleep(5)
            print('ACERCATE MAS ANDA')
        end = timer()
        realTime = end - start
        rtText = str(realTime)
        print(rtText + ' ' +'segundos')
    GPIO.output(24, False)

if __name__ == '__main__':
    main()            
