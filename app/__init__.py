from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import base_path

import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(base_path, 'tmp'))

from app import views, models
