from game_engine import Game
import time

g = Game(log=True)

box = g.create_box(5, 5, 5, 5)
#box2 = g.create_box(5, 5, g.width-2, g.height-2)
g.next_frame(1000)

g.quit()

