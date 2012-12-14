from painter import Painter
import sys
sys.path.append("/home/mhlee/eval-software/Imaging/lib.linux-x86_64-2.6")
import Image, ImageDraw, ImageFont

import urllib
import string

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
    #font = ImageFont.truetype("Inconsolata.otf", 11)
    font = ImageFont.truetype("DejaVuSans.ttf", 11)
    #font = ImageFont.load_default()

    def setup(self):
        text = self.text
        size = self.font.getsize(text)
        size = (size[0], 13)
        self.img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(self.img)
        draw.text((0, 0), text, font=self.font)
    
        self.img_width = self.img.size[0]
        self.img_height = self.img.size[1]
        self.img_offset = 0
        self.pixels = self.img.load()
        self.timer = 0
        
    def init_text_img(self):
            for x in range(self.width):
                for y in range(self.height):
                    self.setPixel(x,y, 0,0,0)                    
            print self.q
            text = ""
            for s in self.q:
                text += "%s: %s  " % (s[0], s[1])
            self.text = text
            print "TEXT=", self.text
            self.setup()

    def draw(self):
        if self.timer % 500 == 0:
            self.q = get_quote(["dwa", "aapl", "goog"])
            if self.timer == 0:
                self.init_text_img()

        for x in range(self.width):
            xm = (x + self.img_offset) % self.img_width
            for y in range(self.img_height):
                self.setPixel(x, y,
                              self.pixels[xm, y][0],
                              self.pixels[xm, y][1],
                              self.pixels[xm, y][2])

        self.timer += 1
                
        if (self.timer % 5) != 0:
            return
        
        self.img_offset += 1

        if self.img_offset >= self.img_width:
            self.img_offset = 0
            self.init_text_img()
