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
	self.clear(0,0,0)

    def draw(self):

        self.timer += 1
        if (self.timer % 10) != 1:
            return

# 	self.clear(0,0,0,opacity=.75)
#	self.clear(0,0,0)

	for x in range(self.width):
            for y in range(self.height):
                ym = (y + self.img_offset) % self.img_height
                color = self.pixels[x,ym]
		self.setPixel(x, y,
                              color[0],
                              color[1],
                              color[2])


        self.img_offset += 1

        if self.img_offset >= self.img_height:
            self.img_offset = 0
