
row = [[],[],[]]
row2 = [[],[],[]]
row3 = [[],[],[]]
board = [row, row2, row3]

def getColumn(n):
    column = []
    for i in board:

        column.append(i[n-1])
    return column

def getDiagonal(n):
    diagonal = []
    if n == 0:
        for i in range(3):
            diagonal.append(board[i][i])
    if n == 1:
        for i in range(1, 4):
            diagonal.append(board[-i][-i])
    return diagonal

def printBoard():
    for i in board:
        print(i)

def makeMoveX(x, y):
    print(x, y)
    if board[y-1][x-1] == []:
       board[y-1][x-1] = ["X"]

def makeMoveO(x,y):
    if board[y-1][x-1] == []:
        board[y-1][x-1] = ["O"]

def ifAll(lst, value):
    all([n == value for n in lst])

def checkWin():
    for i in board:
        if ifAll(i, ["X"]):
            return "X wins"
        elif ifAll(i, ["O"]):
            return "O wins"
    for j in range(1,4):
        if  ifAll(getColumn(j), ["X"]):
            return "X wins"
        elif ifAll(getColumn(j), ["O"]):
            return "O wins"
    for k in range(0,2):
        if ifAll(getDiagonal(k), ["X"]):
            return "X wins"
        if ifAll(getDiagonal(k), ["O"]):
            return "O wins"

def playGame():
    turnNumber = 0
    while (checkWin() == None):
        print("Turn Number: " + str(turnNumber))
        play = input()
        if not (int(play[0]) > 0 or int(play[0]) < 4 or int(play[1]) > 0 or int(play[1]) < 4) or len(play)!= 2 or (not play.isdecimal()):
            print("You entered an invalid value")
            continue
        if turnNumber % 2 == 0:
            makeMoveX(int(play[0]), int(play[1]))
            turnNumber += 1
            printBoard()
            print(checkWin())
        elif turnNumber % 2 == 1:
            makeMoveO(int(play[0]), int(play[1]))
            turnNumber += 1
            printBoard()
            print(checkWin())
    else:
        print(checkWin())

playGame()
