# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()
#root.attributes('-fullscreen',True)
w,h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d" % (w,h))
window_list = []
for i in range(4):
    top = Toplevel(root)
    top.title("window"+str(i))
    top.geometry("300x300")
    msg = Message(top, text=str(i))
    msg.pack()
    button = Button(top, text="Dismiss")
    button.pack()
    window_list.append(top)

root.mainloop()
