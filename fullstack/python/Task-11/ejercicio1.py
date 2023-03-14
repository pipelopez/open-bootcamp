import sqlite3

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE alumnos(id INT, nombre TEXT, apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Juan', 'Lopez')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Lupe', 'Luna')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Maria', 'García')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Francisco', 'Ferrer')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Jorge', 'Oñate')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Clara', 'Méndez')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Monica', 'Naranjo')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Pablo', 'Neruda')")

conn.commit()

cursor.execute("SELECT * FROM alumnos WHERE Nombre = 'Monica'")

filas = cursor.fetchall()

print(filas)

conn.close()