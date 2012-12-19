from painter import Painter
from random import randint, sample

class UserPainter(Painter):

    def initializeImg(self):
        tmpArray = [[0 for col in range(self.width)] for row in range(self.height)]
        return tmpArray

    def emitSnow(self):
        numFlakes = randint(1,2)
        xpix = range(self.width)
        snowPixels = sample(xpix, numFlakes)
        for p in snowPixels:
            self.imgArray[0][p] = 1

    def saveSnow(self):
        tmpArray = self.initializeImg()

        for y in range(1, self.height):
            tmpArray[y] = self.imgArray[y-1]
        tmpArray[0] = [0 for col in range(self.width)]
        
        #Well, this is ugly
        for y in range(self.height):
            for x in range(self.width):
                try:
                    if (self.imgArray[y][x] == 1 and self.imgArray[y+1][x] == 2) or self.imgArray[y][x] == 2:
                        tmpArray[y][x] = 2
                except IndexError:
                    tmpArray[y][x] = 2        
        self.imgArray = tmpArray

    def clearSnow(self):
        if 2 in self.imgArray[1]:
            self.imgArray = self.initializeImg()

    def setup(self):
        self.timer = 0
        self.img = None
        self.imgArray = self.initializeImg()   
          
    def draw(self):
        if self.timer % 15 == 0:
            self.clearSnow()               
            self.emitSnow()
            for x in range(self.width):
                for y in range(self.height):
                    if self.imgArray[y][x] == 1 or self.imgArray[y][x] == 2:
                        self.setPixel(x, y, 255, 255, 255)
                    else:
                        self.setPixel(x, y, 0, 0, 0)
            self.saveSnow()
        self.timer += 1

