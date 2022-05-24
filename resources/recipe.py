from flask_restful import Resource

from hf_db import *

cuisines = []


class Recipe(Resource):

    @staticmethod
    def post(recipe, description, prep_time, cuisine_id):
        create_recipe(recipe, description, prep_time, cuisine_id)
        # cuisines.append(cuisine)
        return {'message': "Recipe '{}' added successfully ".format(recipe)}, 201
