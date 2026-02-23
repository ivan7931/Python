
print("Introduce tu nombre: ")
nombre = input()
print("Introduce tu edad: ")
edad = input()
print("Introduce tu direccion: ")
direccion = input()
print("Introduce tu telefono: ")
telefono = input()
persona = {"nombre" : nombre, "edad" : edad , "direccion": direccion, "telefono" : telefono}
print(f"{persona["nombre"]} tiene {persona["edad"]} años, vive en {persona["direccion"]} y su numero de telefono es {persona["telefono"]}")