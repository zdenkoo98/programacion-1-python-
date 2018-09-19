lista1=["manzana","pera","banana","naranja"]
lista2=["tomate","sandia","durazno","banana"]
def superposicion(lista1, lista2):
    i=0
    for x in lista1:
        for z in lista2:
            if z==x:
                print(x + z)
                i=i+1
                continue
            else:
                print(x + z)
                continue
    if i>0:
        return True
    else:
        return False
print(superposicion(lista1, lista2))
