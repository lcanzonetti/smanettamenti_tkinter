import tkinter as tk

border_effects = {
    "flat" : tk.FLAT,
    "sunken" : tk.SUNKEN,
    "raised" : tk.RAISED,
    "groove" : tk.GROOVE,
    "ridge" : tk.RIDGE
}

window = tk.Tk()

#for relief_name, relief in border_effects.items():
#    frame = tk.Frame(master = window, relief = relief, borderwidth=5)
#    frame.pack(side=tk.LEFT)
#    label = tk.Label(master = frame, text = relief_name)
#    label.pack()

frame_a = tk.Frame(master = window, relief = "raised", borderwidth = 5)
frame_a.pack()
label_a = tk.Label(master = frame_a, text = "ciao sono il label A e sono raised")
label_a.pack()

frame_b = tk.Frame(master = window, relief = "groove", borderwidth = 5)
frame_b.pack()
label_b = tk.Label(master = frame_b, text = "ciao sono il label B e sono groove")
label_b.pack()

window.mainloop()