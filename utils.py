

def check_is_digit(string):
    """
    @param  STRING
            String is the question that is meant to be asked for input
    @return INT
            Integer that is the response to the output
    """
    # Uses try/except to make sure the inputed response is an integer
    try:
        # Tries to force the input into a string
        inp = int(input(string))
    except ValueError:
        # If the input isn't a string, prints error message and recursively asks the question
        print('Please input an integer')
        return check_is_digit(string)
    # Returns the integer
    return inp

def check_if_exists(name, brand):
    return True
