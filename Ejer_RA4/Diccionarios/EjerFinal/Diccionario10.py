clientes = {}
opcion = 7
while opcion != 6:
    print("Selecciona una opcion:")
    print("1.- Añadir un cliente")
    print("2.- Eliminar un cliente")
    print("3.- Mostrar cliente")
    print("4.- Listar todos los clientes")
    print("5.- Listar clientes preferentes")
    print("6.- Salir")
    opcion = int(input())
    match opcion:
        case 1:
            print("Introduce tu nif")
            nif = input()
            print("Introduce tu nombre")
            nombre = input()
            print("Introduce tu direccion")
            direccion = input()
            print("Introduce tu telefono")
            telefono = int(input())
            print("Introduce tu correo")
            correo = input()
            print("Eres un cliente preferente(1.-Si 2.-No)?")
            res = int(input())
            if res > 3:
                print("Preferente erroneo")
            elif res == 2:
                preferente = False
            else:
                preferente = True
            diccionarioInfo = {
                "nombre":nombre,
                "direccion": direccion,
                "telefono": telefono,
                "correo": correo,
                "preferente": preferente
            }
            clientes[nif] = diccionarioInfo
        case 2:
            print("Introduce el nif del cliente")
            nif = input()
            if clientes.get(nif) is not None:
                clientes.pop(nif)
                print("Cliente eliminado")
            else:
                print("Nif incorrecto")
        case 3:
            print("Introduce el nif del cliente")
            nif = input()
            print(clientes[nif])
        case 4:
            print("Mostrando todos los clientes")
            for cliente in clientes:
                print(f"Nif : {cliente}, nombre : {clientes[cliente].get("nombre")}")
        case 5:
            print("Mostrando clientes preferentes")
            for cliente in clientes:
                if clientes[cliente].get("preferente"):
                    print(f"Nif : {cliente}, nombre : {clientes[cliente].get("nombre")}")
        case 6:
            print("Saliendo...")
        case _:
            print("Opcion ivalida")