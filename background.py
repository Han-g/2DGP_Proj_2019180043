from pico2d import *
import random

class Hole:
    def __init__(self):
        self.Himage = (load_image('Hole1.png'), load_image('Hole2.png'))
        self.x, self. y = 400, 250

    def draw(self):
        # i = random.randint(0, 1)
        i = 0
        self.Himage[i].draw(400, 250)

    def update(self):
        pass


class Background:
    def __init__(self):
        self.frame = 0
        self.stage = 0
        self.x, self.y = 400, 250
        self.image = load_image('background.png')

        self.Door_image = load_image('Door_UP.png')

    def add_event(self, event):
        pass

    def draw(self):
        self.image.draw(400, 250)
        self.Door_image.clip_draw(self.frame * 128, 0, 128, 128, 400, 470)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 7
        # delay(0.2)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x + 210, self.y + 130, self.x + 400, self.y + 250

    def get_bb4(self):
        return self.x + 210, self.y + 130, self.x + 400, self.y + 250, \
               self.x - 210, self.y + 130, self.x - 400, self.y + 250, \
               self.x - 210, self.y - 250, self.x - 400, self.y - 130, \
               self.x + 210, self.y - 250, self.x + 400, self.y - 130
