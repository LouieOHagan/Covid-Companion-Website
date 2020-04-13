import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/update-profile")
def update_profile():
    return render_template("update-profile.html")


@app.route("/get-help", methods=["GET", "POST"])
def get_help():
    if request.method == "GET":
        counties = mongo.db.counties.find()
        return render_template("get-help.html",
                               title="Get Help",
                               counties=counties)
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        order_number = request.form["order_number"]
        county = request.form["county"]
        address = request.form["address"]
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]

        if order_number == "":
            order_number = "N/A"

        new_post = {'title': title,
                    'description': description,
                    'order_number': order_number,
                    'county': county,
                    'address': address,
                    'name': name,
                    'email': email,
                    'phone_number': phone_number,
                    'status': 'Available'
                    }

        mongo.db.posts.insert_one(new_post)
        return redirect(url_for('give_help'))


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "GET":
        post_info = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
        counties = mongo.db.counties.find()
        return render_template("edit-post.html", title="Edit Post",
                               post=post_info,
                               counties=counties)

    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        order_number = request.form["order_number"]
        county = request.form["county"]
        address = request.form["address"]
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]

        if order_number == "":
            order_number = "N/A"

        updated_info = {'title': title,
                        'description': description,
                        'order_number': order_number,
                        'county': county,
                        'address': address,
                        'name': name,
                        'email': email,
                        'phone_number': phone_number
                        }
        update_post = mongo.db.posts
        update_post.update_one({"_id": ObjectId(post_id)},
                               {'$set': updated_info})
        return redirect(url_for('give_help'))


@app.route("/update-status/<post_id>/<status>/")
def update_status(status, post_id):
    if status == "Available":
        update_status = mongo.db.posts
        update_status.update_one({"_id": ObjectId(post_id)},
                                 {'$set': {'status': "Available"}})
        return redirect(url_for('give_help'))
    elif status == "In Progress":
        update_status = mongo.db.posts
        update_status.update_one({"_id": ObjectId(post_id)},
                                 {'$set': {'status': "In Progress"}})
        return redirect(url_for('give_help'))
    elif status == "Completed":
        update_status = mongo.db.posts
        update_status.update_one({"_id": ObjectId(post_id)},
                                 {'$set': {'status': "Completed"}})
        return redirect(url_for('give_help'))


@app.route("/remove-post-confirmation/<post_id>")
def remove_post_confirmation(post_id):
    post_name = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("remove-post.html",
                           title="Remove Post Confirmation",
                           post=post_name)


@app.route("/remove-post/<post_id>")
def remove_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    return redirect(url_for('give_help'))


@app.route("/give-help")
def give_help():
    posts = mongo.db.posts.find()
    return render_template("give-help.html", title="Give Help", posts=posts)


# Error Handlers - Returning content if error occurs
@app.errorhandler(404)
def error404(error):
    return render_template("404.html", title="Page Not Found"), 404


@app.errorhandler(403)
def error403(error):
    return render_template("403.html"), 403


@app.errorhandler(500)
def error500(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
