diccionario = {
    'Euro' : '€',
    'Dollar' : '$',
    'Yen' : '¥'
}
print("Escriba una divisa")
divisa = input()
comprobacion = diccionario.get(divisa)
if comprobacion is None:
    print("La divisa no existe en el diccionario")
else:
    print(f"Divisa {divisa} : {diccionario.get(divisa)}")