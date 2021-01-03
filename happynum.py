def sqadd(n,ln):
    nsum = 0
    while ln >= 0:
        nsum += (n//(10**(ln-1)))**2
        n = n%(10**(ln-1))
        ln -= 1
        return nsum
def happy(n):
    condition = True
    i = n
    while condition:
        l = len(str(i))
        i = sqadd(int(i),l)
        if i == 1:
            print(f"{n} is a happy number")
            condition = False


num = int(input("Enter to check if it is happy: "))
happy(num)
