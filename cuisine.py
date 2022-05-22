from flask_restful import Resource, Api

from hf_db import *

cuisines = []


class Cuisine(Resource):
    def get(self, name):
        # cuisine = next(filter(lambda x: x['name'] == name, cuisines), None)
        # return {'cuisine': cuisine}, 200 if cuisine else 404
        return {'cuisine': retrieveCuisine(name)}

    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, cuisines), None):
        #     return {'message': "Cuisine '{}' already exists. ".format(name)}, 400

        # cuisine = {'name': name, 'status': True}
        create_cuisine(name)
        # cuisines.append(cuisine)
        return {'message': "Cuisine '{}' added successfully ".format(name)}, 201


class CuisineList(Resource):
    def get(self):
        return {'cuisines': retrieveAllCuisines()}
