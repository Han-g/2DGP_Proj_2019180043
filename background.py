from pico2d import *
import random

class Background:
    def __init__(self):
        self.frame = 0
        self.stage = 0
        self.image = load_image('background.png')
        self.H1image = load_image('Hole1.png')
        self.H2image = load_image('Hole2.png')
        self.Door_image = load_image('Door_UP.png')

    def add_event(self, event):
        pass

    def draw(self):
        self.image.draw(400, 250)
        if self.stage == 0:
            self.H1image.draw(400, 250)
        if self.stage == 1:
            self.H2image.draw(400, 250)

        self.Door_image.clip_draw(self.frame * 128, 0, 128, 128, 400, 470)

    def update(self):
        self.frame = (self.frame + 1) % 7
        # delay(0.2)

    def handle_event(self, event):
        pass