try:
    numero = int(input("Introduce un numero: "))

    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es inpar")
except ValueError:
    print("Error, se debe introducir un valor valido")