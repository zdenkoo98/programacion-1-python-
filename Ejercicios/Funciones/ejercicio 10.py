def max_de_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
a=int(input())
b=int(input())
c=int(input())
print(max_de_tres(a,b,c))
