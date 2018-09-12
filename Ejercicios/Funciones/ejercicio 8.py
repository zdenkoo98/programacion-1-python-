def func(a):
    if a%2==0 and a >2:
        print("El numero no es primo")
    elif a%3==0 and a>3:
        print("El numero no es primo")
    elif a%5==0 and a> 5:
        print("EL numero no es primo")
    elif a%7==0 and a>7:
        print("EL numero no es primo")
    elif a%11==0 and a>11:
        print("El numero no es primo")
    elif a%13==0 and a>13:
        print("El numero no es primo")
    else:
        print("El numero es primo")
    return a
a=int(input())
print(func(a))
