#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

# == СОЗДАНИЕ СЕКРЕТНОГО КЛЮЧА СЕССИИ ==
secret_key = os.urandom(20).hex()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/movies.db'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'order.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =============== ПАМЯТКА КОМАНД ========================================
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/movies.db'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/test.db'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # # basedir = os.path.abspath(os.path.dirname(__file__))
    # BASE_DIR = os.path.abspath(path="data")
    # POST_PATH = os.path.join(BASE_DIR, "posts.json")
    # COMMENT_PATH = os.path.join(BASE_DIR, "comments.json")
    # BOOKMARKS_PATH = os.path.join(BASE_DIR, "bookmarks.json")
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, "images")
    # MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    # =========================================================
