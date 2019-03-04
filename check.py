# 运行 python3.5 Regular_visit.py
#!/bin/python3.5
# -*- coding:utf-8 -*-
# author: neo
# date: 2017-05-31

import xlwt
import paramiko
import os
import sys

def header(work_sheet):
    work_sheet.write(0, 0,'检查主机',style0)
    work_sheet.write(0, 1, '项目', style0)
    work_sheet.write(0, 2, '执行命令', style0)
    work_sheet.write(0, 3, '检查结果', style0)
    return work_sheet

def run(text):
    for line in text.readlines():
        if line[0:1] == '#':continue
        items = line.split()
        run_command(items)

def run_command(item):
    host,user,passwd,port,type = item
    try:
        cmds = open('./conf/'+item[4]+'.conf','r',encoding='utf-8')
    except:
        print ("Command conf error,please check cfg file.",item[4])
        exit(1)
    work_sheet = work_book.add_sheet(item[0])
    work_sheet = header(work_sheet)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,int(port),user,passwd,timeout=5)
    except:
        print ("ssh connect timeout,please check network connect.",item[0])
    for cmd in cmds.readlines():
        rows = len(work_sheet.rows)
        items = cmd.split('#')
        check_type = items[0].encode('utf-8')
        command = items[1].encode('utf-8')
        stdin, stdout, stderr = ssh.exec_command(command.decode('utf-8'))
        return_info = stdout.read().strip()

        work_sheet.write(rows,0,host)
        work_sheet.write(rows,1,items[0])
        work_sheet.write(rows,2,items[1])
        work_sheet.write(rows,3,return_info.decode('utf-8'))
    print ('host command success :',host)
    cmds.close()

if __name__ == '__main__':
    style0 = xlwt.easyxf('pattern: pattern solid,fore_colour yellow;' +
                         'font: name Times New Roman, color-index black, bold on;' +
                         'borders: left thick, right thick, top thick, bottom thick;' +
                         'align: horiz center ',
                         num_format_str='0,000.00')

    work_book = xlwt.Workbook(encoding='utf-8')
    host_info = open('./conf/host_info.ini','r',encoding='utf-8')
    run(host_info)
    work_book.save('check.xls')
    host_info.close()