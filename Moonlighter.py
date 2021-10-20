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


# char_move = load_image('charmove2.png')
# char_attack = load_image('attack.png')

class Character:
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = 0
        self.Mimage = load_image('charmove2.png')
        self.Aimage = load_image('attack.png')

    def move(self):
        global run, frame, w, a, s, d

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

        # 키 상호작용
        events1 = get_events()
        for event in events1:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_w:
                    w = (w + 1) % 4
                    self.y = self.y + 5
                    frame = 1 + 4 * w
                elif event.key == SDLK_s:
                    s = (s + 1) % 4
                    self.y = self.y - 5
                    frame = 0 + 4 * s
                elif event.key == SDLK_a:
                    a = (a + 1) % 4
                    self.x = self.x - 5
                    frame = 3 + 4 * a
                elif event.key == SDLK_d:
                    d = (d + 1) % 4
                    self.x = self.x + 5
                    frame = 2 + 4 * d
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_w:
                    self.y = self.y + 5
                elif event.key == SDLK_s:
                    self.y = self.y - 5
                elif event.key == SDLK_a:
                    self.x = self.x - 5
                elif event.key == SDLK_d:
                    self.x = self.x + 5
            elif event.type == SDL_QUIT:
                run = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    run = False

    def attack(self):
        events2 = get_events()
        for event in events2:
            if event.type == SDL_KEYDOWN and event.key == SDLK_j:
                print('j pressed')
                for f in range(0, 8):
                    clear_canvas()
                    self.Aimage.clip_draw(f * 30, 0, 30, 42, self.x, self.y)
                    update_canvas()
                    delay(0.1)


open_canvas(back_x, back_y)
background = Background()
charcater = Character()
w, a, s, d = 0, 0, 0, 0

while run:
    clear_canvas()
    background.draw()
    charcater.move()
    delay(0.001)
    charcater.attack()
    update_canvas()
    delay(0.01)

close_canvas()
