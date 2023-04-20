import RPi.GPIO as GPIO
import time


def senseStart(run):
    try:
        GPIO.setmode(GPIO.BCM)

        Sensor1 = 12
        Sensor2 = 27

        GPIO.setup(Sensor1, GPIO.IN)
        GPIO.setup(Sensor2, GPIO.IN)

        while run:

            if(GPIO.input(Sensor1) == True):
                print("Water Detected from Non-Contact Sensor")
            elif (GPIO.input(Sensor1) == False):
                print("No Water Detected from Non-Contact Sensor")
            else: print("error")

            if(GPIO.input(Sensor2) == False):
                print("Water is at maximum level Inside")
            elif (GPIO.input(Sensor2) == True):
                print("Water is not at maximum level")
            else: print("error")
            
            time.sleep(1)
    finally:
        GPIO.cleanup()

