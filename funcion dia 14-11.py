x=input()
def es_palindromo(x):
    global p
    p=""
    i=len(x)
    z=''
    i=i-1
    while i>=0:
        z=z+x[i]
        i=i-1
    if z==x:
        print("La palabra",x,"es palindromo")
        p="true"
        return True
    else:
        print("La palabra",x,"no es palindromo")
        p="false"
        return False
print(es_palindromo(x))#funcion1

def palindromo(x):
    if p=="true":
        print("La palabra",x,"ya es palindromo")
    elif p=="false":
        i=len(x)
        z=x
        i=i-2
        while i>=0:
            z=z+x[i]
            i=i-1
        print("La palabra convertida a palindromo es:",z)
palindromo(x)
