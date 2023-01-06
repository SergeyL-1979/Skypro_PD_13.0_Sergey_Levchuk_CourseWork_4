#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.dao.user import UserDAO
from app.dao.movie import MovieDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.setup_db import db
from app.services.user import UserService
from app.services.movie import MovieService
from app.services.director import DirectorService
from app.services.genre import GenreService


user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
