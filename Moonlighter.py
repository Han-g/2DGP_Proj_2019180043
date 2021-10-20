from pico2d import *

back_x, back_y = 800, 500
character_x, character_y = 400, 250
run = True
frame = 0


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 250)


class Character:
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = 0
        self.Mimage = load_image('charmove2.png')
        self.Aimage = load_image('attack.png')

        self.pressed = {
            'w': False,
            'a': False,
            's': False,
            'd': False,
            'j': False,
            ' ': False
        }

    def move(self):
        global run, frame, w, a, s, d

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
                self.pressed[' '] = True
            if event.type == SDL_KEYUP:
                self.pressed.update({
                    'w': False,
                    'a': False,
                    's': False,
                    'd': False,
                    'j': False,
                    ' ': False
                })


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
            self.y = self.y + 5
            frame = 1 + 4 * w
        if self.pressed['s']:
            s = (s + 1) % 4
            self.y = self.y - 5
            frame = 0 + 4 * s
        if self.pressed['a']:
            a = (a + 1) % 4
            self.x = self.x - 5
            frame = 3 + 4 * a
        if self.pressed['d']:
            d = (d + 1) % 4
            self.x = self.x + 5
            frame = 2 + 4 * d

    def attack(self):
        # events = get_events()
        # for event in events:

        if self.pressed['j']:
            print('j pressed')
            for f in range(0, 8):
                clear_canvas()
                background.draw()
                self.Aimage.clip_draw(f * 31, 0, 31, 42, self.x, self.y)
                update_canvas()
                delay(0.1)
    #
    # def roll(self):
    #     if self.pressed[' ']:




open_canvas(back_x, back_y)
background = Background()
charcater = Character()
w, a, s, d = 0, 0, 0, 0

while run:
    print(charcater.pressed)
    clear_canvas()
    background.draw()
    charcater.move()
    charcater.attack()
    update_canvas()
    delay(0.05)

close_canvas()
