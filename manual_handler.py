from utils import *

def ingredient_name():
    name = input('Please input the ingredient name: ')
    return name

def ingredient_brand():
    brand = input('Please input the ingredient brand: ')
    return brand

def ingredient_amount():
    print('Please input the amount of ingredient use in the format: # lbs') 
    print('Units of measure to choose from: lbs, oz, cup, tbsp, tsp, pint, quart, gallon, L, mL, g, dash, pinch')
    numstr = input('Amount: ')
    l = numstr.split(' ')
    if len(l) != 2:
        print('Incorrect amount of arguments, try again.')
        ingredient_amount()
        return l
    n = 3
    n = check_unit(l)
    if n == 0:
        ingredient_amount()
    else:
        return l

def ingredient_info():
    """
    Calls functions that manually receive input from the user about the ingredient name, brand, and amount used in the recipe
    @return TUPLE
            TUPLE which holds the string of the ingredient name, the string of the brand, and the integer of the amount used in the recipe
    """
    # Asks the user for the ingredient name
    name = ingredient_name()
    # Asks the user for the brand name
    brand = ingredient_brand()
    # Error checks to see if the ingredient exists
    exists = check_if_exists(name, brand)
    # If the ingredient doesn't exist, recursively call the function
    if exists != True:
        print('Ingredient does not exist, please try again.')
        ingredient_info()
    # If the ingredient exists, find the amount and return the tuple
    else:
        amount = ingredient_amount()
        number = int(amount[0])
        unit = amount[1]
        tuplet = (name, brand, number, unit)
        return tuplet

def manual_handler():
    """
    Manually receives recipe input and organizes the ingredient information into tuples, which are stored in a list
    @return LIST
            List of tuples which holds (ingredient name, brand, amount in lowest conversion)
    """
    # Initializes the recipe list
    recipe = []
    # Loops through continueing asking the user for the ingrdients of the recipe until there are no more
    while True:
        item = ingredient_info()
        string = 'To add another ingredient, hit enter, else enter 0: '
        answer = input(string)
        # If the answer doesn't equal to 0 add the ingredient to the recipe
        if answer == '0':
            break
        # Potentially ask if the user incorrectly added information. Not here yet.
        recipe.append(item)    
    return recipe

def check_unit(l):
    """
    Checks the unit of the amount of ingredient input from manual_handler.py
    @param  LIST
            List of two things which is the amount of ingredient, and the measurement
    @return INT
            Either 0 if the input failed the checks, 1 if the input passed the checks
    """
    # Removes the first amount from the list and checks the input is a float
    num = l[0]
    # Checks if the first input is a float
    try:
        num = float(num)
    # Returns error message if failes
    except ValueError:
        print('Please input an floating point number as the first argument.')
        return 0
    # Checks the unit which is the second string in the list
    # If it does not match up with the units listed here, it is not accepted
    unit = l[1]
    # Singular units of measure
    if unit == 'lbs' or unit == 'oz' or unit == 'cup' or unit == 'tbsp' or unit == 'tsp' or unit == 'pint' or unit == 'quart' or unit == 'gallon' or unit == 'L' or unit == 'mL' or unit == 'g' or unit == 'dash' or unit == 'pinch':
        return 1
    # Plural units of measure
    elif unit == 'lb' or unit == 'ozs' or unit == 'cups' or unit == 'pints' or unit == 'quarts' or unit == 'gallons' or unit == 'dashes' or unit == 'pinches':
        return 1
    else:
        print('Please put an accurate unit of measure as listed.')
        return 0