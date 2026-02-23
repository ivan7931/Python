permitidos = 0
noPermitidos = 0
with open("log.txt","r") as fichero:
    for linea in fichero:
        if "permitido" in linea:
            permitidos += 1
        elif "denegado" in linea:
            noPermitidos += 1
            usuario = linea.split(":")
            with open("denegados.txt", "a") as denegados:
                denegados.write(f"{usuario[0]}\n")
with open("resumen.txt","w") as resumen:
    resumen.write(f"Accesos permitidos: {permitidos}\n")
    resumen.write(f"Accesos denegados: {noPermitidos}")