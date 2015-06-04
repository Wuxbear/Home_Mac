# -*- coding: utf-8 -*-
import telnetlib
import time

HOST_IP = "192.168.198.151"
USER = "root"
PASSWORD = "fortinet"

tn = telnetlib.Telnet(HOST_IP, 22)
tn.read_until(b"login as: ", 5)
tn.write(USER.encode('ascii') + b"\n")
tn.read_until(b"root@192.168.198.191's password:")
tn.write(PASSWORD.encode('ascii') + b"\n")
time.sleep(3)
tn.write(b"ls\n")
print("step3")
tn.write(b"exit\n")
print("step4")
print(tn.read_all().decode('ascii'))
