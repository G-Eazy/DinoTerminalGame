from game_engine import Game

g = Game()

print(g)
print(g.dimensions())
print(g.next_frame())

b = g.create_box(10, 10)

print(b.set_x(19))
print(b.set_y(19))
print(b.set_height(19))
print(b.set_width(19))
print(b.destroy())


print(g.quit())



# example of using next_frame
while True:
    k = g.next_frame(200) # enter delay in ms

    if k is None:
        print("no key pressed, time finished")
    elif k == Game.SPACE_KEY:
        print("space key pressed")
