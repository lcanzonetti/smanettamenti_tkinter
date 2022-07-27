import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master = frame_a, text="ciao sono il frame A")
label_b = tk.Label(master = frame_b, text="ciao sono il frame B")

frame_a.pack()
frame_b.pack()
label_a.pack()
label_b.pack()

window.mainloop()