from flask_restful import Resource
from http import HTTPStatus


class SmokeResource(Resource):
    def get(self):
        return HTTPStatus.OK
