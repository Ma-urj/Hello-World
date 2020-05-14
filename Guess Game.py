import random
print('''Hello and welcome to the guess game!
The rules are simple:
    The console will select a number from 1-100
    If you guess within a range of 10 numbers on your first try the console will say WARM
    If you guess outside the range then it will say COLD
    From second turn onwards the console will say WARMER or COLDER with respect to your previous guess!
    See how many turns it take for you to get it right!
    Now make your first guess''')
num = random.randint(1, 100)
cnts = 0
Status = True
ar = []
while Status:
    guess = int(input('Your Guess \n'))
    cnts += 1
    if guess != num:
        ar.append(guess)
        if len(ar) == 1:
            if abs(guess - num) <= 10:
                print('WARM')
            else:
                print('COLD')
        else:
            previous = ar[-2]
            if abs(previous - num) > abs(guess - num):
                print('WARMER')
            else:
                print('Colder')
    else:
        print(f'You got it right the number is {num}! You got it right in {cnts} turns!')
        Status = False