import tkinter as tk

window = tk.Tk()

button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg = "red",
    fg = "green"
)

button.pack()

window.mainloop()