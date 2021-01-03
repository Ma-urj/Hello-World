def prime(n):
    div = 0
    for i in range(2,n):
        if n%i == 0:
            div += 1
    if div == 0:
        return n
    else:
        return 0



num = int(input("Please enter integer to be prime factorised: "))
pfactors = []
for i in range(2,num):
    if num%i == 0:
        if prime(i) == i:
            pfactors.append(i)
print(f"The prime factors are {pfactors}")
