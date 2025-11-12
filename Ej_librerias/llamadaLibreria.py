import libreria as lib

try:
    print("Opciones de conversión:")
    print("1. Euros → Dólares")
    print("2. Dólares → Euros")
    print("3. Euros → Libras")
    print("4. Libras → Euros")
    print("5. Euros → Yenes")
    print("6. Yenes → Euros")

    opcion = int(input("Elige una opción (1-6): "))

    match opcion:
        case 1:
            cantidad = float(input("Introduce la cantidad en euros: "))
            resultado = lib.eurosDolares(cantidad)
            print(cantidad," de euros son ", resultado, " dolares")
        case 2:
            cantidad = float(input("Introduce la cantidad en dólares: "))
            resultado = lib.dolaresEuros(cantidad)
            print(cantidad," de dolares son ", resultado, " euros")
        case 3:
            cantidad = float(input("Introduce la cantidad en euros: "))
            resultado = lib.eurosLibras(cantidad)
            print(cantidad," de euros son ", resultado, " libras")
        case 4:
            cantidad = float(input("Introduce la cantidad en libras: "))
            resultado = lib.librasEuros(cantidad)
            print(cantidad," de libras son ", resultado, " euros")
        case 5:
            cantidad = float(input("Introduce la cantidad en euros: "))
            resultado = lib.eurosYenes(cantidad)
            print(cantidad," de euros son ", resultado, " yenes")
        case 6:
            cantidad = float(input("Introduce la cantidad en yenes: "))
            resultado = lib.yenesEuros(cantidad)
            print(cantidad," de yenes son ", resultado, " euros")
        case _:print("Opción no válida. Debes elegir 1-6")

except ValueError:
    print("Error: Debes introducir un número válido.")