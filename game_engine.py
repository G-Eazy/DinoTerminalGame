# Author:   Forat Seif
# Email:    foratseif@gmail.com
# Desc:     GameEngine that is the frontend to G-eazy's DinoTerminal Game.

import time
import curses

_BLOCK = "█"

_logFile = None
def _log_start():
    global _logFile
    _logFile = open("GameEngine.log", "w")
    _logFile.write("## Started log ##\n")

def _log_print(*kargs):
    if _logFile is not None:
        for a in kargs:
            _logFile.write(str(a)+" ")
        _logFile.write("\n")


class Game:

    def __init__(self, log=False):

        # start file log
        if log: _log_start()

        # print to log
        _log_print("# Gone from terminal mode to GUI mode")

        # init gui
        self.scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        # get dimensions
        h, w = self.scr.getmaxyx()
        self.width, self.height = w//2, h
        _log_print("#  - width:", self.width)
        _log_print("#  - height:", self.height)

        # list to keep track of all boxes
        self._boxes = []


    def dimensions(self):
        return self.width, self.height

    def next_frame(self, delay, score=None):
        _log_print("# Rendered the next frame")

        # clear screen
        self.scr.clear()

        gw = self.width * 2
        gh = self.height
        _log_print("#  - game_width:", gw)
        _log_print("#  - game_height:", gh)


        # draw boxes
        for b in self._boxes:
            _log_print("#  - Drawing box")

            bw = b.width * 2
            bh = b.height
            bx = b.x * 2
            by = b.y

            _log_print("#    - box width:", bw)
            _log_print("#    - box height:", bh)
            _log_print("#    - box x:", bx)
            _log_print("#    - box y:", by)

            # check if box is is outside the frame
            if bx+bw < 0 or bx > gw or by+bh < 0 or by > gh:
                _log_print("#    - SKIPPED")
                continue

            # check if the box is on edge of frame
            draw_w = bw
            if bx+bw > gw:
                draw_w = bw - (gw-bx)

            draw_h = bh
            if by+bh > gh:
                draw_h = bh - (gh-by)

            draw_x = bx
            if bx < 0:
                draw_x = 0
                draw_w = bw+bx

            draw_y = by
            if by < 0:
                draw_y = 0
                draw_h = bh+by

            _log_print("#    - drawing width:", draw_w)
            _log_print("#    - drawing height:", draw_h)
            _log_print("#    - drawing x:", draw_x)
            _log_print("#    - drawing y:", draw_y)

            for i in range(draw_h):
                self.scr.addstr(draw_y+i, draw_x, _BLOCK*draw_w)

        # show score
        if score is not None:
            self.scr.addstr(10, 10, "Score: {}".format(score))

        # show changes
        self.scr.refresh()
        time.sleep(delay/1000)


    def quit(self, score=None):
        if score is not None:
            self.scr.clear()
            self.scr.addstr(10, 10, "Score: {}".format(score))
            self.scr.refresh()
            time.sleep(3)
        _log_print("# Exit GUI-mode gracefully")
        curses.endwin()

    def create_box(self, width, height, x=0, y=0):
        b = _Box(width, height, x, y)
        self._boxes.append(b)
        return b

    def destroy_box(self, b):
        self._boxes.remove(b)


class _Box:

    def __init__(self, width, height, x=0, y=0):

        _log_print("# Created box:")
        _log_print("#  - width =", width)
        _log_print("#  - height =", height)
        _log_print("#  - x =", x)
        _log_print("#  - y =", y)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def set_x(self, x):
        _log_print("# Set box variable:")
        _log_print("#  - x =", x)
        self.x = int(x)

    def set_y(self, y):
        _log_print("# Set box variable:")
        _log_print("#  - y =", y)
        self.y = int(y)

    def set_height(self, height):
        _log_print("# Set box variable:")
        _log_print("#  - height =", height)
        self.height = int(height)

    def set_width(self, width):
        _log_print("# Set box variable:")
        _log_print("#  - width =", width)
        self.width = int(width)

    def collision(self, b):
        _log_print("# Checking for collision between self and other box")
        if b.x < self.x < b.x+b.width            \
        or b.y < self.y < b.x+b.height           \
        or self.x < b.x < self.x+self.width       \
        or self.y < b.y < self.y+self.height:
            return True
        return False

