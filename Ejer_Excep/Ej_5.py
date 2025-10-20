while True:
    print("1.- Ver perfil")
    print("2.- Editar perfil")
    print("3.- Salir")
    try:
        opcion = int(input("Introduce la opcion del menu 1-3: "))

        match opcion:
            case 1:
                print("Mostrando perfil")
            case 2:
                print("Editando perfil")
            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida, 1,2 o 3")
    except ValueError:
        print("Error, se debe introducir un valor valido")