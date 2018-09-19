x=input()
def es_palindromo(x):
    i=len(x)
    z=''
    i=i-1
    while i>=0:
        z=z+x[i]
        print(z)
        i=i-1
    if z==x:
        print('El string x es palindromo')
    else:
        print("El string x no es un palindromo")
es_palindromo(x)
