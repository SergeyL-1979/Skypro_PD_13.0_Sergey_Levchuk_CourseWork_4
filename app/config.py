#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

# === ИМПОРТИРУЕМ load_dotenv ===
from dotenv import load_dotenv
load_dotenv(override=True)

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False
    # === МОЖНО ИСПОЛЬЗОВАТЬ ВАРИАНТА =======
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # === ИЛИ ВОТ ТАКОЙ ВАРИАНТ =============
    SECRET_KEY = os.environ.get('SECRET_KEY')
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
