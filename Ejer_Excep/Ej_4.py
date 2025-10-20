try:
    clave = input("Introduce la clave: ")

    if clave == "python123":
        print("Contraseña correcta, accediendo...")
    else:
        print("Contraseña incorrecta, acceso denegado")
except ValueError:
    print("Error se debe introducir un valor valido.")