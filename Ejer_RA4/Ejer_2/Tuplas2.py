
def analizar_texto(texto):
    palabras = texto.split()
    numCarac = 0
    numPalab = 0
    primeraPalabra = palabras[0]
    numPalab = len(palabras)
    for palabra in palabras:
        for letra in palabra:
            numCarac += 1
        numCarac += 1
    lista = (numCarac, numPalab, primeraPalabra)
    return lista

texto = "Hola buenas noches a todos"
lista = analizar_texto(texto)
print(f"Numero total de caracteres: {lista[0]}")
print(f"Numero de palabras: {lista[1]}")
print(f"Primera palabra del texto: {lista[2]}")