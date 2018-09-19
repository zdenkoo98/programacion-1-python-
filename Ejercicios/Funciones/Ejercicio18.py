a=[1,2,3,4,5,6,7,8,9,10]
b=[]
def fun(a,b):
    i=1
    c=len(a)
    b.append(a[0])
    while i<c:
        print(a[i])
        b.append(a[i]+b[i-1])
        i=i+1
    return b
print(fun(a,b))
        
