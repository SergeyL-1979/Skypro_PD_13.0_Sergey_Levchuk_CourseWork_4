#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from marshmallow import Schema, fields

from app.setup_db import db


tags = db.Table(
    'tags',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)
    updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)

    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    tags = db.relationship("Movie", secondary=tags)

    role = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
        # return f"<User {self.name}, {self.favorite_genre_id}>"


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    surname = fields.Str()
    created_on = fields.DateTime("%d-%m-%Y %H:%M")
    updated_on = fields.DateTime("%d-%m-%Y %H:%M")
    role = fields.Str()
