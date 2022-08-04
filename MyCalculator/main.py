# Calculator app in a GUI

import tkinter as tk

#class calculator:
#   def __init__(self):
#        self.total = 0
#        self.currentVal = 0


def entry_input_callback(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        return False

#adds two integer values
def add_method(value1, value2):
    print(value1)
    print(value2)
    
    sum = value1 + value2
    user_entry.delete(0, tk.END)
    user_entry.insert(0, str(sum))
    
    print(sum)
    return sum

#initialise required settings



main_window = tk.Tk()

#text = tk.Label(text="My Calculator", foreground = "white", background = "black")
#text.pack()

top_frame = tk.Frame()
button_frame = tk.Frame(width = 6)

user_entry = tk.Entry(master = top_frame, bg = "white", fg = "black", justify = "right")
user_entry.pack()
if not user_entry.get() == "":
    currentVal = user_entry.get()
    print(currentVal)

print(currentVal)

label2 = tk.Label(master = button_frame, text = "Base")
label2.pack(fill = tk.X)

print(total)

plus_button = tk.Button(master = button_frame, text = "+", command=lambda: add_method(total, int(currentVal)))
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

