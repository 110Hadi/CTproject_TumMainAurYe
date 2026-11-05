import tkinter as tk
from tkinter import ttk

mainWindow = tk.Tk()
mainWindow.title('Super Tic-Tac-Toe')
mainWindow.geometry('700x700')

# for r in range(9):
#     for c in range(c):
#         butt = tk.Button(text='', width=3, height=5).grid(row=r,column=c)
#         butt.pack()
#     butt.pack()
# butt = tk.Button(text='', width=5, height=2).pack(padx=5,pady=5)
# butt1 = tk.Button(text='', width=5, height=2).grid(row=5,column=5)
# butt2 = tk.Button(text='', width=5, height=2).grid(row=5,column=6)
colours = ['yellow','orange']

buttons = {i : [['' for j in range(3)] for k in range(3)] for i in range(9)}
print(buttons)
def toggle(c):
    if c == 0:
        return 1
    else:
        return 0


colAdder = 0
rowAdder = 0
c = 0
for i in range(9):

    if i >0 and i % 3 == 0:
            rowAdder += 3
            colAdder = 0
            c = toggle(c)
    elif i > 0:
        c = toggle(c)
        colAdder += 3

    for r in range(3):
        
        for col in range(3):
            buttons[i][r][col] = tk.Button(text='', width=7, height=3, bg=colours[c]).grid(row = rowAdder+ r, column = colAdder + col)

    

    
    
    

# butt.pack()

mainWindow.mainloop()