import os 

def file_handler():
    """
    """
    recipe = []
    file = ''
    while True:
        item = file_parser(file)
        string = 'To add another ingredient, hit enter, else enter 0: '
        answer = input(string)
        # If the answer doesn't equal to 0 add the ingredient to the recipe
        if answer == '0':
            break
        recipe.append(item)
    return recipe

def file_parser(file):
    name = ''
    brand = ''
    amount = 1
    unit = ''
    tuplet = (name, brand, amount, unit)
    return tuplet

# def ingredient_info():
#     """
#     Calls functions that manually receive input from the user about the ingredient name, brand, and amount used in the recipe
#     @return TUPLE
#             TUPLE which holds the string of the ingredient name, the string of the brand, and the integer of the amount used in the recipe
#     """
#     # Asks the user for the ingredient name
#     name = ingredient_name()
#     # Asks the user for the brand name
#     brand = ingredient_brand()
#     # Error checks to see if the ingredient exists
#     exists = check_if_exists(name, brand)
#     # If the ingredient doesn't exist, recursively call the function
#     if exists != True:
#         print('Ingredient does not exist, please try again.')
#         ingredient_info()
#     # If the ingredient exists, find the amount and return the tuple
#     else:
#         amount = ingredient_amount()
#         number = int(amount[0])
#         unit = amount[1]
#         tuplet = (name, brand, number, unit)
#         return tuplet