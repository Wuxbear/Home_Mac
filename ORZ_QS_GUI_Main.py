from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo
from tkinter.scrolledtext import ScrolledText
from time import sleep
from threading import *

class ORZ_GUI:
    fake_test_items = ["item1", "item2", "item3", "item4"]
    Global_Data = {"IP":"192.168.1.1", "SW_version":"0000"}
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
        showinfo("Version",
                 """Hahahahahahaha!!!~~~~\n""" + "SW Version : " + self.Global_Data["SW_version"])

    def load_test_package(self):
        # load config data
        fname = askopenfilename(filetypes=(("python files", "*.py"),
                                           ("All files", "*.*") ))
        #if fname:

        print(fname)
                # create manager process, service process
                # global data, server IP,port, PID
                # create device windows
        self.devWindow = []
        for number in range(ORZ_GUI.Test_Package["Max_devices"]):  #(self.fake_max_devs):
            devWindow = Toplevel(self.master)
            #self.devs = ORZ_GUI_DEV_WINDOW(self.devWindow, ORZ_GUI.Test_Package)
            devs = DEV_WINDOW(devWindow, ORZ_GUI.Test_Package)
            self.devWindow.append(devs)

    def Global_setup(cls):
        print(cls.Global_Data)
            
    def TP_data(cls):
        print(cls.Test_Package)

class Test_Thread(Thread):
    def __init__(self,xxx,stop_event):
        self.xxx = xxx
        self.stop_event = stop_event
        Thread.__init__(self)

    def run(self):
        for x in range(25):
            if (self.stop_event.is_set()):
                break
            msg = str(x) + "b\n"
            self.xxx.text.insert(END, msg)
            sleep(1)
            if x in [5, 10, 15, 20]:
                self.xxx.chks[self.xxx.testing_item].config(text = self.xxx.item_list[self.xxx.testing_item] + " : PASS")
                self.xxx.testing_item += 1
                
            
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
        
    def FRAME_DATA_CHECK(self):
        self.frame = Frame(self.parent)
        self.dev_data = StringVar()
        self.device_info = self.test_package["Device_SN"].copy() #{"SN":'', "HW":'', "SW":''}
        #self.labels = []
        #for x in self.device_info.keys():
        #    l = Label(self.frame, text = x, relief=RIDGE)
        #    l.grid(anchor = W, padx=10)
        #    self.labels.append(l)
        self.l1 = Label(self.frame, text = " SN: ", relief=RIDGE)
        self.l1.grid(sticky = W, padx=10)
        self.l2 = Label(self.frame, text = " HW: ", relief=GROOVE)
        self.l2.grid(sticky= W, padx=10)
        self.l3 = Label(self.frame, text = " SW: ", relief=SUNKEN)
        self.l3.grid(sticky= W, padx=10)
        self.entry = Entry(self.frame, textvariable = self.dev_data)
        #entry.focus()
        self.entry.grid()
        self.entry.bind("<Return>", self.FRAME_DATA_CHECK_run)
        self.frame.grid()

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
            self.FRAME_TEST_PACKAGE()
            #self.FRAME_LIST_ITEM()
            # run test package

    def FRAME_LIST_ITEM(self):
        self.frame = Frame(self.parent)
        self.check_list = self.test_package["Test_Items"]
        self.check_var = []
        for pick in self.check_list:
            var = BooleanVar()
            var.set(True)
            chk = Checkbutton(self.frame, text = pick, variable = var)
            chk.grid(sticky = W)
            self.check_var.append(var)
        go_button = Button(self.frame, text = "Go", command = self.FRAME_LIST_ITEM_run)
        go_button.grid()
        self.frame.grid()
        
    def FRAME_LIST_ITEM_run(self):
        print("run test package!!")
        self.frame.destroy()
        #self.FRAME_DATA_CHECK()
        self.FRAME_TEST_PACKAGE()

    def FRAME_TEST_PACKAGE(self):
        self.frame = Frame(self.parent)
        self.testing_item = 0
        self.item_list = self.test_package["Test_Items"]
        self.check_var = []
        self.chks = []
        for item in self.item_list:
            var = BooleanVar()
            var.set(True)
            chk = Checkbutton(self.frame, text = item, variable = var)
            chk.grid(sticky = W)
            self.check_var.append(var)
            self.chks.append(chk)
        #for x in self.item_list:
        #    l = Label(self.frame, text = x, relief=RIDGE)
        #    l.grid(sticky = W)
        #    self.labels.append(l)
            
        self.s = Button(self.frame, text = "Go", command = self.FRAME_TEST_PACKAGE_go, bg="green")
        self.s.grid()
        self.FakePass = Button(self.frame, text = "FakePass", command = self.FRAME_TEST_PACKAGE_fakepass)
        self.FakePass.grid()
        self.FakeFail = Button(self.frame, text = "FakeFail", command = self.FRAME_TEST_PACKAGE_fakefail)
        self.FakeFail.grid()
        #self.scrollbar = Scrollbar(self.frame)
        #self.scrollbar.grid()
        #self.text = Text(self.frame, height=20, width = 50)
        #self.text.grid()
        #self.scrollbar.config(command = self.text.yview)
        self.text = ScrolledText(self.frame)
        self.text.grid()
        #text.insert(END, data)
        self.frame.grid()
        
    def FRAME_TEST_PACKAGE_go(self):
        print("start test")
        for x in self.chks:
            x.config(state="disabled")
        self.s.config(text = "Stop", command = self.FRAME_TEST_PACKAGE_stop, bg = "red")
        self.stop_event = Event()
        t = Test_Thread(self, self.stop_event)
        t.start()
        
    def FRAME_TEST_PACKAGE_stop(self):
        print("stop test")
        self.stop_event.set()
        # stop the process

    def FRAME_TEST_PACKAGE_restart(self):
        print("restart test")
        self.frame.destroy()
        # renew window for next test
        #self.FRAME_LIST_ITEM()
        showinfo("oooooooooo")
        self.FRAME_DATA_CHECK()
        
    def FRAME_TEST_PACKAGE_fakepass(self):
        self.chks[self.testing_item].config(text = self.item_list[self.testing_item] + " : PASS")
        self.testing_item += 1
        if self.testing_item == len(self.item_list):
            print("All item passed, show PASS window")
            self.stop.config(text = "restart", bg = "green", command = self.FRAME_TEST_PACKAGE_restart)
            # generate report

    def FRAME_TEST_PACKAGE_fakefail(self):
        self.chks[self.testing_item].config(text = self.item_list[self.testing_item] + " : FAIL")
        self.testing_item += 1
        print("stop test when fail happened!, show FAIL window!")
        showerror("dddddd")


def main():
    root = Tk()
    root.title("ORZ_QS_TOOL")
    root.configure(width=640,height=480)
    orz = ORZ_GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()

