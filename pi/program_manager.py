#!/usr/bin/python

import RPi.GPIO as GPIO, sys, time

# Configurable values
dev       = "/dev/spidev0.0"
boardWidth=19
boardHeight=13
numPixels = 248
MAX_TIME = 15

# Open SPI device, load image in RGB format and get dimensions:
spidev    = file(dev, "wb")
# R, G, B byte per pixel, plus extra '0' byte at end for latch.

spiBytes = bytearray(numPixels * 3 + 1)

# For testing, solid red
#for pixel in range(numPixels):
#       spiBytes[pixel*3 + 0] = 0
#       spiBytes[pixel*3 + 1] = 255
#       spiBytes[pixel*3 + 2] = 0



def getIndex(x, y):
    """
    The strand starts at the bottom right and snakes up and to the 
    left, like so (assuming width of 4):

      ^  11---10---09---08
      |  04---05---06---07
      y  03---02---01---00
       x --->

     So, y*width will tell us the minimum index it could be.  Since
     the rows alternate ordering, if the row is even, the additional
     offset is width-x-1.
    """
    index = y * boardWidth + 1;
    if (y%2==1):
      index += x
    else:
      index += (boardWidth-x-1)

    return index

def setIndexColor(i, r, g, b):
    spiBytes[i*3 + 0] = r
    spiBytes[i*3 + 1] = g
    spiBytes[i*3 + 2] = b

def setPixelColor(x, y, r, g, b):
    i = getIndex(x, y)
    setIndexColor(i, r, g, b)


def main():
    progs = sys.argv[1:]
    painters = []
    pIndex = 0
    for prog in progs:
        mod = __import__(prog)
        cls = getattr(mod, "UserPainter")
        painters.append(cls())
    for painter in painters:
        painter.setup()

    start = time.time()
    while(1):
        painters[pIndex].draw()
        for x in range(boardWidth-1,-1,-1):
            for y in range(boardHeight):
                color = painters[pIndex].pixelBuffer.getPixel(x,y)
                try:
                    setPixelColor(x, y, color[0], color[1], color[2] )
                except IndexError:
                    setPixelColor(x, y, 0, 0, 0)

        # Display the pixels
        spiBytes[numPixels] = 0 # Make sure latch is set
        spidev.write(spiBytes)
        spidev.flush()
        if time.time() > start + MAX_TIME:
            start = time.time()
            pIndex = (pIndex + 1) % len(painters)


if __name__ == '__main__':
    main()
