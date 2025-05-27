board = []

player1 = 1
player2 = 4
toure = 0
joueur = 0
win = 0
big_pos = None

#---------Creation du tableau correspondant au plateau de jeu----------#

def CreateBoard():
    global board
    for i in range(9):
        board.append([])
        for j in range(3):
            board[i].append([0,0,0])

#---------detection de la position du click et lancement des focntions----------#

def DetectClick(x,y):
    ligne = 0
    colone = 0
    forme_pos = None
    libre = 0
    for n in range(0,900,100):
        if y>=n and y<n+100:
            ligne = int(n/100)
            y = n+50
            for i in range(0,900,100):
                if x>=i and x<i+100:
                    colone = int(i/100)
                    x = i+50
    if VerifLibre(ligne,colone):
        Toure()
        insert(ligne,colone)
        forme_pos = (x,y)
        VerifAll()
        return forme_pos
    else:
        print("awa")

#---------fonction qui lance toutes les fonction de verification----------#

def VerifAll():
    VerifLigne()
    VerifColone()
    VerifDiagG()
    VerifDiagD()

#---------gère le tour de chaque joueur----------#

def Toure():
    global toure, joueur
    joueur = player1 if toure % 2 == 0 else player2
    toure += 1

#---------Reinitialise le Jeu----------#

def ResetGame():
    global board, toure, win
    board = []
    for i in range(9):
        board.append([])
        for j in range(3):
            board[i].append([0,0,0])
    toure = 0
    win = 0

#---------Insertion des positions des jetons dans le tableau----------#

def insert(ligne, colone):
    if ligne<=2:
        if colone<=2:
            if joueur == player1:
                board[0][ligne][colone] = player1
            else:
                board[0][ligne][colone] = player2
        elif colone>2 and colone<=5:
            if joueur == player1:
                board[1][ligne][colone-3] = player1
            else:
                board[1][ligne][colone-3] = player2
        elif colone > 5:
            if joueur == player1:
                board[2][ligne][colone-6] = player1
            else:
                board[2][ligne][colone-6] = player2
    elif ligne>2 and ligne<=5:
        l = ligne-3
        if colone<=2:
            if joueur == player1:
                board[3][l][colone] = player1
            else:
                board[3][l][colone] = player2
        elif colone>2 and colone<=5:
            if joueur == player1:
                board[4][l][colone-3] = player1
            else:
                board[4][l][colone-3] = player2
        elif colone > 5:
            if joueur == player1:
                board[5][l][colone-6] = player1
            else:
                board[5][l][colone-6] = player2
    elif ligne>5:
        l = ligne-6
        if colone<=2:
            if joueur == player1:
                board[6][l][colone] = player1
            else:
                board[6][l][colone] = player2
        elif colone>2 and colone<=5:
            if joueur == player1:
                board[7][l][colone-3] = player1
            else:
                board[7][l][colone-3] = player2
        elif colone > 5:
            if joueur == player1:
                board[8][l][colone-6] = player1
            else:
                board[8][l][colone-6] = player2

#---------Verfication de victoire sur ligne----------#

def VerifLigne():
    global win
    for n in range(9):
        for i in range(3):
            count = 0
            for j in range(3):
                if board[n][i][j] != 0:
                    count += board[n][i][j]
            if count==3:
                print("win player 1")
                win = player1
                board[n]=[]
                for v in range(3):
                    board[n].append([5,5,5])
                ValideCarre(n)
            elif count==12:
                print("win player 2")
                win = player2
                board[n]=[]
                for v in range(3):
                    board[n].append([5,5,5])
                ValideCarre(n)

#---------Verfication de victoire sur colone----------#

def VerifColone():
    global win
    for n in range(9):
        for i in range(3):
            count = 0
            for j in range(3):
                if board[n][j][i] != 0:
                    count += board[n][j][i]
            if count == 3:
                print("win player 1")
                win = player1
                board[n]=[]
                for v in range(3):
                    board[n].append([5,5,5])
                ValideCarre(n)
            elif count == 12:
                print("win player 2")
                win = player2
                board[n]=[]
                for v in range(3):
                    board[n].append([5,5,5])
                ValideCarre(n)

#---------Verfication de victoire sur Diagonal partant de la gauche----------#

def VerifDiagG():
    global win
    for n in range(9):
        count = 0
        for i in range(3):
            if board[n][i][i] != 0:
                count += board[n][i][i]
        if count == 3:
            print("win player 1")
            win = player1
            board[n] = []
            for v in range(3):
                board[n].append([5, 5, 5])
            ValideCarre(n)
        elif count == 12:
            print("win player 2")
            win = player2
            board[n] = []
            for v in range(3):
                board[n].append([5, 5, 5])
            ValideCarre(n)

#---------Verfication de victoire sur Diagonal partant de la droite----------#

def VerifDiagD():
    global win
    for n in range(9):
        count = 0
        j=2
        for i in range(3):
            if board[n][i][j] != 0:
                count += board[n][i][j]
            j -= 1
        if count == 3:
            print("win player 1")
            win = player1
            board[n] = []
            for v in range(3):
                board[n].append([5, 5, 5])
            ValideCarre(n)
        elif count == 12:
            print("win player 2")
            win = player2
            board[n] = []
            for v in range(3):
                board[n].append([5, 5, 5])
            ValideCarre(n)

#---------Verfication de case libre----------#

def VerifLibre(ligne, colone):
    if ligne<=2:
        if colone<=2:
            if board[0][ligne][colone] == 0:
                return True
        elif colone>2 and colone<=5:
            if board[1][ligne][colone-3] == 0:
                return True
        elif colone > 5:
            if board[2][ligne][colone-6] == 0:
                return True
    elif ligne>2 and ligne<=5:
        l = ligne-3
        if colone<=2:
            if board[3][l][colone] == 0:
                return True
        elif colone>2 and colone<=5:
            if board[4][l][colone-3] == 0:
                return True
        elif colone > 5:
            if board[5][l][colone-6] == 0:
                return True
    elif ligne>5:
        l = ligne-6
        if colone<=2:
            if board[6][l][colone] == 0:
                return True
        elif colone>2 and colone<=5:
            if board[7][l][colone-3] == 0:
                return True
        elif colone > 5:
            if board[8][l][colone-6] == 0:
                return True

#---------Valide si un grand carre a etait gagner----------#

def ValideCarre(carre):
    global big_pos
    ligne = None
    if carre<=2:
        ligne = 0
    elif carre>2 and carre<=5:
        ligne = 1
        carre-=3
    elif carre>5:
        ligne = 2
        carre-=6
    x = carre * 300 + 150
    y = ligne * 300 + 150
    big_pos = (x,y)

#verif win sur carre totale
#obligation de positon