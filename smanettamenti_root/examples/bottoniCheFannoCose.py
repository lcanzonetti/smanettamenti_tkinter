import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))
print(PATH)

window = tk.Tk()

gattino = tk.PhotoImage(file = PATH + '/auora.png')

def command():
    showinfo(title = 'Information', message = 'Ciao! Un tasto è stato premuto!')

for i in range(2):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(2):
        relieff = tk.RAISED
        
        frame_ij = ctk.CTkFrame(master = window, corner_radius = 12)
        frame_ij.grid(row=i, column=j, padx=50, pady=50)
        button = ctk.CTkButton(
                                master = frame_ij, 
                                text   = None,
                                corner_radius = 12,
                                # compound = "top",
                                command = lambda: command(),
                                image = gattino
                                )
        button.pack()


window.mainloop()