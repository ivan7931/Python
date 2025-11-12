def make_pizza(tamaño, *ing):
    print("Ingredientes para la pizza de ", tamaño, " porciones")
    for i in ing:
        print("-" , i)