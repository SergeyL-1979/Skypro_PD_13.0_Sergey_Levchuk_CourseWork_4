#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from marshmallow import Schema, fields

from app.setup_db import db


favorite_movie = db.Table(
    'favorite_movie',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

favorite_genre = db.Table(
    'favorite_genre',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    role = db.Column(db.String(25), nullable=False)

    # favorite_genre_id = db.Column(db.ForeignKey("genre.id"), db.Integer)
    favorite_genre = db.relationship("Genre", secondary=favorite_genre)
    favorite_movie = db.relationship("Movie", secondary=favorite_movie)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)
        # return f"<User {self.name}, {self.favorite_genre_id}>"


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()  # чтобы не отображать load_only=True
    surname = fields.Str()
    created_on = fields.DateTime("%d-%m-%Y %H:%M")
    updated_on = fields.DateTime("%d-%m-%Y %H:%M")
    role = fields.Str()
