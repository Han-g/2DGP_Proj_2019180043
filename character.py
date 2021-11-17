from pico2d import *
import Framework
import Game_World

PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KMPH = 20
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

UP_ON, UNDER_ON, LEFT_ON, RIGHT_ON, UP_OFF, UNDER_OFF, LEFT_OFF, RIGHT_OFF, ATT_ON, ATT_OFF, \
DFF_ON, DFF_OFF, ROLL_ON, ROLL_OFF = range(14)

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): UP_ON,
    (SDL_KEYDOWN, SDLK_a): LEFT_ON,
    (SDL_KEYDOWN, SDLK_s): UNDER_ON,
    (SDL_KEYDOWN, SDLK_d): RIGHT_ON,
    (SDL_KEYUP, SDLK_w): UP_OFF,
    (SDL_KEYUP, SDLK_a): LEFT_OFF,
    (SDL_KEYUP, SDLK_s): UNDER_OFF,
    (SDL_KEYUP, SDLK_d): RIGHT_OFF,
    (SDL_KEYDOWN, SDLK_j): ATT_ON,
    (SDL_KEYUP, SDLK_j): ATT_OFF,
    (SDL_KEYDOWN, SDLK_k): DFF_ON,
    (SDL_KEYUP, SDLK_k): DFF_OFF,
    (SDL_KEYDOWN, SDLK_SPACE): ROLL_ON,
    (SDL_KEYUP, SDLK_SPACE): ROLL_OFF
}


class Move:
    def enter(character, event):
        if event == RIGHT_OFF or event == LEFT_OFF or event == UP_OFF or event == UNDER_OFF:
            character.velocity = 0

        if event == RIGHT_ON:
            character.velocity += MOVE_SPEED_PPS
            character.sight = 2
        elif event == LEFT_ON:
            character.velocity -= MOVE_SPEED_PPS
            character.sight = 3
        elif event == UP_ON:
            character.velocity += MOVE_SPEED_PPS
            character.sight = 1
        elif event == UNDER_ON:
            character.velocity -= MOVE_SPEED_PPS
            character.sight = 0
        character.velocity = clamp(-100, character.velocity, 100)

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 4

        if character.sight  == 0:
            character.y += character.velocity * Framework.frame_time
        elif character.sight == 1:
            character.y += character.velocity * Framework.frame_time
        elif character.sight == 2:
            character.x += character.velocity * Framework.frame_time
        elif character.sight == 3:
            character.x += character.velocity * Framework.frame_time
        # character.x = clamp(25, character.x, 775)
        # character.y = clamp(20, character.y, 470)
        # print(character.velocity * Framework.frame_time)

        # 맵 벗어나지 않게 하기
        if character.x > 776:
            character.x = 776
        elif character.y > 468:
            character.y = 468
        elif character.x < 24:
            character.x = 24
        elif character.y < 21:
            character.y = 21

    def draw(character):
        if character.velocity != 0:
            character.Mimage.clip_draw((character.sight + int(character.frame) * 4) * 24, 0, 24, 42, character.x, character.y)
        elif character.velocity == 0:
            character.Mimage.clip_draw(character.sight * 24, 0, 24, 42, character.x, character.y)


class Attack:
    def enter(character, event):
        if event == ATT_ON:
            pass

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 8
        delay(0.1)

    def draw(character):
        character.Aimage.clip_draw(int(character.frame) * 31, 0, 31, 42, character.x, character.y)


class Dffense:
    def enter(character, event):
        pass

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 8
        delay(0.1)

    def draw(character):
        if character.sight == 0:
            character.Dimage_D.clip_draw(int(character.frame) * 28, 0, 28, 35, character.x, character.y)
        elif character.sight == 1:
            character.Dimage_U.clip_draw(int(character.frame) * 28, 0, 28, 35, character.x, character.y)
        elif character.sight == 2:
            character.Dimage_R.clip_draw(int(character.frame) * 32, 0, 32, 38, character.x, character.y)
        elif character.sight == 3:
            character.Dimage_L.clip_draw(int(character.frame) * 32, 0, 32, 38, character.x, character.y)


class Roll:
    def enter(character, event):
        pass

    def exit(character, event):
        pass

    def do(character):
        if character.sight  == 0:
            character.y += character.velocity * Framework.frame_time
        elif character.sight == 1:
            character.y += character.velocity * Framework.frame_time
        elif character.sight == 2:
            character.x += character.velocity * Framework.frame_time
        elif character.sight == 3:
            character.x += character.velocity * Framework.frame_time

        if character.x > 776:
            character.x = 776
        elif character.y > 468:
            character.y = 468
        elif character.x < 24:
            character.x = 24
        elif character.y < 21:
            character.y = 21

        character.frame = (character.frame + 1) % 8
        delay(0.1)

    def draw(character):
        if character.sight == 0:
            character.Rimage.clip_draw(int(character.frame) * 29, character.sight * 42, 29, 42, character.x, character.y)
        elif character.sight == 1:
            character.Rimage.clip_draw(int(character.frame) * 28, character.sight * 42, 28, 42, character.x, character.y)
        elif character.sight == 2:
            character.Rimage.clip_draw(int(character.frame) * 35, character.sight * 42, 35, 42, character.x, character.y)
        elif character.sight == 3:
            character.Rimage.clip_draw(int(character.frame) * 35, character.sight * 42, 35, 42, character.x, character.y)


state_table = {
    Move: {RIGHT_ON: Move, LEFT_ON: Move, UP_ON: Move, UNDER_ON: Move, \
           RIGHT_OFF: Move, LEFT_OFF: Move, UP_OFF: Move, UNDER_OFF: Move, \
           ATT_ON: Attack, ROLL_ON: Roll, DFF_ON: Dffense, ATT_OFF: Move, ROLL_OFF: Move, DFF_OFF: Move},
    Attack: {RIGHT_ON: Attack, LEFT_ON: Attack, UP_ON: Attack, UNDER_ON: Attack, \
             RIGHT_OFF: Attack, LEFT_OFF: Attack, UP_OFF: Attack, UNDER_OFF: Attack, \
             ATT_ON: Attack, ROLL_ON: Attack, DFF_ON: Attack, ATT_OFF: Move, ROLL_OFF: Move, DFF_OFF: Move},
    Dffense: {RIGHT_ON: Dffense, LEFT_ON: Dffense, UP_ON: Dffense, UNDER_ON: Dffense, \
              RIGHT_OFF: Dffense, LEFT_OFF: Dffense, UP_OFF: Dffense, UNDER_OFF: Dffense, \
              ATT_ON: Dffense, ROLL_ON: Dffense, DFF_ON: Dffense, ATT_OFF: Dffense, ROLL_OFF: Dffense, DFF_OFF: Move},
    Roll: {RIGHT_ON: Roll, LEFT_ON: Roll, UP_ON: Roll, UNDER_ON: Roll, \
           RIGHT_OFF: Roll, LEFT_OFF: Roll, UP_OFF: Roll, UNDER_OFF: Roll, \
           ATT_ON: Roll, ROLL_ON: Roll, DFF_ON: Roll, ATT_OFF: Move, ROLL_OFF: Move, DFF_OFF: Move}
}


class Character:
    state_temp = 8
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = 0
        self.sight = 0
        self.dir = 1
        self.velocity = 0
        self.current = Move
        self.current.enter(self, None)
        self.event_que = []
        self.Mimage = load_image('charmove2.png')
        self.Aimage = load_image('attack.png')
        self.Rimage = load_image('Roll.png')
        self.Dimage_R = load_image('shield_Right.png')
        self.Dimage_L = load_image('shield_Left.png')
        self.Dimage_U = load_image('shield_Up.png')
        self.Dimage_D = load_image('shield_down.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.current.do(self)
        if self.current == Attack and Character.state_temp > 0:
            Character.state_temp -= 1

        elif self.current == Roll and Character.state_temp > 0:
            Character.state_temp -= 1

        elif len(self.event_que) > 0:
            Character.state_temp = 7
            event = self.event_que.pop()
            self.current.exit(self, event)
            self.current = state_table[self.current][event]
            self.current.enter(self, event)

    def draw(self):
        self.current.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x -12, self.y -12, self.x + 12, self.y + 12

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
