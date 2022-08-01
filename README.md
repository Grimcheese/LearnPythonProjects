This repo is a collection of simple programming projects designed to familiarise myself again with the Python programming language and with the version control software git.

Using projects from https://hackr.io/blog/python-projects

1/ MadLibs Generator
    A simple program that takes words as user input and outputs them into a story a la Mad Libs
    The user is prompted to enter a single word and they are given the type, eg adjective, noun, etc. Then according to a chosen template the words are placed into a story to come up with something new and hopefully funny.
    The templates are stored in a json file which the python program can read from and then put the chosen words into for output to the user.

2/ Rock Paper Scissors
    The user plays rock, paper, scissors with the computer. The user chooses an option either with text or numerically and then the computer chooses a random response. The two choices are compared and a winner/loser is determined. 
    Scores are kept track of.
        ToDO
            Store scores in a .txt file to bring them back on later play throughs
            Ability to play with another human player
            Network connectivity

3/ Number Guessing
    The user is asked to guess a random number which is chosen by the computer.
    The user first selects a range for the random number to be in and then the computer chooses a random number within that range (uses random). On each guess the user is given a hint (higher or lower) and their score is adjusted. 

4/ Binary Search
    A simple binary search algorithm.
    A binary search is placed in one method of this program and then tested using a generated list. The generated list is within a range from 0 to n where n is selected by the user. The list is sorted and then given to the binary_search method 
    where it searches for a specific number selected by the user. 
    
5/ Calculator
    A calculator program built in python. A calculator with a GUI that provides basic calculator functions; +, -, *, /. User enters numbers and then pushes buttons to get results. 
        ToDo
            Add scientific calculator functionality