# -*- encoding: utf-8 -*-
'''
@File    : serverApi.py
@Time    : 2023/01/21 19:59:16
@Author  : lxxtec
@Contact : 631859877@qq.com
@Version : 0.1
@Desc    : None
'''

from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


def CreateUUID():
    return uuid4().hex


class AppConfiguration:
    SQLALCHEMY_TRACK_MODIFACATIONS = False
    SQLALCHEMY_ECHO = True
    """this generate a sqlite db file in current directory"""
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"


""" start app server """
app = Flask(__name__)
app.config.from_object(AppConfiguration)

"""set the db object as sqlclchemy"""
db = SQLAlchemy(app)


class User(db.Model):
    # table name
    __tablename__ = 'users'
    # automatic ID generator
    id = db.Column(db.String(32), unique=True, primary_key=True)
    default = CreateUUID()

    """ email column make sure it's unique"""
    email = db.Column(db.String(355), unique=True)

    """ pssword column, make sure nullable is false"""
    password = db.Column(db.String(), nullable=False)


""" this allows us to use the server without having it online"""
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
