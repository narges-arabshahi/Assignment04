def shatranji(n,m):
    n=int(input("Please enter row: "))
    m=int(input("please enter column: "))
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 ==0:
               print("#",end="")
            else:
               print("*",end="")
        print()
    

shatranji(4,5)