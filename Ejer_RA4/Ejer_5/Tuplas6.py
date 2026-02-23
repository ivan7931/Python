def procesar_cadena(cadena):
    cadenaMay = cadena.upper()
    cadenaMin = cadena.lower()
    long = len(cadena)
    lista = (cadenaMay, cadenaMin, long)
    return lista

cadena = "hola buenas"
resultado = procesar_cadena(cadena)
print(f"La cadena en mayusculas es: {resultado[0]}")
print(f"La cadena en minusculas es: {resultado[1]}")
print(f"La longitud de la cadena es: {resultado[2]}")