# This game is from the official documentation of freegames
# https://pypi.org/project/freegames/

# pip install freegames

# Tap on Tile to Move

# import modules
from random import *
import turtle as t
from freegames import square, vector

# Set window title, color and icon
t.title("Snake")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#99ffbb')

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#   Functions
# Change snake direction
def change(x, y):
    aim.x = x
    aim.y = y

# Return True if head inside boundaries
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

# Move snake forward one segment
def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        t.update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    t.clear()

    for body in snake:
        square(body.x, body.y, 9, '#802b00')

    square(food.x, food.y, 9, '#cc99ff')
    t.update()
    t.ontimer(move, 100)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.listen()
t.onkey(lambda: change(10, 0), 'Right')
t.onkey(lambda: change(-10, 0), 'Left')
t.onkey(lambda: change(0, 10), 'Up')
t.onkey(lambda: change(0, -10), 'Down')
move()
t.done()