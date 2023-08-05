def texto(x):
    diccionario={}
    for a in range(0,len(x)):
        letra=x[a]
        apariciones=x.count(letra)
        diccionario[letra]=apariciones
    return diccionario
palabra=str(input("Introduce una frase: "))
print(texto(palabra))