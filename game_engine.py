# Author:   Forat Seif
# Email:    foratseif@gmail.com
# Desc:     GameEngine that is the frontend to G-eazy's DinoTerminal Game.

class Game:

    def __init__(self):
        print("# Gone from terminal mode to GUI mode")
        self.width = 200
        self.height = 100

    def dimensions(self):
        return self.width, self.height

    def next_frame(self):
        print("# Rendered the next frame")

    def quit(self):
        print("# Exit GUI-mode gracefully")

    def create_box(self, width, height, x=0, y=0):
        return _Box(width, height, x=0, y=0)


class _Box:

    def __init__(self, width, height, x=0, y=0):

        print("# Created box:")
        print("#  - width =", width)
        print("#  - height =", height)
        print("#  - x =", x)
        print("#  - y =", y)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def set_x(self, x):
        print("# Set box variable:")
        print("#  - x =", x)
        self.x = x

    def set_y(self, y):
        print("# Set box variable:")
        print("#  - y =", y)
        self.y = y

    def set_height(self, height):
        print("# Set box variable:")
        print("#  - height =", height)
        self.height = height

    def set_width(self, width):
        print("# Set box variable:")
        print("#  - width =", width)
        self.width = width

    def destroy(self):
        print("# Destroyed box")

