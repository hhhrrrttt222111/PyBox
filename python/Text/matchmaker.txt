import random
import time
from tkinter import Tk, Button, DISABLED

# Create main window
tk = Tk()

# Set window title and icon
tk.title('Matchmaker')
tk.iconbitmap("logo-ico.ico")

# Variables
first = True
prev_x = 0
prev_y = 0
buttons = { }
button_symbols = { }

# Matchmaker Symbols
symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
            u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
            u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
            u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728']


random.shuffle(symbols)


# Function to display Icons
def show_symbol(x, y):
    global first
    global prev_x, prev_y
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        prev_x = x
        prev_y = y
        first = False
    elif prev_x != x or prev_y != y:
        if buttons[prev_x, prev_y]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[prev_x, prev_y]['text'] = ' '
            buttons[x, y]['text'] = ' '
        else:
            buttons[prev_x, prev_y]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True


for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y)
                        , width=10, height=8, bg='#b3ffb3', fg='#cc0000')
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()
        buttons[x, y]['font'] = 'Times 12 bold'

tk.mainloop()