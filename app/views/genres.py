#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import GenreSchema, Genre

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



@genre_ns.route('/')
class GenreView(Resource):
    """
    :parameter- `/genres/` —  возвращает все жанры,
    :parameter- `/genres/<id>` — возвращает информацию о жанре с перечислением списка фильмов по жанру,

    :parameter- `POST /genres/` —  добавляет жанр,
    :parameter- `PUT /genres/<id>` —  обновляет жанр,
    :parameter- `DELETE /genres/<id>` —  удаляет жанр.
    """
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        new_genre = Genres(**req_json)

        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    :parameter- `/genres/` —  возвращает все жанры,
    :parameter- `/genres/<id>` — возвращает информацию о жанре с перечислением списка фильмов по жанру,

    :parameter- `POST /genres/` —  добавляет жанр,
    :parameter- `PUT /genres/<id>` —  обновляет жанр,
    :parameter- `DELETE /genres/<id>` —  удаляет жанр.
    """
    def get(self, gid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, gid):
        genre = db.session.query(Genre).get(gid)
        req_json = request.json

        genre.name = req_json.get("name")

        db.session.add(genre)
        db.session.commit()

        return "", 204

    def patch(self, gid):
        genre = db.session.query(Genre).get(gid)
        req_json = request.json

        if "name" in req_json:
            genre.name = req_json.get("name")

        db.session.add(genre)
        db.session.commit()

        return "", 204

    def delete(self, gid):
        genre = db.session.query(Genre).get(gid)

        db.session.delete(genre)
        db.session.commit()

        return "", 204
