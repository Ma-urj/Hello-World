def factorials(n):
    if n == 1:
        return 1
    elif n <= 0:
        print("Invalid input")
    elif n > 1:
        return n*factorials(n-1)


num = int(input("Enter number whose factorials are required: "))
print(factorials(num))
