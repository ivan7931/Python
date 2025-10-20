try:
    edad = int(input("Introduzca su edad: "))
    if edad < 0:
        print("Error, la edad debe ser mayor que 0")
    elif edad < 14:
        print("No puedes conducir ningun vehiculo")
    elif edad < 16:
        print("Puede conducir una moto de poca cilindrada")
    elif edad < 18:
        print("Puede conducir una moto de gran cilindrada")
    else :
        print("Puede conducir hasta un coche")
except ValueError:
    print("Error, se debe introducir un valor valido.")