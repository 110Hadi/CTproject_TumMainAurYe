import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title('Super Tic-Tac-Toe')
mainWindow.geometry('700x700')

colours = ['pink','light blue']
buttons = {i : [[None for j in range(3)] for k in range(3)] for i in range(9)}
states = {i : [['' for j in range(3)] for k in range(3)] for i in range(9)}
boardWinners = {i: '' for i in range(9)}
p1 = True
nextBoard = None    # None = player can choose any board
gameOver = False


# print(states)
# print(buttons)

def toggle(c):
    if c == 0:
        return 1
    else:
        return 0

def check_win(board,mark):
    for r in range(3):
        if board[r][0] == mark and board[r][1] == mark and board[r][2] == mark:
            return True
    for c in range(3):
        if board[0][c]== mark and board[1][c] == mark and board[2][c] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False    


def big_board():
    grid = [['' for j in range(3)] for k in range(3)]
    for i in range(9):
        grid[i // 3][i % 3] = boardWinners[i]
    return grid


def is_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def clicked(i, r, c):
    global p1, nextBoard, gameOver

    # 1. reject invalid clicks
    if gameOver:
        return
    if nextBoard is not None and i != nextBoard:
        return
    if boardWinners[i] != '':
        return

    if p1:
        nishan = 'X'
    else:
        nishan = 'O'


    if type(states[i]) == list and states[i][r][c] == '':
        # 2. place the mark
        buttons[i][r][c].config(text=nishan)
        states[i][r][c] = nishan

        if i % 2 == 0:
            colour = 0
        else:
            colour = 1

        # 3. small board win
        if check_win(states[i], nishan):
            boardWinners[i] = nishan
            # states[i] = nishan

            if i < 3:
                row = 0
            elif i < 6:
                row = 3
            else:
                row = 6
            col = (i % 3) * 3

            for ro in range(3):
                for co in range(3):
                    buttons[i][ro][co].destroy()
                    buttons[i][ro][co] = tk.Label(text=nishan, width=7, height=3, bg=colours[colour], font = ('Calibri', ' 12'))
                    buttons[i][ro][co].grid(row = row + ro, column = col + co)

            # 4. whole game win
            print(big_board())
            if check_win(big_board(), nishan):
                messagebox.showinfo('Game over', nishan + ' wins the game!')
                gameOver = True

        # decide where the opponent must play
        nextBoard = r * 3 + c
        if boardWinners[nextBoard] != '' or is_full(states[nextBoard]):
            nextBoard = None

        p1 = not p1 # switch player



# main
colAdder = 0
rowAdder = 0
colour = 0
for i in range(9):

    if i >0 and i % 3 == 0:
            rowAdder += 3
            colAdder = 0
            colour = toggle(colour)
    elif i > 0:
        colour = toggle(colour)
        colAdder += 3

    for r in range(3):
        
        for c in range(3):
            buttons[i][r][c] = tk.Button(width=7, height=3, bg=colours[colour], command = lambda i=i, r=r, c=c: clicked(i, r, c), font = ('Calibri', ' 12'))
            buttons[i][r][c].grid(row = rowAdder+ r, column = colAdder + c)


# butt.pack()
print('...............................................')
# print(buttons)
# print(states)
mainWindow.mainloop()