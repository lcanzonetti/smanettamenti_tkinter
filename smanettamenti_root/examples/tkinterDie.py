import tkinter as tk
from random import randrange

def roll() :
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{randrange(6) + 1}"

window = tk.Tk()

window.rowconfigure([0, 1], minsize = 50, weight = 1)
window.columnconfigure(0, minsize = 50, weight = 1)



btn_roll = tk.Button(master = window, text = "Roll!", command = roll)
btn_roll.grid(row = 1, column = 0, sticky = "nsew")

lbl_value = tk.Label(master = window, text = "0")
lbl_value.grid(row = 0, column = 0, sticky = "nsew")

window.mainloop()