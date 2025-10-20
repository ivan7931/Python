try:
    productos = ["Manzanas", "Peras" , "Platanos"]
    inventario = [0,0,0]
    while True:
        print("Selecciona una opcion del menu: ")
        print("1.- Añadir stock")
        print("2.- Vender productos")
        print("3.- Mostrar inventario")
        print("4.- Salir del programa")
        opcion = int(input())
        match opcion:
            case 1:
                print("Introduce el producto que deseas añadir (manzanas, peras o platanos)")
                producto = input()
                if producto.lower().replace(" ", "") == "manzanas":
                    print("Cuantas manzanas deseas añadir")
                    cantidad = int(input())
                    inventario[0] += cantidad
                elif producto.lower().replace(" ","") == "peras":
                    print("Cuantas peras deseas añadir")
                    cantidad = int(input())
                    inventario[1] += cantidad
                elif producto.lower().replace(" ","") == "platanos":
                    print("Cuantos platanos deseas añadir")
                    cantidad = int(input())
                    inventario[2] += cantidad
                else:
                    raise ValueError("producto invalido (manzanas, peras o platanos)")
            case 2:
                print("Introduce el producto que deseas vender (manzanas, peras o platanos)")
                producto = input()
                if producto.lower().replace(" ", "") == "manzanas":
                    print("Cuantas manzanas deseas vender")
                    cantidad = int(input())
                    if cantidad > inventario[0]:
                        print("no hay suficientes manzanas para vender")
                    else:
                        inventario[0] -= cantidad
                elif producto.lower().replace(" ","") == "peras":
                    print("Cuantas peras deseas vender")
                    cantidad = int(input())
                    if cantidad > inventario[1]:
                        print("no hay suficientes peras para vender")
                    else:
                        inventario[1] -= cantidad
                elif producto.lower().replace(" ","") == "platanos":
                    print("Cuantos platanos deseas vender")
                    cantidad = int(input())
                    if cantidad > inventario[2]:
                        print("No hay suficientes platanos para vender")
                    else:
                        inventario[2] -= cantidad
                else:
                    raise ValueError("producto invalido (manzanas, peras o platanos)")
            case 3:
                for i in range(0,len(productos)):
                    print(productos[i], ":", inventario[i])
            case 4:
                print("Saliendo...")
                break
            case _: raise ValueError("opcion no valida")


except ValueError as e:
    print("Error",e)