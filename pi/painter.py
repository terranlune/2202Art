import sys, math
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
        self.data[i*3 + 0] = min(255, max(0, int(r)))
        self.data[i*3 + 1] = min(255, max(0, int(g)))
        self.data[i*3 + 2] = min(255, max(0, int(b)))
        
    def getPixel(self, x, y):
        # returns tuple (r,g,b)
        i = x + y*self.width
        d = (self.data[i*3], self.data[i*3+1], self.data[i*3+2])
        return (d)

    def clear(self, r, g, b, opacity=1):
        mul = 1 - opacity
        for p in range(self.width * self.height):
            self.data[p * 3 + 0] = min(255, max(0, int(self.data[p * 3 + 0] * mul + r * opacity)))
            self.data[p * 3 + 1] = min(255, max(0, int(self.data[p * 3 + 1] * mul + g * opacity)))
            self.data[p * 3 + 2] = min(255, max(0, int(self.data[p * 3 + 2] * mul + b * opacity)))


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

    def clear(self, r, g, b, opacity=1):
        self.pixelBuffer.clear(r, g, b, opacity)
    
    def _getPixelBuffer(self):
        return self.pixelBuffer

def HSVtoRGB(h, s, v):
    if s == 0:
        r = g = b = v
        return

    h /= 60
    hsv_i = math.floor(h)
    f = h - hsv_i    #factorial part of h

    vs = v*s
    vsf = vs * f

    p = v - vs
    q = v - vsf
    t = v - vs + vsf

    if hsv_i == 0:
        r = v
        g = t
        b = p
    if hsv_i == 1:
        r = q
        g = v
        b = p
    if hsv_i == 2:
        r = p
        g = v
        b = t
    if hsv_i == 3:
        r = p
        g = q
        b = v
    if hsv_i == 4:
        r = t
        g = p
        b = v
    if hsv_i >= 5:
        r = v
        g = p
        b = q

    return (int(r*255), int(g*255), int(b*255))
