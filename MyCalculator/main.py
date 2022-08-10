# Calculator app in a GUI using tkinter

############- ISSUES -#############
# minus_method does not work as expected. Performs subtraction immediately on runningTotal which displays a negative number.
# equal_method does not work as expected. May require some sort of string parsing to determine what operators to use on values.
#   Could store state of top_frame widgets previous to entry and then parse that for the correct result.
#       This may work well for other button widget commands also. Need to see how that will look.  


import tkinter as tk

# Class that takes in numbers and operators as strings and performs simple arithmetic functions on them 
# Build a "MathString" by appending numbers and operators, then parse the string to do maths on it.
# Two main methods for use of Class: appen_string() and execute_string()
# Essentially just build the string and execute the math
class StringMath:
    VALIDOPERATORS = ["+", "-", "/", "*", "="]
    
    def __init__(self):
        self.operation_string = ""
        self.end_char = 1
        self.numbers = []
        self.operators = []

    def stringmath_string(self):
        print(self.operation_string)
        return self.operation_string

    #
    def append_string(self, new_string):
        latest_operation_is_valid = self.validate_append(new_string)
        if latest_operation_is_valid:
            self.operation_string.append(new_string)
            return True
        else:
            print("Not a valid operation to append.")

    #Two different posibilities: 1/ new_string starts with number
    #                            2/ new_string starts with a math operator
    def validate_append(self, new_string):
        # Need to ensure that the new_string is valid and can be appended
        # to the current operation_string

        new_string_valid = StringMath.validate_string(new_string)
        if new_string_valid:
            #Check first "character" of new string to see if it is compatible
            new_end_char = StringMath.digit_operator_check(new_string[0])
            if new_end_char == -1:
                print("New string starts with an invalid character")
            elif self.end_char is not new_end_char:
                self.operation_string.append(" " + new_string)
            else:
                print("Unable to append that to current string")
                print("Current string: " + self.operation_string)
    
    #Returns integer number to varify what type of input is received
    #       0 : Digit
    #       1 : Valid Operator
    #      -1 : An invalid character
    @classmethod
    def digit_operator_check(cls, in_char):
        if in_char.isdigit():
            return 0
        elif StringMath.validate_operator(in_char):
            return 1
        else:
            return -1

    @classmethod
    def validate_string(cls, in_string):
        split_str = in_string.split(" ")
        for split_char in split_str:
            if not (split_char.isdigit() or StringMath.validate_operator(split_char)): 
                #Character is not a valid operator
                return False
        return True 
    
    @classmethod
    def validate_operator(cls, test_operator):
        for op in StringMath.VALIDOPERATORS:
            if test_operator == op:
                return True
        return False # if no match then test_operator is not valid


        

class Calculator:
    def __init__(self):
        self.running_total = 0
        self.current_val = 0
        self.current_operator = ""
        self.previous_operator = ""

        #New approach to allow for easier manipulation of more numbers and different operators -> pushed into new class StringMath

    
    def perform_operation(self, main_app, input_operator):
        input = main_app.user_entry.get()
        
        if self.validate_input(input):
            self.current_val = int(input)
            self.current_operator = input_operator
            
            if self.current_operator == "+":
                #Perform addition
                self.running_total = self.running_total + self.current_val
                main_app.update_top_frame_values(self)
            elif self.current_operator == "-":
                self.running_total = self.running_total - self.current_val
                main_app.update_top_frame_values(self)
        else:
            print("Invalid input from user_entry widget.")
            print("User input: " + input)

        
        print("The current value in entry is: " + str(self.current_val))
        print("The current value in total is: " + str(self.running_total))

    def validate_input(self, input):
        if input == "":
            return False
        elif input == "+":
            return False
        elif input == "-":
            return False
        else:
            return True
    
    #adds two integer values
    def add_method(self, main_app):
        input = main_app.user_entry.get()
        valid_input = self.validate_input(input)
        if valid_input:
            self.current_operator = "+"
            self.perform_operation(main_app, input)

    def minus_method(self, main_app):
        input = main_app.user_entry.get()
        valid_input = self.validate_input(input)
        if valid_input:
            self.current_operator = "-"
            self.perform_operation(main_app, input)
    


    def equals_method(self, main_app):
        input = main_app.user_entry.get()
        valid_input = self.validate_input(input)
        print(valid_input)
        if valid_input:
            main_app.current_total_label.config(text = str(self.running_total) + " " + str(self.current_operator) + " " + input)

            self.current_operator = "="

            self.perform_operation(main_app, input)

            main_app.current_operator_label.config(text = self.current_operator)
            main_app.user_entry.delete(0, tk.END)
            main_app.user_entry.insert(0, self.running_total)

        

    def clear_vals(self, main_app):
        self.running_total = 0

        main_app.current_total_label.config(text = "")
        main_app.current_operator_label.config(text = "")
        main_app.user_entry.delete(0, tk.END)


    

class MainApp:
    def __init__(self, parent, calc_values):
        self.top_frame = tk.Frame(master = parent, width = 20)
        self.button_frame = tk.Frame(master = parent, width = 6)
        self.button_frame2 = tk.Frame(master = parent, width = 6) 
        

        self.current_total_label = tk.Label(master = self.top_frame, bg = "white", fg = "black", width = 5)
        self.current_total_label.pack(side = tk.LEFT)

        self.current_operator_label = tk.Label(master = self.top_frame, bg = "white", fg = "black", width = 5)
        self.current_operator_label.pack(side = tk.LEFT)

        reg = parent.register(self.entry_input_callback)
        self.user_entry = tk.Entry(master = self.top_frame, validate = "key", validatecommand = (reg, '%P'), relief = tk.FLAT, bg = "white", fg = "black", justify = "right", width = 10)
        self.user_entry.pack(side = tk.RIGHT)
        self.user_entry.focus_set()

        self.plus_button = tk.Button(master = self.button_frame, text = "+", command=lambda: calc_values.perform_operation(self, "+"))
        self.plus_button.pack(fill = tk.X)
        self.minus_button = tk.Button(master = self.button_frame, text = "-", command = lambda: calc_values.perform_operation(self, "-"))
        self.minus_button.pack(fill = tk.X)
        self.times_button = tk.Button(master = self.button_frame, text = "X")
        self.times_button.pack(fill = tk.X)
        self.divide_button = tk.Button(master = self.button_frame, text = "/")
        self.divide_button.pack(fill = tk.X)

        self.clear_button = tk.Button(master = self.button_frame2, text = "C", command = lambda: calc_values.clear_vals(self))
        self.clear_button.pack()
        self.equals_button = tk.Button(master = self.button_frame2, text = "=", command = lambda: calc_values.equals_method(self))
        self.equals_button.pack()

        self.top_frame.pack(side = tk.TOP)
        self.button_frame.pack(side = tk.RIGHT)
        self.button_frame2.pack(side = tk.RIGHT)

        #self.user_entry.config(validate = "key", validatecommand = (reg, '%P'))

    def entry_input_callback(self, input):
        
        print("Raw input: " + input)
        print("Last key input: " + input)
        
        if input.isdigit():
            return True
        elif input == "":
            return True
        elif input == "+":
            return True
        else:
            return False

        
    def update_top_frame_values(self, calc_values):
        self.current_total_label.config(text = str(calc_values.running_total))
        self.current_operator_label.config(text = calc_values.current_operator)
        self.user_entry.delete(0, tk.END)

def parse_input(in_string):
    spaces = in_string.count(" ")

    separated_input = in_string.split(" ")
    return separated_input

#only required when actually running program
#initialise required classes
#calc_values = Calculator()
#main_window = tk.Tk()

#application = MainApp(main_window, calc_values)

#main_window.mainloop()