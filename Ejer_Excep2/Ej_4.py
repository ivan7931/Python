try:
    print("Introduce el saldo inicial de la cuenta")
    saldo = float(input())
    if saldo < 0:
        raise ValueError("el saldo inicial no puede ser menor que 0")
    print("Introduce la cantidad a retirar")
    retiro = float(input())
    if retiro < 0:
        raise ValueError("la cantidad a retirar no puede ser menor que 0")
    elif retiro > saldo:
        raise ValueError("no hay suficiente cantidad de dinero para retirar")
    saldo = saldo - retiro
    print("El saldo restante es de:",saldo)
except ValueError as e:
    print("Error",e)