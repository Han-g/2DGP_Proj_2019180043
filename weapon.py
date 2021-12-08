import refer_object
import Framework
from pico2d import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 18


class Weapon:
    def __init__(self):
        self.x, self.y = 600, 250
        self.spear_image = load_image('spear.png')
        self.sword_image = load_image('s_sword.png')
        self.frame = 0

    def draw(self):
        if refer_object.character.Attack_time():
            if refer_object.character.att_state == 0:
                if refer_object.character.sight == 0:
                    self.sword_image.clip_draw(int(refer_object.character.frame_att) * 128, 3 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 1:
                    self.sword_image.clip_draw(int(refer_object.character.frame_att) * 128, 0 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 2:
                    self.sword_image.clip_draw(int(refer_object.character.frame_att) * 128, 1 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 3:
                    self.sword_image.clip_draw(int(refer_object.character.frame_att) * 128, 2 * 128, 128, 128, self.x, self.y)

            elif refer_object.character.att_state == 1:
                if refer_object.character.sight == 0:
                    self.spear_image.clip_draw(int(refer_object.character.frame_att) * 128, 3 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 1:
                    self.spear_image.clip_draw(int(refer_object.character.frame_att) * 128, 0 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 2:
                    self.spear_image.clip_draw(int(refer_object.character.frame_att) * 128, 1 * 128, 128, 128, self.x, self.y)
                elif refer_object.character.sight == 3:
                    self.spear_image.clip_draw(int(refer_object.character.frame_att) * 128, 2 * 128, 128, 128, self.x, self.y)

    def update(self):
        self.frame = (int(self.frame) + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 18
        self.x, self.y = (refer_object.character.get_x()), refer_object.character.get_y()

    def get_bb(self):
        if refer_object.character.sight == 0: w = (-30, -30, 30, 0)
        elif refer_object.character.sight == 1: w = (-30, 0, 30, 30)
        elif refer_object.character.sight == 2: w = (0, -30, 30, 30)
        elif refer_object.character.sight == 3: w = (-30, -30, 0, 30)
        return self.x + w[0], self.y + w[1], self.x + w[2], self.y + w[3]