def analizar_numeros(numeros):
    pares = 0
    impares = 0
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        suma += numero
    resultado = (pares, impares, suma)
    return resultado

lista = (5,4,3,8,5,9)
resultado = analizar_numeros(lista)
print(f"Hay {resultado[0]} numeros pares")
print(f"Hay {resultado[1]} numeros impares")
print(f"La suma total de los numeros es: {resultado[2]}")