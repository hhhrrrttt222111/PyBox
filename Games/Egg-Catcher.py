# import modules
from itertools import cycle
from random import randrange
from tkinter import *
from tkinter import messagebox


# Set Canvas Size
window_width = 800
window_height = 400

# Create main window
tk = Tk()

# Set window title and icon
tk.title("Egg Catcher")
tk.iconbitmap("logo-ico.ico")

# Create Canvas
c = Canvas(tk, width=window_width, height=window_height, background='#00cccc')
c.create_rectangle(-5, window_height - 100, window_width + 5,
                   window_height + 5, fill='#00cc00', width=0)
c.create_oval(-80, -80, 120, 120, fill='#ffcc00', width=0)
c.pack()

# Declare Variables
color_cycle = cycle(['#ff4d4d', '#ff66cc', '#80ff80', '#ff9966', '#ffff66', '#aa80ff', '#00e64d'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95
catcher_color = '#ff0000'
catcher_width = 100
catcher_height = 100
catcher_start_x = window_width / 2 - catcher_width / 2
catcher_start_y = window_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2,
                       start=200, extent=140, style='arc', outline=catcher_color, width=8)

score = 0
score_text = c.create_text(10, 10, anchor='nw', font=('Arial', 16, 'bold'),
                           fill='#000000', text='Score : ' + str(score))

lives_remaining = 3
lives_text = c.create_text(window_width-10, 10, anchor='ne', font=('Arial', 16, 'bold'),
                           fill='#000000', text='Lives : ' + str(lives_remaining))

eggs = []

    # Functions
# Function to Drop Eggs
def create_eggs():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    tk.after(egg_interval, create_eggs)

# Function to Move Eggs
def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > window_height:
            egg_dropped(egg)
    tk.after(egg_speed, move_eggs)

# Function to Check Dropped Egg
def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('GAME OVER!', 'Final Score : ' + str(score))
        tk.destroy()

# Function to reduce Life
def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives : ' + str(lives_remaining))

# Function to check Catch
def catch_check():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    tk.after(100, catch_check)

# Function to increase Score
def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text='Score : ' + str(score))

# Functions to move tray Left and Right
def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < window_width:
        c.move(catcher, 20, 0)


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()

tk.after(1000, create_eggs)
tk.after(1000, move_eggs)
tk.after(1000, catch_check)

tk.mainloop()
