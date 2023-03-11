import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)

while True:
    if(GPIO.input(4) == True):
        print("Water Detected")
    else:
        print("No Water Detected")

    time.sleep(2)


