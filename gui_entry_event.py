from tkinter import *
data = IntVar()

entry = Entry(textvariable=data)
entry.grid()

def click(event):
    print(data.get() + 1)

entry.bind("<Return>", click)

root.mainloop()
