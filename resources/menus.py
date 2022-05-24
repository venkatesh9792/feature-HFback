from flask_restful import Resource

from models.models import menus


class MenuList(Resource):
    @staticmethod
    def get():
        return {'Menus': menus()}
