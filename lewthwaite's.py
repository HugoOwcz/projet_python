
def newBoard(n):
    valeur = 2
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            if i == n//2 and j == n//2:
                board[i].append(0)
            else:
                board[i].append(valeur)
            valeur = valeur % 2 + 1
    return board


def displayBoard(board, n):
    for i in range(n):
        print(" "*(len(str(n))-len(str(i+1))), i+1, " "*len(str(n)), "|", sep="", end=" ")
        for j in range(n):
            if board[i][j] == 1:
                print("x", " "*len(str(n)), end="")
            elif board[i][j] == 2:
                print("o", " "*len(str(n)), end="")
            else:
                print(".", " "*len(str(n)), end="")
        print()
    print(" "*(len(str(n))*2), end="--")
    for i in range(n):
        print("-"*(len(str(n))+2), end="")
    print()
    print(" "*(len(str(n))*2+1), end=" ")
    for i in range(n):
        print(i+1, " "*(len(str(n))-len(str(i))+1), end="")
    print()


def possiblePawn(board, n, player, i, j):
    if type(i) != int and type(j) != int:
        return False
    if board[i][j] != player:
        return False
    else:
        if i > 0:
            if board[i-1][j] == 0:
                return True
        if i < n-1:
            if board[i+1][j] == 0:
                return True
        if j > 0:
            if board[i][j-1] == 0:
                return True
        if j < n-1:
            if board[i][j+1] == 0:
                return True
        return False


def selectPawn(board, n, player):
    i = eval(input("Quel est le numéro de la ligne du pion ?"))
    j = eval(input("Quel est le numéro de la colonne du pion ?"))
    while not possiblePawn(board, n, player, i-1, j-1):
        i = eval(input("Quel est le numéro de la ligne du pion ?"))
        j = eval(input("Quel est le numéro de la colonne du pion ?"))
    return i-1, j-1


def updateBoard(board, n, i, j):
    if i > 0:
        if board[i-1][j] == 0:
            board[i-1][j] = board[i][j]
            board[i][j] = 0
    if i < n-1:
        if board[i+1][j] == 0:
            board[i+1][j] = board[i][j]
            board[i][j] = 0
    if j > 0:
        if board[i][j-1] == 0:
            board[i][j-1] = board[i][j]
            board[i][j] = 0
    if j < n-1:
        if board[i][j+1] == 0:
            board[i][j+1] = board[i][j]
            board[i][j] = 0


def again(board, n, player):
    pos_i = None
    pos_j = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                pos_i = i
                pos_j = j
    if pos_i > 0:
        if board[pos_i-1][pos_j] == player:
            return True
    if pos_j > 0:
        if board[pos_i][pos_j-1] == player:
            return True
    if pos_i < n-1:
        if board[pos_i+1][pos_j] == player:
            return True
    if pos_j < n-1:
        if board[pos_i][pos_j+1] == player:
            return True
    return False


def lewthwaite(n):
    if (n-1) % 4 != 0:
        n = 9
    board = newBoard(n)
    player = 1
    while again(board, n, player):
        displayBoard(board, n)
        co = selectPawn(board, n, player)
        updateBoard(board, n, co[0], co[1])
        if player == 1:
            player = 2
        else:
            player = 1
    displayBoard(board, n)
    if player == 1:
        print("Le joueur 2 a gagné.")
    else:
        print("Le joueur 1 a gagné.")
