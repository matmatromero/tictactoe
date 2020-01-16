board  =    ["-", "-", "-",
            "-", "-","-",
            "-","-","-"]

gameOngoing = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()
    
    while gameOngoing:
        handle_turn(current_player)
        
        
        gameOver()
        
        #change turn. check if game has ended
        flipPlayer()

    #ending the game
    if winner == "X" or winner == "O":
        print(winner + " wins the game!")
    elif winner == None:
        print("Tie!")

def handle_turn(player):
    position = input("Choose a position for " + player + " from 1 to 9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position for " + player + " from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid. Please choose again.")

    board[position] = player
    display_board()

def gameOver():
    checkWin()
    checkTie()

def checkWin():
    global winner
    #check rows
    rowWinner = checkRows()
    #check columns
    columnWinner = checkColumns()
    #check diagonal
    diagonalWinner = checkDiagonal()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None    
    return

def checkRows():
    global gameOngoing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        gameOngoing = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def checkColumns():
    global gameOngoing
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[4] == board[8] != "-"

    if column_1 or column_2 or column_3:
        gameOngoing = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def checkDiagonal():
    global gameOngoing
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        gameOngoing = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def checkTie():
    global gameOngoing
    if "-" not in board:
        gameOngoing = False
    return

def flipPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()