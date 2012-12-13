from painter import Painter,HSVtoRGB
import sys, time

class UserPainter(Painter):
    img = None
    duration = 10.0

    def setup(self):
        self.start = time.time()

    def draw(self):
        if (time.time()>self.start+self.duration):self.start = time.time()
        timePercent = (time.time()-self.start)/self.duration
        index = 0.0
        numPixels = (float)(self.width*self.height)
        for y in range(self.height):
            for x in range(self.width):
                indexPercent = (float)(index/numPixels)

                h = (indexPercent+timePercent)*360.0
                if (h > 360 ): h -= 360

                color = HSVtoRGB(h, 1, 1)
                self.setPixel(x, y,
                              color[0],
                              color[1],
                              color[2])
                index += 1

