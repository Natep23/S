import RPi.GPIO as GPIO
import time

 #  Active LOW Relay 
def light(forceEnd):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    try:    
            if (forceEnd): 
                 GPIO.output(26, GPIO.HIGH)

            elif (GPIO.input(26) == True):
                GPIO.output(26, GPIO.LOW)
                
            else:
                 GPIO.output(26, GPIO.HIGH)
                 
        
    except:
        print("An Error has Occurred")


