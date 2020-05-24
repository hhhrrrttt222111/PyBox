# This game is from the official documentation of freegames
# https://pypi.org/project/freegames/

# pip install freegames

# Player 1 Controls - Move Up: 'w', Move Down: 's'
# Player 2 Controls - Move Up: 'i', Move Down: 'k'


# import modules
from random import choice, random
import turtle as t
from freegames import vector


# Set window title, color and icon
t.title("Pong")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#cc66ff')

    #Functions
# Randomly generate value between (-5, -3) or (3, 5)
def value():
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


# Move player position by change
def move(player, change):
    state[player] += change

# Draw rectangle at (x, y) with given width and height
def rectangle(x, y, width, height):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for count in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw game and move pong ball
def draw():
    t.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    t.up()
    t.goto(x, y)
    t.dot(10)
    t.update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    t.ontimer(draw, 50)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()

# Set Keyboard Controls
t.onkey(lambda: move(1, 20), 'w')
t.onkey(lambda: move(1, -20), 's')
t.onkey(lambda: move(2, 20), 'i')
t.onkey(lambda: move(2, -20), 'k')
draw()
t.done()