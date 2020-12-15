class TTTboard:
    def __init__(self):
        self.T = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __checkEmpty__(self, x, y):
        if (self.T[x][y] == ' '):
            return True
        else:
            return False

    def fillPosition(self, letter, x, y):
        if (letter != 'X' and letter != 'O'):
            print("Something went wrong")
            exit()
        if self.__checkEmpty__(x, y):
            self.T[x][y] = letter
            return True
        else:
            return False

    def checkFull(self):
        for i in range(3):
            for j in range(3):
                if(self.T[i][j] == ' '):
                    return False
        return True

    def checkWin(self, letter):
        for i in range(3):
            if(self.T[i][0] == self.T[i][1] and self.T[i][1] == self.T[i][2] and self.T[i][0] == letter):
                return True
            elif(self.T[0][i] == self.T[1][i] and self.T[1][i] == self.T[2][i] and self.T[0][i] == letter):
                return True
            elif(self.T[0][0] == self.T[1][1] and self.T[1][1] == self.T[2][2] and self.T[0][0] == letter):
                return True
            elif(self.T[0][2] == self.T[1][1] and self.T[1][1] == self.T[2][0] and self.T[0][2] == letter):
                return True
        return False

    def autoFill(self, letter):
        oposite = ' '
        if (letter == 'X'):
            oposite = 'O'
        elif(letter == 'O'):
            oposite = 'X'
        else:
            print("Something went wrong")
            exit()
        for i in range(3):
            for j in range(3):
                if(self.fillPosition(letter, i, j) == True):
                    if(self.checkWin(letter) == True):
                        return True
                    else:
                        self.T[i][j] = ' '
                else:
                    continue
        for i in range(3):
            for j in range(3):
                if(self.fillPosition(oposite, i, j) == True):
                    if(self.checkWin(oposite) == True):
                        self.T[i][j] = letter
                        return True
                    else:
                        self.T[i][j] = ' '
                else:
                    continue
        if(self.fillPosition(letter, 1, 1) == True):
            return True
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                if(self.fillPosition(letter, i, j) == True):
                    return True
                else:
                    continue
        
        if(self.fillPosition(letter, 0, 1) == True):
            return True
        elif(self.fillPosition(letter, 1, 0) == True):
            return True
        elif(self.fillPosition(letter, 1, 2) == True):
            return True
        
        elif(self.fillPosition(letter, 2, 1) == True):
            return True
        else:
            return False
