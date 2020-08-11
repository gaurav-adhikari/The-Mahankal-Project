from flask import render_template, url_for
from mahankal import app

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')