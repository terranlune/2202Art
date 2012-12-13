from __future__ import division
from painter import Painter
import sys, time, math
from random import random

class Part(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def getPos(self, t):

        x, y = self.cx, self.cy
        for mag, freq, offset in self.xwaves:
            x += math.sin(t*freq+offset) * mag
        for mag, freq, offset in self.ywaves:
            y += math.cos(t*freq+offset) * mag
        
        return x, y

class UserPainter(Painter):
    img = None

    def setup(self):
        self.parts = []
        R = random
        size = min(self.width, self.height)
        for i in range(30):
            shade = R()
            self.parts.append(
                Part(cx=R() * self.width,
                     cy=R() * self.height,
                     color=(50+shade*200, 0, 50+(1-shade)*200),
                     xwaves=[(R() * size, .5+(R()**1.3)*5, R()*10) for n in range(2)],
                     ywaves=[(R() * size, .5+(R()**1.3)*5, R()*10) for n in range(2)])
                )

        self.start = time.time()
        self.lastFrame = self.start

    def draw(self):
        now = time.time()
        dt = now - self.lastFrame
        t = now - self.start

        self.clear(0, 0, 0, opacity=.008*dt)

        for p in self.parts:
            x, y = p.getPos(t)
            if 0 <= x < self.width and 0 <= y < self.height:
                self.setPixel(int(x), int(y), *p.color)
