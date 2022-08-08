# Calculator app in a GUI using tkinter

############- ISSUES -#############
# minus_method does not work as expected. Performs subtraction immediately on runningTotal which displays a negative number.
# equal_method does not work as expected. May require some sort of string parsing to determine what operators to use on values.
#   Could store state of top_frame widgets previous to entry and then parse that for the correct result.
#       This may work well for other button widget commands also. Need to see how that will look.  


import tkinter as tk

class calculator:
    def __init__(self):
        self.runningTotal = 0
        self.currentVal = 0
        self.currentOperator = ""

    
    def perform_operation(self, mainApp, input):
        self.currentVal = int(input)
        
        if self.currentOperator == "+":
            #Perform addition
            self.runningTotal = self.runningTotal + self.currentVal
            mainApp.update_top_frame_values(self)
        elif self.currentOperator == "-":
            self.runningTotal = self.runningTotal - self.currentVal
            mainApp.update_top_frame_values(self)
        elif self.currentOperator == "=":

        
        print("The current value in entry is: " + str(self.currentVal))
        print("The current value in total is: " + str(self.runningTotal))

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
    def add_method(self, mainApp):
        input = mainApp.user_entry.get()
        validInput = self.validate_input(input)
        if validInput:
            self.currentOperator = "+"
            self.perform_operation(mainApp, input)

    def minus_method(self, mainApp):
        input = mainApp.user_entry.get()
        validInput = self.validate_input(input)
        if validInput:
            self.currentOperator = "-"
            self.update_top_frame(mainApp, input)
            #self.runningTotal = self.runningTotal - self.currentVal
    


    def equalsMethod(self, mainApp):
        input = mainApp.user_entry.get()
        validInput = self.validate_input(input)
        if validInput:
            mainApp.current_total_label.config(text = str(self.runningTotal) + " " + str(self.currentOperator) + " " + input)

            self.currentOperator = "="

            self.perform_operation(mainApp, input)

            mainApp.current_operator_label.config(text = self.currentOperator)
            mainApp.user_entry.delete(0, tk.END)
            mainApp.user_entry.insert(0, self.runningTotal)

        

    def clearVals(self, mainApp):
        self.runningTotal = 0

        mainApp.current_total_label.config(text = "")
        mainApp.current_operator_label.config(text = "")
        mainApp.user_entry.delete(0, tk.END)


    

class MainApp:
    def __init__(self, parent, calcValues):
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

        self.plus_button = tk.Button(master = self.button_frame, text = "+", command=lambda: calcValues.add_method(self))
        self.plus_button.pack(fill = tk.X)
        self.minus_button = tk.Button(master = self.button_frame, text = "-", command = lambda: calcValues.minus_method(self))
        self.minus_button.pack(fill = tk.X)
        self.times_button = tk.Button(master = self.button_frame, text = "X")
        self.times_button.pack(fill = tk.X)
        self.divide_button = tk.Button(master = self.button_frame, text = "/")
        self.divide_button.pack(fill = tk.X)

        self.clear_button = tk.Button(master = self.button_frame2, text = "C", command = lambda: calcValues.clearVals(self))
        self.clear_button.pack()
        self.equals_button = tk.Button(master = self.button_frame2, text = "=", command = lambda: calcValues.equalsMethod(self))
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

        
    def update_top_frame_values(self, calcValues):
        self.current_total_label.config(text = str(calcValues.runningTotal))
        self.current_operator_label.config(text = calcValues.currentOperator)
        self.user_entry.delete(0, tk.END)

def parse_input(inString):
    spaces = inString.count(" ")

    separated_input = inString.split(" ")
    return separated_input


#initialise required classes
calcValues = calculator()
main_window = tk.Tk()

application = MainApp(main_window, calcValues)

main_window.mainloop()