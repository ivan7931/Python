def calcular_estadiosticas(numeros):
    vMin = numeros[0]
    vMax = numeros[0]
    total = 0
    for n in numeros:
        if n < vMin:
            vMin = n
        if n > vMax:
            vMax = n
        total += n
    media = total/len(numeros)
    return vMin, vMax, media

lista = (2,3,7,3)
x,y,z = calcular_estadiosticas(lista)
print("El valor minimo es: " , x)
print("El valor maximo es: ", y)
print("La media es: ", z)