try:
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    if num1 == num2:
        print("Ambos numeros son iguales")
    elif num1 > num2:
        print(f"El numero {num1} es mayor que el numero {num2}")
    else:
        print(f"El numero {num2} es mayor que el numero {num1}")
except ValueError:
    print("Error: se debe introducir un valor correcto")