# 运行 python3.5 Regular_visit.py

# -*- coding:utf-8 -*-
# author: neo
# date: 2017-05-31

import paramiko
import os
import sys


def run(text):
    for line in text.readlines():
        if line[0:1] == '#':continue
        items = line.split()
        run_command(items)

def run_command(item):
    host,user,passwd,port,type = item
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,int(port),user,passwd,timeout=5)
        command = "dis cu"
        command=command.encode('utf-8')
        stdin, stdout, stderr = ssh.exec_command(command.decode('utf-8'))
        return_info = stdout.read().strip()
        with open("%s.log"%(item[0]),"w") as f:
            f.write(return_info.decode('utf-8'))
        print ('host command success :',host)
    except:
        print ("ssh connect timeout,please check network connect.",item[0])


if __name__ == '__main__':
    host_info = open('./conf/host_info.ini','r',encoding='utf-8')
    run(host_info)
    host_info.close()