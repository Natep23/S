from flask import Flask, render_template, redirect, request
import socket
# import Pump.py
# import Sense.py

# Grabs the Local IP address to allow the Rasberry Pi Run the Website on Multiple Devices on the same wifi network
def getRaspIp():
   ip = ''
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8", 80))
   ip = s.getsockname() [0]
   s.close()
   return ip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Homepage.html")


if __name__ == "__main__":
    app.run(host=getRaspIp(), port=5000, debug=True) 