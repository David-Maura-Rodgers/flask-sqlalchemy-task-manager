# pylint --generate-rcfile > pylintrc

# set_pg
# pip3 install Flask-SQLAlchemy psycopg2
# python -m pip install --upgrade pip
# pip install pymysql

# psql
# CREATE DATABASE taskmanager;
# \c taskmanager;

# python3
# from taskmanager import db
# db.create_all()

# psql -d taskmanager
# \dt

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes # noqa
