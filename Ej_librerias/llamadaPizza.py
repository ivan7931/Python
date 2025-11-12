import libreriaPizza as lib

tam = int(input("Introduce el numero de porciones de la pizza"))
ingredientes = input("Introduce los ingredientes de la pizza separados unicamente por espacios ").split()

lib.make_pizza(tam, *ingredientes)