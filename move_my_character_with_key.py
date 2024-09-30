from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')


def handle_events():
    global running,dirx,diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
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

while running:
    clear_canvas()
    ground.draw(400,300)
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame+1)%8
    x += dirx * 5
    y += diry * 5

    if(x<0 or x>800):
        break
    elif (y < 0 or y > 600):
        break

    delay(0.05)


close_canvas()

