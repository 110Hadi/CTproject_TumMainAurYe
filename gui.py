import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()
mainWindow.title('Super Tic-Tac-Toe')
mainWindow.geometry('700x700')

colours = ['yellow','orange']

buttons = {i : [[None for j in range(3)] for k in range(3)] for i in range(9)}

states = {i : [['' for j in range(3)] for k in range(3)] for i in range(9)}
print(states)
print(buttons)

def toggle(c):
    if c == 0:
        return 1
    else:
        return 0

p1 = True

def clicked(i,r,c):
    global p1

    if p1:
        nishan = 'X'
    else:
        nishan = 'O'

    if states[i][r][c] != 'X' and states[i][r][c] != 'O':
        buttons[i][r][c].config(text=nishan)
        states[i][r][c] = nishan
    print(states)
    p1 = not p1
    if check_win(states[i], nishan):
        states[i] = p1
        # buttons[i] = tk.Button(width=21, height=9, bg='yellow', font = ('Calibri', ' 12'))
        # buttons[i].grid(r,c)
        print(f'{nishan} wins the {i} board')
        print(states)

def check_win(board,mark):
    print('called')
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
print(buttons)
print(states)
mainWindow.mainloop()