# -*- coding: utf-8 -*-
import sys

# ORZ_QS_KEYWORD = ("console_wait", "console_write", "console_read")

with open('console_cmd.txt','r') as f:
    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        if line.startswith("console_wait"):
            str_buf = line.split(' ',2)
            delay_msec = int(str_buf[1])
            console_cmd = str_buf[2]
            print("wait", delay_msec,console_cmd)
        elif line.startswith("console_write"):
            str_buf = line.split(' ',1)
            console_cmd = str_buf[1]
            print("write",console_cmd)
        elif line.startswith("console_read"):
            str_buf = line.split(' ',2)
            delay_msec = int(str_buf[1])
            console_cmd = str_buf[2]
            print("read", delay_msec,console_cmd)
        else:
            print(len(line), "! Not support cmd !")
            
        #for keyword in ORZ_QS_KEYWORD:
        #    if keyword in line:
        #        print(keyword, line)

f.close()
