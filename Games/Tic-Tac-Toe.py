# import modules
from tkinter import *
import tkinter.messagebox

# Create main window
tk = Tk()

# Set window title and icon
tk.title("Tic Tac Toe")
tk.iconbitmap("logo-ico.ico")

# Player variables
pa = StringVar()
pb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

button_click = True
flag = 0

    # Functions
# Function to disable Buttons
def disableButton():
    B1.configure(state=DISABLED)
    B2.configure(state=DISABLED)
    B3.configure(state=DISABLED)
    B4.configure(state=DISABLED)
    B5.configure(state=DISABLED)
    B6.configure(state=DISABLED)
    B7.configure(state=DISABLED)
    B8.configure(state=DISABLED)
    B9.configure(state=DISABLED)

# Function to display X and O
def buttonClick(buttons):
    global button_click, flag, player2_name, player1_name, pb, pa
    if buttons["text"] == " " and button_click == True:
        buttons["text"] = "X"
        button_click = False
        pb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and button_click == False:
        buttons["text"] = "O"
        button_click = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

# Function to check WIN condition
def checkForWin():
    if (B1['text'] == 'X' and B2['text'] == 'X' and B3['text'] == 'X' or
        B4['text'] == 'X' and B5['text'] == 'X' and B6['text'] == 'X' or
        B7['text'] =='X' and B8['text'] == 'X' and B9['text'] == 'X' or
        B1['text'] == 'X' and B5['text'] == 'X' and B9['text'] == 'X' or
        B3['text'] == 'X' and B5['text'] == 'X' and B7['text'] == 'X' or
        B1['text'] == 'X' and B2['text'] == 'X' and B3['text'] == 'X' or
        B1['text'] == 'X' and B4['text'] == 'X' and B7['text'] == 'X' or
        B2['text'] == 'X' and B5['text'] == 'X' and B8['text'] == 'X' or
        B7['text'] == 'X' and B6['text'] == 'X' and B9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (B1['text'] == 'O' and B2['text'] == 'O' and B3['text'] == 'O' or
          B4['text'] == 'O' and B5['text'] == 'O' and B6['text'] == 'O' or
          B7['text'] == 'O' and B8['text'] == 'O' and B9['text'] == 'O' or
          B1['text'] == 'O' and B5['text'] == 'O' and B9['text'] == 'O' or
          B3['text'] == 'O' and B5['text'] == 'O' and B7['text'] == 'O' or
          B1['text'] == 'O' and B2['text'] == 'O' and B3['text'] == 'O' or
          B1['text'] == 'O' and B4['text'] == 'O' and B7['text'] == 'O' or
          B2['text'] == 'O' and B5['text'] == 'O' and B8['text'] == 'O' or
          B7['text'] == 'O' and B6['text'] == 'O' and B9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)


buttons = StringVar()

# Creating Input Label
label = Label(tk, text="Player 1:", font='Helvetica', bg='pink',
              fg='black', height=1, width=10)
label.grid(row=1, column=0)

label = Label(tk, text="Player 2:", font='Helvetica', bg='pink',
              fg='black', height=1, width=10)
label.grid(row=2, column=0)



# Creating and Styling Buttons
B1 = Button(tk, text=" ", font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B1))
B1.grid(row=3, column=0)

B2 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B2))
B2.grid(row=3, column=1)

B3 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B3))
B3.grid(row=3, column=2)

B4 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B4))
B4.grid(row=4, column=0)

B5 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B5))
B5.grid(row=4, column=1)

B6 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B6))
B6.grid(row=4, column=2)

B7 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B7))
B7.grid(row=5, column=0)

B8 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B8))
B8.grid(row=5, column=1)

B9 = Button(tk, text=' ', font='Times 20 bold', bg='green', fg='yellow',
            height=4, width=8, command=lambda: buttonClick(B9))
B9.grid(row=5, column=2)

tk.mainloop()