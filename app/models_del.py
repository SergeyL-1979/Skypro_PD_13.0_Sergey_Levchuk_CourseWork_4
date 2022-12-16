#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from marshmallow import Schema, fields
#
# from app.database import db


# class User(db.Model):
#     """
#     Модель пользователя имеет следующие поля:
#     - ** id ** - первичный ключ
#     - ** email ** по нему будет осуществлен доступ на сайт (*уникальное*)
#     - ** password ** — не забывайте, что пароль тут будет в хешированном виде
#     - name - имя
#     - surname - фамилия
#     - favorite_genre - любимый жанр
#     """
#     __tablename__ = "user"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     surname = db.Column(db.String(120))
#     favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
#     genre = db.relationship("Genre")
#
#     # favorite_genre_id = db.relationship("Genre", secondary=favorite_genres)
#
#     __table_args__ = (
#         db.PrimaryKeyConstraint('id', name='user_id'),  # Основной ключ
#         db.UniqueConstraint('name'),  # Уникальный ключ
#         db.UniqueConstraint('email'),  # Уникальный ключ
#     )
#
#     def __init__(self, name=None, email=None, password=None):
#         self.name = name
#         self.email = email
#         self.password = password
#
#     def __repr__(self):
#         return f"<User {self.name}, {self.favorite_genre_id}>"


# class UserSchema(Schema):
#     id = fields.Int(dump_only=True)
#     email = fields.Str()
#     password = fields.Str()
#     name = fields.Str()
#     surname = fields.Str()


# class Movie(db.Model):
#     """
#     - ** id ** - первичный ключ
#     - ** title**- название
#     - **description** - описание
#     - **trailer** - ссылка на трейлер
#     - **year** - год выпуска
#     - **rating** - рейтинг
#     - **genre_id** - id жанра
#     - **director_id**  - id режиссера
#     """
#     __tablename__ = "movie"
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String(150), nullable=False)
#     trailer = db.Column(db.Text, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#     genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
#     genre = db.relationship("Genre")
#     director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
#     director = db.relationship("Director")
#
#     # genre_id = db.relationship("Genre", secondary=movie_genre)
#     # director_id = db.relationship("Director", secondary=movie_director)
#
#     def __repr__(self):
#         return f"<Movies: {self.title}, Genre: {self.genre_id}, Director: {self.director_id}>"
#
#
# class MovieSchema(Schema):
#     id = fields.Int(dump_only=True)
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()


# class Director(db.Model):
#     """
#
#     """
#     __tablename__ = "director"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#
#     def __repr__(self):
#         return f"<Directors: {self.name}>"


# class DirectorSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()


# class Genre(db.Model):
#     __tablename__ = "genre"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#
#     def __repr__(self):
#         return f"<Genre: {self.name}>"
#
#
# class GenreSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()
