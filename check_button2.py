from tkinter import *
class Checkbar(Frame):
   #def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
    def __init__(self, parent=None, picks=[]):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var, relief=GROOVE, bd=2)
         chk.pack(anchor=W)
         chk.pack()
         self.vars.append(var)
    def state(self):
        go_button.configure(text="go",state=disable)
        return map((lambda var: var.get()), self.vars)


if __name__ == '__main__':
   root = Tk()
   check_list = ['SN check', 'OS update', 'Reset', 'USB']
   lng = Checkbar(root, check_list)
   
   lng.pack()
   
   #lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      #print(list(lng.state()))
      for x in range(len(check_list)):
          print(lng.vars[x].get())

   go_button = Button(root, text='Go', command=allstates)
   go_button.pack(side=BOTTOM)
   root.mainloop()
