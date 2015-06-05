from tkinter import *

root = Tk()

mb = Menubutton(root, text = "menu", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

mayovar = IntVar()
ketchvar = IntVar()

mb.menu.add_checkbutton( label = "mayo", variable = mayovar)
mb.menu.add_checkbutton( label = "ketchvar", variable = ketchvar)

mb.pack()
root.mainloop()
