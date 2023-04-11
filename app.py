from flask import Flask, render_template, redirect, request
# import Pump.py
# import Sense.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Homepage.html")


if __name__ == "__main__":
    app.run(host="192.168.1.238", port=5000, debug=True) 