import suma as add
import sys
import math
import pprint

from operaciones import resta # si son varios paquetes se separan por coma, se puede usar *
# en el archivo __init__.py del módulo padre o carpeta contenedora crear la variable __all__ = ['paquete1', 'paquete2'] 
# y en ese arreglo meter los subpaquetes que quiero que se importen cuando ponga *

def main():
    res = add.suma(3, 5)
    print("Resultado:",res)
    pprint.pprint(sys.path)
    print(resta.restar(5, 1))
    pprint.pprint(dir("a")) #así puedo ver qué operaciones puedo ejecutar sobre un objecto, en este caso de tipo string
    pprint.pprint(globals()) # imprime todos los tipos de datos  locals() hace lo mismo para la función local, solo cambia el alcance
                            # puedo cambiar una variable así globals() ['res'] = 4

if __name__ == '__main__':
    main()