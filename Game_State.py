from pico2d import *
import Game_World
import Framework

from character import Character
from background import Background
from monster import Monster

def enter():
    global character, background, monster
    character = Character()
    background = Background()
    monster = Monster()

    Game_World.add_object(background, 0)
    Game_World.add_object(character, 1)
    Game_World.add_object(monster, 2)

def update():
    for game_object in Game_World.all_objects():
        game_object.update()

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
