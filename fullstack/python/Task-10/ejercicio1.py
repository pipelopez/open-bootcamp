import tkinter
from tkinter import ttk
from tkinter import StringVar

def seleccionar():
    etiquetaEscogido.config(text="{}".format(seleccion.get()))

def resetear():
    seleccion.set(None)
    etiquetaEscogido.config(text="")

window = tkinter.Tk()
seleccion = StringVar()
seleccion.set(None)

ttk.Radiobutton(window, text="Blanco", variable=seleccion, value='Blanco', command=seleccionar).pack()
ttk.Radiobutton(window, text="Negro", variable=seleccion, value='Negro', command=seleccionar).pack()
ttk.Radiobutton(window, text="Azul", variable=seleccion, value='Azul', command=seleccionar).pack()
ttk.Radiobutton(window, text="Rojo", variable=seleccion, value='Rojo', command=seleccionar).pack()

etiquetaEscogido = ttk.Label(window)
etiquetaEscogido.pack()
ttk.Button(window, text="Reiniciar", command=resetear).pack()

window.mainloop()