import random

try:
    print("Trata de adivinar un numero entre 1 y 100")
    numero = random.randint(1,100)
    print(numero)
    while True:
        print("Introduce el numero")
        num = int(input())
        if num < 1 or num > 100:
            raise ValueError
        elif num < numero:
            print("El numero a adivinar es mayor")
        elif num > numero:
            print("El numero a adivinar es menor")
        else:
            print("Acertaste el numero era",numero,"!!!")
            break
except ValueError:
    print("Error dato invalido (numero entre 1 y 100)")