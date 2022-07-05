def kmm(a,b):
    x=0
    y=0
    z=abs(a*b)+1
    if abs(a)>abs(b):
        x=abs(a)
    else:
        x=abs(b)
    for i in range(x,z):
        if i%a==0 and i%b==0:
            y=i
            break
    return(y)

a=int(input("Please enter a= "))
b=int(input("please enter b= "))
javab=kmm(a,b)
print("kmm= ",javab)

