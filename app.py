from flask import Flask, render_template, redirect, request
import pyqrcode
import socket
import time
import Pump
import Sense
import light



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
    ip_add = getRaspIp()
    url = pyqrcode.create('http://' + ip_add + ':5000/')
    url.svg('QRCode.svg', scale=1)
    print(url.terminal(quiet_zone=1))

app = Flask(__name__)

@app.route('/')
def index():
    ip = getRaspIp()
    localTempTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=4"
    localPhTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=2"
    localHumidityTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=6"
    localTempGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=9"
    localPhGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=7"
    localHumidityGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=8"

    return render_template("Homepage.html", addr1=localTempTime, addr2=localPhTime, addr3=localHumidityTime,
    addr4=localTempGauge, addr5=localPhGauge, addr6=localHumidityGauge)

@app.route('/refill')
def filling():
    ip = getRaspIp()
    localTempTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=4"
    localPhTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=2"
    localHumidityTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=6"
    localTempGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=9"
    localPhGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=7"
    localHumidityGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=8"
    
    Pump.refill()
    return render_template("Homepage.html", addr1=localTempTime, addr2=localPhTime, addr3=localHumidityTime,
    addr4=localTempGauge, addr5=localPhGauge, addr6=localHumidityGauge)

@app.route('/sense')
def isWater():
    ip = getRaspIp()
    localTempTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=4"
    localPhTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=2"
    localHumidityTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=6"
    localTempGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=9"
    localPhGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=7"
    localHumidityGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=8"

    Sense.senseStart(run= True, isFull= False)
    return render_template("Homepage.html", addr1=localTempTime, addr2=localPhTime, addr3=localHumidityTime,
    addr4=localTempGauge, addr5=localPhGauge, addr6=localHumidityGauge)

@app.route('/toggle_light')
def letTherebeLight():
    ip = getRaspIp()
    localTempTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=4"
    localPhTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=2"
    localHumidityTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=6"
    localTempGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=9"
    localPhGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=7"
    localHumidityGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=8"

    light.light(forceEnd=False)
    return render_template("Homepage.html", addr1=localTempTime, addr2=localPhTime, addr3=localHumidityTime,
    addr4=localTempGauge, addr5=localPhGauge, addr6=localHumidityGauge)

@app.route('/stop')
def suspend():
    ip = getRaspIp()
    localTempTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=4"
    localPhTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=2"
    localHumidityTime = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=6"
    localTempGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=9"
    localPhGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=7"
    localHumidityGauge = "http://" + ip + ":3000/d-solo/LApJims4z/sis-sensor-readings?orgId=1&panelId=8"
    
    endlight = True
    light.light(endlight)
    Pump.turnoff()
    Sense.senseStart(run= False, isFull=True)
    return render_template("Homepage.html", addr1=localTempTime, addr2=localPhTime, addr3=localHumidityTime,
    addr4=localTempGauge, addr5=localPhGauge, addr6=localHumidityGauge)


generateQR()

if __name__ == "__main__":
    app.run(host=getRaspIp(), port=5000, debug=True)
    
    