import math
def moadele(a,b,c):
    delta=(b**2)-(4*a*c)
    if delta==0:
        x=(-b+math.sqrt(delta))
        print("Moadele yek javab darad X= ",x)
    elif delta<0:
        print("Moadele javab haghighi nadarad")
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("Moadele 2 javab darad \n X1= ",x1,"\nX2= ",x2)


a=int(input("please enter a= "))
b=int(input("please enter b= "))
c=int(input("please enter c= "))
moadele(a,b,c)
