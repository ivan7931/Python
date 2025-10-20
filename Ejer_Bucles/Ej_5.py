try:
    print("Introduce hasta que numero quieres calcular los primos")
    num = int(input())
    if num < 0 :
        raise ValueError
    j = 2
    while j <= num:
        primo = True
        for i in range(2, j):
            if j % i == 0:
                primo = False
                break
        if primo:
            print(j)
        j += 1

except ValueError:
    print("Error se debe introducir un numerop entero y positivo")