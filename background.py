from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.Himage = load_image('hole.png')

    def draw(self):
        self.image.draw(400, 250)
        self.Himage.draw(704, 60)