#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, flash, redirect, url_for, render_template
from flask_restx import Resource, Namespace

from app.database import db
from app.models import UserSchema, User

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    """
    :parameter- `/users/` — возвращает всех user,
    :parameter- `/users/<id>` — возвращает подробную информацию о user,

    :parameter- `POST /users/` —  добавляет user,
    :parameter- `PUT /users/<id>` —  обновляет user,
    :parameter- `DELETE /users/<id>` —  удаляет user.
    """

    def get(self):
        all_users = db.session.query(User).all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        new_user = User(**req_json)

        with db.session.begin():
            db.session.add(new_user)
        return "", 201


# ======= НАДО ПРОРАБОТАТЬ НАД ПРОФИЛЕМ =======================
# @user_ns.route('/<nickname>')
# # @login_required
# class UserView(Resource):
#     def user(self, nickname):
#         user_profile = User.query.filter(name=nickname).first()
#         if user_profile == None:
#             flash('User ' + nickname + ' not found.')
#             return redirect(url_for('index'))
#         posts = [
#             {'author': user_profile, 'body': 'Test post #1'},
#             {'author': user_profile, 'body': 'Test post #2'}
#         ]
#         return render_template('user.html',
#                                user_profile=user_profile,
#                                posts=posts)
