def suma(*args):
	resultado = 0
	
	for arg in args:
		resultado =+ arg
		
	print(resultado)
	
suma(1,4) 


def sumar(**kwargs):
	print(kwargs)
	
	if 'coche' not in kwargs:
		return
		
	if kwargs['coche'] == 'rojo':
		print("es bonito")
	
	vivienda = kwargs['vivienda'] if 'vivienda' in kwargs and kwargs['vivienda'] == 'piso' else 'otro'
	print(vivienda)
	
sumar(vivienda="piso", coche="rojo")

anonima = lambda nombre, nombre2: print("Hola mundo anónimo,", nombre, "adiós", nombre2 )

anonima("Lupe", "Lola")
