# This game is from the official documentation of freegames
# https://pypi.org/project/freegames/

# pip install freegames

# Tap on Tile to Move

# import modules
from random import *
import turtle as t
from freegames import floor, vector

# Set window title, color and icon
t.title("Tile-15")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#990099')

tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

#   Functions
# Load tiles and scramble
def load():

    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    for count in range(1000):
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot

# Draw white square with black outline and number
def square(mark, number):
    t.up()
    t.goto(mark.x, mark.y)
    t.down()

    t.color('#003325', '#ffb3e6')
    t.begin_fill()
    for count in range(4):
        t.forward(99)
        t.left(90)
    t.end_fill()

    if number is None:
        return
    elif number < 10:
        t.forward(20)

    t.write(number, font=('Arial', 45, 'normal'))

# Swap tile and empty square
def tap(x, y):
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)

# Draw all tiles
def draw():
    for mark in tiles:
        square(mark, tiles[mark])
    t.update()

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
load()
draw()
t.onscreenclick(tap)
t.done()