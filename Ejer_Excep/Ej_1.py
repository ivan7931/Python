try:
    edad= int(input("Introduce tu edad: "))
    if edad < 0:
        print("Error la edad debe ser mayor de 0")
    elif edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
except ValueError:
    print("Error: se debe introducir un numero valido")