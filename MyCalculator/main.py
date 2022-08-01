# Calculator app in a GUI

import tkinter as tk

main_window = tk.Tk()

#text = tk.Label(text="My Calculator", foreground = "white", background = "black")
#text.pack()

top_frame = tk.Frame()
button_frame = tk.Frame(width = 6)

user_entry = tk.Entry(master = top_frame, bg = "white", fg = "black")
user_entry.pack()

label2 = tk.Label(master = button_frame, text = "Base")
label2.pack(fill = tk.X)

plus_button = tk.Button(master = button_frame, text = "+")
plus_button.pack(fill = tk.X)
minus_button = tk.Button(master = button_frame, text = "-")
minus_button.pack(fill = tk.X)
times_button = tk.Button(master = button_frame, text = "X")
times_button.pack(fill = tk.X)
divide_button = tk.Button(master = button_frame, text = "/")
divide_button.pack(fill = tk.X)

top_frame.pack(side = tk.TOP)
button_frame.pack(side = tk.RIGHT)

main_window.mainloop()
