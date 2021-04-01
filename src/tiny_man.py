from game_engine import Game 
import random as rd
import subprocess
g = Game(log=True)


dino = g.create_box(2, 3, 5, 20)
dino.set_text("^^\n-0-\n/\\")
score_box = g.create_box(5, 10, 1, 1)
width, height = g.dimensions()
score = 0
boxes = []
ground = g.create_box(width-1, 3, 0, int(height/2) + 4)
ground.set_text("^"*200, repeatable=True)

def fire():
    #os.system('exec aplay -q ~/Div/waw-files/boing_poing.wav')
    if(count_shots() < 3):
        subprocess.Popen(["aplay", "-q", "../sounds/boing_poing.wav"])
        boxes.append(g.create_box(1, 1, dino.x+dino.width+1, dino.y+1, shot=True))

def jump():
    dino.set_y(dino.y-2)

def crouch():
    dino.set_y(dino.y+2)

def left():
    dino.set_x(dino.x-2)
def right():
    dino.set_x(dino.x+2)

def new_box():

    # 0 - 24 is height from ground to top
    global height
    box_w = rd.randint(1, 6) 
    box_h = rd.randint(1, 6) 
    position = rd.randint(0, 24) 

    boxes.append(g.create_box(box_w, box_h, 100, position))


def check_collisions():
    for _box in boxes:
        if _box.x + _box.width == 0:
            boxes.remove(_box)
            g.destroy_box(_box)
        elif _box.shot and _box.x > 95:
            boxes.remove(_box)
            g.destroy_box(_box)
            
        collision = _box.collision(dino)
        if collision:
            g.destroy_box(_box)
            g.quit(dino, score)
            exit(0)

def check_hit():
    shots = []
    only_boxes = []
    for _box in boxes:
        if(_box.shot):
            shots.append(_box)
        else:
            only_boxes.append(_box)

    for _box in only_boxes:
        for shot in shots:
            collision = _box.collision(shot)
            if collision:
                boxes.remove(_box)
                g.destroy_box(_box)
                boxes.remove(shot)
                g.destroy_box(shot)
                break

def count_shots():
    count = 0
    for _box in boxes:
        if(_box.shot):
            count += 1
    return count

def check_borders():
    """
    Check to see if player is out of bounds
    """
    #bug in top left corner
    if dino.y + dino.height > ground.y:
        dino.y = ground.y - dino.height
    elif dino.y - dino.height < 0:
        dino.y = int(dino.height / 2)
    elif dino.x + dino.width > 95:
        dino.x = 92
    elif dino.x - dino.height < 0:
        dino.x = 0

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
        score += int(time_elapsed) / 1e5
        score_box.set_text("{}".format(int(score)))
        
        # Update speed 
        if time_elapsed % 10000 == 0 and delay >= 15:
            if time_elapsed % 100000 == 0:
                delay -= 1
            else:
                delay -= 3  

        # Update boxes
        for box in boxes:
            if(box.shot):
                box.set_x(box.x + 2)
            else:
                box.set_x(box.x-1)
        
        
        if time_elapsed % frequency == 0:
            new_box()

        #### User Action ###
        if k == Game.ESCAPE:
            g.pause()    
        elif k == Game.SPACE:
            fire()
        elif k == Game.ARROW_UP:
            jump()
        elif k == Game.ARROW_DOWN:
            crouch()
        elif k == Game.ARROW_LEFT:
            left()
        elif k == Game.ARROW_RIGHT:
            right()

            
          

        # Update movement of boxes
        k = g.next_frame(delay)
        
        check_borders()
        # Check for end of frames and collisions 
        check_collisions()
        check_hit()
    
try:
    run()
except KeyboardInterrupt:
    g.quit(dino, score)
