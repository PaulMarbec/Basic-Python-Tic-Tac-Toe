import random
from itertools import count

import customtkinter as ctk
from tkinter.messagebox import showinfo


# when a button is clicked
def set_tile(row, column):
    global currentPlayer
    if buttons[row][column].cget("text") == "":
        buttons[row][column].configure(text=currentPlayer)

    if ifWin():
        print(f"The game is over, : {currentPlayer} player wins")
        showinfo("The game is OVER",
                 f"The {currentPlayer} player wins !!!\n\nThe game will restart after this dialog will be closed")
        renitialise()

    else:
        currentPlayer = player0 if currentPlayer == playerX else playerX
        label.configure(text=currentPlayer + " Turn")
        window.title(f"Tic tac toe - {currentPlayer} player Turn")


# wash the TICTACTOE
def renitialise():
    global currentPlayer
    for line in range(3):
        for row in range(3):
            buttons[line][row].configure(text="")


def isIdentical(liste):
    return liste[0] != "" and all(item == liste[0] for item in liste)


def fullTableOver():
    showinfo("The game is over", "The game is now fully filled this will be restarting after clic on ok")
    renitialise()


def ifWin():
    table = [
        [],
        [],
        []
    ]
    for X in range(3):
        for Y in range(3):
            table[X].append(buttons[X][Y].cget("text"))

    for line in table:
        if isIdentical(line):
            return True

    for i in range(3):
        colone = [table[x][i] for x in range(3)]
        if isIdentical(colone):
            return True

    i1 = 0
    i2 = 0
    first = table[i1][i2]

    # first diagonal if winning
    if first == "":
        pass
    elif table[i1 + 1][i2 + 1] == first:
        if table[i1 + 2][i2 + 2] == first:
            return True

    # second diagonal if winning

    i1 = 2
    i2 = 0
    first = table[i1][i2]
    if first == "":
        pass
    elif table[i1 - 1][i2 + 1] == first:
        if table[i1 - 2][i2 + 2] == first:
            return True

    # if the table is full
    numberFull = 0
    for item in table:
        for content in item:
            if content != "":
                numberFull += 1

    if numberFull == 9:  # clear
        fullTableOver()

    numberFull = 0

    table = [
        [],
        [],
        []
    ]

# define de game variable
playerX = "X"
player0 = "O"
currentPlayer = None

# randomize the current player
chosePlayer = random.randint(0, 1)
if chosePlayer == 0:
    currentPlayer = playerX
else:
    currentPlayer = player0

# define the Tic Tac Toe table
table = [
    [],
    [],
    []
]

# define the color
colorBlue = "#4c7fee"
colorRed = "#f71717"
colorBackground = "#848a88"

# define de window
window = ctk.CTk()
window.title(f"Tic tac toe - {currentPlayer} player Turn")
window.resizable(False, False)

# define the frame (main)
frame = ctk.CTkFrame(window)
frame.pack(padx=20, pady=20)

# label title and renitialise button
label = ctk.CTkLabel(frame, text=currentPlayer + " Turn", font=("Verdana", 20))
label.grid(row=0, column=0, columnspan=3, pady=10)

renitialiseLabel = ctk.CTkButton(window, text="renitialise", command=renitialise)
renitialiseLabel.pack()

# Créer la grille de boutons
buttons = [[None for _ in range(3)] for _ in range(3)]

for x in range(3):
    for y in range(3):
        buttons[x][y] = ctk.CTkButton(
            frame,
            text="",
            font=("Helvetica", 24),
            width=100,
            height=100,
            command=lambda row=x, column=y: set_tile(row, column)
        )
        buttons[x][y].grid(row=x + 1, column=y, padx=5, pady=5)

window.mainloop()
