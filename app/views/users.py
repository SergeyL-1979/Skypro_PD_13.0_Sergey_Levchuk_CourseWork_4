#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import user_service
from app.dao.model.user import UserSchema

from app.decorators import admin_required
from app.decorators import auth_required

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

    @auth_required
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    """
    :parameter- `/users/` —  возвращает все user,
    :parameter- `/users/<id>` — возвращает информацию о жанре с перечислением списка фильмов по user,

    :parameter- `POST /users/` —  добавляет user,
    :parameter- `PUT /users/<id>` —  обновляет user,
    :parameter- `DELETE /users/<id>` —  удаляет user.
    """

    def get(self, uid: int):
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception as e:
            return str(e), 404

    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def patch(self, uid):
        req_json = request.json
        req_json["id"] = uid
        user_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/<name>')
class UserView(Resource):
    def get(self, name):
        try:
            user_name = user_service.get_username(name)
            return user_schema.dump(user_name), 200
        except Exception as e:
            return str(e), 404

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

# @mod.route('/register/', methods=['GET', 'POST'])
# class UserView(Resource):
#     def register(self):
#       """
#       Registration Form
#       """
#       # form = RegisterForm(request.form)
#       if form.validate_on_submit():
#         # create an user instance not yet stored in the database
#         user = User(name=form.name.data, email=form.email.data, \
#           password=generate_password_hash(form.password.data))
#         # Insert the record in our database and commit it
#         db.session.add(user)
#         db.session.commit()
#
#         # Log the user in, as he now has an id
#         session['user_id'] = user.id
#
#         # flash will display a message to the user
#         flash('Thanks for registering')
#         # redirect user to the 'home' method of the user module.
#         return redirect(url_for('users.home'))
#       return render_template("users/register.html", form=form)
