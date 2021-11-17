import time
frame_time = 0.0

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.handle_event = state.handle_event
        self.update = state.update
        self.draw = state.draw
        self.pause = state.pause
        self.resume = state.resume


class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)


run = None
stack = None


def change_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    stack.append(state)
    stack.enter()


def push_state(state):
    global stack
    if (len(stack) > 0):
        stack.pause()
    stack.append(state)
    stack.enter()


def pop_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global run
    run = False


def play(start_state):
    global run, stack, frame_time
    run = True
    stack = [start_state]
    start_state.enter()
    current_time = time.time()
    while run:
        stack[-1].handle_event()
        stack[-1].update()
        stack[-1].draw()
        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time
        # print("Frame Time : %f sec | Frame Rate : %f fps" %(frame_time, frame_rate))

    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test():
    start_state = TestGameState('StartState')
    play(start_state)


if __name__ == '__main__':
    test()