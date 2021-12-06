import refer_object
import Framework
from pico2d import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 18


class Weapon:
    def __init__(self):
        self.x, self.y = 600, 250
        self.image = load_image('spear.png')
        self.frame = 0

    def draw(self):
        if refer_object.character.Attack_time():
            # self.image.clip_draw(self.frame * 128, refer_object.character.sight * 128, 128, 128, self.x, self.y)
            pass

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 18
        self.x, self.y = refer_object.character.get_x(), refer_object.character.get_y()

    def get_bb(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35