from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')


frame_x = [12,73,131,207,309,413]
frame_widths = [41, 40, 41, 65, 65 , 66]
frame_y = [30, 150, 270, 390]
frame_height = 66

def draw_character(character, state, frame, x, y, frame_widths, frame_height, frame_x):
    width = 200
    height = 200
    scale_factor = 1.63
    if state == 1:
        index = 1
    elif state == 2:
        index = 3
    elif state == 3:
        index = 0
    elif state == 4:
       index = 2

    if frame <= 2:
        draw_width = int(frame_widths[frame] * scale_factor)
    else:
        draw_width = frame_widths[frame]

    character.clip_draw(frame_x[frame], frame_y[index], frame_widths[frame], frame_height, x, y, draw_width, frame_height)

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
state = 1

while running:
    clear_canvas()
    ground.draw(400, 300)

    x += dirx * 5  #
    y += diry * 5

    frame = (frame + 1) % 5

    draw_character(character, state, frame, x, y, frame_widths, frame_height, frame_x)

    update_canvas()
    handle_events()
    delay(0.05)

    if(x<0 or x>800):
        break
    elif (y < 0 or y > 600):
        break

    delay(0.01)


close_canvas()

