from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
text = Text(root, height=20, width = 50)

text.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = text.yview)
data = """slkadfj aldkfj
asdlfkj
adflkj
dsfkj
kdzlkcxv
oieu
1283uas
049ulkjha
adfkhkjxhzv
adflkjhp09u"""
text.insert(END, data)
def wt():
    text.insert(END, "button\n")

b = Button(root,text='test',command = wt)
b.pack()
root.mainloop()
