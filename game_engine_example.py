from game_engine import Game

g = Game()

print(g)
print(g.dimensions())

dino = g.create_box(15, 25, 175, 15)

## need to save and display highscore
time_elapsed = 0
score = 0
delay = 200 
while True:
    k = g.next_frame(delay) # enter delay in ms
    
    # Update stats
    time_elapsed += delay 
    score += time_elapsed / 100
    
    # Update boxes
    for box in g.boxes:
        box.set_x(box.x-5)

    if time % 1000 == 0:
        g.boxes.append(g.create_box(25, 25))

    ### User Action ###
    if k is None:
        print(time_elapsed)
    elif k == Game.SPACE_KEY:
        print("space key pressed")
        g.jump()
      
    # Check for collisions and end of frames
    for _box in g.boxes:
        if _box.x <= 0:
            _box.destroy()
            g.remove_box()
        if _box.x < 25:
            collision = box.check_collision(dino)
            if collision:
                g.quit(score)

    # jump
