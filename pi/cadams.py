from painter import Painter
import sys
import time
import random

class UserPainter(Painter):
    img = None

    def setup(self):
        self.board = self._initBoard()
        
    def _initBoard(self):
        self.onColor = self._getRandomColor()
        self.offColor = (0, 0, 0)
        self.boringMeter = 0
        
        board = []
        for i in range(self.height):
            board.append([self.offColor for x in range(self.width)])
            
        self._setDieHard(board)
        return board
        
    def _getRandomColor(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def _setDieHard(self, board):
        board[2][1] = self.onColor
        board[2][2] = self.onColor
        board[3][2] = self.onColor
        
        board[3][6] = self.onColor
        board[3][7] = self.onColor
        board[3][8] = self.onColor
        board[1][7] = self.onColor
        
    def _updateBoard(self):
        cellsToChange = []
        for x in range(self.width):
            for y in range(self.height):
                neighbors = self._countNeighbors(x, y)
                if self.board[y][x] == self.onColor:
                    if neighbors == 2 or neighbors == 3:
                        continue
                    else:
                        cellsToChange.append((x, y, self.offColor))
                else:
                    if neighbors == 3:
                        cellsToChange.append((x, y, self.onColor))
                        
        for x, y, val in cellsToChange:
            self.board[y][x] = val
            
        if 247 - len(cellsToChange) > 242:
            self.boringMeter += 1
        else:
            self.boringMeter = 0
                    
    def _countNeighbors(self, x, y):
        count = 0
        cellsToCheck = [(x+1, y),
                        (x-1, y),
                        (x, y+1),
                        (x, y-1),
                        (x+1, y-1),
                        (x+1, y+1),
                        (x-1, y-1),
                        (x-1, y+1)]
        for x, y in cellsToCheck:
            if x < 0:
                x = self.width - 1
            elif x == self.width:
                x = 0
            if y < 0:
                y = self.height - 1
            elif y == self.height:
                y = 0
                
            if self.board[y][x] != self.offColor:
                count += 1
                
        return count
        
    def draw(self):
        self._updateBoard()        
        for x in range(self.width):
            for y in range(self.height):
                self.setPixel(x, y, self.board[y][x][0], self.board[y][x][1], self.board[y][x][2])
                
        if self.boringMeter > 10:
            self._setDieHard(self.board)
            self.boringMeter = 0
            self.onColor = self._getRandomColor()
            
        time.sleep(.1)

        
    
