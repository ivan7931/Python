try:
    print("Introduce un numero entero y positivo para comprobar si es primo")
    num = int(input())
    primo = True
    if num < 0:
        raise ValueError
    if num <= 1:
        primo = False
    else :
        i = 2
        while i != num:
            if num % i == 0:
                primo = False
            i += 1
    if primo:
        print("El numero",num,"es primo")
    else:
        print("El numero",num,"no es primo")
except ValueError:
    print("Error dato introducido invalido (numero entero y positivo)")