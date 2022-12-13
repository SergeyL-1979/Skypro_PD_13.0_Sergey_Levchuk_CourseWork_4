#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import MovieSchema, Movies

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Запрос всех фильмов. При запросе с параметром
    :parameter- `/movies` — возвращает список всех фильмов, разделенный по страницам;
    :parameter- `/movies/<id>` — возвращает подробную информацию о фильме.

    Организован поиск по режиссерам и жанрам
    :parameter - /movies/?director_id=1
    выводит список фильмов по ID режиссером
    :parameter - /movies/?genre_id=4
    выводит список всех фильмов по ID жанров
    :parameter - /movies/?director_id=2&genre_id=4
    выводит список фильмов по ID режиссера и жанра
    """
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")

        if director and genre is not None:
            all_movies = Movies.query.filter(Movies.director_id == director).filter(Movies.genre_id == genre)
            return movies_schema.dump(all_movies), 200

        if genre is not None:
            all_movies = Movies.query.filter(Movies.genre_id == genre)
            return movies_schema.dump(all_movies), 200

        if director is None:
            all_movies = db.session.query(Movies).all()
        else:
            all_movies = Movies.query.filter(Movies.director_id == director)
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movies(**req_json)

        with db.session.begin():
            db.session.add(new_movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MoviesView(Resource):
    """
    Реализованы все методы
    :parameter- `/movies` — возвращает список всех фильмов, разделенный по страницам;
    :parameter- `/movies/<id>` — возвращает подробную информацию о фильме.

    :parameter- `POST /movies/` —  добавляет кино в фильмотеку,
    :parameter- `PUT /movies/<id>` —  обновляет кино,
    :parameter- `DELETE /movies/<id>` —  удаляет кино.
    """
    def get(self, mid: int):
        try:
            movie = db.session.query(Movies).filter(Movies.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid):
        movie = db.session.query(Movies).get(mid)
        req_json = request.json

        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return "", 204

    def patch(self, mid):
        movie = db.session.query(Movies).get(mid)
        req_json = request.json

        if "title" in req_json:
            movie.title = req_json.get("title")
        if "description" in req_json:
            movie.description = req_json.get("description")
        if "trailer" in req_json:
            movie.trailer = req_json.get("trailer")
        if "year" in req_json:
            movie.year = req_json.get("year")
        if "rating" in req_json:
            movie.rating = req_json.get("rating")
        if "genre_id" in req_json:
            movie.genre_id = req_json.get("genre_id")
        if "director_id" in req_json:
            movie.director_id = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return "", 204

    def delete(self, mid):
        movie = db.session.query(Movies).get(mid)

        db.session.delete(movie)
        db.session.commit()

        return "", 204
