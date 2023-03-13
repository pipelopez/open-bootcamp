stringPaises = input("Introduce países separados por comas:\n")

paises = stringPaises.split(",")

sinEspacios = map(lambda x: x.strip(), paises)

print(", ".join(sorted(list(set(sinEspacios)))))