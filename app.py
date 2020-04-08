import os
from flask import Flask
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
    return "Hello Home"


@app.route("/sign_up")
def sign_up():
    return "Sign Up"


@app.route("/sign_in")
def sign_in():
    return "Sign In"


@app.route("/dashboard")
def dashboard():
    return "Dashboard"


@app.route("/update_profile")
def update_profile():
    return "Update Profile"


@app.route("/get_help")
def get_help():
    return "Get Help"


@app.route("/edit_post")
def edit_post():
    return "Edit Post"


@app.route("/give_help")
def give_help():
    return "Give Help"


@app.errorhandler(404)
def error404(error):
    return "This is a 404 error - Page Not Found"


@app.errorhandler(403)
def error403(error):
    return "This is a 403 Error - Forbidden"


@app.errorhandler(500)
def error500(error):
    return "This is a 500 Error - Internal Server Error"


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
