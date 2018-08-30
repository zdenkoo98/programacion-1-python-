i=0
claveprimera=''
clavesegunda=''
print("Ingrese clavemaestra")
clavemaestra=input()
x=len(clavemaestra)
print(x)
while i < x +1:
   if i % 2 == 0:
      z=clavemaestra[i]
      clavesegunda=clavesegunda + clavemaestra[i]
      i=i+1
   else:  
       z=clavemaestra[i]
       claveprimera=claveprimera + clavemaestra[i]
       i=i+1
print("La clave primera es: " + claveprimera)
print("La clave segunda es: " + clavesegunda)
   