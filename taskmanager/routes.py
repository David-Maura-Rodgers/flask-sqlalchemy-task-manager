# https://docs.sqlalchemy.org/en/14/

# set_pg
# pip3 install Flask-SQLAlchemy psycopg2

# psql
# CREATE DATABASE taskmanager;
# \c taskmanager;

from flask import render_template
from taskmanager import app, db # noqa
from taskmanager.models import Category, Task # noqa


@app.route("/")
def home():
    return render_template("base.html")
