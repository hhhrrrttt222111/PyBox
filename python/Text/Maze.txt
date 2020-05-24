# This game is from the official documentation of freegames
# https://pypi.org/project/freegames/

# pip install freegames

# import modules
import turtle as t
from random import random
from freegames import line

# Set window title, color and icon
t.title("Maze")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#b3ffe6')


#   Functions
# Draw maze
def draw():
    t.color('black')
    t.width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    t.update()

#Draw line and dot for screen tap
def tap(x, y):
    if abs(x) > 198 or abs(y) > 198:
        t.up()
    else:
        t.down()

    t.width(2)
    t.color('red')
    t.goto(x, y)
    t.dot(4)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
draw()
t.onscreenclick(tap)
t.done()