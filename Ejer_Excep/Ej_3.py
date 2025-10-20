try:
    nota = float(input("Introduce la nota entre 0 y 10: "))

    if nota < 0 or nota > 10:
        print("Error, la nota debe estar entre 0 y 10")
    elif nota < 5:
        print("Suspenso")
    elif nota < 7:
        print("Aprobado")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")

except ValueError:
    print("Error: se debe introducir un dato valido")