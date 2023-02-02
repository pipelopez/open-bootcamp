def bisiesto(año):
	return print("El año", año, "es bisiesto") if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0) else print("El año", año, "no es bisiesto")

bisiesto(2023)
