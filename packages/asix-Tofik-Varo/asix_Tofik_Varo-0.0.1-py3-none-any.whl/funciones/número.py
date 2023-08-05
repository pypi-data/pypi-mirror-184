from random import randint, randrange
def aleatorio(x):
    numero=randrange(0,100)

    if x==numero:
        print("Acertaste el número aleatorio")
    else:
        print("Mala suerte")

aleatorio(10)
