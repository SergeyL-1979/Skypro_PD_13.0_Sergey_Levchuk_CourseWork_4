#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request

from app.dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")

        if year is not None:
            movies = Movie.query.filter(Movie.year == year)
            return movies

        if director and genre is not None:
            movies = Movie.query.filter(Movie.director_id == director).filter(Movie.genre_id == genre)
            return movies

        if genre is not None:
            movies = Movie.query.filter(Movie.genre_id == genre)
            return movies

        if director is None:
            movies = self.session.query(Movie).all()
        else:
            movies = Movie.query.filter(Movie.director_id == director)
        return movies

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

        return movie
