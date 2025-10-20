from xml.dom.minidom import ProcessingInstruction

try:
    cantidad = int(input("Introduce la cantidad de euros que cambiar"))
    if cantidad < 0:
        raise ValueError
    print("Seleccione a que divisa desea cambiar los euros: ")
    print("1.-USD")
    print("2.-GBP")
    print("3.-JPY")
    divisa = int(input())
    if divisa != 1 and divisa != 2 and divisa != 3:
        raise ValueError
    else:
        match divisa:
            case 1: print("El valor de",cantidad,"euros es de",cantidad * 1.16,"USD")
            case 2: print("El valor de",cantidad,"euros es de",cantidad * 0.87,"GBP")
            case 3: print("El valor de",cantidad,"euros es de",cantidad * 175.54,"JPY")
            case _: raise ValueError
except ValueError:
    print("Dato introducido incorrecto")