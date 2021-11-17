from pico2d import *
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
        # monster.abs_x = (monster.x - character.x) / abs(monster.x - character.x)
        # monster.abs_y = (monster.y - character.y) / abs(monster.y - character.y)
        pass

    def exit(monster):
        pass

    def do(monster):
        if monster.x > 776:
            monster.x = 776
        elif monster.x < 24:
            monster.x = 24
        if monster.y > 468:
            monster.y = 468
        elif monster.y < 21:
            monster.y = 21

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
        self.x, self.y = random.randint(2, 6) * 100, random.randint(1, 2) * 100
        self.current = Move
        self.frame = 0
        self.sight = 0

    def add_evnet(self, event):
        pass

    def update(self):
        self.current.enter(self)
        self.current.do(self)

    def draw(self):
        self.current.draw(self)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self. x + 20, self.y + 20

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def nearby(self, change):
        change_x, change_y = change
        self.x += change_x * 1
        self.y += change_y * 1
