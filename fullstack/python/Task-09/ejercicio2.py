from functools import reduce

lista = list(range(10))

def sumarParesListaNumeros(listNumeros): 
    impares = list(filter((lambda x: x % 2), listNumeros)) 
    print(impares)
    totalImpares = reduce( (lambda x, y: x + y), impares) 
    print(totalImpares)

resultado = sumarParesListaNumeros(lista)