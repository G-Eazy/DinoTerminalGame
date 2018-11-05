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


