from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image

# Resolution 19x13 SMPTE color bars
color_bars = {}
for row in range(9):
    color_bars[0, row] = [204, 204, 204]
    color_bars[1, row] = [204, 204, 204]
    color_bars[2, row] = [255, 255, 0]
    color_bars[3, row] = [255, 255, 0]
    color_bars[4, row] = [255, 255, 0]
    color_bars[5, row] = [0, 255, 255]
    color_bars[6, row] = [0, 255, 255]
    color_bars[7, row] = [0, 255, 255]
    color_bars[8, row] = [0, 255, 0]
    color_bars[9, row] = [0, 255, 0]
    color_bars[10, row] = [0, 255, 0]
    color_bars[11, row] = [255, 0, 255]
    color_bars[12, row] = [255, 0, 255]
    color_bars[13, row] = [255, 0, 255]
    color_bars[14, row] = [255, 0, 0]
    color_bars[15, row] = [255, 0, 0]
    color_bars[16, row] = [255, 0, 0]
    color_bars[17, row] = [0, 0, 255]
    color_bars[18, row] = [0, 0, 255]
for row in range(9, 10):
    color_bars[0, row] = [0, 0, 255]
    color_bars[1, row] = [0, 0, 255]
    color_bars[2, row] = [19, 19, 19]
    color_bars[3, row] = [19, 19, 19]
    color_bars[4, row] = [19, 19, 19]
    color_bars[5, row] = [255, 0, 255]
    color_bars[6, row] = [255, 0, 255]
    color_bars[7, row] = [255, 0, 255]
    color_bars[8, row] = [19, 19, 19]
    color_bars[9, row] = [19, 19, 19]
    color_bars[10, row] = [19, 19, 19]
    color_bars[11, row] = [0, 255, 255]
    color_bars[12, row] = [0, 255, 255]
    color_bars[13, row] = [0, 255, 255]
    color_bars[14, row] = [19, 19, 19]
    color_bars[15, row] = [19, 19, 19]
    color_bars[16, row] = [19, 19, 19]
    color_bars[17, row] = [204, 204, 204]
    color_bars[18, row] = [204, 204, 204]
for row in range(10, 13):
    color_bars[0, row] = [8, 62, 89]
    color_bars[1, row] = [8, 62, 89]
    color_bars[2, row] = [8, 62, 89]
    color_bars[3, row] = [255, 255, 255]
    color_bars[4, row] = [255, 255, 255]
    color_bars[5, row] = [255, 255, 255]
    color_bars[6, row] = [58, 0, 127]
    color_bars[7, row] = [58, 0, 127]
    color_bars[8, row] = [58, 0, 127]
    color_bars[9, row] = [19, 19, 19]
    color_bars[10, row] = [19, 19, 19]
    color_bars[11, row] = [19, 19, 19]
    color_bars[12, row] = [19, 19, 19]
    color_bars[13, row] = [19, 19, 19]
    color_bars[14, row] = [0, 0, 0]
    color_bars[15, row] = [19, 19, 19]
    color_bars[16, row] = [38, 38, 38]
    color_bars[17, row] = [19, 19, 19]
    color_bars[18, row] = [19, 19, 19]


class UserPainter(Painter):
    img = None

    def setup(self):
        self.pixels = color_bars

    def draw(self):
        for x in range(19):
            for y in range(13):
                self.setPixel(x, y,
                              self.pixels[x, y][0],
                              self.pixels[x, y][1],
                              self.pixels[x, y][2])
