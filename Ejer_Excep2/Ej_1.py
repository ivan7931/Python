try:
    num = int(input("Introduce un numero positivo y entero"))
    primo = True
    if num < 0:
        raise ValueError
    elif num <=1:
        print("El numero",num,"no es primo")
        primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                print("El numero",num,"no es primo")
                primo = False
                break
        if primo:
            print("El numero",num,"es primo")
except ValueError:
    print("Error, numero no valido (positivo y entero)")