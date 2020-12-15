from tttboard import TTTboard


def printBoard(board):
    print("   1   2   3\n")
    print("1  " + board.T[0][0] + " | " +
          board.T[0][1] + " | " + board.T[0][2])
    print("   ---------")
    print("2  " + board.T[1][0] + " | " +
          board.T[1][1] + " | " + board.T[1][2])
    print("   ---------")
    print("3  " + board.T[2][0] + " | " +
          board.T[2][1] + " | " + board.T[2][2])
    print("\n")


def getCoordinate(coordinate):
    a = ''
    while a != '1' and a != '2' and a != '3':
        a = input(coordinate + ": ")
        print()
        if a != '1' and a != '2' and a != '3':
            print("Invalid coordinate. Try again...\n")
    return int(a) - 1


def playerTurn(letter, board):
    filled = False
    print(letter + " turn: Insertate coordinates.\n")
    while (filled == False):
        x = getCoordinate('X')
        y = getCoordinate('Y')
        filled = board.fillPosition(letter, x, y)
        if (filled == False):
            print("This position is filled.")


def computersTurn(playerLetter, board):
    computerLetter = ' '
    if (playerLetter == 'X'):
        computerLetter = 'O'
    elif(playerLetter == 'O'):
        computerLetter = 'X'
    else:
        print("Something went wrong")
        exit()
    board.autoFill(computerLetter)


def checkWiner(board, playerLetter):
    computerLetter = ' '
    if (playerLetter == 'X'):
        computerLetter = 'O'
    elif(playerLetter == 'O'):
        computerLetter = 'X'
    else:
        print("Something went wrong")
        exit()
    if(board.checkWin(playerLetter) == True):
        print("You Won, Congrats!!!\n")
        return True
    elif(board.checkWin(computerLetter) == True):
        print("You loose, sorry...\n")
        return True
    elif(board.checkFull() == True):
        print("It's a tie\n")
        return True
    else:
        return False


def play(letter):
    if (letter == 'X'):
        gameBoard = TTTboard()
        printBoard(gameBoard)
        endFlag = checkWiner(gameBoard, letter)
        while(endFlag == False):
            playerTurn(letter, gameBoard)
            endFlag = checkWiner(gameBoard, letter)
            if(endFlag == True):
                printBoard(gameBoard)
                break
            computersTurn(letter, gameBoard)
            endFlag = checkWiner(gameBoard, letter)
            printBoard(gameBoard)
            if(endFlag == True):
                break
    elif (letter == 'O'):
        gameBoard = TTTboard()
        endFlag = checkWiner(gameBoard, letter)
        while(endFlag == False):
            computersTurn(letter, gameBoard)
            endFlag = checkWiner(gameBoard, letter)
            printBoard(gameBoard)
            if(endFlag == True):
                break
            playerTurn(letter, gameBoard)
            endFlag = checkWiner(gameBoard, letter)
            if(endFlag == True):
                printBoard(gameBoard)
                break
    else:
        print("Something went wrong")
        exit()


def getPlayerLetter():
    a = ''
    while a != 'X' and a != 'O':
        a = input("Who dou you want to play as? (x / o): ")
        print()
        if(a == 'x'):
            a = 'X'
        elif (a == 'o'):
            a = 'O'
        elif(a != 'X' and a != 'O'):
            print("Invalid input. Try again...\n")
    return a
    

    
