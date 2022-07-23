#Number Guessing

import random

class NumberGenerator:
    
    lowerBound = 0
    upperBound = 10

    def __init__(self):
        self.randmNumber = None
        self.hint = None


    def generate_number(self):
        self.randomNumber = random.randint(NumberGenerator.lowerBound, NumberGenerator.upperBound)

        return self.randomNumber

    def compare_numbers(self, userNum):
        winVal = False
        if userNum == self.randomNumber:
            self.hint = "You win!"
            winVal = True
        elif userNum > self.randomNumber:
            self.hint = "Too high!"
        elif userNum < self.randomNumber:
            self.hint = "Too low!"
        
        return winVal

            


# Allow user to guess
def get_user_guess(prompt):
    user_number = input(prompt + ": ")
    return int(user_number)

NumGen = NumberGenerator()
number = NumGen.generate_number()
print(number)

winVal = False
while winVal == False:
    user_guess = get_user_guess("Please guess a number between " + str(NumberGenerator.lowerBound) + " and " + str(NumberGenerator.upperBound))
    winVal = NumGen.compare_numbers(user_guess)
    print(NumGen.hint)
