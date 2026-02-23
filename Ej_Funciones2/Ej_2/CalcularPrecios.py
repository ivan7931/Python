def calcularPrecio(edad, estudiante, precioNormal = 10):
    precioFinal = 0
    if edad < 18 or estudiante:
        precioFinal = float(precioNormal * 0.5)
    else:
        precioFinal = float(precioNormal)
    return precioFinal