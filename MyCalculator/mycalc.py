# Calculator app in a GUI using tkinter

############- ISSUES -#############
# No negative numbers currently supported


import tkinter as tk

# Class that takes in numbers and operators as strings and performs simple arithmetic functions on them 
# Build a "MathString" by appending numbers and operators, then evaluate the equation represented in the string.
# Two main methods for use of Class: append() and execute_string()
# Essentially just build the string and execute the math
class StringMath:
    VALIDOPERATORS = ["+", "-", "/", "*", "="]
    
    def __init__(self, initial = None):
        if initial == None:
            self.operation_string = ""
        else:
            self.operation_string = initial
        self.end_char = 1

    # Prints the full string saved in the StringMath class then returns it
    def string(self):
        print("Operation string: " + self.operation_string + ".")
        return self.operation_string

    def isempty(self):
        if self.operation_string == "":
            return True
        else:
            return False

    # Appends a new string to the current operation_string.
    # Performs validation checking
    def append(self, new_string):
        latest_operation_is_valid = self.validate_append(new_string)
        if latest_operation_is_valid:
            if self.operation_string == "":
                self.operation_string = new_string
            else:
                self.operation_string = self.operation_string + " " + new_string
            print(new_string + " added to string")
            self.end_char = StringMath.digit_operator_check(self.operation_string[-1])
            return True
        else:
            print("Not a valid operation to append.")
            return False

    # Returns the object to a cleared state
    def clear(self):
        self.operation_string = ""
        self.end_char = 1

    # Carries out the math equation that is represented by the string
    def execute_string(self):
        split_string = self.operation_string.split(" ")
        
        split_string = self.check_for_operation(split_string, "*")
        split_string = self.check_for_operation(split_string, "/")
        split_string = self.check_for_operation(split_string, "+")
        split_string = self.check_for_operation(split_string, "-")

        return split_string

    def check_for_operation(self, split_string, operator):
        for i in range(split_string.count(operator)):
            index = split_string.index(operator)
            print("The index for " + operator + " is: " + str(index))
            if operator == "/":
                temp_result = self.divide(split_string[index - 1], split_string[index + 1])
            elif operator == "*":
                temp_result = self.multiply(split_string[index - 1], split_string[index + 1])
            elif operator == "+":
                temp_result = self.add(split_string[index - 1], split_string[index + 1])
            elif operator == "-":
                temp_result = self.subtract(split_string[index - 1], split_string[index + 1])
            
            print("Removing: " + split_string[index - 1])
            del split_string[index - 1]
            print("Removing: " + split_string[index - 1])
            del split_string[index - 1]
            print("Removing: " + split_string[index - 1])
            del split_string[index - 1]

            print("Inserting: " + temp_result)
            split_string.insert(index - 1, temp_result)

            print(split_string)

        return split_string

    def divide(self, val1, val2):
        print("Dividing " + val1 + " by " + val2)
        return str(float(val1) / float(val2))

    def multiply(self, val1, val2):
        return str(float(val1) * float(val2))

    def add(self, val1, val2):
        return str(float(val1) + float(val2))

    def subtract(self, val1, val2):
        return str(float(val1) - float(val2))


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
                return False
            elif self.end_char is not new_end_char:
                return True
            else:
                print("Unable to append that to current string")
                print("Current string: " + self.operation_string)
                return False
        
        return False
    
    #Returns integer number to varify what type of input is received
    #       0 : Digit
    #       1 : Valid Operator
    #      -1 : An invalid character
    @classmethod
    def digit_operator_check(cls, in_char):
        if in_char.isdigit():
            return 0
        elif is_float(in_char):
            return 0
        elif StringMath.validate_operator(in_char):
            return 1
        else:
            return -1

    @classmethod
    def validate_string(cls, in_string):
        split_str = in_string.split(" ")
        for split_char in split_str:
            if not (split_char.isdigit() or is_float(split_char) or StringMath.validate_operator(split_char)): 
                #Character is not a valid operator
                print(split_char + " <-- is not valid")
                return False
        return True 
    
    @classmethod
    def validate_operator(cls, test_operator):
        for op in StringMath.VALIDOPERATORS:
            if test_operator == op:
                return True
        return False # if no match then test_operator is not valid


        
# Calculator is used by MainApp to store and perform the mathematic functions of the "Calculator"
# Calculator relies on StringMath to be able to store equations as strings and then evaluate them
class Calculator:
    def __init__(self):
        self.memory_display = StringMath()
        self.prev_mem_display = StringMath()

    def add_to_calc(self,main_app, operator):
        input = main_app.user_entry.get()
        self.memory_display.append(input + " " + operator)

        main_app.current_total_label.config(text = self.memory_display.string())
        main_app.user_entry.delete(0, tk.END)

    def equals_method(self, main_app):
        final_input = main_app.user_entry.get()
        self.memory_display.append(final_input)

        solution = self.memory_display.execute_string()

        main_app.current_total_label.config(text = self.memory_display.string())
        main_app.user_entry.delete(0, tk.END)
        main_app.user_entry.insert(0, solution)

        self.prev_mem_display = self.memory_display
        self.memory_display.clear()

    def clear_vals(self, main_app):
        self.memory_display.clear()

        main_app.current_total_label.config(text = "")
        main_app.current_operator_label.config(text = "")
        main_app.user_entry.delete(0, tk.END)


    
# MainApp defines what the GUI looks like to the user and how it will behave
# All information is stored in Calculator.calc_values
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

        self.plus_button = tk.Button(master = self.button_frame, text = "+", command=lambda: calc_values.add_to_calc(self, "+"))
        self.plus_button.pack(fill = tk.X)
        self.minus_button = tk.Button(master = self.button_frame, text = "-", command = lambda: calc_values.add_to_calc(self, "-"))
        self.minus_button.pack(fill = tk.X)
        self.times_button = tk.Button(master = self.button_frame, text = "*", command = lambda: calc_values.add_to_calc(self, "*"))
        self.times_button.pack(fill = tk.X)
        self.divide_button = tk.Button(master = self.button_frame, text = "/", command = lambda: calc_values.add_to_calc(self, "/"))
        self.divide_button.pack(fill = tk.X)

        self.clear_button = tk.Button(master = self.button_frame2, text = "C", command = lambda: calc_values.clear_vals(self))
        self.clear_button.pack()
        self.equals_button = tk.Button(master = self.button_frame2, text = "=", command = lambda: calc_values.equals_method(self))
        self.equals_button.pack()

        self.top_frame.pack(side = tk.TOP)
        self.button_frame.pack(side = tk.RIGHT)
        self.button_frame2.pack(side = tk.RIGHT)

    def entry_input_callback(self, input):
        
        print("Raw input: " + input)
        print("Last key input: " + input)
        
        if input.isdigit():
            return True
        elif is_float(input):
            return True
        elif input == "":
            return True
        else:
            return False


def is_float(num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False

#only required when actually running program
#initialise required classes
calc_values = Calculator()
main_window = tk.Tk()

application = MainApp(main_window, calc_values)

main_window.mainloop()