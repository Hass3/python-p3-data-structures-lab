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
    return[f['name']for f in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return[f for f in spicy_foods if f["heat_level"]> 5]


def print_spicy_foods(spicy_foods):
    for f in spicy_foods:
        name = f["name"]
        cuisine =f["cuisine"]
        pepper = "🌶" * f["heat_level"] 
        print(f'{name} ({cuisine}) | Heat Level: {pepper}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for f in spicy_foods:
        if f["cuisine"] == cuisine:
            return dict(f)

def print_spiciest_foods(spicy_foods):
    for f in spicy_foods:
        name = f["name"]
        cuisine = f["cuisine"]
        peppers = "🌶" * f["heat_level"] 
        if f["heat_level"] > 5:
            print(f'{name} ({cuisine}) | Heat Level: {peppers}')
            

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for f in spicy_foods:
        total_heat += f["heat_level"]
    return total_heat / len(spicy_foods)
            
        

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


