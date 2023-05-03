import RPi.GPIO as GPIO
import time


def senseStart(run, isFull):
    try:
        GPIO.setmode(GPIO.BCM)

        Sensor1 = 20
        Sensor2 = 27
        

        GPIO.setup(Sensor1, GPIO.IN)
        GPIO.setup(Sensor2, GPIO.IN)

        if(GPIO.input(Sensor1) == True):
            print("Water Detected from Non-Contact Sensor")
        elif (GPIO.input(Sensor1) == False):
            print("No Water Detected from Non-Contact Sensor")
        else: print("error")

        if(GPIO.input(Sensor2) == False):
            print("Water is at maximum level Inside")
            isFull = True
        elif (GPIO.input(Sensor2) == True):
            print("Water is not at maximum level")
        else: print("error")
               
    except:
        print("Error")

    finally:
        GPIO.cleanup()
    
    
def check(message):
    try:
        GPIO.setmode(GPIO.BCM)

        Sensor1 = 20
        Sensor2 = 27

        GPIO.setup(Sensor1, GPIO.IN)
        GPIO.setup(Sensor2, GPIO.IN)

        if(GPIO.input(Sensor2) == False):
            message = "Your System is Full"
            print(message)
            return  message
        elif(GPIO.input(Sensor1) == False) & (GPIO.input(Sensor2) == True):
            message = "Your System Needs Water"
            print(message)
            return message
        elif(GPIO.input(Sensor2)== True):
            message = "Your System is not Full"
            print(message)
            return message
        else:
            message = "Error in Checking"
            print(message)
            return message
    except:
        message = "Error: Sensor Check Did Not Run."
        print(message)
        return message
    
# senseStart(run=True, isFull=False)
# check( message="")

