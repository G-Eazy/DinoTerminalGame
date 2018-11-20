from game_engine import Game
import time

g = Game(log=True)

box = g.create_box(5, 5, 5, 5)
g.next_frame()

time.sleep(1)
g.quit()

