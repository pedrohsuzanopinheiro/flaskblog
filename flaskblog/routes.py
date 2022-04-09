from flask import flash, redirect, render_template, url_for

from flaskblog import app
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import Post, User

posts = [
    {
        "author": "Pedro Pinheiro",
        "title": "Blog post 1",
        "content": "That's my first post!",
        "date_posted": "April 20, 2022",
    },
    {
        "author": "Droka",
        "title": "Blog post 2",
        "content": "That's my second post!",
        "date_posted": "April 28, 2022",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "blog@blog.com" and form.password.data == "123":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check credentials.", "danger")
    return render_template("login.html", title="Login", form=form)
