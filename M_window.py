import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = "New Window", width = 25, command = self.new_window)
        self.button2 = tk.Button(self.frame, text = "quit", width = 25, command = self.close_window)
        self.button1.pack()
        self.button2.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def close_window(self):
        self.master.destroy()
        
class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = "quit", width = 25, command = self.close_window)
        self.quitButton.pack()
        self.frame.pack()
    def close_window(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
