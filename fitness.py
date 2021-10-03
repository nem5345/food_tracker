# This will be a fitness script that calculate/show how many calories you need to consume based on 
# Don't forget to add error handling
from utils import *

def main():
    BMR = information_BMR()
    # BMR is multiplied by 1.2 to account for normal everyday activity BMR is if you don't move
    BMR = BMR * 1.2
    calorie_loss = weight_loss()
    calorie_burned = workout_calories()
    calories = BMR - calorie_loss + calorie_burned
    string = str(calories) + ' is the amount you should eat to hit your goals'
    print(string)
    exit()

def information_BMR():
    # Ask for Weight in lbs and Error check it
    string = 'Weight(lbs): '
    weight = check_is_digit(string)
    # Ask for Height in in and Error check it
    print('(5 ft = 60 in & 6 ft is 72 in)')
    string = 'Height(in): '
    height = check_is_digit(string)
    # Ask for Age in years and error check it
    string = 'Age: '
    age = check_is_int(string)
    # Calculate BMR which is calories burned if you didn't move ever
    BMR_int = BMR(weight, height, age)
    return BMR_int

def BMR (weight, height, age):
    # BMR Calculation according to scientific professionals
    BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.67 * age)
    return BMR

def weight_loss():
    string = 'How many pounds of fat would you like to lose a week? (Recomended value is 2 or less)\n'
    fat_loss = check_is_digit(string)
    calorie_loss = fat_loss * 500
    return calorie_loss

def workout_calories():
    string = 'How many hours of strength training a day?: '
    strength_workout = check_is_digit(string)
    calories_strength = strength_workout * 500
    string = 'How many miles do you run per day?: '
    running_workout = check_is_digit(string)
    calories_run = running_workout * 125
    return calories_run + calories_strength

if __name__ == "__main__":
    main()