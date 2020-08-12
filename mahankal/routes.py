from flask import render_template, url_for
from mahankal import app
from mahankal.forms import LoginForm

@app.route("/", methods=["GET", "POST"])
def home():
    form=LoginForm()
    return render_template('home.html',form=form)


