#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Метод хеширование пароля
import hashlib
import base64
import hmac

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from app.dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_username(self, user_name):
        return self.dao.get_username(user_name)

    def get_user_by_email(self, user_email):
        return self.dao.get_user_by_email(user_email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data_user):
        data_user["password"] = self.get_hash(data_user["password"])
        return self.dao.create(data_user)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    # ==== Удаление по имени ====
    def delete(self, name):
        self.dao.delete(name)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Преобразовать пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        return self.dao.compare_passwords(password_hash, other_password)

    # ==== ВАРИАНТ ОБНОВЛЕНИЯ ДАННЫХ ====
    # def update(self, u_data):
    #     uid = u_data.get("id")
    #     user = self.get_one(uid)
    #     if "name" in u_data:
    #         user.name = u_data.get("name")
    #     if "surname" in u_data:
    #         user.surname = u_data.get("surname")
    #     if "email" in u_data:
    #         user.email = u_data.get("email")
    #     if "role" in u_data:
    #         user.role = u_data.get("role")
    #     self.dao.update(user)

    # ==== Удаление по ID ====
    # def delete(self, uid):
    #     self.dao.delete(uid)
