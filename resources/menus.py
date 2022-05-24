from flask_restful import Resource

from hf_db import menus


class MenuList(Resource):
    @staticmethod
    def get():
        return {'Menus': menus()}
