# Calculator app in a GUI using tkinter

import tkinter as tk

class calculator:
    def __init__(self):
        self.runningTotal = 0
        self.currentVal = 0

    def clearVals(self):
        self.runningTotal = 0

class MainApp:
    def __init__(self, parent, calcValues):
        self.top_frame = tk.Frame(master = parent)
        self.button_frame = tk.Frame(master = parent, width = 6)
        self.button_frame2 = tk.Frame(master = parent, width = 6) 
        

        self.current_total_label = tk.Label(master = self.top_frame, text = str(calcValues.runningTotal), bg = "white", fg = "black")
        self.current_total_label.pack(side = tk.LEFT)

        reg = parent.register(self.entry_input_callback)
        self.user_entry = tk.Entry(master = self.top_frame, validate = "key", validatecommand = (reg, '%P'), bg = "white", fg = "black", justify = "right")
        self.user_entry.pack(side = tk.LEFT)
        self.user_entry.focus_set()

        self.label2 = tk.Label(master = self.button_frame, text = "Base")
        self.label2.pack(fill = tk.X)

        self.plus_button = tk.Button(master = self.button_frame, text = "+", command=lambda: self.add_method(calcValues))
        self.plus_button.pack(fill = tk.X)
        self.minus_button = tk.Button(master = self.button_frame, text = "-")
        self.minus_button.pack(fill = tk.X)
        self.times_button = tk.Button(master = self.button_frame, text = "X")
        self.times_button.pack(fill = tk.X)
        self.divide_button = tk.Button(master = self.button_frame, text = "/")
        self.divide_button.pack(fill = tk.X)
        #equals_button = tk.Button(master = button_frame, text = "=", command = lambda: equals_method(total, curentVal))

        self.clear_button = tk.Button(master = self.button_frame2, text = "C", command = calcValues.clearVals)
        self.clear_button.pack()

        self.top_frame.pack(side = tk.TOP)
        self.button_frame.pack(side = tk.RIGHT)
        self.button_frame2.pack(side = tk.RIGHT)

        #self.user_entry.config(validate = "key", validatecommand = (reg, '%P'))




    #adds two integer values
    def add_method(self, calcValues):

        calcValues.currentVal = self.get_entry_value()   
        calcValues.runningTotal = calcValues.runningTotal + calcValues.currentVal
        print("The current value in entry is: " + str(calcValues.currentVal))
        print("The current value in total is: " + str(calcValues.runningTotal))
        
        self.user_entry.delete(0, tk.END)
        self.user_entry.insert(0, str(calcValues.runningTotal))
        self.user_entry.insert(tk.END, " + ")
        

    def get_entry_value(self):
        parsed_input = parse_input(self.user_entry.get())
        print("Parsed input: " + parsed_input[-1])
        return int(parsed_input[-1])
    


    def entry_input_callback(self, input):
        
        split_input = parse_input(input)
        print("Raw input: " + input)
        print("Last key input: " + split_input[-1])
        
        if split_input[-1].isdigit():
            return True
        else:
            return False

def parse_input(inString):
    spaces = inString.count(" ")

    separated_input = inString.split(" ")
    return separated_input


#initialise required classes
calcValues = calculator()
main_window = tk.Tk()

application = MainApp(main_window, calcValues)

main_window.mainloop()

