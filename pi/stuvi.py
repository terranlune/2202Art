from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image, ImageDraw, ImageFont

class UserPainter(Painter):
    img = None

    def setup(self):
        font = ImageFont.load_default()
        text = "Hello World!"
        size = font.getsize(text)
        print "size=", size
        size = (size[0], 13)
        self.img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(self.img)
        draw.text((0, 0), text, font=font)
    
        self.img_width = self.img.size[0]
        self.img_height = self.img.size[1]
        self.img_offset = 0
        self.pixels = self.img.load()
        self.timer = 0

    def draw(self):
        for x in range(self.width):
            xm = (x + self.img_offset) % self.img_width
            for y in range(self.img_height):
                self.setPixel(x, y,
                              self.pixels[xm, y][0],
                              self.pixels[xm, y][1],
                              self.pixels[xm, y][2])

        self.timer += 1
        if (self.timer % 10) != 0:
            return

        self.img_offset += 1

        if self.img_offset >= self.img_width:
            self.img_offset = 0
