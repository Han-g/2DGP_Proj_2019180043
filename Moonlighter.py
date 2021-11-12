from pico2d import *
import Game_State
import Framework

open_canvas(800, 500)
Framework.play(Game_State)
close_canvas()

'''
back_x, back_y = 800, 500
character_x, character_y = 400, 250
run = True
frame = 0

class Character:
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = 0
        self.Mimage = load_image('charmove2.png')
        self.Aimage = load_image('attack.png')
        self.Rimage_R = load_image('Roll_Right.png')
        self.Rimage_L = load_image('Roll_Left.png')
        self.Rimage_U = load_image('Roll_Up.png')
        self.Rimage_D = load_image('Roll_Down.png')


        self.pressed = {
            'w': False,
            'a': False,
            's': False,
            'd': False,
            'j': False,
            'h': False,
            'SPACE': False
        }

    def move(self):
        global run, frame, w, s, a, d

        self.Mimage.clip_draw(frame * 24, 0, 24, 42, self.x, self.y)

        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_w:
                self.pressed['w'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_s:
                self.pressed['s'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_a:
                self.pressed['a'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_d:
                self.pressed['d'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_j:
                self.pressed['j'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                self.pressed['SPACE'] = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                run = False
            if event.type == SDL_KEYUP and event.key == SDLK_w:
                self.pressed['w'] = False
            if event.type == SDL_KEYUP and event.key == SDLK_s:
                self.pressed['s'] = False
            if event.type == SDL_KEYUP and event.key == SDLK_a:
                self.pressed['a'] = False
            if event.type == SDL_KEYUP and event.key == SDLK_d:
                self.pressed['d'] = False
            if event.type == SDL_KEYUP and event.key == SDLK_j:
                self.pressed['j'] = False
            if event.type == SDL_KEYUP and event.key == SDLK_SPACE:
                self.pressed['SPACE'] = False


        # 맵 벗어나지 않게 하기
        if self.x > 776:
            self.x = 776
        elif self.y > 468:
            self.y = 468
        elif self.x < 24:
            self.x = 24
        elif self.y < 21:
            self.y = 21

        # 키 상호작용
        if self.pressed['w']:
            w = (w + 1) % 4
            a, s, d, = 0, 0, 0
            self.y = self.y + 5
            frame = 1 + 4 * w
        if self.pressed['s']:
            s = (s + 1) % 4
            w, a, d = 0, 0, 0
            self.y = self.y - 5
            frame = 0 + 4 * s
        if self.pressed['a']:
            a = (a + 1) % 4
            w, s, d = 0, 0, 0
            self.x = self.x - 5
            frame = 3 + 4 * a
        if self.pressed['d']:
            d = (d + 1) % 4
            w, a, s = 0, 0, 0
            self.x = self.x + 5
            frame = 2 + 4 * d

    def attack(self):
        # events = get_events()
        # for event in events:

        if self.pressed['j']:
            #print('j pressed')
            for f in range(0, 8):
                clear_canvas()
                background.draw()
                self.Aimage.clip_draw(f * 31, 0, 31, 42, self.x, self.y)
                update_canvas()
                delay(0.1)

    def roll(self):
        if self.pressed['SPACE']:
            for f in range(0, 8):
                clear_canvas()
                background.draw()
                if self.pressed['w']:
                    self.Rimage_U.clip_draw(f * 28, 0, 28, 42, self.x, self.y)
                    self.y = self.y + 5
                if self.pressed['a']:
                    self.Rimage_L.clip_draw(f * 35, 0, 35, 42, self.x, self.y)
                    self.x = self.x - 5
                if self.pressed['s']:
                    self.Rimage_D.clip_draw(f * 28, 0, 28, 42, self.x, self.y)
                    self.y = self.y - 5
                if self.pressed['d']:
                    self.Rimage_R.clip_draw(f * 35, 0, 35, 42, self.x, self.y)
                    self.x = self.x + 5
                update_canvas()
                delay(0.1)

open_canvas(back_x, back_y)
background = Background()
charcater = Character()
w, a, s, d = 0, 0, 0, 0

while run:
    print(w, a, s, d, charcater.pressed)
    clear_canvas()
    background.draw()
    charcater.move()
    charcater.attack()
    charcater.roll()
    update_canvas()
    delay(0.05)

close_canvas()
'''