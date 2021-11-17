from pico2d import *
from character import Character
import random

PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KMPH = 10
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)


class Stop:
    def enter(monster):
        pass

    def exit(monster):
        pass

    def do(monster):
        pass

    def draw(monster):
        pass


class Move:
    def enter(monster):
        # if (monster.x - character.x) / abs(monster.x - character.x) > 0:
        #     pass
        # else:
        #     pass
        # if (monster.y - character.y) / abs(monster.y - character.y) > 0:
        #     pass
        # else:
        #     pass
        pass

    def exit(monster):
        pass

    def do(monster):
        # if monster.x != character.x:
        #     monster.x += (monster.x - character.x) / abs(monster.x - character.x)
        # if monster.y != character.y:
        #     monster.y += (monster.y - character.y) / abs(monster.y - character.y)
        pass

    def draw(monster):
        monster.M1image.clip_draw(monster.frame * 36, 0, 36, 60, monster.x, monster.y)


class Attack:
    def enter(monster):
        pass

    def exit(monster):
        pass

    def do(monster):
        pass

    def draw(monster):
        pass


class Monster:
    def __init__(self):
        self.M1image = load_image('M1_Move.png')
        self.x, self.y = random.randint(100, 700), random.randint(100, 300)
        self.current = Move
        self.frame = 0
        self.sight = 0

    def add_evnet(self, event):
        pass

    def update(self):
        self.current.do(self)

    def draw(self):
        self.current.draw(self)

    def handle_event(self, event):
        pass
