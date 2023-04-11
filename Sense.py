import RPi.GPIO as GPIO
import time


def senseStart(run):
    
    GPIO.setmode(GPIO.BCM)

    Sensor1 = 4
    Sensor2 = 27

    GPIO.setup(Sensor1, GPIO.IN)
    GPIO.setup(Sensor2, GPIO.IN)


    while True:

        if(GPIO.input(Sensor1) == True):
            print("Water Detected from Outside Sensor")
        else:
            print("No Water Detected from Outside Sensor")

        if(GPIO.input(Sensor2) == False):
            print("Water from Inside")
        else:
            print("No Water from Inside Sensor")

        time.sleep(2)

run = True
senseStart(run)