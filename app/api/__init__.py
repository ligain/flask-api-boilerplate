from flask_restful import Api

from app.api.resources.smoke import SmokeResource

api = Api()

api.add_resource(SmokeResource, '/smoke', endpoint='smoke')

