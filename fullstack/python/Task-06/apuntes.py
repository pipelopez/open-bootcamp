class Juguete:
	_encendido = True

	def encendido():
		self._encendido = True

	def apaga():
		self._encendido = False

	def isEncendido(self):
		return self._encendido()


d = Juguete()
d.apaga()
d.encendido()

# La herencia es poniendo entre paréntesis la clase padre, cuando son varios padres se ponen de mejor a mayor separados por coma ','
class Potato(Juguete):

	color = None
	nombre = None

	def __init__(self, nombre):
		#formas de llamar el constructor del padre
		Juguete().__init__(self)  # forma 1 
		super().__init__(self) # forma 2

		self.color = "Verde"
		self.nombre = nombre
		print("Estoy en el constructor", nombre)

	def __del__(self): 
		print("Estoy en el destructor de la clase", self.__class__)

	def quitarOreja():
		pass

	def ponerOreja():
		pass

p = Potato("Mi papa")
p.encendido()
print(p.color)
print(p.nombre)

# Esta es una clase estática
class Estatica:
	numero = 1

	def incrementa():
		Estatica.numero +=1

Estatica.incrementa()
print(Estatica.numero)

#clases abstractas
from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def sonido(self):
		pass

	def diHola():
		print("Hola")

class Perro(Animal):
	def sonido(self):
		print("Guau")

lazy = Perro()

lazy.diHola()
lazy.sonido()

#composición
class Motor:
	tipo = "Diesel"

class Ventanas:
	cantidad = 5

class Carrocería:
	Ventanas = Ventanas()

class Coche:
	motor = Motor()
	carroceria = Carrocería()
