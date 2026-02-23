def multiplicar(*numeros):
    if len(numeros) == 0:
        return None
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def multiplicandoUnaSuma(*numeros, multiplicador):
    suma = 0
    for n in numeros:
        suma += n
    resultado = suma*multiplicador
    return resultado

def contarArgumentos(*args):
    return len(args)