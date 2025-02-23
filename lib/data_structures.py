spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [item.get("name") for item in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_list = [item for item in spicy_foods if item.get("heat_level") > 5]
    return spiciest_list

def print_spicy_foods(spicy_foods):
    [print(f'{item.get("name")} ({item.get("cuisine")}) | Heat Level: {item.get("heat_level") * "🌶"}') for item in spicy_foods]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine_spicy = [item for item in spicy_foods if item.get("cuisine") == cuisine]
    for item in cuisine_spicy:
        return item

def print_spiciest_foods(spicy_foods):
    [print(f'{item.get("name")} ({item.get("cuisine")}) | Heat Level: {item.get("heat_level") * "🌶"}') for item in spicy_foods if  item.get("heat_level") > 5]

def get_average_heat_level(spicy_foods):
    heat_level = [item.get("heat_level") for item in spicy_foods]
    total = 0
    for num in heat_level:
        total += num
    return int(total / len(heat_level))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

