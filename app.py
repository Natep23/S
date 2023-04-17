from flask import Flask, render_template, redirect, request
import pyqrcode
import socket
import time
import Pump
import Sense


# Grabs the Local IP address to allow the 
# Rasberry Pi Run the Website on Multiple 
# Devices on the same wifi network
def getRaspIp():
   ip = ''
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   ip = s.getsockname() [0]
   s.close()
   return ip

#generates QR code for quick loading
def generateQR():
    time.sleep(3)
    ip = getRaspIp()
    url = pyqrcode.create('http://' + ip + ':5000/')
    url.svg('QRCode.svg', scale=1)
    print(url.terminal(quiet_zone=1))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Homepage.html")

@app.route('/refill')
def filling():
    On = True
    Pump.refill(On)
    return render_template("Homepage.html")

@app.route('/sense')
def isWater():
    run = True
    Sense.senseStart(run)
    return render_template("Homepage.html")


@app.route('/stop')
def suspend():
    Off = False
    run = False
    Pump.refill(Off)
    Sense.senseStart(run)
    return render_template("Homepage.html")

generateQR()

if __name__ == "__main__":
    app.run(host=getRaspIp(), port=5000, debug=True)
    
    