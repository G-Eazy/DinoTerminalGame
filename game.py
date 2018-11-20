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
speed = 2000

while True:
    if score > 200:
        break
    k = g.next_frame(delay, score) # enter delay in ms

    # Update stats
    time_elapsed += delay 
    score += int(time_elapsed / 10000) + 1
    
    # Update boxes
    for box in boxes:
        box.set_x(box.x-1)
    
    #if time_elapsed % 10000 == 0:
        #speed -= 10
    if time_elapsed % (delay+speed) == 0:
        if rd.randint(0, 10) > 7:
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
      
    # Check for collisions and end of frames
    for _box in boxes:
        if _box.x < 5:
            #_box.destroy()
            _box.set_x(0)
            _box.set_y(30)
            del boxes[0] 
        #if _box.x < 25:
            #collision = box.check_collision(dino)
            #if collision:
                #g.quit(score)

    # jump

g.quit(score)
