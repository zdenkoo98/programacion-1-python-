i=0
v=0
x=0
l=0
c=0
class Numero:
    def __init__(self, valor):
        self.valor=valor
    def convertir(valor):
        global i
        global v
        global x
        global l
        global c
        valor=int(Numero.self.valor)
        if valor>100:
           c=valor/100
           c=int(c)
           valor=valor-c*100
           if valor>50:
               l=valor/50
               l=int(l)
               valor=valor-l*50
           elif valor<50:
                x=valor/10
                x=int(x)
                valor=valor-x*10
                if valor>5:
                    v=valor/5
                    v=int(v)
                    valor=valor-v*5
                elif valor<5:
                    i=valor/1
                    i=int(i)
                    valor=valor-i*1
        elif valor <100 and valor>50:
            l=valor/50
            l=int(l)
            valor=valor-l*50
            if valor<50:
                x=valor/10
                x=int(x)
                valor=valor-x*10
                if valor>5:
                    v=valor/5
                    v=int(v)
                    valor=valor-v*5
                elif valor<5:
                    i=valor/1
                    i=int(i)
                    valor=valor-i*1
    print("C"*c+"L"*l+"X"*x+"V"*v+"I"*i)   
o=int(input())
p1=Numero(o)
p1.convertir()
