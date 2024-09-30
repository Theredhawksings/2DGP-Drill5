from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')

frame_x = [0,132,264,379,510]
frame_widths = [132,132,115,131,119]
frame_y = [139,20]
frame_height = 119

def handle_events():
    global running,dirx,diry,facing_right

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                facing_right = True
            elif event.key == SDLK_LEFT:
                dirx -= 1
                facing_right = False
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
facing_right = True


while running:
    clear_canvas()
    ground.draw(400,300)

    if frame <= 4:
        if facing_right:
            character.clip_draw(frame_x[frame], frame_y[0], frame_widths[frame], frame_height, x, y)
        else:
            character.clip_composite_draw(frame_x[frame], frame_y[0], frame_widths[frame], frame_height,0, 'h', x, y, frame_widths[frame], frame_height)
    else:
        if facing_right:
            character.clip_draw(frame_x[frame % 5], frame_y[0], frame_widths[frame % 5], frame_height, x, y)
        else:
            character.clip_composite_draw(frame_x[frame % 5], frame_y[0], frame_widths[frame % 5], frame_height, 0, 'h', x, y, frame_widths[frame % 5], frame_height)

    update_canvas()
    handle_events()
    frame = (frame+1)%9

    x += dirx * 10
    y += diry * 10

    if(x<0 or x>800):
        break
    elif (y < 0 or y > 600):
        break

    delay(0.1)


close_canvas()

