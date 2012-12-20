from painter import Painter
from noise import perlin
import math

class UserPainter(Painter):

    def setup(self):
        self.z = 1
        self.rNoise = perlin.SimplexNoise()
        self.gNoise = perlin.SimplexNoise()
        self.bNoise = perlin.SimplexNoise()
        self.zNoise = perlin.SimplexNoise()

        self.rNoise.randomize()
        self.gNoise.randomize()
        self.bNoise.randomize()
        self.zNoise.randomize()

        self.timescale = 0.002
        self.scale = 0.02
        self.freq = 24
        

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                z = self.z  # + 1.0 * self.zNoise.noise2(0.04*x, 0.04*y)
                r = math.cos(self.freq * self.rNoise.noise3(self.scale*x, self.scale*y, z)) * 128 + 128
                g = math.cos(self.freq*1.1 * self.rNoise.noise3(self.scale*x, self.scale*y, z)) * 128 + 128
                b = math.cos(self.freq*1.2 * self.rNoise.noise3(self.scale*x, self.scale*y, z)) * 128 + 128

                self.setPixel(x, y, r, g, b)
                
        self.z += self.timescale

