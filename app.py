from flask import Flask
import requests
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# python -m flask run