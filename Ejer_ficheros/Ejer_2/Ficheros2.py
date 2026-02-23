import csv
productos = []
encontrado = False
try:
    with open("productos.csv", "r") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")
        for fila in lector:
            productos.append({
                "producto": fila["producto"],
                "precio" : float(fila["precio"]),
                "stock" : int(fila["stock"])
            })

    print("Introduce el producto que desea comprar: ")
    nombre_producto = input().strip().lower()
    print("Cuantas unidades desea comprar")
    cantidad = int(input())

    for producto in productos:
        if producto.get("producto").lower() == nombre_producto:
            encontrado = True
            if int(producto.get("stock")) < cantidad:
                print("SIN STOCK")
            else:
                precio_total = float(producto.get("precio")) * cantidad
                producto["stock"] = int(producto.get("stock")) - cantidad

    if not encontrado:
        print("Producto NO ENCONTRADO")

    with open("productos.csv", "w", newline="") as archivo:
        campos = ["producto","precio", "stock"]
        escritor = csv.DictWriter(archivo,fieldnames = campos,delimiter=";")
        escritor.writeheader()
        for producto in productos:
            escritor.writerow({
                "producto": producto["producto"],
                "precio": f"{producto["precio"]:.2f}",
                "stock": producto["stock"]
            })

except ValueError:
    print("Dato introducido incorrectamente")