#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Configuration)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
