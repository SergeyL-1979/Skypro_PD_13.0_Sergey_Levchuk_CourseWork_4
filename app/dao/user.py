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

    def get_email(self, user_email):
        return self.session.query(User).filter(User.email == user_email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    # def delete(self, uid):
    #     user = self.get_one(uid)
    #     self.session.delete(user)
    #     self.session.commit()
    #     return user

    def delete(self, name):
        nikname = self.get_username(name)
        self.session.delete(nikname)
        self.session.commit()
        return nikname

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
