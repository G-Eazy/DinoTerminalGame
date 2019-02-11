from game_engine import Game
import random as rd

g = Game(log=True)

dino = g.create_box(2, 3, 5, 20)
dino.set_text("^^\n-0-\n/\\")
score_box = g.create_box(1, 10, 1, 1)
width, height = g.dimensions()
score = 0
boxes = []
ground = g.create_box(width-1, 3, 0, int(height/2) + 4)
ground.set_text("^") #repeatable = true

def jump():
    dino.set_y(dino.y-2)

def crouch():
    dino.set_y(dino.y+2)

def left():
    dino.set_x(dino.x-2)
def right():
    dino.set_x(dino.x+2)

def new_box():
    global height
    num1 = rd.randint(0, 10) 
    num2 = rd.randint(0, 10) 
    num3 = rd.randint(0, 10) 
    seed_height = rd.randint(0, height-1)

    if num1 < 7:
        if num2 < 5:
            boxes.append(g.create_box(2, 2, 70, seed_height))
        else:
            boxes.append(g.create_box(2, 3, 70, 18))
    else:
        if num3 < 5:
            boxes.append(g.create_box(2, 2, 70, 19))
        else:
            boxes.append(g.create_box(3, 2, 70, 19))


def check_collisions():
    for _box in boxes:
        if _box.x + _box.width == 0:
            boxes.remove(_box)
            g.destroy_box(_box)
        collision = _box.collision(dino)
        if collision:
            g.destroy_box(_box)
            g.quit()
            exit(0)
            a=0


def run(): 
    global score
## need to save and display highscore
    time_elapsed = 0
    delay = 50
    frequency = 2000
    k = 0
    while True:

        # Update stats
        time_elapsed += 50
        score += int(time_elapsed / 1000)
        score_box.set_text(str(score))  
        
        # Update speed 
        if time_elapsed % 10000 == 0 and delay >= 5:
            if time_elapsed % 100000 == 0:
                delay -= 1
            else:
                delay -= 3  

        # Update boxes
        for box in boxes:
            box.set_x(box.x-1)
        
        
        if time_elapsed % frequency == 0:
            new_box()
            a=0

        #### User Action ###
        if k == Game.ESCAPE:
            a = 0 
        elif k == Game.SPACE or k == Game.ARROW_UP:
            jump()
        elif k == Game.ARROW_DOWN:
            crouch()
        elif k == Game.ARROW_LEFT:
            left()
        elif k == Game.ARROW_RIGHT:
            right()

            
          

        # Update movement of boxes
        k = g.next_frame(delay)
        

        # Check for end of frames and collisions 
        check_collisions()
    
try:
    run()
except KeyboardInterrupt:
    g.quit()
