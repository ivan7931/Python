import CalcularPrecios
try:
    edad = int(input("Introduce tu edad: "))
    precio = float(input("Introduce el precio normal de la entrada: "))
    opcion = int(input("Eres estudiante? (1.-Si, 2.-No)"))
    estudiante = False
    if opcion == 1:
        estudiante = True
    elif opcion == 2:
        estudiante = False
    else:
        raise ValueError

    print("El precio final de su entrada es de: ", CalcularPrecios.calcularPrecio(edad, estudiante,precio))
except ValueError:
    print("Error los datos introducidos deben ser correctos")