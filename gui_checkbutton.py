from tkinter import *

#check_list = {'item1':[0,0], 'item2':[1,0], 'item3':[1,0]}
check_list = ["auto1", "a2", "aa3"]

root = Tk()
item_check_var1 = IntVar()
item_check_var1.set(1)
item_check_var2 = BooleanVar()
item_check_var3 = BooleanVar()

c1 = Checkbutton(root, text ="item1", variable = item_check_var1,
                 onvalue = 1, offvalue = 0)
c2 = Checkbutton(root, text ="item2", variable = item_check_var2,
                 onvalue = 1, offvalue = 0)
c3 = Checkbutton(root, text ="item3", variable = item_check_var3,
                 onvalue = 1, offvalue = 0)

c1.pack()
c2.pack()
c3.pack()

for x in range(len(check_list)):
    x = Checkbutton(root, text = check_list[x], onvalue = 1, offvalue = 0)
    x.pack()
    
root.mainloop()

