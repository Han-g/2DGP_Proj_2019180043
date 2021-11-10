from pico2d import *
import Game_World

from character import Character
from background import Background
from monster import Monster

def enter():
    global character, background, monster
    character = Character()
    background = Background()
    monster = Monster()

    Game_World.add_object(character, 0)
    Game_World.add_object(background, 1)
    Game_World.add_object(monster, 2)

def exit():
    Game_World.clear()


