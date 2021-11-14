from pico2d import *
import random

class Move:
    pass

class Attack:
    pass

class Monster:
    def __init__(self):
        self.M1image = load_image('M1_Move.png')
        self.x, self.y = random.randint(100, 700), random.randint(100, 300)
        self.sight = 0

    def add_evnet(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.M1image.clip_draw(self.frame * 36, 0, 36, 60, self.x, self.y)

    def handle_event(self, event):
        pass