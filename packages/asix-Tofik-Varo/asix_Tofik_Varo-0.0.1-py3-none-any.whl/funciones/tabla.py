def tablas(x):        
    print (f"Tabla del {x}")

    print (" ")

    for contador in range (1,11):
        print (x,"*",contador,"=",(x*contador))

numero=int(input("Introduce un número: "))

tablas(numero)