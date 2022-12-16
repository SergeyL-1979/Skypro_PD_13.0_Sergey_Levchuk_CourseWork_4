#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        user.name = data.get("name")
        user.email = data.get("email")
        user.password = data.get("password")
        user.surname = data.get("surname")

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "name" in data:
            user.name = data.get("name")
        if "email" in data:
            user.email = data.get("email")
        if "password" in data:
            user.password = data.get("password")
        if "surname" in data:
            user.surname = data.get("surname")

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

