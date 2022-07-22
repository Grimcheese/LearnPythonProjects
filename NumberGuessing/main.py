#Number Guessing

import random

lowerBound = 0
upperBound = 10

#Generate random number
def number_generator(lower, upper):
    number = random.randint(lower, upper)

    return number



# Allow user to guess
def get_user_guess(prompt):
    user_number = input(prompt + ": ")
    return user_number


# Compare guess to generated number
def compare_numbers(randNum, userNum):
    if userNum > randNum:


random_number = number_generator(lowerBound, upperBound)
user_guess = get_user_guess("Please guess a number between " + lowerBound + " and " + upperBound)
result = compare_numbers(random_number, user_guess)