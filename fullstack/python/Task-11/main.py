import sqlite3
import getpass

def main():
    crear_usuario(3, "pepe", "superclave")
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"select id from users where username='{username}' and password='{password}'"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print("DATA: ", data)

    if data == None:
        return False
    else:
        return True


    cursor.close()
    conn.close()

def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"insert into users(id, username, password) values({identificador}, '{usuario}', '{clave}')"
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    print(type(rows))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

