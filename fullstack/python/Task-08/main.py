numero = 511
texto = "quijote"
otromas = 1.2

#hasta la versión 3.6 de Python
print("El número es %d y el texto es %s y tiene %f" % (numero, texto, otromas))

print("El número es {} y el texto es {} y tiene {}".format(numero, texto, otromas))

#Format es un array y puedo poner en las llaves la posición
print("El número es {1} y el texto es {0} y tiene {2}".format(numero, texto, otromas))

#También podemos poner las variables nombradas
print("El número es {num} y el texto es {txt} y tiene {flt}".format(num=numero, txt=texto, flt=otromas))

#Forma más moderna de hacerlo y lo que va entre las llaves es código python, puedo hacer un llamado de función ahí
print(f'El numero es {numero} y el texto es {texto} y tiene {otromas}')

num = 511
print(str(num)) #str convierte a texto, puedo sobrecargar el __str__ para imprimir correctaemnte un objeto

print(repr(num)) # para desarrollo y depuración, salidas técnicas, y lo puedo sobrecargar

#def __repr__(self):
 #   return f'Potato({self.nombre, {self.precio}})' #la salida será Potato(PotatoName, Valor)

import pprint

pprint.pprint(dir('')) #Me imprime todos los métodos aplicables al tipo dentro del dir, en este caso string
# .title: mayuscula primera inicial de cada palabra
# .upper y .lower
# .count('a') cuenta la cantidad de letras a en el texto
# .isDigit() es número?
# .isalpha() es letra?
# .isalnum() es alfanumerico? si pones signos especiales da false
# .strip quita espacios principio y final
# .lstrip quita espacios izquierdo .rstrip los quita al final.abs
# .split partir texto
# .startwith .endswith

f = open('/etc/passwd', 'r') 
# r: read, a: append, w: write, x: create, t: texto, b: binary, +: adicionar otros 

datos = f.read(100) #lee el archivo hasta la ubicación 100
# .readline(), lee línea a línea, toca usarlo en un loop para leer todo

# .readlines(), crea una lista con todas las líneas del fichero
lineas = f.readlines()

resultado = []
for linea in lineas:
    if linea[0] == '#': # Me salta los comentarios del archivo
        continue

    if linea[0] == '_':
        continue

    partes = linea.split(':')
    print(partes[0]) #imprimir solo  la primera parte
    resultado.append(partes[0])
    print(resultado)

f.close()

print(datos)

f=open('mifichero.txt', 'w')

lines = [
    'una línea\n',
    'dos lineas\n',
    'tres líneas\n'
]

f.write("datos\n")
f.write("datos2\n")
f.writelines(lines)
f.close()

import pickle #Libreria para serializar y deserializar datos 
#pickle.dump(j1, f) donde j1=Juguete("Potato", 10.5) y f= open('filename.bin', 'wb')
#pickle.load(f) donde f = open('filename.bin', 'rb')