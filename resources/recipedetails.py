from flask_restful import Resource, request

from models.models import ingredients, nutrition, update_recipe_rating


class RecipeDetails(Resource):
    @staticmethod
    def get(cui_name, rec_id):
        return {'ingredients': ingredients(cui_name, rec_id), 'nutrition': nutrition(cui_name, rec_id)}

    @staticmethod
    def put(cui_name, rec_id):
        data = request.get_json()
        update_recipe_rating(rec_id, data['rating'])
        return {'message': "Cuisine rating updated "}, 200
