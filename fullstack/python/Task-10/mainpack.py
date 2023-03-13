import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Hola!", bg="yellow", fg="blue")
label_saludo.pack(ipadx=50, ipady=50, expand=True)

label_adios = tkinter.Label(window, text="Hola!", bg="red", fg="blue")
label_adios.pack(ipadx=50, ipady=50, fill='both')

window.mainloop()