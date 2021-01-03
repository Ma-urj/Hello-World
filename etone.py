#Calculates e to the nth precision.
n = 10
p = int(input("Enter precision of e: "))
x = 1
sum = 0
while x <= n:
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    sum = sum + (x/fact)
    x += 1
print('%.*f'%(p, sum))
