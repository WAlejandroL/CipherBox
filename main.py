from DB import register_user, login
    
if __name__ == "__main__":
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    opcion = input("Seleccione una opcion (1 o 2): ")
    if opcion == '1':
        register_user()
    elif opcion == '2':
        succes = login()
        if succes:
            print("Sesion iniciada correctamente")
        else:
            print("Error en el login")

