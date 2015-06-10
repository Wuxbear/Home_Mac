from tkinter import *

def input_string_check(event):
    if data.get() == "ORZ":
        l1.config(text = " SN : " + data.get())
        device_info["SN"] = data.get()
    elif data.get() == "hw0000":
        l2.config(text = " HW : " + data.get())
        device_info["HW"] = data.get()
    elif data.get() == "sw0001":
        l3.config(text = " SW : " + data.get())
        device_info["SW"] = data.get()
    else:
        print("not match")
    entry.delete(0,'end')
    ## check all device_info and quit if all data match!
    dc = 0
    for i in device_info.values():
        if i == '':
            break
        dc += 1
    if dc == len(device_info):
        print("all data has value, quit this window!")
            
root = Tk()
data = StringVar()
device_info = {"SN":'', "HW":'', "SW":''}

l1 = Label(root, text = " SN: ", relief=RIDGE)
l1.grid(sticky = W)
l2 = Label(root, text = " HW: ", relief=GROOVE)
l2.grid(sticky = W)
l3 = Label(root, text = " SW: ", relief=SUNKEN)
l3.grid(sticky = W)


entry = Entry(textvariable=data)
entry.focus()
entry.grid()
entry.bind("<Return>", input_string_check)

root.mainloop()
