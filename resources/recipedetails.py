from flask_restful import Resource

from hf_db import recipes_for_cuisine, ingredients, nutrition


class RecipeDetails(Resource):
    @staticmethod
    def get(cui_name, rec_id):
        return {'ingredients': ingredients(cui_name, rec_id), 'nutrition': nutrition(cui_name, rec_id)}
