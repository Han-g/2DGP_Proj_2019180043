from pico2d import *
import Framework
import threading
import refer_object
import Game_World

PIXEL_PER_METER = (10.0 / 0.3)
MOVE_SPEED_KMPH = 20
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8
FRAME_PER_ATTACK = 18

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
        if character.velocity != 0:
            if event == RIGHT_OFF or event == LEFT_OFF or event == UP_OFF or event == UNDER_OFF:
                character.velocity = 0
        elif event == RIGHT_OFF: character.velocity -= 1
        elif event == LEFT_OFF: character.velocity += 1
        elif event == UP_OFF: character.velocity -= 1
        elif event == UNDER_OFF: character.velocity += 1

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
        character.x = clamp(25, character.x, 775)
        character.y = clamp(20, character.y, 470)
        # print(character.velocity * Framework.frame_time)

    def draw(character):
        if character.velocity != 0:
            character.Mimage.clip_draw((character.sight + int(character.frame) * 4) * 24, 0, 24, 42, character.x, character.y)
        elif character.velocity == 0:
            character.Mimage.clip_draw(character.sight * 24, 0, 24, 42, character.x, character.y)


class Attack:
    def enter(character, event):
        pass

    def exit(character, event):
        pass

    def do(character):
        character.frame_att = (character.frame_att + FRAME_PER_ATTACK * ACTION_PER_TIME * Framework.frame_time) % 17

    def draw(character):
        if character.att_state == 0:
            if character.sight == 0:
                character.Short_Aimage.clip_draw(int(character.frame_att) * 128, 128*3, 128, 128, character.x, character.y)
            elif character.sight == 1:
                character.Short_Aimage.clip_draw(int(character.frame_att) * 128, 128*0, 128, 128, character.x, character.y)
            elif character.sight == 2:
                character.Short_Aimage.clip_draw(int(character.frame_att) * 128, 128*1, 128, 128, character.x, character.y)
            elif character.sight == 3:
                character.Short_Aimage.clip_draw(int(character.frame_att) * 128, 128*2, 128, 128, character.x, character.y)

        elif character.att_state == 1:
            if character.sight == 0:
                character.Spear_Aimage.clip_draw(int(character.frame_att) * 128, 128*3, 128, 128, character.x, character.y)
            elif character.sight == 1:
                character.Spear_Aimage.clip_draw(int(character.frame_att) * 128, 128*0, 128, 128, character.x, character.y)
            elif character.sight == 2:
                character.Spear_Aimage.clip_draw(int(character.frame_att) * 128, 128*1, 128, 128, character.x, character.y)
            elif character.sight == 3:
                character.Spear_Aimage.clip_draw(int(character.frame_att) * 128, 128*2, 128, 128, character.x, character.y)

        elif character.att_state == 2:
            if character.sight == 0:
                character.Long_Aimage.clip_draw(int(character.frame_att) * 128, 128*3, 128, 128, character.x, character.y)
            elif character.sight == 1:
                character.Long_Aimage.clip_draw(int(character.frame_att) * 128, 128*0, 128, 128, character.x, character.y)
            elif character.sight == 2:
                character.Long_Aimage.clip_draw(int(character.frame_att) * 128, 128*1, 128, 128, character.x, character.y)
            elif character.sight == 3:
                character.Long_Aimage.clip_draw(int(character.frame_att) * 128, 128*2, 128, 128, character.x, character.y)


class Dffense:
    def enter(character, event):
        pass

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 8

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

        character.x = clamp(25, character.x, 775)
        character.y = clamp(20, character.y, 470)
        character.frame = (character.frame + FRAME_PER_ACTION * ACTION_PER_TIME * Framework.frame_time) % 8

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
             RIGHT_OFF: Move, LEFT_OFF: Move, UP_OFF: Move, UNDER_OFF: Move, \
             ATT_ON: Attack, ROLL_ON: Attack, DFF_ON: Attack, ATT_OFF: Move, ROLL_OFF: Attack, DFF_OFF: Attack},
    Dffense: {RIGHT_ON: Dffense, LEFT_ON: Dffense, UP_ON: Dffense, UNDER_ON: Dffense, \
              RIGHT_OFF: Move, LEFT_OFF: Move, UP_OFF: Move, UNDER_OFF: Move, \
              ATT_ON: Dffense, ROLL_ON: Dffense, DFF_ON: Dffense, ATT_OFF: Dffense, ROLL_OFF: Dffense, DFF_OFF: Move},
    Roll: {RIGHT_ON: Roll, LEFT_ON: Roll, UP_ON: Roll, UNDER_ON: Roll, \
           RIGHT_OFF: Move, LEFT_OFF: Move, UP_OFF: Move, UNDER_OFF: Move, \
           ATT_ON: Roll, ROLL_ON: Roll, DFF_ON: Roll, ATT_OFF: Move, ROLL_OFF: Move, DFF_OFF: Move}
}


class Character:
    state_temp = 18
    hp = 200
    def __init__(self):
        self.x, self.y = 650, 250
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame = 0
        self.frame_att = 0
        self.sight = 0
        self.dir = 1
        self.Time = 0
        self.velocity = 0
        self.current = Move
        self.current.enter(self, None)
        self.att_state = 0
        self.event_que = []
        self.Mimage = load_image('charmove2.png')
        self.Short_Aimage = load_image('sword_att.png')
        self.Long_Aimage = load_image('attack.png')
        self.Spear_Aimage = load_image('spear_att.png')
        self.Rimage = load_image('Roll.png')
        self.Dimage_R = load_image('shield_Right.png')
        self.Dimage_L = load_image('shield_Left.png')
        self.Dimage_U = load_image('shield_Up.png')
        self.Dimage_D = load_image('shield_down.png')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.current.do(self)
        self.weapon_change()

        if self.current == Attack and Character.state_temp > 0:
            Character.state_temp -= 1
            self.current.exit(self, Attack)
            self.current.enter(self, Attack)
            print(Character.state_temp)
        elif self.current == Attack and Character.state_temp == 0:
            Character.state_temp = 18

        if self.current == Roll and Character.state_temp > 0:
            Character.state_temp -= 1
            self.current.exit(self, Roll)
            self.current.enter(self, Roll)
            print(Character.state_temp)
        elif self.current == Roll and Character.state_temp == 0:
            Character.state_temp = 18

        if Character.state_temp == 18:
            if len(self.event_que) > 0:
                if Character.state_temp <= 0:
                    Character.state_temp = 8
                event = self.event_que.pop()
                self.current.exit(self, event)
                self.current = state_table[self.current][event]
                self.current.enter(self, event)

    def draw(self):
        self.current.draw(self)
        self.font.draw(30, 450, 'HP : %d' % int(Character.hp), (255, 10, 5))
        # draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def init_coor(self):
        self.x, self.y = 650, 250
        self.current.draw(self)

    def collide_gimmick(self):
        Framework.timer += Framework.frame_time
        if Framework.timer > 0.5 and self.current != Dffense:
            Framework.timer = 0
            Character.hp -= 10

    def weapon_change(self):
        # if SDL_KEYDOWN and SDLK_l:
        #     print('change')
        #     self.att_state = (self.att_state + 1) % 3
        pass

    def Attack_time(self):
        if self.current == Attack:
            return True

    def get_bb(self):
        return self.x - 12, self.y - 12, self.x + 12, self.y + 12

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
