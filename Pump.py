import RPi.GPIO as GPIO
import time
import Sense

 #  Active LOW Relay 
def refill():
    
    message = ""
    Sense.check(message)

    #Try to setup the Pins in a separate function 
    # to see if the error dissapears 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(21, GPIO.OUT)

    try: 
    
          if (GPIO.input(27) == False):
               stop = True
               print(stop)
          else: 
           stop = False 
           print(stop)


          if(stop == True):
                 GPIO.output(21, GPIO.HIGH)

          elif(GPIO.input(21) == True):
                 print("Pumping")
                 GPIO.output(21, GPIO.LOW)
                 time.sleep(5)
                 GPIO.output(21, GPIO.HIGH)
                 GPIO.cleanup()
                 
          else:
                 GPIO.output(21, GPIO.HIGH)                 
    except:
        GPIO.cleanup()
        print("An Error has Occurred")

# refill()

def turnoff():
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(21, GPIO.OUT)
     try:
          GPIO.output(21, GPIO.HIGH)
     except:
          print("error")
     GPIO.cleanup()

# turnoff()


