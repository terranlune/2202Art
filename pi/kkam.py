from __future__ import division
from painter import Painter
import sys, time, math
from random import random

class Line(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.start = time.time()
        
    def getRGB(self):
        R = random
        rand = R()
        r = b = 35
        g = 170+rand*85
        if rand > .9:
            r = b = 75
            g = 255
        return (r, g, b)
    
    def getPos(self):
        if self.delay > 0:
            self.delay -= 1;
            return -1, -1
        if self.delay < 0:
	    self.reset(False)
	    self.delay = 0

        now = time.time()
        t = now - self.start
        x, y = self.cx, self.cy
        for mag in self.ymag:
            y += t * mag
                
        return x, y
        
    def reset(self, delay=True):
        R = random
        self.start = time.time()
        self.color = self.getRGB()
        self.ymag = [(R() * self.height+1.5) for n in range(2)]
	if delay:
	    self.delay = R() * 20

class UserPainter(Painter):
    img = None

    def setup(self):
        self.lines = []
        R = random
        for i in range(self.width):
            self.lines.append(
                Line(cx = i,
                     cy = 0,
                     color=(0, 0, 0),
                     delay=R() * 150,
                     height=self.height,
                     ymag=[(R() * self.height+1.5) for n in range(2)])
                )
        self.lastFrame = time.time()

    def draw(self):
        now = time.time()
        dt = now - self.lastFrame
        self.lastFrame = now 
        
        self.clear(0, 0, 0, opacity=4.5*dt)

        for p in self.lines:
            x, y = p.getPos()
            if 0 <= x < self.width and 0 <= y < self.height:
                self.setPixel(int(x), int(y), *p.color)
            else:
		if y >= self.height:
                    p.reset()
