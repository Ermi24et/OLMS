from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# initializing codes and configure the flask application packages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///olms.db"
app.config['SECRET_KEY'] = '93b832a6610615832be732a4'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
from olms import routes
