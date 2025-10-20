try:
    print("Introduce el numero del que deseas saber la tabla de multiplicar")
    num = int(input())
    print("Tabla del",num)
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

except ValueError:
    print("Error, dato invalido")