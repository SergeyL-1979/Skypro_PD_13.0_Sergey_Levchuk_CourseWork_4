#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from marshmallow import Schema, fields

from app.database import db


class User(db.Model):
    """
    Модель пользователя имеет следующие поля:
    - ** id ** - первичный ключ
    - ** email ** по нему будет осуществлен доступ на сайт (*уникальное*)
    - ** password ** — не забывайте, что пароль тут будет в хешированном виде
    - name - имя
    - surname - фамилия
    - favorite_genre - любимый жанр
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    surname = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now())
    updated_on = db.Column(db.DateTime(), default=datetime.now(), onupdate=datetime.utcnow)
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")

    # __table_args__ = (
    #     db.PrimaryKeyConstraint('id', name='user_id'),  # Основной ключ
    #     db.UniqueConstraint('name'),  # Уникальный ключ
    #     db.UniqueConstraint('email'),  # Уникальный ключ
    # )

    # === НУЖНО ДЛЯ ИНИЦИЛИЗАЦИИ ==========
    # def __init__(self, name=None, email=None, password=None, surname=None):
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.surname = surname

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
    favorite_genre_id = fields.Int()
