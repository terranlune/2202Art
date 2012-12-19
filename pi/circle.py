from painter import Painter,HSVtoRGB
import sys, time, math

class UserPainter(Painter):
    img = None
    duration = 10.0

    def setup(self):
        self.start = time.time()
        self.totalTimeStart = time.time()

    def draw(self):
        if (time.time()>self.start+self.duration):self.start = time.time()
        timePercent = (time.time()-self.start)/self.duration
        totalTime = time.time()-self.totalTimeStart
        index = 0.0
        numPixels = (float)(self.width*self.height)
        for y in range(self.height):
            for x in range(self.width):
                indexPercent = (float)(index/numPixels)

                #h = (indexPercent+timePercent)*360.0
                #if (h > 360 ): h -= 360
                xu = ((float(x) - 9.5)/19.0)
                yu = ((float(y) - 6.5)/13.0)
                dist = math.sqrt(xu*xu+yu*yu)
                val = (1.0+math.cos((dist+(totalTime))*math.pi))/2.0
                h = 0.0
                theta = math.atan(abs(yu/xu))*360.0/(math.pi*2)
                eta = math.atan(abs(xu/yu))*360.0/(math.pi*2)
                #print theta
                if (xu>=0 and yu >=0 ):                
                    h = theta
                if (xu>=0 and yu<0):
                    h = 270 + eta
                    #h = 0
                if (xu<0 and yu<0):
                    h = 180 + theta
                    #h = 0
                if (xu<0 and yu >= 0):
                    h = 90 + eta
                    #h = 0
                #if (h <0.0): h = h*-1.0
                h += timePercent*360.0
                if (h > 360 ): h -= 360
                color = HSVtoRGB(h, 1, val)
                self.setPixel(x, y,
                              color[0],
                              color[1],
                              color[2])
                index += 1

