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

    def next_frame(self, delay):
        _log_print("# Rendered the next frame")

        # clear screen
        self.scr.clear()

        ## draw boxes
        #for b in self._boxes:

        #    # check if the box is outside the frame and compensate
        #    draw_w = b.width
        #    if b.x + b.width > self.width:
        #        draw_w = b.x + b.width - self.width

        #    draw_h = b.height
        #    if b.x + b.height > self.height:
        #        draw_w = b.height - self.height

        #    _log_print("# drawing width:", draw_w)
        #    _log_print("# drawing height:", draw_h)

        #    for i in range(draw_h):
        #        self.scr.addstr(b.y+i, b.x, _BLOCK*draw_w)

        # draw boxes
        for b in self._boxes:
            for i in range(b.height):
                self.scr.addstr(b.y+i, b.x*2, _BLOCK*(b.width*2))

        # show changes
        self.scr.refresh()
        time.sleep(delay/1000)


    def quit(self):
        _log_print("# Exit GUI-mode gracefully")
        curses.endwin()

    def create_box(self, width, height, x=0, y=0):
        b = _Box(width, height, x, y)
        self._boxes.append(b)
        return b


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

    def destroy(self):
        _log_print("# Destroyed box")

    def collision(self, b):
        _log_print("# Checking for collision between self and other box")
        return False

