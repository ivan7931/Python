try:
    print("Introduce la cantidad a invertir:")
    cantidad = float(input())
    print("Introduce el interes anual en %")
    interes = float(input())
    print("Introduce el numero de años")
    annos = int(input())

    for i in range(1,annos + 1):
        cantidad += cantidad * (interes/100)
        print("Año",i,cantidad,"euros")
except ValueError:
    print("Error dato invalido")