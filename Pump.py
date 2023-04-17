import RPi.GPIO as GPIO
import time

 #  Active LOW Relay 
def refill(start):
    #Try to setup the Pins in a separate function 
    # to see if the error dissapears 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    try:
        print('Pump Off')
        GPIO.output(21, GPIO.HIGH)
        time.sleep(1)
        
        while start:
            GPIO.output(21, GPIO.LOW)
            print("Pump On")
            time.sleep(2)
        
            print('Pump Off')
            GPIO.output(21, GPIO.HIGH)
            time.sleep(5)
            
    finally:
        GPIO.cleanup()