import os
# API Key
# Find the best ways to query for certain foods
# Allow option to receive info from txt file or from manual input
# Ask for Ingredient name and brand
# Ask for how much of the ingredient was used
# Use conversions to convert the amount used in recipe to amount in recipe
# Query For Ingredient name
# Multiply Calorie, Macro-nutrient, and Micro-nutrient by the Scalar
# Ask if user would like to save recipe and ask a name
# Create GUI to allow user to visually see recipe name

def conversion_amount():
    """
    """
    # Asks user for the amount used 

    # Reduce using conversion to lowest amount per item

    num = 0
    return num

def find_ingredient_man():
    """
    """
    ingredient = input('Please input the name of the ingredient used: ')
    ingredient = ingredient.lower()
    # error check
    brand = input('Please input the brand of the ingredient used: ')
    brand = brand.lower()
    # error check
    tuplet = (ingredient, brand)
    return tuplet

def check_exists(tup):
    return True

def recipe_info_man():
    """
    @return Dictionary of tuples which contain 2 Strings the first being the name of the ingredient and the second being the brand
    """
    # Initialize Dictionary
    # Ask for amount of ingredient used
    key = conversion_amount()
    # Ask for name of ingredient & brand
    tup = find_ingredient_man()
    exists = check_exists(tup)

    
    
    return recipe

def recipe_info_file(file):
    """
    @param String
    @return Dictionary of tuples which contain 2 Strings the first being the name of the ingredient and the second being the brand
    """
    
    return recipe

def check_is_digit(string):
    """
    """
    try:
        inp = int(input(string))
    except ValueError:
        print('Please input an integer')
        check_is_digit(string)
    return inp