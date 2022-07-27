import tkinter as tk



window = tk.Tk()

for i in range(7):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(7):
        if abs(j-i)%2 == 0 :
            relieff=tk.SUNKEN
        else :
            relieff=tk.RAISED
        
        frame_ij = tk.Frame(
            master=window,
            relief=relieff,
            borderwidth=1
        )
        frame_ij.grid(row=i, column=j, padx=1, pady=1)
        label = tk.Label(master=frame_ij, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()