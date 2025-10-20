try:
    print("Porfavor introduce el valor de a de una ecuacion cuadratica de la forma ax^2 + bx + c = 0")
    numA = float(input())
    if numA == 0:
        raise ValueError("el valor de a no puede ser 0")
    print("Porfavor introduce el valor de b de una ecuacion cuadratica de la forma ax^2 + bx + c = 0")
    numB = float(input())
    print("Porfavor introduce el valor de c de una ecuacion cuadratica de la forma ax^2 + bx + c = 0")
    numC = int(input())
    discriminante = numB**2 - (4*numA*numC)
    if discriminante < 0:
        raise ValueError("no hay raices reales")
    else:
        sol1 = (-numB + (discriminante**0.5))/(2*numA)
        sol2 = (-numB - (discriminante**0.5))/(2*numA)
        print("Las soluciones de la ecuacion son:",sol1,"y",sol2)
except ValueError as e:
    print("Error dato incorrecto",e)