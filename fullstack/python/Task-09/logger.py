import logging

logging.basicConfig(level=logging.INFO)
logging.info("prueba de info")
logging.warning("Hace calor")


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def miFuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(miFuncion, numeros)
resultado2 = filter(lambda x: x% 2 == 0, numeros)
print(list(resultado))
print("hola")

from functools import reduce
reducing = reduce(lambda a,b: a + b, numeros) #suma todos los valores de la lista

mapping = map(lambda x: x * x, numeros)

zipping =  zip(["Hola", "Lola"], numeros) # [("Hola", 1), ("Lola", 2)] lista de tuplas de valores

listaA = [1 == 1, 2 == 2]
rest = any(listaA) #devuelve true porque se cumple al menos para uno
rest2 = all(listaA) # devuelve true si se cumple para todos

round(5.5) # redondea al valor más próximo, por encima o por debajo.and

min(numeros) #devuelve el mínimo

pow(2, 4) # 2 a la 4 = 16 = 2**4

sorted(numeros, reverse=True, key=lambda x: str(x).startswith(1)) #ordena la lista como queramos

#Pedir datos al usuario
user = input("username: ")

from getpass import getpass
passwd = getpass("Password: ")

print(user, passwd)

int("45") # convierte a número
