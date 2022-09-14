import tkinter as tk

numberOfButtons = 20

window = tk.Tk()

gattino = tk.PhotoImage(file='./smanettamenti_root/examples/auora.png')

for i in range(numberOfButtons):
    button_i = tk.Button(
        text = "Click me!",
        width = 300,
        height = 200,
        bg = "red",
        fg = "green",
        image=gattino
    )
    button_i.pack()



window.mainloop()