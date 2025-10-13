"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
 return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    alcohol_ingredients = [
        'whiskey', 'whisky', 'vodka', 'rum', 'gin', 'tequila', 'brandy', 'liqueur',
        'bourbon', 'scotch', 'rye', 'cognac', 'absinthe', 'sake', 'soju',
        'vermouth', 'sherry', 'port', 'wine', 'champagne', 'prosecco',
        'beer', 'ale', 'stout', 'cider', 'mezcal', 'pisco', 'schnapps'
    ]
    
    # Check if any alcoholic ingredient is in the drink ingredients
    has_alcohol = any(alcohol in drink_ingredients for alcohol in alcohol_ingredients)
    
    if has_alcohol:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    special_ingredients = set(ingredients) & SPECIAL_INGREDIENTS
    return (dish_name, special_ingredients)


def compile_ingredients(dishes):
    master_ingredients = set()
    for dish_ingredients in dishes:
        master_ingredients.update(dish_ingredients)
    return master_ingredients


def separate_appetizers(dishes, appetizers):
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    
    # Remove appetizers from dishes and convert back to list
    main_dishes = list(dishes_set - appetizers_set)
    
    return main_dishes


def singleton_ingredients(dishes, intersection):
    ingredient_count = {}
    
    for dish in dishes:
        for ingredient in dish:
            ingredient_count[ingredient] = ingredient_count.get(ingredient, 0) + 1
    
    # Find ingredients that appear exactly once
    singletons = {ingredient for ingredient, count in ingredient_count.items() if count == 1}
    
    return singletons