def calcularPrecio(precioInicial, descuento = 0):
    precioFinal = precioInicial - (precioInicial * descuento/100)
    return precioFinal
try:
    precioInicial = float(input("Introduce el precio sin descuento del producto: "))
    descuento = int(input("Introduce el descuento que se le va a aplicar: "))
    print("El precio con descuento es: ", calcularPrecio(precioInicial,descuento))
except ValueError:
    print("Error se debe introducir un valor valido, precio(decimal), descuento(entero)")