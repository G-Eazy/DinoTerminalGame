from dev_game_engine import Game
import random as rd

g = Game(log=True)

dino = g.create_box(2, 3, 5, 20)

boxes = []
boxes.append(g.create_box(2, 2, 70, 21))

## need to save and display highscore
time_elapsed = 0
score = 0
delay = 50

while True:
    #k = g.next_frame(delay, score) # enter delay in ms

    # Update stats
    time_elapsed += 50
    score += int(time_elapsed / 10000) + 1
    
    # Update boxes
    for box in boxes:
        box.set_x(box.x-1)
    
    #if time_elapsed % 10000 == 0:
        #delay -= 2
    if time_elapsed % 1000 == 0:
        if rd.randint(0, 10) < 7:
            boxes.append(g.create_box(2, 2, 70, 21))
        else:
            boxes.append(g.create_box(2, 2, 70, 19))

    #### User Action ###
    #if k is None:
        #print(time_elapsed)
    #    a=0
    #elif k == Game.SPACE_KEY:
        #print("space key pressed")
    #    g.jump()
      
    k = g.next_frame(delay, time_elapsed) # enter delay in ms
    # Check for collisions and end of frames
    for _box in boxes:
        if _box.x + _box.width == 0:
            boxes.remove(_box)
            g.destroy_box(_box)
        if _box.x < 15:
            collision = _box.collision(dino)
            if collision:
                g.destroy_box(_box)
                g.quit(score)
                exit(0)

    # jump

#g.quit(score)

