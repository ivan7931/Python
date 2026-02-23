

precios = {
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera" : 0.85,
    "Naranja" : 0.70
}
print("Introduce una fruta")
fruta = input()
print("Introduce la cantidad de kilos")
kilo = float(input())
if precios.get(fruta) is None:
    print("La fruta no esta disponible")
else:
    precio = precios[fruta]
    precioTotal = float(kilo * precio)
    print(f"El precio total es {precioTotal}")