import time

date = time.localtime()

hora = date.tm_hour
minutos = date.tm_min

if int(hora) >= 19:
    print("Hora de irte a casa")
else:
    print("Aún faltan {} horas {} minutos para irte".format(18 - int(hora), 59 - int(minutos)))