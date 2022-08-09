# Calculator app in a GUI using tkinter

############- ISSUES -#############
# minus_method does not work as expected. Performs subtraction immediately on runningTotal which displays a negative number.
# equal_method does not work as expected. May require some sort of string parsing to determine what operators to use on values.
#   Could store state of top_frame widgets previous to entry and then parse that for the correct result.
#       This may work well for other button widget commands also. Need to see how that will look.  


import tkinter as tk

# Class that takes in numbers and operators as strings and performs simple arithmetic functions on them 
# Build a "MathString" by appending numbers and operators, then parse the string to do maths on it.
class StringMath:
    VALIDOPERATORS = ["+", "-", "/", "*", "="]
    
    def __init__(self):
        self.numbers = []
        self.operators = []

    def include_num(self, in_number):
        if in_number.isdigit():
            self.numbers.append(in_number)
        else:
            print("ERROR. StringMath: includeNum(self, inNumber. Number not provided")

    def include_operator(self, in_operator):
        
        if self.validate_operator(in_operator):
            self.operators.append(in_operator)
        else:
            print("ERROR. StringMath: includeOperator(self, inOperator. Invalid operator provided")

    def validate_operator(self, in_operator):
        
        for op in StringMath.VALIDOPERATORS:
            if in_operator == op:
                return True

        return False        

    #Performs math operations using the math string that has been built.

        

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


#initialise required classes
calc_values = Calculator()
main_window = tk.Tk()

application = MainApp(main_window, calc_values)

main_window.mainloop()