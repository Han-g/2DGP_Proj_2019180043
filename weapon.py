import refer_object
from pico2d import *

class Weapon:
    def __init__(self):
        self.x, self.y = 600, 250
        # self.image = load_image()

    def get_bb(self):
        return self.x - 12, self.y - 12, self.x + 12, self.y + 12