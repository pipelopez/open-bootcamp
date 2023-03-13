import tkinter
from tkinter import ttk
from tkinter import StringVar

window = tkinter.Tk()

def saludar(event):
    print("Han hecho clic en saludar")


def saludarDobleClick(event):
    print("Han hecho clic en saludar doble")

boton = tkinter.Button(window, text='Haz clic')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDobleClick)

def salir(event):
    print("Adios")
    window.quit()

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)


# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)

# label entry (2, 0)
# label entry (2, 1)
# (0,2) (1,2) Button

#window.columnconfigure(0, weight=1)
#window.columnconfigure(1, weight=3)





window.mainloop()

sys.exit(0) # no se va a ejecutar el código de ahí hacia abajo

#checkbox
def mifuncion():
    print("Clicado")

seleccion = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='Acepto las condiciones', variable=seleccion, command=mifuncion)
checkbox.grid(row=0, column=0)


#radio button
seleccionado = tkinter.StringVar
r1 = ttk.Radiobutton(window, text="Sí", value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text="No", value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text="Quizá", value='3', variable=seleccionado)

r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)
r3.grid(column=0, row=2, padx=5, pady=5)

#listas
lista = ['Windows', 'MacOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
lista_items = StringVar(value=lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)
listbox.grid(column=0, row=0,sticky=tkinter.W )

#Frames
frame = ttk.Frame(window)
label = ttk.Label(frame, text="hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)
frame.grid(column=0, row=0, sticky=tkinter.W)