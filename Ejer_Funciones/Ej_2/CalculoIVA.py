def calcular_precio(precio_base, iva = 21):
    try:
        precio_base = float(precio_base)
        iva = float(iva)
    except ValueError:
        return "Error: los valores deben ser numericos"
    precio_final = precio_base + (precio_base * iva / 100)
    return precio_final
print(calcular_precio(100))
print(calcular_precio(100,10))