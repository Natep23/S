import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


 # Relay 1 (Active LOW)

GPIO.setup(21, GPIO.OUT)


try:
    while True:
        GPIO.output(21, GPIO.LOW)
        print("Pump On")
        time.sleep(5)
    
        print('Pump Off')
        GPIO.output(21, GPIO.HIGH)
        time.sleep(5)
finally:
    GPIO.cleanup()