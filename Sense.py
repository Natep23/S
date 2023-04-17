import RPi.GPIO as GPIO
import time


def senseStart(run):
    try:
        GPIO.setmode(GPIO.BCM)

        x=1
        Sensor1 = 4
        Sensor2 = 27

        

        GPIO.setup(Sensor1, GPIO.IN)
        GPIO.setup(Sensor2, GPIO.IN)

        while run:
            if(x >= 5):
                run=False

            if(GPIO.input(Sensor1) == True):
                print("Water Detected from Non-Contact Sensor")
            else:
                print("No Water Detected from Non-Contact Sensor")

            if(GPIO.input(Sensor2) == False):
                print("Water is at maximum level Inside")
            else:
                print("Water is not at maximum level")

            print(x)
            x += 1
            time.sleep(4)
    finally:
        GPIO.cleanup()
