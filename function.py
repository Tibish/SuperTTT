board = []

player1 = 1
player2 = 4
toure = 0
joueur = 0
win = 0

def CreateBoard():
    global board
    for i in range(9):
        board.append([])
        for j in range(3):
            board[i].append([])
            for n in range(3):
                board[i][j].append([i,j,n])

def DetectClick(x,y):
    ligne = 0
    colone = 0
    forme_pos = None
    for n in range(0,900,100):
        if y>=n and y<n+100:
            ligne = int(n/100)
            y = n+50
            for i in range(0,900,100):
                if x>=i and x<i+100:
                    colone = int(i/100)
                    x = i+50
    insert(ligne,colone)
    forme_pos = (x,y)
    return forme_pos

def Toure():
    global toure, joueur
    joueur = player1 if toure % 2 == 0 else player2
    toure += 1

def ResetGame():
    global board, toure, win
    board = [[0,0,0], [0,0,0], [0,0,0]]
    toure = 0
    win = 0

def insert(ligne, colone):
    if ligne<=2:
        if colone<=2:
            print(board[0][ligne][colone])
            board[0][ligne][colone] = 1
        elif colone>2 and colone<=5:
            print(board[1][ligne][colone-3])
            board[1][ligne][colone-3] = 1
        elif colone > 5:
            print(board[2][ligne][colone-6])
            board[2][ligne][colone-6] = 1
    if ligne>2 and ligne<=5:
        l = ligne-3
        if colone<=2:
            print(board[3][l][colone])
            board[3][l][colone] = 1
        elif colone>2 and colone<=5:
            print(board[4][l][colone-3])
            board[4][l][colone-3] = 1
        elif colone > 5:
            print(board[5][l][colone-6])
            board[5][l][colone-6] = 1
    if ligne>5:
        l = ligne-6
        if colone<=2:
            print(board[6][l][colone])
            board[6][l][colone] = 1
        elif colone>2 and colone<=5:
            print(board[7][l][colone-3])
            board[7][l][colone-3] = 1
        elif colone > 5:
            print(board[8][l][colone-6])
            board[8][l][colone-6] = 1

# a faire verif ligne/colone/diagG-D