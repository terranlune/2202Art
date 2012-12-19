from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image

class UserPainter(Painter):
    img = None

    def setup(self):
        self.img = Image.open("all_sprites_flat.png")
        self.img_width = self.img.size[0]
        self.img_height = self.img.size[1]
        self.img_offset = 0
        self.pixels = self.img.load()
        self.timer = 0

    def draw(self):        
        for x in range(self.width):
            for y in range(self.height):
                ym = (y + self.img_offset) % self.img_height
                self.setPixel(x, y,
                              self.pixels[x, ym][0],
                              self.pixels[x, ym][1],
                              self.pixels[x, ym][2])

        self.timer += 1
        if (self.timer % 10) != 0:
            return

        self.img_offset += 1

        if self.img_offset >= self.img_height:
            self.img_offset = 0
