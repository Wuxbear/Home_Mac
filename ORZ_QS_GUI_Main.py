from tkinter import *

Global_Setup_Var = [1,"2",3,"44"]

def donothing():
    print("do nothing")

def load_test_script():
    print("load_test_script")

def Global_setup():
    for i in Global_Setup_Var:
        print(i)
    
root = Tk()
menubar = Menu(root)
file_menu = Menu(menubar, tearoff = 0)
file_menu.add_command(label="Open", command=load_test_script)
menubar.add_cascade(label="File", menu=file_menu)

setup_menu = Menu(menubar, tearoff = 0)
setup_menu.add_command(label="Golbal Setup", command = Global_setup)
setup_menu.add_separator()
setup_menu.add_command(label="Device Setup", command=donothing)
menubar.add_cascade(label="Setup", menu = setup_menu)

setup_menu = Menu(menubar, tearoff = 0)
setup_menu.add_command(label="Sync", command = donothing)
menubar.add_cascade(label="DataBase", menu = setup_menu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Info", command = donothing)
menubar.add_cascade(label="Help", menu = helpmenu)

root.config(menu=menubar)
root.mainloop()

