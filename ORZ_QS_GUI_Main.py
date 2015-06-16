from tkinter import *

class ORZ_GUI:
    fake_test_items = ["item1", "item2", "item3", "item4"]
    Global_Data = {"IP":"192.168.1.1", "SW_version":"0001"}
    Device_SN = {"SN":"", "HW":"", "SW":""}
    Console_Setup_Parameter = {"BaudRate":9600, "StopBit":1}
    Test_Package = {"Max_devices":2, "Test_Items":fake_test_items, "Device_SN":Device_SN}
    # test package path, Service Process PID, systme setting
    # Device_data = 
    def __init__(self, master):
        self.master = master
        self.menubar = Menu(self.master)
        self.file_menu = Menu(self.menubar, tearoff = 0)
        self.file_menu.add_command(label="Open", command = self.load_test_package)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.setup_menu = Menu(self.menubar, tearoff = 0)
        self.setup_menu.add_command(label="Golbal Setup", command = self.Global_setup)
        self.setup_menu.add_separator()
        self.setup_menu.add_command(label="Device Setup", command = self.TP_data)
        self.menubar.add_cascade(label="Setup", menu = self.setup_menu)

        self.setup_menu = Menu(self.menubar, tearoff = 0)
        self.setup_menu.add_command(label="Sync", command = self.sync)
        self.menubar.add_cascade(label="DataBase", menu = self.setup_menu)

        self.help_menu = Menu(self.menubar, tearoff = 0)
        self.help_menu.add_command(label="Info", command = self.help)
        self.menubar.add_cascade(label="Help", menu = self.help_menu)
        self.master.config(menu = self.menubar)

    def sync(self):
        print("sync data to DB")

    def help(self):
        self.newWindow = Toplevel(self.master)
        self.app = ORZ_GUI_MSG_BOX(self.newWindow, "SW Version : " + self.Global_Data["SW_version"])

    def load_test_package(self):
        print("load_test_package")
        # load config data
        # create manager process, service process
        # global data, server IP,port, PID
        # create device windows
        for number in range(ORZ_GUI.Test_Package["Max_devices"]):  #(self.fake_max_devs):
            self.devWindow = Toplevel(self.master)
            #self.devs = ORZ_GUI_DEV_WINDOW(self.devWindow, ORZ_GUI.Test_Package)
            self.devs = DEV_WINDOW(self.devWindow, ORZ_GUI.Test_Package)

    def Global_setup(cls):
        print(cls.Global_Data)
            
    def TP_data(cls):
        print(cls.Test_Package)
            
        
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

### Frame test
class DEV_WINDOW:
    number = 0
    def __init__(self, parent, Test_Package):
        self.parent = parent
        self.test_package = Test_Package
        DEV_WINDOW.number += 1
        parent.title("DEV"+str(DEV_WINDOW.number))
        #self.FRAME_LIST_ITEM()
        self.FRAME_DATA_CHECK()

    def FRAME_LIST_ITEM(self):
        self.frame = Frame(self.parent)
        self.check_list = self.test_package["Test_Items"]
        self.check_var = []
        for pick in self.check_list:
            var = BooleanVar()
            var.set(True)
            chk = Checkbutton(self.frame, text = pick, variable = var)
            chk.pack()
            self.check_var.append(var)
        go_button = Button(self.frame, text = "Go", command = self.FRAME_LIST_ITEM_run)
        go_button.pack(side = BOTTOM)
        self.frame.pack()
        
    def FRAME_LIST_ITEM_run(self):
        print("run test package!!")
        self.frame.destroy()
        #self.FRAME_DATA_CHECK()
        self.FRAME_TEST_PACKAGE()
        
    def FRAME_DATA_CHECK(self):
        self.frame = Frame(self.parent)
        self.dev_data = StringVar()
        self.device_info = self.test_package["Device_SN"] #{"SN":'', "HW":'', "SW":''}
        #self.labels = []
        #for x in self.device_info.keys():
        #    l = Label(self.frame, text = x, relief=RIDGE)
        #    l.pack(anchor = W, padx=10)
        #    self.labels.append(l)
        self.l1 = Label(self.frame, text = " SN: ", relief=RIDGE)
        self.l1.pack(anchor = W, padx=10)
        self.l2 = Label(self.frame, text = " HW: ", relief=GROOVE)
        self.l2.pack(anchor = W, padx=10)
        self.l3 = Label(self.frame, text = " SW: ", relief=SUNKEN)
        self.l3.pack(anchor = W, padx=10)
        self.entry = Entry(self.frame, textvariable = self.dev_data)
        #entry.focus()
        self.entry.pack()
        self.entry.bind("<Return>", self.FRAME_DATA_CHECK_run)
        self.frame.pack()

    def FRAME_DATA_CHECK_run(self, event):
        if self.dev_data.get() == "ORZ":
            self.l1.config(text = " SN : " + self.dev_data.get())
            self.device_info["SN"] = self.dev_data.get()
        elif self.dev_data.get() == "hw0000":
            self.l2.config(text = " HW : " + self.dev_data.get())
            self.device_info["HW"] = self.dev_data.get()
        elif self.dev_data.get() == "sw0001":
            self.l3.config(text = " SW : " + self.dev_data.get())
            self.device_info["SW"] = self.dev_data.get()
        else:
            print("not match")
            
        self.entry.delete(0,'end')
        ## check all device_info and quit if all data match!
        self.dc = 0
        for i in self.device_info.values():
            if i == '':
                break
            self.dc += 1
            
        if self.dc == len(self.device_info):
            print("all data has value, quit this window!")
            self.frame.destroy()
            #self.FRAME_TEST_PACKAGE()
            self.FRAME_LIST_ITEM()
            # run test package

    def FRAME_TEST_PACKAGE(self):
        self.frame = Frame(self.parent)
        self.labels = []
        self.testing_item = 0
        self.item_list = self.test_package["Test_Items"]
        for x in self.item_list:
            l = Label(self.frame, text = x, relief=RIDGE)
            l.pack(anchor = W)
            self.labels.append(l)
            
        self.stop = Button(self.frame, text = "Stop", command = self.FRAME_TEST_PACKAGE_stop, bg="red")
        self.stop.pack()
        self.FakePass = Button(self.frame, text = "FakePass", command = self.FRAME_TEST_PACKAGE_fakepass)
        self.FakePass.pack()
        self.FakeFail = Button(self.frame, text = "FakeFail", command = self.FRAME_TEST_PACKAGE_fakefail)
        self.FakeFail.pack()
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(self.frame, height=20, width = 50)

        self.text.pack(side = LEFT, fill = BOTH)
        self.scrollbar.config(command = self.text.yview)
        #text.insert(END, data)
        self.b = Button(self.frame, text='fake_console_input',command = self.FRAME_TEST_PACKAGE_wt)
        self.b.pack()
        self.frame.pack()

    def FRAME_TEST_PACKAGE_wt(self):
        self.text.insert(END, "button\n")

    def FRAME_TEST_PACKAGE_stop(self):
        print("stop test")
        # stop the process

    def FRAME_TEST_PACKAGE_restart(self):
        print("restart test")
        self.frame.destroy()
        # renew window for next test
        #self.FRAME_LIST_ITEM()
        self.FRAME_DATA_CHECK()
        
    def FRAME_TEST_PACKAGE_fakepass(self):
        self.labels[self.testing_item].config(text = self.item_list[self.testing_item] + " : PASS")
        self.testing_item += 1
        if self.testing_item == len(self.item_list):
            print("All item passed, show PASS window")
            self.stop.config(text = "restart", bg = "green", command = self.FRAME_TEST_PACKAGE_restart)
            # generate report

    def FRAME_TEST_PACKAGE_fakefail(self):
        self.labels[self.testing_item].config(text = self.item_list[self.testing_item] + " : FAIL")
        self.testing_item += 1
        print("stop test when fail happened!, show FAIL window!")


        
class ORZ_GUI_DEV_WINDOW:
    number = 0
    def __init__(self, master, Test_Package):
        self.master = master
        self.test_package = Test_Package
        ORZ_GUI_DEV_WINDOW.number += 1
        self.master.title("DEV"+str(ORZ_GUI_DEV_WINDOW.number))
        self.frame = Frame(self.master)
        self.check_list = Test_Package["Test_Items"]
        self.check_var = []
        for pick in self.check_list:
            var = BooleanVar()
            var.set(True)
            chk = Checkbutton(self.frame, text = pick, variable = var)
            chk.pack()
            self.check_var.append(var)
        go_button = Button(self.frame, text = "Go", command = self.run_test)
        go_button.pack(side = BOTTOM)
        self.frame.pack()

    def run_test(self):
        print("run test package!!")
        self.frame.pack_forget()
        self.sn = ORZ_GUI_DEV_SN_INPUT(self.master, self.test_package)

      
class ORZ_GUI_DEV_SN_INPUT:
    def __init__(self, master, Test_Package):
        self.master = master
        self.test_package = Test_Package
        self.frame = Frame(self.master)
        #self.frame.pack_forget()
        self.dev_data = StringVar()
        self.fake_device_info = {"SN":'', "HW":'', "SW":''}
        self.l1 = Label(self.frame, text = " SN: ", relief=RIDGE)
        self.l1.pack(anchor = W, padx=10)
        self.l2 = Label(self.frame, text = " HW: ", relief=GROOVE)
        self.l2.pack(anchor = W, padx=10)
        self.l3 = Label(self.frame, text = " SW: ", relief=SUNKEN)
        self.l3.pack(anchor = W, padx=10)
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
            self.frame.pack_forget()
            #self.fake_list = ["item1", "item2", "item3"]
            self.test = ORZ_GUI_DEV_RUN_TEST_PACKAGE(self.master, self.test_package)


class ORZ_GUI_DEV_RUN_TEST_PACKAGE:
    def __init__(self, master, Test_Package):
        self.master = master
        self.test_package = Test_Package
        self.list_frame = Frame(self.master)
        #self.fake_list = ["item1", "item2", "item3"]
        self.labels = []
        self.testing_item = 0
        self.item_list = Test_Package["Test_Items"]
        for x in self.item_list:
            l = Label(self.list_frame, text = x, relief=RIDGE)
            l.pack(anchor = W)
            self.labels.append(l)
            
        self.stop = Button(self.list_frame, text = "Stop", command = self.stop_test, bg="red")
        self.stop.pack()
        self.FakePass = Button(self.list_frame, text = "FakePass", command = self.FakePass)
        self.FakePass.pack()
        self.FakeFail = Button(self.list_frame, text = "FakeFail", command = self.FakeFail)
        self.FakeFail.pack()
        self.list_frame.pack()
        self.console_frame = Frame(self.master)
        self.scrollbar = Scrollbar(self.console_frame)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(self.console_frame, height=20, width = 50)

        self.text.pack(side = LEFT, fill = BOTH)
        self.scrollbar.config(command = self.text.yview)
        #text.insert(END, data)
        self.b = Button(self.console_frame, text='fake_console_input',command = self.wt)
        self.b.pack()
        self.console_frame.pack()

    def wt(self):
        self.text.insert(END, "button\n")

    def stop_test(self):
        print("stop test")
        # stop the process

    def restart(self):
        print("restart test")
        self.__init__( self.master, self.test_package)
        # renew window and data
        
    def FakePass(self):
        self.labels[self.testing_item].config(text = self.item_list[self.testing_item] + " : PASS")
        self.testing_item += 1
        if self.testing_item == len(self.item_list):
            print("All item passed, show PASS window")
            self.stop.config(text = "restart", bg = "green", command = self.restart)
            # generate report

    def FakeFail(self):
        self.labels[self.testing_item].config(text = self.item_list[self.testing_item] + " : FAIL")
        self.testing_item += 1
        print("stop test when fail happened!, show FAIL window!")

 
def main():
    root = Tk()
    root.title("ORZ_QS_TOOL")
    orz = ORZ_GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()

