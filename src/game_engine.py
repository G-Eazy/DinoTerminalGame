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
    ESCAPE = 27
    ENTER = 10
    SPACE = 32
    ARROW_UP = 259
    ARROW_DOWN = 258
    ARROW_LEFT = 260
    ARROW_RIGHT = 261

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

        self.scr.keypad(True)

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

            w_offset = 0
            h_offset = 0

            _log_print("#    - box width:", bw)
            _log_print("#    - box height:", bh)
            _log_print("#    - box x:", bx)
            _log_print("#    - box y:", by)

            # check if box is is outside the frame
            if bx+bw < 0 or bx >= gw or by+bh < 0 or by >= gh:
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
                w_offset = abs(bx)

            draw_y = by
            if by < 0:
                draw_y = 0
                draw_h = bh+by
                h_offset = abs(by)

            _log_print("#    - drawing width:", draw_w)
            _log_print("#    - drawing height:", draw_h)
            _log_print("#    - drawing x:", draw_x)
            _log_print("#    - drawing y:", draw_y)
            

            #for i in range(draw_h):
            for str, i in b.draw(draw_h, draw_w, h_offset, w_offset):
                self.scr.addstr(draw_y+i, draw_x, str)
        
        

        # show changes
        self.scr.refresh()
        #time.sleep(delay/1000)
        self.scr.timeout(delay)
        x = self.scr.getch()
        _log_print("# GET CHAR:", x)
        return x

    def pause(self):
        b=self.create_box(10, 5, 40, 15)
        b.set_text("Game paused")
        self.next_frame(0)

        x = self.scr.getch()
        while x == -1:
            x = self.scr.getch()
        
        _log_print("***********************", self._boxes.pop().text)
        self.next_frame(0)


    def quit(self, dino, score):
        score = int(score)
        _log_print("# Exit GUI-mode gracefully")
        
        score_file = open(".highscore", "r")
        highscore = int(score_file.readline())
       
        dino.set_x(35)
        dino.set_y(15)
        b=self.create_box(10, 5, 40, 15)
        if int(score) <= highscore:
            b.set_text("Score: " + str(score) + "\nHighscore:" + str(highscore))
        else:
            b.set_text("New Highscore!! " + str(score))
            score_file2 = open(".highscore", "w")
            score_file2.write(str(score))

        self._boxes.append(b)
        self.next_frame(0)
        time.sleep(3)
        curses.endwin()

    def create_box(self, width, height, x=0, y=0, shot=False):
        b = _Box(width, height, x, y, shot)
        self._boxes.append(b)
        return b

    def destroy_box(self, b):
        self._boxes.remove(b)


class _Box:

    def __init__(self, width, height, x=0, y=0, shot=False):

        _log_print("# Created box:")
        _log_print("#  - width =", width)
        _log_print("#  - height =", height)
        _log_print("#  - x =", x)
        _log_print("#  - y =", y)

        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)

        self.fill = _BLOCK
        self.repeat_fill = True

        self.text = None
        self.shot = shot

    def draw(self, h, w, offset_h, offset_w):
        _log_print("# Print box:")

        # check if there is no text
        if self.text is None:

            _log_print("#  - print regular blocks")
            for i in range(h): yield _BLOCK*w, i

        # check if text is defined
        else:
            _log_print("#  - print text:", self.text, (h, w, offset_h, offset_w))
            #for i in range(offset_h, h):
            i = 0
            for str in self.text[offset_h: h]:
                _log_print("#  - yielding:", str[offset_w:w], i)
                yield str[offset_w:w], i
                i=i+1


    def set_text(self, string, repeatable=False, breakable=False):
        _log_print("# Set box text to:", string)
        if(repeatable):
            self.text = string.splitlines()
        else:
            self.text = string.splitlines()

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
        #_log_print("# Checking for collision between self and other box")

        #_log_print("#  - box.width =", b.width)
        #_log_print("#  - box.height =", b.height)
        #_log_print("#  - box.x =", b.x)
        #_log_print("#  - box.y =", b.y)

        #_log_print("#  - self.width =", self.width)
        #_log_print("#  - self.height =", self.height)
        #_log_print("#  - self.x =", self.x)
        #_log_print("#  - self.y =", self.y)


        # Check if any of boxes corners is in self
        if  self.x <= b.x <= self.x+self.width \
        and self.y <= b.y <= self.y+self.height:
            return True

        if  self.x <= b.x+b.width <= self.x+self.width \
        and self.y <= b.y         <= self.y+self.height:
            return True

        if  self.x <= b.x          <= self.x+self.width \
        and self.y <= b.y+b.height <= self.y+self.height:
            return True

        if  self.x <= b.x+b.width  <= self.x+self.width \
        and self.y <= b.y+b.height <= self.y+self.height:
            return True

        # Check if any of selfs corners is in box
        if  b.x <= self.x <= b.x+b.width \
        and b.y <= self.y <= b.y+b.height:
            return True

        if  b.x <= self.x+self.width <= b.x+b.width \
        and b.y <= self.y         <= b.y+b.height:
            return True

        if  b.x <= self.x          <= b.x+b.width \
        and b.y <= self.y+b.height <= b.y+b.height:
            return True

        if  b.x <= self.x+self.width  <= b.x+b.width \
        and b.y <= self.y+self.height <= b.y+b.height:
            return True

        return False
