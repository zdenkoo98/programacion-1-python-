print("Ingrese 3 numeros")
a=int(input())
b=int(input())
c=int(input())
if a > b and a > c:
    a=str(a)
    print(a + " es el mayor numero")
elif b > a and b > c:
    b=str(b)
    print(b + " es el mayor numero")
elif c > a and c > b:
    c=str(c)
    print(c + " es el mayor numero")
