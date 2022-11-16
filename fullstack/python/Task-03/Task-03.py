peso = float(input('Escribe tu peso en Kg: '))
estatura = float(input('Escribe tu estatura en Mts: '))
imc = round((peso / (estatura ** 2)), 2)
print('Tu indice de masa corporal es: ' + str(imc))

