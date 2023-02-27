file = open('archivo.txt', 'w')
file.write('Línea 1\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('Línea 2.\n')

file.seek(0)
print(file.read())
file.close()