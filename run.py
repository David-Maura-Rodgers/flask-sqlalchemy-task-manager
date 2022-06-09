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
from taskmanager import app


if __name__ == "__main__":
    # app.debug = True
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
