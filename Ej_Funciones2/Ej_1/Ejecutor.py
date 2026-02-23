import Calculos
try:

    radio = float(input("Introduce el radio del circulo"))
    lado = float(input("Introduce el lado del cuadrado"))
    altura = float(input("Introduce la altura del triangulo"))

    print("Area del circulo: ", Calculos.areaCirculo(radio))
    print("Area del cuadrado: ", Calculos.areaCuadrado(lado))
    print("Area del triangulo: ", Calculos.areaTriangulo(altura = altura))
except ValueError:
    print("Error, se deben introducir valores numericos correctos")