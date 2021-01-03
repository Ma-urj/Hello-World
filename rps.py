#Game of Rock Paper Scissors
import random
print("Hello and welcome to a game of rock paper scissors. The rules are simple.\n Your type your option and try to win against COM.")
choices = {"rock":0,"paper":1,"scissors":2}
win_condition = [(0,2),(1,0),(2,1)]
lose_condition = [(0,1),(1,2),(2,0)]
while True:
    choice = input("Rock Paper Scissors(Your option?): ")
    com = random.randint(0,2)
    condition = (choices[choice.lower()],com)
    if condition in win_condition:
        print("You won")
    elif condition in lose_condition:
        print("You lose")
    else:
        print("Tie!")
    regame = input("Would you like to go again?(Y/N): ")
    if regame.upper() == 'Y':
        continue
    elif regame.upper() == 'N':
        break
    else:
        print("I did not understand so I assume you said yes!")
        continue
