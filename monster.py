from pico2d import *
import random
import Framework
import refer_object
import math

PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KMPH = 10
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8


class Move:
    def enter(monster):
        monster.Mnumber = len(refer_object.monster)
        monster.otherMonsters = [m for m in refer_object.monster if m != monster]

    def exit(monster):
        pass

    def do(monster):
        monster.frame = (monster.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 8

        new_x = monster.x + monster.velocity_x * Framework.frame_time
        new_y = monster.y + monster.velocity_y * Framework.frame_time

        for other in monster.otherMonsters:
            diff_x = other.x - monster.x
            diff_y = other.y - monster.y
            distance = math.sqrt(diff_x ** 2 + diff_y ** 2)
            if distance < 20:
                other.x += diff_x / 5
                other.y += diff_y / 5
                monster.velocity_x /= 2
                monster.velocity_y /= 2


        monster.x = clamp(25, new_x, 775)
        monster.y = clamp(20, new_y, 470)

    def draw(monster):
        if monster.Mkind == 0:
            monster.M1image.clip_draw(int(monster.frame) * 36, 0, 36, 60, monster.x, monster.y)
        elif monster.Mkind == 1:
            monster.M2image.clip_draw(int(monster.frame) * 48, 0, 48, 48, monster.x, monster.y)
        elif monster.Mkind == 2:
            monster.M3image.clip_draw(int(monster.frame) * 48, 0, 48, 48, monster.x, monster.y)


class Attack:
    def enter(monster):
        pass

    def exit(monster):
        pass

    def do(monster):
        pass

    def draw(monster):
        pass


class Clear:
    def draw(monster):
        pass


class Monster:
    def __init__(self):
        self.M1image = load_image('M1_Move.png')
        self.M2image = load_image('M2_Move.png')
        self.M3image = load_image('M3_Move.png')
        self.x, self.y = self.START_VAL()
        self.Mnumber = 0
        self.Mkind = random.randint(0, 2)
        self.current = Move
        self.hp = 100
        self.timer = random.randint(2, 4)
        self.Time = 500
        self.frame = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.sight = 0
        self.otherMonsters = []

    def add_evnet(self, event):
        pass

    def update(self):
        self.current.enter(self)
        self.current.do(self)

    def draw(self):
        self.current.draw(self)

    def clear(self):
        pass

    def handle_event(self, event):
        pass

    def collide_gimmick(self):
        Framework.timer += Framework.frame_time
        print(Framework.timer)
        if Framework.timer > 0.5:
            self.hp -= 10
            if self.x - refer_object.character.x > 0:
                self.x += 3
            elif self.x - refer_object.character.x < 0:
                self.x -= 3
            if self.y - refer_object.character.y > 0:
                self.y += 3
            elif self.y - refer_object.character.y < 0:
                self.y -= 3

    def count_num_monster(self):
        return self.Mnumber

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def START_VAL(self):
        if refer_object.hole.num == 0:
            return random.randint(1, 2) * 100, random.randint(2, 3) * 100
        elif refer_object.hole.num == 1:
            return random.randint(3, 6) * 100, random.choice((1, 4)) * 100

    def nearby(self, change):
        change_x, change_y = change
        if self.timer <= 0:
            self.velocity_x = change_x * (30 * random.randint(1, 50) / 30)
            self.velocity_y = change_y * (30 * random.randint(1, 50) / 30)
            self.timer = random.randint(100, 130)
        else:
            self.timer -= 1
