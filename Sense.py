import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)

while True:
    if(GPIO.input(4) ==True)
        print("No Water Detected")
    else:
        print("Water Detected")

    time.sleep(2)


