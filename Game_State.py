import random

from pico2d import *
import Game_World
import Framework

from character import Character
from background import Background
from background import Hole
from monster import Monster
from weapon import Weapon
import refer_object


def enter():
    global character, background, monster, hole, weapon
    refer_object.character = Character()
    refer_object.background = Background()
    refer_object.hole = Hole()
    refer_object.monster = [Monster() for i in range(random.randint(3, 8))]
    refer_object.weapon = Weapon()

    Game_World.add_object(refer_object.background, 0)
    Game_World.add_object(refer_object.character, 2)
    Game_World.add_object(refer_object.hole, 1)
    Game_World.add_object(refer_object.weapon, 3)
    Game_World.add_objects(refer_object.monster, 2)


def update():
    for game_object in Game_World.all_objects():
        game_object.update()
        for i in refer_object.monster:
            i.nearby(near_by(refer_object.character, i))

    m = []

    for index, monsters in enumerate(refer_object.monster):
        monsters.nearby(near_by(refer_object.character, monsters))
        if refer_object.character.Attack_time() and collide(refer_object.weapon, monsters):
            monsters.collide_gimmick()
        elif collide(refer_object.character, monsters):
            refer_object.character.collide_gimmick()

        if monsters.hp <= 0:
            print('Dead')
            m.append(monsters)

    refer_object.monster = [monsters for monsters in refer_object.monster if monsters not in m]
    for monsters in m:
        Game_World.remove_object(monsters)

    if len(refer_object.monster) == 0:
        refer_object.background.door_open()

    if fallen(refer_object.background, refer_object.character):
        refer_object.character.init_coor()

    if refer_object.character.hp <= 0:
        exit()
        enter()


def exit():
    Game_World.clear()


def pause():
    pass


def draw():
    clear_canvas()
    for game_object in Game_World.all_objects():
        game_object.draw()
    update_canvas()


def resume():
    pass


def handle_event():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                Framework.quit()
        else:
            refer_object.character.handle_event(event)


def collide(a, b):
    return intersect(a.get_bb(), b.get_bb())


def fallen(a, b):
    boxes = a.get_bb4()
    player_bb = b.get_bb()
    length = 4
    for i in range(length):
        box = boxes[(i * length):(i * length) + length]
        if intersect(player_bb, box):
            return True
    return False


def contains(value, min, max):
    return min <= value <= max


def unpack_into_region(box):
    from_X_axis = box[0]
    from_Y_axis = box[1]
    to_X_axis = box[2]
    to_Y_axis = box[3]

    x = min(from_X_axis, to_X_axis)
    y = min(from_Y_axis, to_Y_axis)
    w = max(from_X_axis, to_X_axis) - x
    h = max(from_Y_axis, to_Y_axis) - y

    return x, y, w, h


def intersect(a, b):
    Ax, Ay, Aw, Ah = unpack_into_region(a)
    Bx, By, Bw, Bh = unpack_into_region(b)

    intersect_X = contains(Ax, Bx, Bx + Bw) or contains(Bx, Ax, Ax + Aw)
    intersect_Y = contains(Ay, By, By + Bh) or contains(By, Ay, Ay + Ah)

    return intersect_X and intersect_Y


def get_coordinate(a):
    x = a.get_x()
    y = a.get_y()
    return x, y


def near_by(a, b):
    x1, y1 = get_coordinate(a)
    x2, y2 = get_coordinate(b)
    move_val_x, move_val_y = 0, 0
    if x1 - x2 == 0:
        move_val_x = 1
    elif x1 - x2 < 0:
        move_val_x = -1
    elif x1 - x2 > 0:
        move_val_x = 1
    if y1 - y2 == 0:
        move_val_y = 1
    elif y1 - y2 < 0:
        move_val_y = -1
    elif y1 - y2 > 0:
        move_val_y = 1
    return move_val_x, move_val_y
