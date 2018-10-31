print("Menu: ")
print("1)")
print("2)")
print("3)")
print("4)")
print("5)")
print("6)")
while 1==1:
    a=int(input())
    while a==1 or a==2 or a==3 or a==4 or a==5 or a==6:
        if a==1:
            print("Se ejecuto el programa1")
            break
        elif a==2:
            print("Se ejecuto el programa2")
            break
        elif a==3:
            print("Se ejecuto el programa3")
            break
        elif a==4:
            print("Se ejecuto el programa4")
            break
        elif a==5:
            print("Se ejecuto el programa 1, 3 y 4")
            break
        elif a==6:
            print("Se cerro el programa")
            break
    else:
        print("Error, ingrese un valor correcto")
        break
