try:
    print("Introduce el primer numero para hacer la operacion: ")
    num1 = float(input())
    print("Introduce el segundo numero para hacer la operacion: ")
    num2 = float(input())
    print("Selecciona una operacion: ")
    print("+")
    print("-")
    print("*")
    print("/")
    operador = input()
    match operador:
        case "+": resultado = num1 + num2
        case "-": resultado = num1 - num2
        case "*": resultado = num1 * num2
        case "/": resultado = num1 / num2
        case _: raise ValueError("operador introducido no valido")
    print("El resultado de la operacion es: ",resultado)

except ValueError as e:
    print("Error",e)
except ZeroDivisionError as e:
    print("Error no se puede dividir entre 0")