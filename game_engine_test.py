from game_engine import Game
import time

g = Game(log=True)

# create box in frame
box = g.create_box(4, 4, 10, 10)
g.next_frame(250)

# create box top left
box2 = g.create_box(4, 4, -2, -2)
g.next_frame(250)

# create box top right
box3 = g.create_box(4, 4, g.width-2, -2)
g.next_frame(250)

# create box bottom left
box4 = g.create_box(4, 4, -2, g.height-2)
g.next_frame(250)

# create box bottom right
box5 = g.create_box(4, 4, g.width-2, g.height-2)
g.next_frame(250)

# create box outside
box6 = g.create_box(4, 4, -10, -10)
g.next_frame(1000)

g.quit()

