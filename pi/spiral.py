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

        dir = 'RIGHT' #RIGHT,DOWN,LEFT,UP
        x = y = x_min = 0
        y_min = 1
        x_max = self.width - 1
        y_max = self.height - 1

        numPixels = (float)(self.width*self.height)
        for i in range(int(numPixels)):
            indexPercent = (float)(i/numPixels)
            h = (indexPercent+timePercent)*360.0
            if (h > 360 ): h -= 360
            color = HSVtoRGB(h, 1, 1)

            self.setPixel(x, y,
                          color[0],
                          color[1],
                          color[2])

            if dir == 'RIGHT':
                if x + 1 > x_max:
                    dir = 'DOWN'
                    x_max -= 1
                    y += 1
                else:
                    x += 1
            elif dir == 'DOWN':
                if y + 1 > y_max:
                    dir = 'LEFT'
                    y_max -= 1
                    x -= 1
                else:
                    y += 1
            elif dir == 'LEFT':
                if x - 1 < x_min:
                    dir = 'UP'
                    x_min += 1
                    y -= 1
                else:
                    x -= 1
            elif dir == 'UP':
                if y - 1 < y_min:
                    dir = 'RIGHT'
                    y_min += 1
                    x += 1
                else:
                    y -= 1


