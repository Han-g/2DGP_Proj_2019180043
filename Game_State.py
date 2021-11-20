import random

from pico2d import *
import Game_World
import Framework

from character import Character
from background import Background
from background import Hole
from monster import Monster

def enter():
    global character, background, monster, hole
    character = Character()
    background = Background()
    hole = Hole()
    monster = [Monster() for i in range(random.randint(3, 8))]

    Game_World.add_object(background, 0)
    Game_World.add_object(character, 1)
    Game_World.add_object(hole, 2)
    Game_World.add_objects(monster, 2)

def update():
    for game_object in Game_World.all_objects():
        game_object.update()
        for i in monster:
            i.nearby(near_by(character, i))
    for monsters in monster:
        monsters.nearby(near_by(character, monsters))
        if collide(background, monsters):
            pass
    if fallen(background, character):
        print('falling')
        character.init_coor()
    print(fallen(background, character))

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
            character.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def fallen(a, b):
    left_ru, bottom_ru, right_ru, top_ru,\
    left_lu, bottom_lu, right_lu, top_lu,\
    left_ld, bottom_ld, right_ld, top_ld,\
    left_rd, bottom_rd, right_rd, top_rd = a.get_bb4()

    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_ru > right_b or right_ru < left_b or top_ru < bottom_b or bottom_ru > top_b:
        return False
    elif left_lu > right_b or right_lu < left_b or top_lu < bottom_b or bottom_lu > top_b:
        return False
    elif left_ld > right_b or right_ld < left_b or top_ld < bottom_b or bottom_ld > top_b:
        return False
    elif left_rd > right_b or right_rd < left_b or top_rd < bottom_b or bottom_rd > top_b:
        return False

    return True

def get_coordinate(a):
    x = a.get_x()
    y = a.get_y()
    return x, y

def get_abs(a):
    return a / abs(a)

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

