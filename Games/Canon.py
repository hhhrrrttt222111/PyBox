# This game is from the official documentation of freegames
# https://pypi.org/project/freegames/

# pip install freegames

# Tap on Screen to Fire

# import modules
from random import randrange
import turtle as t
from freegames import vector

# Set window title, color and icon
t.title("Canon Fire")
root = t.Screen()._root
root.iconbitmap("logo-ico.ico")
t.bgcolor('#99ffbb')

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
    # Functions
# Respond to screen tap
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# Return True if xy within screen
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Draw ball and targets
def draw():
    t.clear()

    for target in targets:
        t.goto(target.x, target.y)
        t.dot(20, '#8000ff')

    if inside(ball):
        t.goto(ball.x, ball.y)
        t.dot(6, '#cc0000')

    t.update()

#  Move ball and targets
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    t.ontimer(move, 50)

t.setup(420, 420, 370, 0)
t.hideturtle()
t.up()
t.tracer(False)
t.onscreenclick(tap)
move()
t.done()