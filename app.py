from flask import Flask
from flask import render_template
import icons
app = Flask(__name__)

@app.route("/")
def home():
    imgs = icons.getAllApps()
    return render_template("index.html", icons=imgs)


# python -m flask run