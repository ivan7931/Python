def calcular_descuento(precio_original, descuento = 10):
    try:
        precio_original = float(precio_original)
        descuento = float(descuento)
    except ValueError:
        return "Error, los datos deben ser numeros correctos"
    precio_final = precio_original - precio_original * descuento/100
    return precio_final

print(calcular_descuento(40))