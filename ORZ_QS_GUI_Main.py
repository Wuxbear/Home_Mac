from tkinter import *

class ORZ_GUI:
    Global_Setup_Var = [1,"2",3,"44"]
    Global_Data = {"IP":"192.168.1.1", "SW_version":"0001"}
    #Device_data = 
    def __init__(self, master):
        self.master = master
        self.menubar = Menu(self.master)
        self.file_menu = Menu(self.menubar, tearoff = 0)
        self.file_menu.add_command(label="Open", command = self.load_test_script)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.setup_menu = Menu(self.menubar, tearoff = 0)
        self.setup_menu.add_command(label="Golbal Setup", command = self.Global_setup)
        self.setup_menu.add_separator()
        self.setup_menu.add_command(label="Device Setup", command = self.donothing)
        self.menubar.add_cascade(label="Setup", menu = self.setup_menu)

        self.setup_menu = Menu(self.menubar, tearoff = 0)
        self.setup_menu.add_command(label="Sync", command = self.donothing)
        self.menubar.add_cascade(label="DataBase", menu = self.setup_menu)

        self.help_menu = Menu(self.menubar, tearoff = 0)
        self.help_menu.add_command(label="Info", command = self.donothing)
        self.menubar.add_cascade(label="Help", menu = self.help_menu)
        self.master.config(menu = self.menubar)

    def donothing(self):
        print("do nothing")
        self.newWindow = Toplevel(self.master)
        self.app = ORZ_GUI_MSG_BOX(self.newWindow, "SW Version : " + self.Global_Data["SW_version"])

    def load_test_script(self):
        print("load_test_script")
        # load config data
        # create manager process, service process
        # global data, server IP,port, PID
        # create device windows
        self.fake_max_devs = 2
        self.fake_list = ["item1", "item2", "item3"]
        for number in range(self.fake_max_devs):
            self.devWindow = Toplevel(self.master)
            self.devs = ORZ_GUI_DEV_ITEM_LIST(self.devWindow, self.fake_list)

    def Global_setup(self):
        for i in self.Global_Setup_Var:
            print(i)

class ORZ_GUI_MSG_BOX:
    def __init__(self, master, msg):
        self.master = master
        self.msg = msg
        self.master.title("MSG BOX")
        self.frame = Frame(self.master)
        self.label = Label(self.master, text = self.msg)
        self.okButton = Button(self.frame, text = "ok", width = 25, command = self.close_window)
        self.label.pack()
        self.okButton.pack()
        self.frame.pack()
    def close_window(self):
        self.master.destroy()
 
class ORZ_GUI_DEV_ITEM_LIST:
    def __init__(self, master, item_list = []):
        self.master = master
        self.master.title("DEV")
        self.frame = Frame(self.master)
        self.check_list = []
        self.check_var = []
        for pick in item_list:
            var = IntVar()
            chk = Checkbutton(self.frame, text = pick, variable = var)
            chk.pack(anchor = W)
            chk.pack()
            self.check_var.append(var)
        go_button = Button(self.frame, text = "Go", command = self.run_test)
        go_button.pack(side = BOTTOM)
        self.frame.pack()

    def run_test(self):
        print("run test package!!")
        self.frame.pack_forget()
        self.sn = ORZ_GUI_DEV_SN_INPUT(self.master)
        
class ORZ_GUI_DEV_SN_INPUT:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.dev_data = StringVar()
        self.fake_device_info = {"SN":'', "HW":'', "SW":''}
        self.l1 = Label(self.frame, text = " SN: ", relief=RIDGE)
        self.l1.pack()
        self.l2 = Label(self.frame, text = " HW: ", relief=GROOVE)
        self.l2.pack()
        self.l3 = Label(self.frame, text = " SW: ", relief=SUNKEN)
        self.l3.pack()
        self.entry = Entry(self.frame, textvariable = self.dev_data)
        #entry.focus()
        self.entry.pack()
        self.entry.bind("<Return>", self.input_string_check)
        self.frame.pack()
    def input_string_check(self, event):
        if self.dev_data.get() == "ORZ":
            self.l1.config(text = " SN : " + self.dev_data.get())
            self.fake_device_info["SN"] = self.dev_data.get()
        elif self.dev_data.get() == "hw0000":
            self.l2.config(text = " HW : " + self.dev_data.get())
            self.fake_device_info["HW"] = self.dev_data.get()
        elif self.dev_data.get() == "sw0001":
            self.l3.config(text = " SW : " + self.dev_data.get())
            self.fake_device_info["SW"] = self.dev_data.get()
        else:
            print("not match")
        self.entry.delete(0,'end')
        ## check all device_info and quit if all data match!
        self.dc = 0
        for i in self.fake_device_info.values():
            if i == '':
                break
            self.dc += 1
        if self.dc == len(self.fake_device_info):
            print("all data has value, quit this window!")

def main():
    root = Tk()
    root.title("ORZ_QS_TOOL")
    orz = ORZ_GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

