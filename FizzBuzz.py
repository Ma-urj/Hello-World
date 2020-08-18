n = int(input("Please enter the value of n,i.e, the place to which numbers are to be printed:"))
for i in range(n):
  if i%3 == 0 and i%5 != 0:
    print("Fizz")
  elif i%3 != 0 and i%5 == 0:
    print("Buzz")
  elif i%3 == 0 and i%5 == 0:
    print("FizzBuzz")
  else:
    print(i)
