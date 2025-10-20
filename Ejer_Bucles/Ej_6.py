
notas = [7,4,9,3,6,9,2,5]
contador = 0
total = 0
notaBaja = 10
notaAlta = 0
for nota in notas:
    total += nota
    if nota >= 5:
        contador +=1
    if nota > notaAlta:
        notaAlta = nota
    if nota < notaBaja:
        notaBaja = nota
print("Han aprobado",contador,"alumnos")
print("La media de las notas es",total / len(notas))
print("La nota mas alta es",notaAlta)
print("La nota mas baja es",notaBaja)