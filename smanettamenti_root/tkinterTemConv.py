import tkinter as tk

def fahrenheit_to_celsius() :
    fahrenheit = ent_temperaturef.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    ent_temperaturec.delete(0, tk.END)
    ent_temperaturec.insert(0, round(celsius, 2))

def celsius_to_fahrenheit() :
    celsius = ent_temperaturec.get()
    fahrenheit = (9 / 5) * float(celsius) + 32
    ent_temperaturef.delete(0, tk.END)
    ent_temperaturef.insert(0, round(fahrenheit, 2))

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width = False, height = False)

frm_entryf = tk.Frame(master = window)
frm_entryc = tk.Frame(master = window)
ent_temperaturef = tk.Entry(master = frm_entryf, width = 10)
ent_temperaturec = tk.Entry(master = frm_entryc, width = 10)

ent_temperaturef.grid(row = 0, column = 0, sticky = "e")
ent_temperaturec.grid(row = 0, column = 2)

btn_convert_ftoc = tk.Button(
    master = window,
    text = "°F to °C",
    command = fahrenheit_to_celsius
)

btn_convert_ctof = tk.Button(
    master = window,
    text = "°C to °F",
    command = celsius_to_fahrenheit
)

lbl_resultc = tk.Label(master = window, text = "°C")
lbl_resultf = tk.Label(master = window, text = "°F")

frm_entryf.grid(row = 0, column = 0, padx = 5)
frm_entryc.grid(row = 0, column = 4, padx = 5)
btn_convert_ftoc.grid(row = 0, column = 2, padx = 5, pady = 5)
btn_convert_ctof.grid(row = 0, column = 3, padx = 5, pady = 5)
lbl_resultc.grid(row = 0, column = 5, padx = 5)
lbl_resultf.grid(row = 0, column = 1, padx = 5)

window.mainloop()

