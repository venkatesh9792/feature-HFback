INSERT INTO public.cuisines(cuisine, status) VALUES ('Indian', true);
INSERT INTO public.cuisines(cuisine, status) VALUES ('american', true);
INSERT INTO public.cuisines(cuisine, status) VALUES ('Italian', true);

INSERT INTO public.recipes(recipe, description, "prepTime", "cuisineId_id", rating, comments) VALUES ('Briyani', 'Briyani', '30 mins', 1, 4, '');
INSERT INTO public.recipes(recipe, description, "prepTime", "cuisineId_id", rating, comments) VALUES ('jajaj', 'jajaj', '40 mins', 1, 4, '');

INSERT INTO public.ingredients(ingredient, status) VALUES ('Rice', True);
INSERT INTO public.ingredients(ingredient, status) VALUES ('Chicken', True);
INSERT INTO public.ingredients(ingredient, status) VALUES ('Chilli', True);
INSERT INTO public.ingredients(ingredient, status) VALUES ('salt', True);

INSERT INTO public.menus(menu, description, status) VALUES ('Menu-Amaze', 'Varitey Indian ', True);
INSERT INTO public.menus(menu, description, status) VALUES ('Menu-Classic', 'Varitey Indian ', True);	

INSERT INTO public.nutritioninformation(nutrition, status) VALUES ('Energy', True);
INSERT INTO public.nutritioninformation(nutrition, status) VALUES ('Carbs', True);	
INSERT INTO public.nutritioninformation(nutrition, status) VALUES ('Protein', True);


INSERT INTO public.recipeingredients("recipeId_id", amount, "ingredientId_id", "Instructions") VALUES (1, '1 kg', 1, 'Boil Rice');
INSERT INTO public.recipeingredients("recipeId_id", amount, "ingredientId_id", "Instructions") VALUES (1, '1 kg', 2, 'Slow cook Chicken');
INSERT INTO public.recipeingredients("recipeId_id", amount, "ingredientId_id", "Instructions") VALUES (1, '3', 3, 'Cut into slices');
INSERT INTO public.recipeingredients("recipeId_id", amount, "ingredientId_id", "Instructions") VALUES (1, '10 grams', 4, 'Add it once cooked');



INSERT INTO public.recipenutritioninformation("recipeId_id", "nutritionInformationId_id") VALUES (1, 1);
INSERT INTO public.recipenutritioninformation("recipeId_id", "nutritionInformationId_id") VALUES (1, 2);
INSERT INTO public.recipenutritioninformation("recipeId_id", "nutritionInformationId_id") VALUES (1, 2);


INSERT INTO public.menurecipes("recipeId_id", "menuId_id") VALUES (2, 1);
INSERT INTO public.menurecipes("recipeId_id", "menuId_id") VALUES (1, 1);

commit;