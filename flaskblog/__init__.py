from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "009ed827052896fc6ae7426c140ea46d"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Supressing notifications
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes
