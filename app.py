import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/sign_up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/sign_in")
def sign_in():
    return render_template("sign-in.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/update_profile")
def update_profile():
    return render_template("update-profile.html")


@app.route("/get_help")
def get_help():
    return render_template("get-help.html")


@app.route("/edit_post")
def edit_post():
    return render_template("edit-post.html")


@app.route("/give_help")
def give_help():
    return render_template("give-help.html")

# Error Handlers - Returning content if error occurs
@app.errorhandler(404)
def error404(error):
    return render_template("404.html")


@app.errorhandler(403)
def error403(error):
    return render_template("403.html")


@app.errorhandler(500)
def error500(error):
    return render_template("500.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
