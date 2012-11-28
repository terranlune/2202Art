from painter import Painter
from noise import perlin

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

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                z = self.z + 1.0 * self.zNoise.noise2(0.04*x, 0.04*y)
                r = self.rNoise.noise3(0.02*x, 0.02*y, z) * 128 + 128
                g = self.gNoise.noise3(0.02*x, 0.02*y, z) * 128 + 128
                b = self.bNoise.noise3(0.02*x, 0.02*y, z) * 128 + 128

                self.setPixel(x, y, r, g, b)
                
        self.z += .01

