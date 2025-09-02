from pymongo import MongoClient
import bcrypt
from getpass import getpass

# Parametros para conectar a la base de datos
uri = ("")
client = MongoClient(uri)
db = client["cipherDB"]
user_col = db["users"]

def login():
    print("--------- INICIO DE SESION ------------")
    user_input = input("Usuario: ")
    password_input = getpass("Contraseña: ")

    usuario_encontrado = user_col.find_one({"usuario": user_input})

    if not usuario_encontrado:
        print("Usuario no encontrado.")
        return False

    if password_input == usuario_encontrado["password"]:
        print(f"Bienvenido {usuario_encontrado['nombre']}!")
        return True
    else:
        print("Contraseña incorrecta!")
        return False
    
if __name__ == "__main__":
    succes = login()
    if succes:
        print("Sesion iniciada correctamente")
    else:
        print("Error en el login")

