from tkinter import *
def hello():
    print("x")

top = Tk()

  
l = Label(top, text="labeltext")
B1 = Button(top,text="say hello",command = hello)
l.pack()
B1.pack()

top.mainloop()
