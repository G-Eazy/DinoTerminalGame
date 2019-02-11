from game_engine import Game
import random as rd

g = Game(log=True)

dino = g.create_box(2, 3, 5, 20)

score = 0
boxes = []
boxes.append(g.create_box(2, 2, 70, 21))

def jump():
    dino.set_x(x)

def new_box():
    num1 = rd.randint(0, 10) 
    num2 = rd.randint(0, 10) 
    num3 = rd.randint(0, 10) 

    if num1 < 7:
        if num2 < 5:
            boxes.append(g.create_box(2, 2, 70, 21))
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
        if _box.x < 15:
            collision = _box.collision(dino)
            if collision:
                #g.destroy_box(_box)
                #g.quit(score)
                #exit(0)
                a=0


def run(): 
    global score
## need to save and display highscore
    time_elapsed = 0
    delay = 50
    frequency = 2000

    while True:

        # Update stats
        time_elapsed += 50
        score += int(time_elapsed / 1000)

        
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

        #### User Action ###
        #if k == Game.ESCAPE:
            #g.
        #elif k == Game.SPACE or k == Game.ARROW_UP:
            #print("space key pressed")
        #    jump()
        #elif k == Game.ARROW_DOWN:
            #crouch()

            
          

        # Update movement of boxes
        k = g.next_frame(delay, score)
        

        # Check for end of frames and collisions 
        check_collisions()
    
try:
    run()
except:
    g.quit(score)
