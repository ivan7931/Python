def tabla_multiplicar(numero,hasta = 10):
    tabla = []
    for i in range(1,hasta + 1):
        tabla.append(numero * i)
    return tabla
print(tabla_multiplicar(3))