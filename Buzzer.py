import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
while True:
    GPIO.output(24, True)
    time.sleep(0.3)
    GPIO.output(24, False)
    time.sleep(1)
