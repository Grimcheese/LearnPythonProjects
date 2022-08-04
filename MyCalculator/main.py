# Calculator app in a GUI

import tkinter as tk

class calculator:
   def __init__(self):
        self.runningTotal = 0
        self.currentVal = 0


def entry_input_callback(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

#adds two integer values
def add_method(calcValues):

    currentVal = int(get_entry_value())   
    calcValues.runningTotal = calcValues.runningTotal + currentVal
    print("The current value in entry is: " + str(currentVal))
    print("The current value in total is: " + str(calcValues.runningTotal))
    
    user_entry.insert(0, " + " + str(calcValues.runningTotal))


def get_entry_value():
    if not user_entry.get() == "":
        return int(user_entry.get())
    else:
        return 0

#initialise required settings
calcValues = calculator()
main_window = tk.Tk()

#text = tk.Label(text="My Calculator", foreground = "white", background = "black")
#text.pack()

top_frame = tk.Frame()
button_frame = tk.Frame(width = 6)

user_entry = tk.Entry(master = top_frame, bg = "white", fg = "black", justify = "right")
user_entry.pack()

label2 = tk.Label(master = button_frame, text = "Base")
label2.pack(fill = tk.X)

plus_button = tk.Button(master = button_frame, text = "+", command=lambda: add_method(calcValues))
plus_button.pack(fill = tk.X)
minus_button = tk.Button(master = button_frame, text = "-")
minus_button.pack(fill = tk.X)
times_button = tk.Button(master = button_frame, text = "X")
times_button.pack(fill = tk.X)
divide_button = tk.Button(master = button_frame, text = "/")
divide_button.pack(fill = tk.X)
#equals_button = tk.Button(master = button_frame, text = "=", command = lambda: equals_method(total, curentVal))

top_frame.pack(side = tk.TOP)
button_frame.pack(side = tk.RIGHT)

reg = main_window.register(entry_input_callback)
user_entry.config(validate = "key", validatecommand = (reg, '%P'))


main_window.mainloop()

