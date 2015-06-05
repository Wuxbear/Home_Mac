from tkinter import *
import tkinter.messagebox

root = Tk()
item_check_var1 = IntVar()
item_check_var1.set(1)
item_check_var2 = IntVar()

c1 = Checkbutton(root, text ="item1", variable = item_check_var1,
                 onvalue = 1, offvalue = 0, height=5, width =20)

c2 = Checkbutton(root, text ="item2", variable = item_check_var2,
                 onvalue = 1, offvalue = 0, height=5, width =20)


c1.pack()
c2.pack()
root.mainloop()

