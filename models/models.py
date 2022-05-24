from peewee import *

# Db connection parameters
db = PostgresqlDatabase('postgres', user='postgres', password='admin',  host='database')


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
    # connect to DB
    db.connect()

    # Create all the tables
    db.create_tables([Cuisines,
                      Ingredients,
                      Menus,
                      NutritionInformation,
                      Recipes,
                      RecipeIngredients,
                      RecipeNutritionInformation,
                      MenuRecipes])


# ER Maps
def create_cuisine(cuisine, status):
    Cuisines.create(cuisine=cuisine, status=status)


def update_cuisine(cuisine, status):
    row = Cuisines.get(Cuisines.cuisine == cuisine)
    row.status = status
    row.save()


def update_recipe_rating(recipe_id, rating):
    qry = Recipes.update({Recipes.rating: rating}).where(Recipes.recipeId == recipe_id)
    qry.execute()


def delete_cuisine(cuisine):
    qry = Cuisines.delete().where(Cuisines.cuisine == cuisine)
    qry.execute()


def retrieveAllCuisines():
    qs = Cuisines.select().dicts()
    return getList(qs)


def retrieveCuisine(cuisine):
    qs = Cuisines.select().where(Cuisines.cuisine == cuisine).dicts()
    return getList(qs)


def create_recipe(recipe, description, prep_time, cuisine_id):
    Recipes.create(recipe=recipe,
                   description=description,
                   prepTime=prep_time,
                   cuisineId=cuisine_id
                   )


def recipes_for_cuisine(cuisine):
    qs = Recipes.select().join(Cuisines).where((Cuisines.cuisine == cuisine)).dicts()
    return getList(qs)


def ingredients(cuisine, recipe_id):
    qs = Cuisines.select(Ingredients).join(Recipes).join(RecipeIngredients).join(Ingredients).where(
        (Cuisines.cuisine == cuisine) & (Recipes.recipeId == recipe_id)).dicts()

    return getList(qs)


def nutrition(cuisine, recipe_id):
    qs = Cuisines.select(NutritionInformation).join(Recipes).join(RecipeNutritionInformation).join(
        NutritionInformation).where(
        (Cuisines.cuisine == cuisine) & (Recipes.recipeId == recipe_id)).dicts()

    return getList(qs)


def menus():
    qs = Menus.select(Menus.menu, Recipes.recipe).join(MenuRecipes).join(Recipes).dicts()
    return getList(qs)


# obtain list from dicts
def getList(qs):
    lst = []
    for q in qs:
        lst.append(q)
    return lst
