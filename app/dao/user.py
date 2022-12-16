#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_by_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_all(self):
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

    # def get_by_email(self, email):
    #     return {}
    #
    # def get_by_name(self, name):
    #     return {}

    def delete(self, uid):
        user = self.get_by_one(uid)
        self.session.delete(user)
        self.session.commit()
        return user