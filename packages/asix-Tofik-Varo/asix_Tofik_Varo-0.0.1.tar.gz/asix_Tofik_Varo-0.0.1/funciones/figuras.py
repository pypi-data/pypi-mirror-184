from cmath import pi

def areas(x):
    while x in ["a", "b", "c", "d", "e", "f"]:
            
        if x=="a":
            cuadrado=float (input("Introduce la base/altura: "))
            print(f"{cuadrado**2}")
            break
        elif x=="b":
            rectanguloa=float (input("Introduce la altura: "))
            rectangulob=float (input("Introduce la base: "))
            print(f"{rectanguloa*rectangulob}")
            break

        elif x=="c":
            trapecioa= int (input("Introduce la altura: "))
            trapeciob1= int (input("Introduce la base 1: "))
            trapeciob2= int (input("Introduce la base 2: "))
            print(f"{((trapeciob1+trapeciob2)*trapecioa)/2}")
            break
        
        elif x=="d":
            trianguloa= int (input("Introduce la altura: "))
            triangulob= int (input("Introduce la base: "))
            print(f"{(trianguloa*triangulob)/2}")
            break
        
        elif x=="e":
            circulo= int (input("Escribe el radio: "))
            print(f"{pi*(circulo**2)}")
            break
        
        elif x=="f":
            romboidea=float (input("Introduce la altura: "))
            romboideb=float (input("Introduce la base: "))
            print(f"{romboidea*romboideb}")
            break
        
        else:
            print ("Elige una opción válida")
            exit()


print ("Elige una x geométrica: ")
print ("a. Cuadrado")
print ("b. Rectángulo")
print ("c. Trapecio")
print ("d. Triángulo")
print ("e. Círculo")
print ("f. Romboide")
figura=input("Que figura quieres calcular: ")

areas(figura)