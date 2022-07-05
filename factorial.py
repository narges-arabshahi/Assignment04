number=int(input("Please enter number= "))
factorial=1
array=[]
if number<0:
    print("sorry factorial does not exist for negative number ")
elif number==0:
    print("factorial of 0 is 1")
else:
    while factorial<=number:
        for i in range(1,number+1):
            factorial=i*factorial
            array.append(factorial)
    if number in array:
        print("Yes")
    else:
        print("No")

