"""Hacer un programa que tenga las siguientes funciones:
.DEC a BIN ---> convierte un nro decimal entero a binario
.BIN a DEC ---> convierte un nro binario a decimal
.BIN a HEX ---> convierte un nro binario a hexadecimal
Dada una IP el programa debe convertir la direccion a binario y a hexadecimal
Dado un nro binario (EJ 00100101) convertirlo a decimal
Permitir al usuario una vez cargado el programa ejecutar las funciones tantas veces como las desee sin salir del programa
"""
def dec_bin(decimal):
    int(decimal)
    x=decimal
    x=int(x)
    while x>=2:
        r=x%2
        r=int(r)
        x=x/2
        print("algo")
        lista.append(r)
    if x<2:
        x=int(x)
        lista.append(x)
        print("algo2")
def DECABIN():
    global lista
    lista=[]
    print("Ingrese un numero entero")
    decimal=input()
    dec_bin(decimal)
    print("algo3")
    lista.reverse()
    print("El numero en binario es: ")
    print(lista)
#DECABIN()

def BINADEC():
    global a
    a=""
    print("Ingrese un numero binario, ingrese fin para finalizar el numero")
    global binario
    binario=[]
    while a!="fin":
        a=input()
        if a=="fin":
            break
        binario.append(a)
    print(binario)
BINADEC()
def bin_dec(binario):
    binario.reverse()
    binario= list(map(int, binario))
    x=0
    z=0
    while x<=len(binario)-1:
        z=z+binario[x]*2**x
        x=x+1
    print("El numero en decimal es:", z)
bin_dec(binario)
    
