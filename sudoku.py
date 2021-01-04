#Program to Solve Sudoku
#Display
def Display(set):
    for i in set:
        if i == set[0]:
            print("-"*19)
        rec = ""
        rec = "|" + "|".join(map(str,i)) + "|"
        print(rec)
        if i == set[-1]:
            print("-"*19)
        if i == set[2]:
            print("-"*19)
        if i == set[5]:
            print("-"*19)
#Checking Row
def RowCheck(set,row,blocked):
    for i in range(1,10):
        if i not in blocked and i in set[row]:
            blocked.append(i)
    return blocked
#Checking Column
def ColumnCheck(set,column,blocked):
    for i in range(1,10):
        for j in range(0,9):
            if i not in blocked and i == set[j][column]:
                blocked.append(i)
    return blocked
#Parameter Set
def Parameter(column,row):
    if column >= 0 and column < 3:
        if row >= 0 and row < 3:
            return [[0,3],[0,3]]
        elif row >= 3 and row < 6:
            return [[0,3],[3,6]]
        elif row >= 6 and row < 9:
            return [[0,3],[6,9]]
    elif column >= 3 and column < 6:
        if row >= 0 and row < 3:
            return [[3,6],[0,3]]
        elif row >= 3 and row < 6:
            return [[3,6],[3,6]]
        elif row >= 6 and row < 9:
            return [[3,6],[6,9]]
    elif column >= 6 and column < 9:
        if row >= 0 and row < 3:
            return [[6,9],[0,3]]
        elif row >= 3 and row < 6:
            return [[6,9],[3,6]]
        elif row >= 6 and row < 9:
            return [[6,9],[6,9]]
#Block Check
def BlockCheck(set,column,row,blocked):
    param = Parameter(column,row)
    columnparam = param[0]
    rowparam = param[1]
    for k in range(1,10):
        for i in range(rowparam[0],rowparam[1]):
            for j in range(columnparam[0],columnparam[1]):
                if k not in blocked and k==set[i][j]:
                    blocked.append(k)
    return blocked
#Setting in per block
def PerBlock(set):
    for i in range(0,9):
        for j in range(0,9):
            if set[i][j] == 0:
                possible = []
                blocked = []
                blocked = RowCheck(set,i,blocked)
                blocked = ColumnCheck(set,j,blocked)
                blocked = BlockCheck(set,j,i,blocked)
                for k in range(1,10):
                    if k not in blocked:
                        possible.append(k)
                if len(possible) == 1:
                    set[i][j] = possible[0]
    return set
#Getting Sudoku from User
def GetSudoku():
    infoset = [[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27],[28,29,30,31,32,33,34,35,36],[37,38,39,40,41,42,43,44,45],[46,47,48,49,50,51,52,53,54],[55,56,57,58,59,60,61,62,63],[64,65,66,67,68,69,70,71,72],[73,74,75,76,77,78,79,80,81]]
    print("Please Enter prompts as the given order:")
    Display(infoset)
    set = [[],[],[],[],[],[],[],[],[]]
    n=1
    for i in range(0,9):
        for j in range(0,9):
            element = int(input(f"Enter {n}:"))
            set[i].append(element)
            n+=1
    return set
#Function to Solve the Sudoku
def Solver(choice):
    if choice:
        set1 = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]
    else:
        set1 = GetSudoku()
    set2 = set1
    print("Original")
    Display(set1)
    Unfinished = True
    while Unfinished:
        set2 = PerBlock(set2)
        n = 0
        for i in set2:
            if 0 in i:
                n+=1
        if n == 0:
            Unfinished = False
    print("Solved")
    Display(set2)
#Function to debug the checking functions
def FunctionTest():
    blockt = [[0,2,3,4,5,6,7,8,9],[4,5,6],[7,8,9],[2],[3],[5],[6],[8],[9]]
    print("Original")
    Display(blockt)
    possible = []
    blocked = []
    blocked = ColumnCheck(blockt,0,blocked)
    blocked = RowCheck(blockt,0,blocked)
    blocked = BlockCheck(blockt,0,0,blocked)
    for i in range(1,10):
        if i not in blocked:
            possible.append(i)
    if len(possible) == 1:
        blockt[0][0] = possible[0]
    print("Solved")
    Display(blockt)
    print(possible)
    print(blocked)

#Main Program
choiceTF = True
while choiceTF:
    choice = input("Do you want to input your own Sudoku?(Y/N):")
    if choice.upper() == "Y":
        choiceTF = False
        n = False
    elif choice.upper() == "N":
        n = True
        choiceTF = False
    else:
        print("Please enter a valid choice")

Solver(n)
