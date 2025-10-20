try:
    print("Introduce el valor desde el que hacer la cuenta atras")
    num = int(input())
    if num < 0:
        raise ValueError
    for i in range(num, -1,-1):
        print(i, end=",")
except ValueError:
    print("Error valor incorrecto debe ser un numero entero positivo")