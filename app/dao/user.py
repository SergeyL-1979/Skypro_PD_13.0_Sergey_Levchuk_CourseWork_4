#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Метод хеширование пароля
import hashlib
import base64
import hmac

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

from app.dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_username(self, user_name):
        return self.session.query(User).filter(User.name == user_name).first()

    def get_user_by_email(self, user_email):
        return self.session.query(User).filter(User.email == user_email).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    # === ВАРИАНТ ИЗ ВИДЕОРАЗБОРА КУРСОВОЙ ====
    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        for k, v in user_d.items():
            setattr(user, k, v)

        self.session.add(user)
        self.session.commit()

    # ==== УДАЛЕНИЕ ПО ИМЕНИ ====
    def delete(self, name_d):
        name = self.get_username(name_d)
        self.session.delete(name)
        self.session.commit()
        return name

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    # === MY VARIANT =====
    # def update(self, user_d):
    #     self.session.add(user_d)
    #     self.session.commit()
    #     return user_d

    # ==== VARIANT UPDATE ====
    # def update(self, user_d):
    #     user = self.get_one(user_d.get("id"))
    #     user.name = user_d.get("name")
    #     user.password = user_d.get("password")
    #     self.session.add(user)
    #     self.session.commit()

    # ==== УДАЛИТЬ ПО ID ====
    # def delete(self, uid):
    #     user = self.get_one(uid)
    #     self.session.delete(user)
    #     self.session.commit()
    #     return user


