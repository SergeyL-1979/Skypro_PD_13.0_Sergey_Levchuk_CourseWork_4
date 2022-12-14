#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False
    # SECRET_HERE = '249y823r9v8238r9u'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/movies.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./data/test.db'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'order.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =======================================================
    # # basedir = os.path.abspath(os.path.dirname(__file__))
    # BASE_DIR = os.path.abspath(path="data")
    # POST_PATH = os.path.join(BASE_DIR, "posts.json")
    # COMMENT_PATH = os.path.join(BASE_DIR, "comments.json")
    # BOOKMARKS_PATH = os.path.join(BASE_DIR, "bookmarks.json")
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, "images")
    # MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    # =========================================================
