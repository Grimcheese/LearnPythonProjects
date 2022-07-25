# Main Python file for Rock Paper Scissors game
import random

# Rock, Paper and Scissors are each represented with an integer value; 0, 1, and 2
# Rock = 0
# Paper = 1
# Scissors = 2

# Generate Rock, Paper or Scissors

class RockPaperScissors:
    
    #Constructors
    def __init__(self, name, newRPSString = None):
        self.rpsName = name
        if newRPSString == None:
            self.rpsVal = self.make_random_rock_paper_scissors()
            self.rpsString = self.get_rps_val_string(self.rpsVal)
        else:
            self.rpsString = newRPSString
            self.rpsVal = self.get_rps_string_val(newRPSString) #Sets rpsString to standardised value

    
    @classmethod
    def validate_RPS_int(self, newVal):
        if newVal < 0 or newVal > 2:
            return False
        else:
            return True

    @classmethod
    def validate_RPS_string(self, newStr):
        validStr = ["rock", "Rock", "paper", "Paper", "scissors", "Scissors", "0", "1", "2"]

        isValid = False
        for str in validStr:
            if newStr == str:
                isValid = True

        
        return isValid

    #returns integer value 0, 1, 2
    # 0 = It is a tie
    # 1 = First RPS wins
    # 2 = Second RPS wins
    @classmethod
    def compare_rock_paper_scissors(self, rps1, rps2):
        result = -1
        if rps1.rpsVal == rps2.rpsVal:
            print("It is a draw!")
            result = 0
        elif rps1.rpsString == "Rock" and rps2.rpsString == "Scissors" or rps1.rpsString == "Paper" and rps2.rpsString == "Rock" or rps1.rpsString == "Scissors" and rps2.rpsString == "Paper":
            result = 1
            print(rps1.rpsName + " wins!")
        else:
            result = 2
            print(rps2.rpsName + " wins!")

        return result


    def make_random_rock_paper_scissors(self):
        rNum = random.randint(0,2)

        return rNum
    
    def new_random_state(self):
        self.rpsVal = self.make_random_rock_paper_scissors()
        self.rpsString = self.get_rps_val_string(self.rpsVal)

    def get_rps_val_string(self, rpsVal):
        newStr = None
        if rpsVal == 0:
            newStr = "Rock"
        elif rpsVal == 1:
            newStr = "Paper"
        elif rpsVal == 2:
            newStr = "Scissors"
        else:
            newStr = "Not valid"
        
        return newStr

    def get_rps_string_val(self, rpsString):
        newVal = None
        if rpsString == "Rock" or rpsString == "rock" or rpsString == "0":
            self.rpsString = "Rock"
            newVal = 0
        elif rpsString == "Paper" or rpsString == "paper" or rpsString == "1":
            self.rpsString = "Paper"
            newVal = 1
        elif rpsString == "Scissors" or rpsString == "scissors" or rpsString == "2":
            self.rpsString = "Scissors"
            newVal = 2
        else:
            self.rpsString = "Not valid"

        return newVal
        

def get_user_rock_paper_scissors():
    isValid = False

    while isValid == False:
        userInput = input("Please choose: ")
        isValid = RockPaperScissors.validate_RPS_string(userInput)
        if isValid == True:
            print("Valid")
        else:
            print("Not valid")
    
    return userInput



print("Welcome to Rock, Paper, Scissors!")
play = True
while play == True:
    userRPS = RockPaperScissors("User", get_user_rock_paper_scissors())
    print("User chose: " + userRPS.rpsString)

    ai = RockPaperScissors("AI")
    print("AI chose: " + ai.rpsString)
    RockPaperScissors.compare_rock_paper_scissors(userRPS, ai)

    #user input with no validation
    
    if input("Play again?(y/n): ") == "n":
        play = False
        break
        


