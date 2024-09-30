from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('b242f551a6e70ca619a2059f17cb3236.png')
frame = 0
for x in range(0, 800, 10):
    clear_canvas()
    grass.draw(400, 30)
    if(frame<=4):
        character.clip_draw(frame * 132, 0, 120, 140, x, 100)

    else :
        character.clip_draw(frame % 5 * 132, 140, 120, 140, x, 120)

    #character.clip_composite_draw(frame * 100, -60, 100, 100, 0, '', x, 130, 200, 200)
    update_canvas()
    frame = (frame + 1) % 9


    delay(0.05)
close_canvas()