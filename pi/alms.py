from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
from random import random

class UserPainter(Painter):
    def setup(self):
        self.red = 255*random()
        self.green = 255*random()
        self.blue = 255*random()
        self.timer = 0

    def draw(self):
        for x in range(self.width):
            xred = ((x+1)*self.red)
            xgreen = ((x+1)*self.green)
            xblue = ((x+1)*self.blue)
            for y in range(self.height):
                 yred = xred*self.timer % 255
                 ygreen = xgreen*self.timer % 255
                 yblue = xblue*self.timer % 255
                 self.setPixel(x, y,
                               yred,
                               ygreen,
                               yblue)
        self.timer += .1
        self.timer %= 10
#        print "x = " + str(x) + " y = " + str(y) + " self.timer = " + str(self.timer)
#        print "   red = " + str(self.red) + " green = " + str(self.green) + " blue = " + str(self.blue)

