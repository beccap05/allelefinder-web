from flask import render_template, flash, redirect, url_for, Flask, request
#from app import app

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "POST" or request.method == "GET":
        return render_template("about.html")
