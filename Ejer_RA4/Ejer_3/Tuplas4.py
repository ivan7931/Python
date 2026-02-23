def convertir_temperatura(celsius):
    faren = (celsius * (9/5)) + 32
    kelvin = celsius + 273.15
    lista = (faren, kelvin)
    return lista

celsius = 20
lista = convertir_temperatura(celsius)
print(f"{celsius} grados celsius son {lista[0]} grados farenheit")
print(f"{celsius} grados celsius son {lista[1]} grados kelvin")