
try:
    while True:
        print("Introduce el primero numero para hacer la operacion")
        num1 = float(input())
        print("Introduce el segundo numero para hacer la operacion")
        num2 = float(input())
        print("Selecciona una de las opciones: ")
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.- Salir")
        opcion = int(input())
        match opcion:
            case 1: resultado = num1 + num2
            case 2: resultado = num1 - num2
            case 3: resultado = num1 * num2
            case 4: resultado = num1 / num2
            case 5:
                print("Saliendo... ")
                break
            case _: print("Error opcion invalida")
        print("El resultado de la operacion es",resultado)
except ValueError as e:
    print("Error dato no valido")
except ZeroDivisionError:
    print("Error no se puede dividir por 0")