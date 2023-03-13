import tkinter
from tkinter import ttk
from tkinter import StringVar

ventana = tkinter.Tk()
elemento = StringVar()

label = ttk.Label(text="Selecciona un color")
label.pack()

listbox = tkinter.Listbox(ventana)
for item in ["Rojo", "Blanco", "Negro", "Azul", "Amarillo", "Verde", "Gris", "Púrpura"]: 
    listbox.insert(tkinter.END, item)
    listbox.pack()

ventana.mainloop()