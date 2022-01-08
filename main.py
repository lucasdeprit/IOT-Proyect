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
    while True:
            distance = sensor.get_distance()
            print('{} cm'.format(distance))
            
            if distance < 50:
                print('WARNING DEMASIADO CERCA')
                GPIO.output(24, True)
                time.sleep(1)
                GPIO.output(24, False)
                payload = 'meas_test,distance=bad' + ' value=' + str(distance)
                r = requests.post(url, params=params, data=payload)

            elif distance <= 150 and distance >= 50:
                print('DISTANCIA OPTIMA PARSERO!')
                GPIO.output(24, False)
                payload = 'meas_test,distance=optimum' + ' value=' + str(distance)
                r = requests.post(url, params=params, data=payload)
            else:
                print('ACERCATE MAS ANDA')
            GPIO.output(24, False)
            time.sleep(3)

if __name__ == '__main__':
    main()

