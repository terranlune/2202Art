from __future__ import division
from painter import Painter
import sys, time
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image

class UserPainter(Painter):
    img = None

    def setup(self):
        self.img = Image.open("movie1.png")
        self.img_offset = 0
        self.pixels = self.img.load()
        self.lastTime = time.time()
        self.frame = 0
        self.img_height = self.img.size[1]

    def draw(self):
        now = time.time()
        if now < self.lastTime + 1/30:
            return
        self.lastTime = now

        for x in range(self.width):
            for y in range(self.height):
                ym = (y + self.frame*self.height) % self.img_height
                self.setPixel(x, y,
                              self.pixels[x, ym][0],
                              self.pixels[x, ym][1],
                              self.pixels[x, ym][2])
        self.frame += 1

