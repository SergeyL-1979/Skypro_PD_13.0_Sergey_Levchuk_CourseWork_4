#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.models import DirectorSchema, Directors

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    """
    :parameter- `/directors/` — возвращает всех режиссеров,
    :parameter- `/directors/<id>` — возвращает подробную информацию о режиссере,

    :parameter- `POST /directors/` —  добавляет режиссера,
    :parameter- `PUT /directors/<id>` —  обновляет режиссера,
    :parameter- `DELETE /directors/<id>` —  удаляет режиссера.
    """
    def get(self):
        all_directors = db.session.query(Directors).all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = Directors(**req_json)

        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    :parameter- `/directors/` — возвращает всех режиссеров,
    :parameter- `/directors/<id>` — возвращает подробную информацию о режиссере,

    :parameter- `POST /directors/` —  добавляет режиссера,
    :parameter- `PUT /directors/<id>` —  обновляет режиссера,
    :parameter- `DELETE /directors/<id>` —  удаляет режиссера.
    """
    def get(self, did: int):
        try:
            director = db.session.query(Directors).filter(Directors.id == did).one()
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, did):
        director = db.session.query(Directors).get(did)
        req_json = request.json

        director.name = req_json.get("name")

        db.session.add(director)
        db.session.commit()

        return "", 204

    def patch(self, did):
        director = db.session.query(Directors).get(did)
        req_json = request.json

        if "name" in req_json:
            director.name = req_json.get("name")

        db.session.add(director)
        db.session.commit()

        return "", 204

    def delete(self, did):
        director = db.session.query(Directors).get(did)

        db.session.delete(director)
        db.session.commit()

        return "", 204


