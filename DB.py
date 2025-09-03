from pymongo import MongoClient
import bcrypt
from getpass import getpass

# Parametros para conectar a la base de datos
uri = ("")
client = MongoClient(uri)
db = client["cipherDB"]
user_col = db["users"]

def register_user():
    print("--------- REGISTRO DE USUARIO ------------")
    nombre = input("Nombre: ")
    usuario = input("Usuario: ")
    password = getpass("Contraseña: ")
    
    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    nuevo_usuario = {
        "id": user_col.count_documents({}) + 1,
        "nombre": nombre,
        "usuario": usuario,
        "password": hashed_password.decode('utf-8')  # Guardar como string
    }

    user_col.insert_one(nuevo_usuario)
    print("Usuario registrado exitosamente!")

def login():
    print("--------- INICIO DE SESION ------------")
    user_input = input("Usuario: ")
    password_input = getpass("Contraseña: ")

    usuario_encontrado = user_col.find_one({"usuario": user_input})

    if not usuario_encontrado:
        print("Usuario no encontrado.")
        logs(user_input, "login_fail")
        return False

    # Verificar la contraseña usando bcrypt
    hashed = usuario_encontrado["password"].encode('utf-8')

    if bcrypt.checkpw(password_input.encode('utf-8'), hashed):
        print(f"Bienvenido {usuario_encontrado['nombre']}!")
        logs(user_input, "login")
        return True
    else:
        print("Contraseña incorrecta!")
        logs(user_input, "login_fail")
        return False

def logs(usuario, accion, archivo=None):
    from datetime import datetime
    logs_col = db["logs"]
    now = datetime.now()
    log_entry = {
        "id": logs_col.count_documents({}) + 1,
        "usuario": usuario,
        "accion": accion,
        "archivo": archivo if archivo else "",
        "fecha": now.strftime("%Y-%m-%d"),
        "hora": now.strftime("%H:%M:%S")
    }
    logs_col.insert_one(log_entry)