# https://docs.sqlalchemy.org/en/14/

# set_pg
# pip3 install Flask-SQLAlchemy psycopg2
# python -m pip install --upgrade pip
# pip install pymysql
# pylint --generate-rcfile > pylintrc

# psql
# CREATE DATABASE taskmanager;
# \c taskmanager;

# python3
# from taskmanager import db
# db.create_all()
from flask import render_template, request, redirect, url_for
from taskmanager import app, db # noqa
from taskmanager.models import Category, Task # noqa


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
