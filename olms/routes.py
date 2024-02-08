from olms import app
from flask import render_template
from olms.models import Course

@app.route("/")
@app.route("/home")
def home():
    """ simply return hello world """
    return render_template("home.html")


@app.route("/enrollment")
def enroll():
    """ returns the enrollment details """
    courses = Course.query.all()
    return render_template("enroll.html", courses=courses)