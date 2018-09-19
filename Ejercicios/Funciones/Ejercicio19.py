a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=input()
def elimina(a,b):
    a.pop(0)
    a.pop()
    b=a
    return b
if c==1:
    print(elimina(a,b))
    print(a)
def media(a,b):
    i=1
    c=len(a)
    for i in range(c):
        b.append(a[i])
        i=i+1
    return b
print(media(a,b))
print(a)
