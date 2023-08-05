def primos(x):
    contador=0

    if x<=0:
        print("¡El número introducido debe ser un entero mayor de cero!")
        exit()
    for n in range(2,x):
        if x%n==0:
            contador+=1
            print ("Divisor: ", n)
    
    if contador>0:
        print(f"El número {x} no es primo")
    else:
        print(f"El número {x} es primo")

primos(4)