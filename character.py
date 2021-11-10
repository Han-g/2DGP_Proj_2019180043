from pico2d import *

UP_ON, UNDER_ON, LEFT_ON, RIGHT_ON, UP_OFF, UNDER_OFF, LEFT_OFF, RIGHT_OFF, ATT_ON, ATT_OFF, ROLL_ON, ROLL_OFF = range(12)

key_event = {
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
    (SDL_KEYDOWN, SDLK_SPACE): ROLL_ON,
    (SDL_KEYUP, SDLK_SPACE): ROLL_OFF
}

class Stop:
    pass


class Move:
    pass


class Attack:
    pass


class Roll:
    pass


state_table = {
    Stop: {RIGHT_ON: Move, LEFT_ON: Move, UP_ON: Move, UNDER_ON: Move, ROLL_ON: Roll},
    Move: {ATT_ON: Attack, ATT_OFF: Move, RIGHT_OFF: Stop, LEFT_OFF: Stop, UP_OFF: Stop, UNDER_OFF: Stop},
    Attack: {ATT_OFF: Stop, ROLL_ON: Attack, RIGHT_ON: Attack, LEFT_ON: Attack, UP_ON: Attack, UNDER_ON: Attack},
    Roll: {ROLL_OFF: Stop}
}


class Character:
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame - 0
        self.Mimage = load_image('charmove2.png')
        self.Aimage = load_image('attack.png')
        self.Rimage_R = load_image('Roll_Right.png')
        self.Rimage_L = load_image('Roll_Left.png')
        self.Rimage_U = load_image('Roll_Up.png')
        self.Rimage_D = load_image('Roll_Down.png')

    def move(self, event):
        global frame
        self.Mimage.clip_draw(frame * 24, 0, 24, 42, self.x, self.y)

        # 맵 벗어나지 않게 하기
        if self.x > 776:
            self.x = 776
        elif self.y > 468:
            self.y = 468
        elif self.x < 24:
            self.x = 24
        elif self.y < 21:
            self.y = 21