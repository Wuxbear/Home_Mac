# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
left = Frame(root)
left.pack(side=LEFT, expand=True, fill=Y)

right = Frame(root,height=200,width=200)
right.pack(expand=True, fill=BOTH)

def changeColor(c):
        def change():
                right.config(background=c)
	return change
	
colors = ['red','green','blue','yellow']
for c in colors:
	b = Button(left, text=c, command=changeColor(c))
	b.pack(side=TOP,expand=True)

root.mainloop()
