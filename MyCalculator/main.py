# Calculator app in a GUI

import tkinter as tk

main_window = tk.Tk()

text = tk.Label(text="My Calculator")
user_input_number = tk.Entry()
user_input_number.pack()

main_window.mainloop()
