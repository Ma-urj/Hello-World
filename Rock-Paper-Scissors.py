import random
print('''
Let's play a game of Rock Paper Scissors!
The rules are simple:
    Type either rock, paper or scissors(make sure the spelling is as given)
    The console will select one of the three at the same time.
    See if you win!
    (Rock beats Scissors, Scissors beats Paper and Paper beats Rock)
    ''')
list1 = ['rock','paper','scissors']
Status = True
while Status:
    deal = random.choice(list1)
    throw = input('Try ').lower().strip()
    if throw == 'rock':
        if deal == 'paper':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Lose')
            Status = False
        if deal == 'scissors':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Win')
            Status = False
    elif throw == 'paper':
        if deal == 'scissors':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Lose')
            Status = False
        if deal == 'rock':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Win')
            Status = False
    elif throw == 'scissors':
        if deal == 'rock':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Lose')
            Status = False
        if deal == 'paper':
            print(f'Console chose {deal.title()}, you chose {throw.title()}.\nYou Win')
            Status = False
    else:
        print(f'Please type your option correctly!(you typed {throw.title()})')