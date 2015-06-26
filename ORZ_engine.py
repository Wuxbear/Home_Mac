# -*- coding: utf-8 -*-
from telnetlib import *
from time import sleep
import socket


# map cmd_string function, args
def telnet_connect(x):
    #global tn.open
    print(x.split()[1])

def telnet_disconnect(x):
    #global tn.close
    print(x)

def telnet_read(x):
    print(x)

def telnet_write(x):
    print(x)

def engine_sleep(x):
    print(x)
    
def power1_on(x):
    print(x)

def power1_off(x):
    print(x)
    
def power2_on(x):
    print(x)

def power2_off(x):
    print(x)

def system_read(x):
    print(x)

def system_write(x):
    print(x)

def system_lock(x):
    print(x)

def system_unlock(x):
    print(x)

TP_KEY_WORDS_MAP = {"telnet_connect":telnet_connect,
                    "telnet_close":telnet_disconnect,
                    "telnet_read":telnet_read,
                    "telnet_write":telnet_write,
                    "sleep":engine_sleep,
                    "power1_on":power1_on,
                    "power1_off":power1_off,
                    "power2_on":power2_on,
                    "power2_off":power2_off,
                    }

# Label dict = {LABLE_name: line}
# timer, store the engine run time
def tp_engine(tp_cmds):
    tp_len = len(tp_cmds)
    line = 0
    while line != tp_len:
        tp_key = tp_cmds[line].split()[0]
        if tp_key in TP_KEY_WORDS_MAP.keys():
            TP_KEY_WORDS_MAP[tp_key](tp_cmds[line])
        else:
            print("Not support keyword : %s" % tp_key)
            break
        line += 1


def test_package_engine(tp_cmds):
    tp_len = len(tp_cmds)
    for line in range(tp_len):
        try:
            if tp_cmds[line].startswith("telnet_connect"):
                print("tn.telnet", tp_cmds[line].split(' ',1)[1])
                #raise TEL_CONNECT_ERROR
            elif tp_cmds[line].startswith("telnet_read"):
                buf = tp_cmds[line].split(' ',2)
                wait_time = buf[1]
                wait_msg = buf[2]
                print("tn.read ", wait_time, wait_msg)
                #raise TEL_READ_ERROR
            elif tp_cmds[line].startswith("telnet_write"):
                cmd = tp_cmds[line].split()[1]
                print("tn.write ", cmd)
                #raise TEL_WRITE_ERROR
            elif tp_cmds[line].startswith("sleep"):
                print("sleep x secs")
                sleep(float(tp_cmds[line].split()[1]))
            elif tp_cmds[line].startswith("telnet_close"):
                print("tn.close")
            elif tp_cmds[line].startswith("power1_on"):
                print("Power 1 ON")
            elif tp_cmds[line].startswith("power1_off"):
                print("Power 1 OFF")
        except:
            print("%s fail!" % tp_cmds[line])
            
        #sleep(1)


def test():
    tp_cmds = [
        "power1_on",
        "telnet_connect 192.168.1.2",
        "telnet_read 10 login:",
        "telnet_write fap-get-status",
        "telnet_read 10 SW version:",
        "sleep 5",
        "telnet_write exit",
        "telnet_close",
        "power1_off",
        ]
    #test_package_engine(tp_cmds)
    tp_engine(tp_cmds)
    
if __name__ == "__main__":
    test()
