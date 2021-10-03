# This will be a fitness script that calculate/show how many calories you need to consume based on 
# Don't forget to add error handling
from utils import *

def fitness():
    # Initialize list for information ollected to go into
    info = []
    info = info_collection()
    # BMR is multiplied by 1.2 to account for normal everyday activity BMR is if you don't move
    BMR_n = 0
    BMR_n = BMR(info[0], info[1], info[2]) * 1.2
    # The amount of calories eaten is your BMR + the calories you burn + the amount of fat you want to lose
    calories = BMR_n + info[4] - (info[3] * 500)
    string = str(calories) + 'cal is the amount of calories you should eat a day to hit your goals'
    print(string)

def info_collection():
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
    i = 0
    while i == 0:
        # Ask for fat loss goal in pounds and error check it
        string = 'How many pounds of fat would you like to lose in lbs?'
        fat_goal = check_is_digit(string)
        # Ask for time goal in weeks and error check it
        string = 'How many weeks would you like to take on your diet?'
        weeks = check_is_int(string)
        if reality_check(fat_goal, weeks) == True:
            i == 1
            break
    # Ask for strength training time and error check it
    string = 'How many hours of strength training a day?: '
    calories_strength = check_is_digit(string) * 500
    # Ask for miles ran and error check it
    string = 'How many miles do you run per day?: '
    calories_run = check_is_digit(string) * 125 
    # Calculate how many calories are burned a day
    calories_burn =  calories_run + calories_strength
    # Return all the information 
    return weight, height, age, fat_goal/weeks, calories_burn

def reality_check(fat_goal, weeks): 
    # Check if their goal is to lose more than 2lbs of fat a week and keep making them rethink their goals
    if (fat_goal/weeks) > 2:
        print("Your fat loss goal is unrealistic and unhealthy. On average someone can lose 1-2 lbs of body fat a week.")
        print("Please try readjusting your goals. It is ok for it to take longer than you want as long as you stay consistent.")
        print("We do not support unhealthy lifestyles so I will ask you again what your fat loss goal is and for a new time period")
        return False
    return True

def BMR(weight, height, age):
    # BMR Calculation according to scientific professionals
    BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.67 * age)
    return BMR



def main():
    fitness()
    exit()

if __name__ == "__main__":
    main()