from pico2d import *
import random
import refer_object

class Hole:
    num = 0

    def __init__(self):
        self.Himage = (load_image('Hole1.png'), load_image('Hole2.png'))
        self.x, self. y = 400, 250
        Hole.num = random.randint(0, 1)

    def draw(self):
        i = self.num
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

    l = 0
    def draw(self):
        self.image.draw(400, 250)
        if len(refer_object.monster) != 0:
            self.Door_image.clip_draw(0, 0, 128, 128, 400, 470)
        elif len(refer_object.monster) == 0:
            if Background.l != 0:
                self.Door_image.clip_draw(self.frame * 128, 0, 128, 128, 400, 470)
                Background.l -= 0.01
            elif Background.l == 0:
                self.Door_image.clip_draw(768, 0, 128, 128, 400, 470)

    def update(self):
        self.frame = (self.frame + 0.01) % 7

    def handle_event(self, event):
        pass

    def stage_change(self):
        pass

    def get_bb(self):
        return self.x + 10, self.y + 220, self.x + 10, self.y + 250

    def get_bb4(self):
        if Hole.num == 0:
            return self.x + 210, self.y + 130, self.x + 400, self.y + 250, \
                   self.x - 210, self.y + 130, self.x - 400, self.y + 250, \
                   self.x - 210, self.y - 250, self.x - 400, self.y - 130, \
                   self.x + 210, self.y - 250, self.x + 400, self.y - 130
        if Hole.num == 1:
            return self.x, self.y, self.x + 190, self.y + 120, \
                   self.x, self.y, self.x - 190, self.y + 120, \
                   self.x, self.y, self.x - 190, self.y - 120, \
                   self.x, self.y, self.x + 190, self.y - 120
