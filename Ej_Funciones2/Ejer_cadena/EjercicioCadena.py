print("Introduce una frase: ")

frase = input()
palabras = frase.split()

palabraLarga = palabras[0]
for palabra in palabras:
    if len(palabra) > len(palabraLarga):
        palabraLarga = palabra

fraseNueva = []

for palabra in palabras:
    if len(palabra) % 2 == 1:
        for caracter in palabra:
            palabraInvertida = ""
            for letra in palabra:
                palabraInvertida = letra + palabraInvertida

            fraseNueva.append(palabraInvertida)
            break
    else :
        fraseNueva.append(palabra)
fraseCambiada = " ".join(fraseNueva)

ultimaLetra = frase[-1].lower()
contador = frase.lower().count(ultimaLetra)

print("Frase original: ", frase)
print("Palabra mas larga: ", palabraLarga)
print("Frase transformada: ", fraseCambiada)
print(f"Apariciones de la ultima letra {ultimaLetra} :", contador)