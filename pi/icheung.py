from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image

class UserPainter(Painter):
    img = None

    def setup(self):
        self.img = Image.open("pacman2.png")
        self.img_width = self.img.size[0]
        self.img_height = self.img.size[1]
        self.img_offset = -13 # start with the right most edge of img entering
        self.pixels = self.img.load()
        self.timer = 0

    def draw(self):
        for x in range(self.width): # 19
            for y in range(self.height): # 13
                # modified x, starts at xm = 13
                # offset : -13, -12
                # xm     :  13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,
                xm = (x - self.img_offset)
                if xm < 0:
                    xm = 0
                if xm > 18:
                    xm = 0
                
                self.setPixel(x, y,
                              self.pixels[xm, y][0],
                              self.pixels[xm, y][1],
                              self.pixels[xm, y][2])

                # white dots
                if x==4 and xm>7:
                    self.setPixel(4,6,255,255,255)
                if x==8 and xm>7:
                    self.setPixel(8,6,255,255,255)
                if x==12 and xm>7:
                    self.setPixel(12,6,255,255,255)
                if x==16 and xm>7:
                    self.setPixel(16,6,255,255,255)

        self.timer += 1
        if (self.timer % 10) != 0:
            return

        self.img_offset += 1

        if self.img_offset >= self.img_width: # when offset is leftmost edge, reseti
            self.img_offset = -13
        

