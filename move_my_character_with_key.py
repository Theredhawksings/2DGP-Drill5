from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')


def handle_events():
    global running,dirx,diry,state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                state = 4
                dirx += 1
            elif event.key == SDLK_LEFT:
                state = 3
                dirx -= 1
            elif event.key == SDLK_UP:
                state = 1
                diry += 1
            elif event.key == SDLK_DOWN:
                state = 2
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1


running = True
x = 800 // 2 #정수형 나누기 // 실수형 나누기
y = 200
frame = 0

dirx = 0
diry = 0
facing_right = True
state = 1

while running:
    clear_canvas()
    ground.draw(400,300)

    if state == 1:
        character.clip_draw(48 * frame, 0, 48, 48, x, y, 200, 200)
    elif state == 2:
        character.clip_draw(48 * frame, 144, 48, 48, x, y, 200, 200)
    elif state == 3:
        character.clip_draw(48 * frame, 96, 48, 48, x, y, 200, 200)
    elif state == 4:
        character.clip_draw(48 * frame, 48, 48, 48, x, y, 200, 200)

    update_canvas()
    handle_events()
    frame = (frame+1)%2

    x += dirx * 10
    y += diry * 10

    if(x<0 or x>800):
        break
    elif (y < 0 or y > 600):
        break

    delay(0.1)


close_canvas()

