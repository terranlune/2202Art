from painter import Painter
import sys
import random

class UserPainter(Painter):

    def setup(self):
        self.board = self._initBoard()
        self.counter = 0
        self.doomsdayLimit = 5000
        self.clock = 7
        self._draw()
        
    def _initBoard(self):
        self.lastColor = (0, 0, 0)
        self.onColor = self._getRandomColor()
        self.offColor = (0, 0, 0)
        self.boringMeter = 0
        
        board = []
        for i in range(self.height):
            board.append([self.offColor for x in range(self.width)])
            
        self._setDieHard(board, self._getRandomOffset())
        return board
        
    def _getRandomColor(self):
        prettyColors = [(255, 0, 0),
                        (0, 255, 0),
                        (0, 0, 255),
                        (255, 255, 0),
                        (0, 255, 255),
                        (255, 0, 255)]
        color = prettyColors[random.randint(0, len(prettyColors) - 1)]
        while color == self.lastColor:
            color = prettyColors[random.randint(0, len(prettyColors) - 1)]
        self.lastColor = color
        return color
    
    def _setDebug(self, board, offset):
        offsetX, offsetY = offset
        cells = [(0+offsetY, 0+offsetX)]
        cells = [self._realignCell(cell) for cell in cells]
        for x, y in cells:
            board[y][x] = self.onColor
            
    def _setDieHard(self, board, offset):
        offsetX, offsetY = offset
        cells = [(2+offsetY, 1+offsetX),
                 (2+offsetY, 2+offsetX),
                 (3+offsetY, 2+offsetX),
                 (3+offsetY, 6+offsetX),
                 (3+offsetY, 7+offsetX),
                 (3+offsetY, 8+offsetX),
                 (1+offsetY, 7+offsetX)]
        cells = [self._realignCell(cell) for cell in cells]
        for x, y in cells:
            board[y][x] = self.onColor

    def _realignCell(self, cell):
        y, x = cell
        while x < 0:
            x += self.width
            
        while y < 0:
            y += self.height
            
        while x >= self.width:
            x -= self.width
            
        while y >= self.height:
            y -= self.height
            
        return (x, y)
    
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
        
    def _getRandomOffset(self):
        return (random.randint(0, self.width-1), random.randint(0, self.height-1))
    
    def draw(self):
        if self.counter%self.clock == 0:
            self._updateBoard()
            if self.boringMeter > 30:
                self._setDieHard(self.board, self._getRandomOffset())
                self.boringMeter = 0
                self.onColor = self._getRandomColor()
            self._draw()

        self.counter += 1
        
        if self.counter == self.doomsdayLimit:
            self.board = self._initBoard()
            self.counter = 0
        
    def _draw(self):        
        for x in range(self.width):
            for y in range(self.height):
                self.setPixel(x, y, self.board[y][x][0], self.board[y][x][1], self.board[y][x][2])
