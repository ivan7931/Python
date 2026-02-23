def crear_usuario(nombre, email, activo = True):
    if activo:
        resultado = [nombre,email,activo]
    else:
        return None
    return resultado
print(crear_usuario("pepe", "ygjhvdsf"))