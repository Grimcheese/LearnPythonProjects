#Number Guessing

import random

class NumberGenerator:
    
    lowerBound = 0
    upperBound = 10

    def __init__(self):
        self.randmNumber = None
        self.hint = None
        self.score = 10
        self.loseVal = False


    def generate_number(self):
        self.randomNumber = random.randint(NumberGenerator.lowerBound, NumberGenerator.upperBound)

        return self.randomNumber

    def compare_numbers(self, userNum):
        winVal = False
        if userNum == self.randomNumber:
            self.hint = "You win!"
            self.modify_score(10)
            winVal = True
        elif userNum < NumberGenerator.lowerBound or userNum > NumberGenerator.upperBound:
            self.hint = "Outside of range!"
            self.modify_score(-5)
        elif userNum > self.randomNumber:
            self.hint = "Too high!"
            self.modify_score(-2)
        elif userNum < self.randomNumber:
            self.hint = "Too low!"
            self.modify_score(-2)
        
        return winVal

    def modify_score(self, val):
        if type(val) == int:
            self.score = self.score + val
            if self.score <= 0:
                self.hint = "You lose"
                self.loseVal = True
        else:
            print("Not a valid modifier")

    @classmethod
    # Allow user to guess and validate input
    def get_user_guess(cls, prompt):
        
        while True:
            try:
                user_number = int(input(prompt + ": "))
            except ValueError:
                print("Input not a valid integer")
                continue
            else:
                return int(user_number)

NumGen = NumberGenerator()
number = NumGen.generate_number()
print(number)

winVal = False
while winVal == False and NumGen.loseVal == False:
    user_guess = NumberGenerator.get_user_guess("Please guess a number between " + str(NumberGenerator.lowerBound) + " and " + str(NumberGenerator.upperBound))
    winVal = NumGen.compare_numbers(user_guess)
    print(NumGen.hint)
    print("Current score: " + str(NumGen.score))
