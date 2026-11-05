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