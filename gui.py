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
butt1 = tk.Button(text='', width=5, height=2).grid(row=5,column=5)
butt2 = tk.Button(text='', width=5, height=2).grid(row=5,column=6)
colours = ['yellow','orange']


def toggle(c):
    if c == 0:
        return 1
    else:
        return 0
flag = False
c = 0
for i in range(9):

    for j in range(9):
        if j % 3 == 0 and j > 0:
            c = toggle(c)
        
        butt = tk.Button(text='', width=7, height=3, bg=colours[c]).grid(row=i,column=j)
    if i % 3 == 2:
        c = toggle(c)
    
    
    

# butt.pack()

mainWindow.mainloop()