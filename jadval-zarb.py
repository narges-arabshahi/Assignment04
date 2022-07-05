def zarb(n,m):
    for i in range(1,n+1):
        print(" ")
        for j in range(1,m+1):
            print(f"{i*j:3}",end="")

n=int(input("please enter n= "))
m=int(input("please enter m= "))
zarb(n,m)
