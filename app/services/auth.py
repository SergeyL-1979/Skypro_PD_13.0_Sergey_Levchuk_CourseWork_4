#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import calendar
import jwt
from flask import request, abort

from ..constants import JWT_SECRET, JWT_ALGORITHM
from ..services.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    # def generate_tokens(self, username, password, is_refresh=False):
    def generate_tokens(self, user_mail, password, is_refresh=False):
        # user = self.user_service.get_username(email)
        mails = self.user_service.get_email(user_mail)

        # if user is None:
        #     raise abort(404)
        if mails is None:
            raise abort(404)

        if not is_refresh:
            # if not self.user_service.compare_passwords(user.password, password):
            if not self.user_service.compare_passwords(mails.password, password):
                abort(400)

        data = {
            # "name": user.name,
            # "role": user.role,
            "email": mails.email,
            "role": mails.role
        }

        # 30 minutes for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # 130 days for refresh_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=130)
        data["exp"] = calendar.timegm(min30.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        # name = data.get("name")
        mails = data.get("email")

        # return self.generate_tokens(name, None, is_refresh=True)
        return self.generate_tokens(mails, None, is_refresh=True)
