from pico2d import *

class Background:
    def __init__(self):
        self.frame = 0
        self.image = load_image('background.png')
        self.Himage = load_image('hole.png')
        self.Door_image = load_image('Door_UP.png')

    def draw(self):
        self.image.draw(400, 250)
        self.Himage.draw(704, 60)
        self.Door_image.clip_draw(self.frame * 128, 0, 128, 128, 400, 470)

    def update(self):
        pass