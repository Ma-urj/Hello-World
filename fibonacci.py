def sfib(n):
    counter = 0
    if n<0:
        print("Invalid Input")
    f1 = 0
    f2 = 1
    result = "0 "
    while counter != n-1:
        f3 = f1+f2
        f1 = f2
        f2 = f3
        counter+=1
        result = result+str(f3)+" "
    print(result)


def rfib(n):
    if n<0:
        print("Incorrect Input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return rfib(n-1)+rfib(n-2)

number = int(input("Please enter place to which the sequence is to be calculated: "))
choice = input("Do you want sequence(S) or final result(R)? ")
if choice.lower() == "s":
    sfib(number)
elif choice.lower() == "r":
    print(rfib(number))
else:
    print("Please pick a valid option")
