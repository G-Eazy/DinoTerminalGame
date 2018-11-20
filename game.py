from game_engine import Game

g = Game(log=True)

dino = g.create_box(5, 5, 0, 20)

boxes = []
boxes.append(g.create_box(5, 5, 70, 20))

## need to save and display highscore
time_elapsed = 0
score = 0
delay = 1000

while True:
    k = g.next_frame(delay) # enter delay in ms

    # Update stats
    time_elapsed += delay 
    score += time_elapsed / 100
    g.quit()
    # Update boxes
    for box in boxes:
        print(box.x)
        box.set_x(box.x-5)
        #box.set_x(60)
    
    #k = g.next_frame(delay) 
    break
    #if time_elapsed > 2000:
        #break
"""
    if time_elapsed % 1000 == 0:
        boxes.append(g.create_box(25, 25))

    ### User Action ###
    if k is None:
        #print(time_elapsed)
        a=0
    elif k == Game.SPACE_KEY:
        #print("space key pressed")
        g.jump()
      
    # Check for collisions and end of frames
    for _box in boxes:
        if _box.x <= 0:
            _box.destroy()
            g.remove_box()
        if _box.x < 25:
            collision = box.check_collision(dino)
            if collision:
                g.quit(score)

    # jump

"""
g.quit()
