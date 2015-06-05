# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

var = StringVar()
label = Message(root, textvariable = var, relief = RAISED)
var.set("Msgbox!!")
label.pack()

root.mainloop( )

