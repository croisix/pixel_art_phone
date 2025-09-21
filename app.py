from flask import Flask
from flask import render_template
import getImage
app = Flask(__name__)

@app.route("/")
def home():
    apps_icons = getImage.getImages('static/images/icons')
    status_bar_icons = getImage.getImages('static/images/phone/status_bars')
    return render_template("index.html", app_icons=apps_icons, status_bar_icons=status_bar_icons)


# python -m flask run