def prime(n):
    div = 0
    for i in range(2,n):
        if n%i == 0:
            div += 1
    if div == 0:
        return n
    else:
        return 0


num = int(input("Please enter number after which prime is to be found: "))
condition = True
i = num+1
while condition:
    if prime(i)==i:
        condition = False
        print(f"The next prime is {i}")
    else:
        i+=1
