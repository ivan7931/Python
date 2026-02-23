def formatear_nombre(nombre, apellido, orden = "nombre_apellido"):
    if orden == "nombre_apellido" or orden == "apellido_nombre":
        if orden == "nombre_apellido":
            resultado = f"{nombre} {apellido}"

        else:
            resultado = f"{apellido} {nombre}"
        return resultado
    else:
        return None
print(formatear_nombre("pepe","garcia","apellido_nombre"))
print(formatear_nombre("pepe","garcia"))