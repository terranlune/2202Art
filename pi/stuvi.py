from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image, ImageDraw, ImageFont

<<<<<<< HEAD
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
=======
import urllib
import string
import random

def get_quote(symbols):
    data = []
    url = 'http://finance.yahoo.com/d/quotes.csv?s='
    for s in symbols:
        url += s+"+"
    url = url[0:-1]
    url += "&f=sb3b2l1l"
    f = urllib.urlopen(url,proxies = {})
    rows = f.readlines()
    for r in rows:
        values = [x for x in r.split(',')]
        symbol = values[0][1:-1]
        bid = string.atof(values[1])
        ask = string.atof(values[2])
        last = string.atof(values[3])
        data.append([symbol,bid,ask,last,values[4]])
    return data

class UserPainter(Painter):
    img = None
    text = "Hello World!"
    font = ImageFont.truetype("DejaVuSans.ttf", 11)
    #font = ImageFont.load_default()

    def setup(self):
        text = self.text
        self.timer = 0
        self.create_img()
        self.pixels = self.img.load()

    def create_img(self):
        size = self.font.getsize(self.text)
        size = (size[0], self.height)
        self.img = Image.new('RGBA', size, (0, 0, 0, 0))
        self.textdraw = ImageDraw.Draw(self.img)
        self.img_width = self.img.size[0]
        self.img_height = self.img.size[1]
        self.img_offset = 0

    def init_text_img(self):
            for x in range(self.width):
                for y in range(self.height):
                    self.setPixel(x,y, 0,0,0)                    
            text = ""
            offset = 0
            for s in self.q:
                text += "%s: %s  " % (s[0], s[1])
            self.text = text
            self.create_img()
            for s in self.q:
                text = "%s: %s  " % (s[0], s[1])
                size = self.font.getsize(text)                
                color = (random.randint(10,255), random.randint(10,255), random.randint(10,255))
                self.textdraw.text((offset, 0), text, font=self.font, fill=color)
                offset += size[0]
            self.pixels = self.img.load()


    def draw(self):
        if self.timer % 500 == 0:
            self.q = get_quote(["dwa", "aapl", "goog"])
            if self.timer == 0:
                self.init_text_img()

>>>>>>> 3d36aee6caf6ed334d9a20f41b05b539552d57b3
        for x in range(self.width):
            xm = (x + self.img_offset) % self.img_width
            for y in range(self.img_height):
                self.setPixel(x, y,
                              self.pixels[xm, y][0],
                              self.pixels[xm, y][1],
                              self.pixels[xm, y][2])

        self.timer += 1
<<<<<<< HEAD
        if (self.timer % 10) != 0:
            return

=======
                
        if (self.timer % 3) != 0:
            return
        
>>>>>>> 3d36aee6caf6ed334d9a20f41b05b539552d57b3
        self.img_offset += 1

        if self.img_offset >= self.img_width:
            self.img_offset = 0
<<<<<<< HEAD
=======
            self.init_text_img()
>>>>>>> 3d36aee6caf6ed334d9a20f41b05b539552d57b3
