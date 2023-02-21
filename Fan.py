import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


 

GPIO.setup(4, GPIO.OUT)


try:
    while True:
        GPIO.output(4, GPIO.HIGH)
        print('Fan is ON')
        time.sleep(5)
        GPIO.output(4, GPIO.LOW)
        print('Fan is OFF')
        time.sleep(5)
finally:

    GPIO.cleanup()