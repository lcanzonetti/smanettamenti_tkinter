import tkinter as tk

window = tk.Tk()

def handle_keypress(event) :
    print(event.char)

def handle_click(event) :
    print("The button was Clicked!!")

button = tk.Button(text = "Click me!")
button.bind("<Button-1>", handle_click)
button.pack()

window.bind("<Key>", handle_keypress)

window.mainloop()