import os
from functools import wraps
from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
mongo = PyMongo(app)


def check_logged_in(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        if 'logged-in' in session:
            return(func(*args, **kwargs))
        else:
            return render_template('access-denied.html', title="Access Denied")
    return wrapped_function


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        if 'logged-in' in session:
            return redirect(url_for('dashboard'))
        else:
            return render_template("sign-up.html", title="Sign Up for Free")
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        user_email = request.form["email"]
        password = request.form["pword"]
        user_phone = request.form["phone"]
        user_address = request.form["address"]
        user_type = request.form["user_type"]
        is_over_18 = request.form["age_confirmation"]
        hash = pbkdf2_sha256.hash(password)

        new_user = {'first_name': first_name,
                    'last_name': last_name,
                    'user_email': user_email,
                    'password': hash,
                    'user_phone': user_phone,
                    'user_address': user_address,
                    'user_type': user_type,
                    'is_over_18': is_over_18
                    }

        mongo.db.users.insert_one(new_user)
        return redirect(url_for('login'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'logged-in' in session:
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", title="Login")
    if request.method == "POST":
        form_email = request.form["email"]
        user = mongo.db.users.find_one({'user_email': form_email})
        form_password = request.form["pword"]
        user_password = user['password']
        if pbkdf2_sha256.verify(form_password, user_password):
            session['logged-in'] = True
            session['user_id'] = str(user['_id'])
        return redirect(url_for('dashboard'))


@app.route("/logout")
@check_logged_in
def logout():
    session.pop('logged-in', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route("/dashboard")
@check_logged_in
def dashboard():
    user_id = session['user_id']
    user_info = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("dashboard.html", title="Dashboard", user=user_info)


@app.route("/edit-profile", methods=["GET", "POST"])
@check_logged_in
def edit_profile():
    if request.method == "GET":
        user_id = session['user_id']
        user_info = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("edit-profile.html",
                               title="Edit Profile",
                               user=user_info)
    if request.method == "POST":
        first_name = request.form["fname"]
        last_name = request.form["lname"]
        user_email = request.form["email"]
        user_phone = request.form["phone"]
        user_address = request.form["address"]
        user_type = request.form["user_type"]

        edit_user = {'first_name': first_name,
                     'last_name': last_name,
                     'user_email': user_email,
                     'user_phone': user_phone,
                     'user_address': user_address,
                     'user_type': user_type,
                     }

        update_user = mongo.db.users
        user_id = session['user_id']
        update_user.update_one({"_id": ObjectId(user_id)},
                               {'$set': edit_user})
        return redirect(url_for('dashboard'))


@app.route("/get-help", methods=["GET", "POST"])
@check_logged_in
def get_help():
    if request.method == "GET":
        user_id = session['user_id']
        user_info = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        counties = mongo.db.counties.find()
        return render_template("get-help.html",
                               title="Get Help",
                               counties=counties,
                               user=user_info)
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
                    'status': 'Available',
                    'post_creator': session['user_id']
                    }

        mongo.db.posts.insert_one(new_post)
        return redirect(url_for('give_help'))


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
@check_logged_in
def edit_post(post_id):
    if request.method == "GET":
        post_info = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
        if session['user_id'] == post_info['post_creator']:
            counties = mongo.db.counties.find()
            return render_template("edit-post.html", title="Edit Post",
                                   post=post_info,
                                   counties=counties)
        else:
            return render_template('not-your-post.html')

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
@check_logged_in
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
@check_logged_in
def remove_post_confirmation(post_id):
    post_name = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if session['user_id'] == post_name['post_creator']:
        return render_template("remove-post.html",
                               title="Remove Post Confirmation",
                               post=post_name)
    else:
        return render_template('not-your-post.html')


@app.route("/remove-post/<post_id>")
@check_logged_in
def remove_post(post_id):
    post_name = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    if session['user_id'] == post_name['post_creator']:
        mongo.db.posts.delete_one({"_id": ObjectId(post_id)})
        return redirect(url_for('give_help'))
    else:
        return render_template('not-your-post.html')


@app.route("/give-help")
@check_logged_in
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
