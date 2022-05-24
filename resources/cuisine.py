from flask_restful import Resource, Api, request

from hf_db import *

cuisines = []


class Cuisine(Resource):
    @staticmethod
    def get(name):

        return {'cuisine': retrieveCuisine(name)}

    @staticmethod
    def post(name):

        data = request.get_json()
        create_cuisine(name, data['status'])
        return {'message': "Cuisine '{}' added successfully ".format(name)}, 201

    @staticmethod
    def put(name):

        data = request.get_json()
        update_cuisine(name, data['status'])
        return {'message': "Cuisine '{}' updated successfully ".format(name)}, 201

    @staticmethod
    def delete(name):

        delete_cuisine(name)
        return {'message': "Cuisine '{}' deleted successfully ".format(name)}, 201


class CuisineList(Resource):
    @staticmethod
    def get():
        return {'cuisines': retrieveAllCuisines()}
