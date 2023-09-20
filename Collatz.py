suma=0
print("ingrese 11 valores\n")
for i in range(11):
    x= int(input())
    if(x>0):
        suma=suma+x
    else: print("este dato no se cuenta")
promedio=suma/11
z=int(promedio)
print("su promedio es ",z)
if (x<258):
    print("Su secuencia de Collatz es" )
    while(z!=1):
        if(z%2==0):
            z=z/2
            w=int(z)
            print(w)
        else:
            z=(z*3)+1
            w=int(z)
            print(w)
else:
    print("no se puede realizar su secuencia de Collatz" )
