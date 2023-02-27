from pickle import *

class Vehiculo:

    def __init__(self, model, size):
        self.model = model
        self.size = size

    def __str__(self):
        return self.model + " " + self.size


v1 = Vehiculo("Wolvo", "Grande")
print(v1)

file = open('vehiculoFile', 'w+b')

dump(v1, file)

file.seek(0)
nuevoVehiculo = load(file)

print(nuevoVehiculo)
file.close()