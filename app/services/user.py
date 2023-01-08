#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Метод хеширование пароля
import hashlib
import base64
import hmac

from ..constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from app.dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_username(self, user_name):
        return self.dao.get_username(user_name)

    def get_email(self, user_email):
        return self.dao.get_email(user_email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data_user):
        data_user["password"] = self.get_hash(data_user["password"])
        return self.dao.create(data_user)

    def update(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "name" in data:
            user.name = data.get("name")
        if "surname" in data:
            user.surname = data.get("surname")
        if "email" in data:
            user.email = data.get("email")
        if "password" in data:
            user.password = self.get_hash(data.get("password"))
        if "role" in data:
            user.role = data.get("role")
        if "favorite_genre_id" in data:
            user.favorite_genre_id = data.get("favorite_genre_id")

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Преобразовать пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
