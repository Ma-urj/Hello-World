#To calculate pi to nth digit
nume = 22
deno = 7
ans = ""
seclen = len(str(nume//deno))
n = int(input("Enter decimal place to which Pi is to be calculated: "))
while len(ans) < n+1+seclen:
    if "." in ans and nume < 7:
        nume = nume*10
    elif "." not in ans and nume < 7:
        ans = ans + "."
        nume = nume*10
    ans = ans + str(nume//deno)
    nume = nume%deno
print(ans)
