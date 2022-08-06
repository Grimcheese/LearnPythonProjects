# Calculator app in a GUI

import tkinter as tk

class calculator:
   def __init__(self):
        self.runningTotal = 0
        self.currentVal = 0

class MainApp:
    def __init__(self, parent, calcValues):
        self.top_frame = tk.Frame(master = parent)
        self.button_frame = tk.Frame(master = parent, width = 6)

        self.user_entry = tk.Entry(master = self.top_frame, bg = "white", fg = "black", justify = "right")
        self.user_entry.pack()

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

        self.top_frame.pack(side = tk.TOP)
        self.button_frame.pack(side = tk.RIGHT)

        reg = parent.register(entry_input_callback)
        self.user_entry.config(validate = "key", validatecommand = (reg, '%P'))




    #adds two integer values
    def add_method(self, calcValues):

        currentVal = int(self.get_entry_value())   
        calcValues.runningTotal = calcValues.runningTotal + currentVal
        print("The current value in entry is: " + str(currentVal))
        print("The current value in total is: " + str(calcValues.runningTotal))
        
        self.user_entry.insert(tk.END, " + ")

    def get_entry_value(self):
        if not self.user_entry.get() == "":
            return int(self.user_entry.get())
        else:
            return 0


def entry_input_callback(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False



#initialise required settings
calcValues = calculator()
main_window = tk.Tk()

application = MainApp(main_window, calcValues)

#text = tk.Label(text="My Calculator", foreground = "white", background = "black")
#text.pack()



main_window.mainloop()

