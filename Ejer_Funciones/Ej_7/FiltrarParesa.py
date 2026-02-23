def filtar_pares(numeros):
    pares = []
    for n in numeros:
        if n % 2 != 0:
            pares.append(n)
    return pares
numeros = [1,2,3,4,5,6,7,8,9]
print(filtar_pares(numeros))