# -*- coding: utf-8 -*-
from tkinter import *

class Device:
    "Device Window class ..."
    dev_number = 0

    def __init__(self, i):
        self.__i = i
        #Device.dev_number += 1
        self.dev_number += 1

    def hello(self):
        print("Hello", self.__i)

    def getX(cls):
        return cls.dev_number

class subDevice(Device):
    pass

a = subDevice(123)
a.hello()
print(a.getX())

b = subDevice(456)
b.hello()
print(b.getX())

       
    

