from utils import *
from file_handler import *
from manual_handler import *

def choose_input():
    """
    Asks the user to choose how they would like to input the recipe
    @return INT
            1 Represents one-by-one ingredient recipe input
            2 Represents a recipe in the form of a text file
    """
    # Asks the user to input an integer choosing how they would like to input the recipe
    print('How would you like to input the recipe information?')
    string = 'Choose 1 to input ingredients one-by-one. Choose 2 to submit a recipe in a text file.\n'
    # Error checks if the input is a integer
    choice = check_is_digit(string)
    # Error checks if the input is in with the bounds of the question
    if choice < 1 or choice > 2:
        print('Invalid input, please input 1 or 2')
        choose_input() 
    else:
        return choice

def main():
    """ 
    This program will receive a recipe for a meal and return the nutrient information that is relavent.
    """
    # Ask the user to choose how the recipe will be inputed
    choice = choose_input()
    # Uses the user's input to decided if to call the manual input or file input method
    if choice == 1:
        query_list = manual_handler()
    else:
        query_list = file_handler()
    # query_list is a list of dictionaries which holds the information
    exit()

if __name__ == "__main__":
    main()  
    