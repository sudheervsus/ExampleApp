from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Flask. Start Aping."


@app.route("/About")
def aboutPage():
    return "ABOUT - This is an example page to learn flask.. Don't contact us."
