from peewee import *

db = PostgresqlDatabase('postgres', user='postgres', password='admin', host='localhost')


class BaseModel(Model):
    class Meta:
        database = db


class Cuisines(BaseModel):
    cuisineId = AutoField(primary_key=True)
    cuisine = TextField()
    status = BooleanField()


class Ingredients(BaseModel):
    ingredientId = AutoField(primary_key=True)
    ingredient = TextField()
    status = BooleanField()


class Menus(BaseModel):
    menuId = AutoField(primary_key=True)
    menu = TextField()
    description = TextField()
    status = BooleanField()


class NutritionInformation(BaseModel):
    nutritionInformationId = AutoField(primary_key=True)
    nutrition = TextField()
    status = BooleanField()


class Recipes(BaseModel):
    recipeId = AutoField(primary_key=True)
    recipe = TextField()
    description = TextField()
    prepTime = TextField()
    cuisineId = ForeignKeyField(Cuisines, backref='recipes')
    rating = IntegerField()
    comments = TextField()


class RecipeIngredients(BaseModel):
    recipeIngredientId = AutoField(primary_key=True)
    recipeId = ForeignKeyField(Recipes, backref='recipe-ingredients')
    amount = TextField()
    ingredientId = ForeignKeyField(Ingredients, backref='recipe-ingredients')
    cuisineId = ForeignKeyField(Cuisines, backref='recipes')
    Instructions = TextField()


class RecipeNutritionInformation(BaseModel):
    recipeNutInfoId = AutoField(primary_key=True)
    recipeId = ForeignKeyField(Recipes, backref='recipeNutrition-information')
    nutritionInformationId = ForeignKeyField(NutritionInformation, backref='recipeNutrition-information')


class MenuRecipes(BaseModel):
    menuRecipeId = AutoField(primary_key=True)
    recipeId = ForeignKeyField(Recipes, backref='menuRecipes')
    menuId = ForeignKeyField(Menus, backref='menuRecipes')


def setup():
    db.connect()
    db.create_tables([Cuisines,
                      Ingredients,
                      Menus,
                      NutritionInformation,
                      Recipes,
                      RecipeIngredients,
                      RecipeNutritionInformation,
                      MenuRecipes])


def create_cuisine(cuisine):
    Cuisines.create(cuisine=cuisine, status=True)


def retrieveAllCuisines():
    qs = Cuisines.select().dicts()
    lst = []
    for q in qs:
        lst.append(q)
    return lst


def retrieveCuisine(cuisine):
    qs = Cuisines.select().where(Cuisines.cuisine == cuisine).dicts()
    lst = []
    for q in qs:
        lst.append(q)
    return lst
