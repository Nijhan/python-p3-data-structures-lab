# data_structures.py

def get_names(spicy_foods):
    """Returns a list of names of all spicy foods."""
    return [food['name'] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Returns a list of foods with heat_level greater than 5."""
    return [food for food in spicy_foods if food['heat_level'] > 5]


def print_spicy_foods(spicy_foods):
    """Prints all foods formatted with name, cuisine, and 🌶 emojis."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the first food that matches the given cuisine."""
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # in case no food matches


def print_spiciest_foods(spicy_foods):
    """Prints only the foods with heat_level over 5 formatted with 🌶 emojis."""
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    """Returns the average heat_level of all spicy foods."""
    total = sum(food['heat_level'] for food in spicy_foods)
    return total // len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
    """Returns a new list containing all spicy foods plus the new food."""
    return spicy_foods + [new_food]
