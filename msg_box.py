from tkinter import *
def hello():
    print("x")

top = Tk()

  
l = Label(top, text="labeltext")
B1 = Button(top,text="say hello",command = hello, cursor="plus")
l.pack()
B1.pack(side = BOTTOM)

top.mainloop()
