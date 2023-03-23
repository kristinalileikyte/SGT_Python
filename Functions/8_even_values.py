# A function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value.

junk_food = {"BBQ Ribs" : 212, "Cheeseburger" : 263, "Fajita" : 147, "McNuggets" : 302, "Fish and Chips" : 195, "French Fries" : 312, "Onion Rings" : 411}

def even_value(dict):
    even_calories_foods = []
    for food in dict:
        if dict[food] % 2 == 0:
            even_calories_foods.append(food)
    return even_calories_foods


print(even_value(junk_food))