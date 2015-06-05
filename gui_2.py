# -*- coding: utf-8 -*-
import sys
from tkinter import *

#w = Label(root, text="Red Sun", bg="red", fg="white")
#w.pack(fill=X)
#w = Label(root, text="Green Grass", bg="green", fg="black")
#w.pack(fill=X)
#w = Label(root, text="Blue Sky", bg="blue", fg="white")
#w.pack(fill=X)

def show_entry_fields():
   print("function!!")
   
def main():
   master = Tk()
   Label(master, text="First Name").grid(row=0)
   Label(master, text="Last Name").grid(row=1)
   Label(master, text="XXXXX").grid(row=2,column=4)

   #e1 = Entry(master)
   #e2 = Entry(master)
   #e1.grid(row=0, column=1)
   #e2.grid(row=1, column=1)
   #Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
   Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
   Button(master, text='Test', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
   mainloop( )

if __name__ == '__main__':
   main()
