def bmm(a,b):
    x=y=0
    if a>b:
        x=a
    else:
        x=b
    for i in range(1,x+1):
        if a%i==0 and b%i==0:
            y=i
            print("Khoroji= ",y)
    return(y)

a=int(input("Please enter a= "))
b=int(input("please enter b= "))
javab=bmm(a,b)
print("BMM= ",javab)


