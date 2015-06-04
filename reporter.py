# -*- coding: utf-8 -*-
import csv
import sys
import datetime

Model = ["Model", "OOXX_1"]
HW_SN = ["HW_SN", "OOXX_HW_1"]
SW_SN = ["SW_SN", "OOXX_SW_1"]
Uniq_data = ["Uniq_data", "MAC???"]
PN = ["PN", "PN_OOXX_1"]
Date = ["Date", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
Test_case = ["Test case"]
Result = ["Result"]

Reporter_formate=( ["======= ORZ_QS ======="],
                   Model,
                   HW_SN,
                   SW_SN,
                   Uniq_data,
                   PN,
                   Date,
                   Test_case,
                   [],
                   Result
                   )

f = open('reporter.csv','w',newline='')
w = csv.writer(f)
w.writerows(Reporter_formate)
f.close()

csv_file_name = PN[1]
with open(csv_file_name+".csv",'w',encoding='utf-8',newline='') as f:
    w = csv.writer(f)
    try:
        w.writerows(Reporter_formate)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
f.close()
