import sys
import array

class PixelBuffer(object):
    data = None

    def __init__(self, width, height):
        #self.data = bytearray(width*height*3)
        self.data = array.array('i', range(width*height*3))
        self.width = width
        self.height = height
        
    def setPixel(self, x, y, r, g, b):
        i = x + y*self.width
        self.data[i*3 + 0] = r
        self.data[i*3 + 1] = g
        self.data[i*3 + 2] = b
        
    def getPixel(self, x, y):
        # returns tuple (r,g,b)
        i = x + y*self.width
        d = (self.data[i*3], self.data[i*3+1], self.data[i*3+2])
        return (d)


class Painter(object):
    width = 19
    height = 13
    numPixels = width*height
    pixelBuffer = None

    def __init__(self):
        self.pixelBuffer = PixelBuffer(self.width, self.height)

    def setup(self):
        pass

    def draw(self): 
        pass

    def setPixel(self, x, y, r, g, b):
        self.pixelBuffer.setPixel(x,y,r,g,b)
    
    def _getPixelBuffer(self):
        return self.pixelBuffer
