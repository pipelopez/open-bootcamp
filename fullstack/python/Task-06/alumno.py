class Alumno:
    def crear(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Nota: ",self.nota)

    def isAprobado(self):
        if self.nota < 3:
            print("Reprobado")
        else:
            print("Aprobado")

alumno = Alumno()
alumno.crear("Juan", 4)
alumno.mostrar()
alumno.isAprobado()