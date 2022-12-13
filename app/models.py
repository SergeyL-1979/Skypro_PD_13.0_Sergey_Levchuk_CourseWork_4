#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields

from app.database import db

favorite_genres = db.Table('favorite_genres',
                           db.Column('user_id', db.Integer, db.ForeignKey('user.pk')),
                           db.Column('genre_id', db.Integer, db.ForeignKey('genre.pk'))
                           )
movie_genre = db.Table('movie_genre',
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.pk')),
                       db.Column('genre_id', db.Integer, db.ForeignKey('genre.pk'))
                       )

movie_director = db.Table('movie_director',
                          db.Column('movie_id', db.Integer, db.ForeignKey('movie.pk')),
                          db.Column('director_id', db.Integer, db.ForeignKey('director.pk'))
                          )


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

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    surname = db.Column(db.String(120))
    favorite_genre_id = db.relationship("Genres", secondary=favorite_genres)

    __table_args__ = (
        db.PrimaryKeyConstraint('pk', name='user_pk'),  # Основной ключ
        db.UniqueConstraint('name'),  # Уникальный ключ
        db.UniqueConstraint('email'),  # Уникальный ключ
    )

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.name}, {self.favorite_genre_id}>"


class UserSchema(Schema):
    pk = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()


class Movies(db.Model):
    """
    - ** id ** - первичный ключ
    - ** title**- название
    - **description** - описание
    - **trailer** - ссылка на трейлер
    - **year** - год выпуска
    - **rating** - рейтинг
    - **genre_id** - id жанра
    - **director_id**  - id режиссера
    """
    __tablename__ = "movie"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    trailer = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    genre_id = db.relationship("Genres", secondary=movie_genre)
    director_id = db.relationship("Directors", secondary=movie_director)

    # genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    # genre = db.relationship("Genre")
    #
    # director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    # director = db.relationship("Director")

    def __repr__(self):
        return f"<Movies: {self.title}, Genre: {self.genre_id}, Director: {self.director_id}>"


class MovieSchema(Schema):
    pk = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()


class Directors(db.Model):
    """
    
    """
    __tablename__ = "director"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(150))

    def __repr__(self):
        return f"<Directors: {self.name}>"


class DirectorSchema(Schema):
    pk = fields.Int(dump_only=True)
    name = fields.Str()


class Genres(db.Model):
    __tablename__ = "genre"

    pk = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Genre: {self.name}>"


class GenreSchema(Schema):
    pk = fields.Int(dump_only=True)
    name = fields.Str()
